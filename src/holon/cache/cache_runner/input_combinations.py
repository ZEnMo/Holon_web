import itertools
from typing import Iterator
from holon.models.interactive_element import (
    InteractiveElement,
)

from holon.models.scenario import Scenario
from holon.cache.cache_runner.config import Config

from holon.serializers.interactive_element import InteractiveElementInput

from main.pages.casus import CasusPage
from main.pages.storyline import StorylinePage
from main.pages.challengemode import ChallengeModePage
from main.blocks.storyline_section import InteractiveInputBlock, StorylineSectionBlock
from main.pages.base_storyline_challengemode import BaseStorylineChallengeMode

from typing import Type


def get_holon_input_combinations(
    scenario: Scenario,
) -> tuple[Iterator[tuple[InteractiveElementInput]], int]:
    """Return a HolonInputConfigurationGenerator which can return all possible combinations of input options for each interactive element for a challange in a scenario"""
    try:
        casus_page = CasusPage.objects.filter(scenario=scenario).first()

        Config.logger.log_print(
            f"Computing input combinations for scenario {scenario} ({scenario.id})"
        )

        casus_combinations_iterators, n_casus_combinations = get_holon_input_combinations_per_page(
            casus_page, StorylinePage
        )
        (
            challenge_combinations_iterators,
            n_challenge_combinations,
        ) = get_holon_input_combinations_per_page(casus_page, ChallengeModePage)

        return (
            itertools.chain.from_iterable(
                challenge_combinations_iterators + casus_combinations_iterators
            ),
            n_casus_combinations + n_challenge_combinations,
        )

    except CasusPage.DoesNotExist:
        Config.logger.log_print(f"No CasusPage found for scenario {scenario} with id {scenario.id}")
        return []
    except:
        return []


def get_holon_input_combinations_per_page(
    casus_page: CasusPage, page_type: Type[BaseStorylineChallengeMode]
) -> tuple[list[Iterator[tuple[InteractiveElementInput]]], int]:
    """Return a HolonInputConfigurationGenerator which can return all possible combinations of input options for a specific type of casuspage"""

    interative_input_blocks_per_section = get_interactive_input_blocks_per_section(
        casus_page, page_type
    )

    iterators, n_combinations = generate_interactive_input_combinations(
        interative_input_blocks_per_section
    )

    return iterators, n_combinations


def get_interactive_input_blocks_per_section(
    casus_page: CasusPage, page_type: Type[BaseStorylineChallengeMode] = StorylinePage
) -> list[list[InteractiveInputBlock]]:
    """Return a list of sections containing a list of interactive inputs for a on the casuspage"""

    try:
        page_with_interactive_inputs = page_type.objects.descendant_of(casus_page).first()

        sections = [
            block
            for block in page_with_interactive_inputs.storyline
            if type(block.block) == StorylineSectionBlock
        ]
        interative_input_blocks_per_section = [
            [
                dict(block.value)
                for block in section.value["content"]
                if type(block.block) == InteractiveInputBlock
            ]
            for section in sections
        ]
        return interative_input_blocks_per_section

    except page_type.DoesNotExist:
        Config.logger.log_print(
            f"No {page_type.__name__} found for for casuspage {casus_page} with id {casus_page.id}"
        )
        return []

    except Exception as e:
        Config.logger.log_print(
            f"Something went wrong generating interactive input combinations for scenario  {casus_page} with id {casus_page.id}. {e}"
        )
        return []


def generate_interactive_input_combinations(
    sections: list[list[InteractiveInputBlock]],
) -> tuple[list[Iterator[tuple[InteractiveElementInput]]], int]:
    """Return a list of generators which can return all possible combinations of input options for each interactive element for the given sections. Also returns the total number of combinations"""

    iterators: list(Iterator[tuple[InteractiveElementInput]]) = []
    target_values: dict[int, InteractiveInputBlock] = {}

    total_combinations = 0

    for section in sections:

        section_combinations = 1

        interactive_element_input_lists: dict[int, list[InteractiveElementInput]] = {}

        # Set target values if from previous sections
        for key, value in target_values.items():
            interactive_element_input_lists[key] = [
                InteractiveElementInput(
                    value["interactive_input"],
                    value["default_value"],
                )
            ]

        for interactive_input_block in section:
            interactive_element = interactive_input_block["interactive_input"]

            if not interactive_input_block["visible"]:
                interactive_element_input_lists[interactive_element.id] = [
                    InteractiveElementInput(
                        interactive_element,
                        interactive_input_block["default_value"],
                    )
                ]

            else:
                interactive_element_input_lists[interactive_element.id] = [
                    InteractiveElementInput(interactive_element, value)
                    for value in interactive_element.get_possible_values()
                ]

                section_combinations *= len(interactive_element_input_lists[interactive_element.id])

            # Update targets
            if interactive_input_block["target_value"]:
                target_values[interactive_element.id] = interactive_input_block

        total_combinations += section_combinations

        # Put all combinations in iterator list
        interactive_element_input_lists = interactive_element_input_lists.values()
        iterators.append(itertools.product(*interactive_element_input_lists))

    return iterators, total_combinations


# def get_holon_input_combinations_old(
#     scenario: Scenario,
# ) -> Iterator[tuple[InteractiveElementInput]]:
#     """Return a HolonInputConfigurationGenerator which can return all possible combinations of input options for each interactive element for a challange in a scenario"""

#     Config.logger.log_print(
#         f"Computing possible input combinations for scenario {scenario} with id {scenario.id}"
#     )

#     # retrieve all individual interactive element input possibilities
#     interactive_elements = InteractiveElement.objects.filter(scenario=scenario).all()
#     interactive_element_input_lists = [
#         [
#             InteractiveElementInput(interactive_element, value)
#             for value in interactive_element.get_possible_values()
#         ]
#         for interactive_element in interactive_elements
#     ]

#     # log our findings
#     Config.logger.log_print(f"Found {len(interactive_elements)} interactive elements: ")
#     n_combinations = 1
#     for interactive_element_input_list in interactive_element_input_lists:
#         print(
#             f" - {interactive_element_input_list[0].interactive_element}, with {len(interactive_element_input_list)} possible values:"
#         )
#         print(
#             f"   - {[interactive_element_input.value for interactive_element_input in interactive_element_input_list]}"
#         )
#         n_combinations *= len(interactive_element_input_list)

#     print(f"For a total of {n_combinations} possible input combinations")

#     # return a generator for all possible combinations
#     # TODO take series into account
#     return itertools.product(*interactive_element_input_lists)
