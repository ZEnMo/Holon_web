#%%
import anylogiccloudclient
from anylogiccloudclient.client.cloud_client import CloudClient

client = CloudClient(
    "f105b75c-4265-4c79-ab36-a9d6e7532fc0"
)  # key is included in .env but docker doesn't work for me rn

model = client.get_model_by_name("Holon buurt model")
version = client.get_latest_model_version(model)
inputs = client.create_inputs_from_experiment(version, "Experiment")


modelrun = client.create_simulation(inputs)
outputs = modelrun.get_outputs_and_run_if_absent()


#%%


def set_inputs(
    inputs: anylogiccloudclient.client.inputs.Inputs,
    neighbourhood1: dict,
    neighbourhood2: dict,
    heatholon: bool,
    windholon: bool,
) -> dict:
    TRANLATES_INPUTS = {
        "P buurt A evs": neighbourhood1["evadoptation"],
        "P buurt A pv": neighbourhood1["solarpanels"],
        "P buurt B evs": neighbourhood2["evadoptation"],
        "P buurt B pv": neighbourhood2["solarpanels"],
        "P warmte holon": heatholon,
        "P wind holon": windholon,
    }

    for name, value in TRANLATES_INPUTS.items():
        inputs.set_input(name, value)

    return inputs


def map_anylogickey_to_api_key(al_key: str) -> str:

    TRANSLATES_OUTPUTS = {
        "betaalbaarheid": "affordability",
        "betrouwbaarheid": "reliability",
        "duurzaamheid": "renewability",
        "zelfconsumptie": "selfconsumption",
    }

    for key, value in TRANSLATES_OUTPUTS.items():

        if key in al_key:
            al_key = value

    return al_key


def round_or_unknown(name: str) -> str:

    # for now betrouwbaarheid should remain unknown
    if "betrouwbaarheid" in name:
        safe_value = "?"
    else:
        value = outputs.value(name)
        safe_value = str(int(float(value)))  # weird type converts to round number

    return safe_value


def get_results(outputs: anylogiccloudclient.client.single_run_outputs.SingleRunOutputs) -> dict:

    results = {"local": {}, "national": {}}
    for name in outputs.names():

        if "lokaal" in name:
            results["local"].update({map_anylogickey_to_api_key(name): round_or_unknown(name)})
        if "nationaal" in name:
            results["national"].update({map_anylogickey_to_api_key(name): round_or_unknown(name)})

    return results


def handle_request(request):

    client = CloudClient(
        "f105b75c-4265-4c79-ab36-a9d6e7532fc0"
    )  # key is included in .env but docker doesn't work for me rn

    model = client.get_model_by_name("Holon buurt model")
    version = client.get_latest_model_version(model)
    inputs = client.create_inputs_from_experiment(version, "Experiment")

    inputs = set_inputs(
        inputs,
        request["neighbourhood1"],
        request["neighbourhood2"],
        request["heatholon"],
        request["windholon"],
    )

    modelrun = client.create_simulation(inputs)
    outputs = modelrun.get_outputs_and_run_if_absent()

    results = get_results(outputs)

    return results


mock_request = {
    "neighbourhood1": {"evadoptation": 70, "solarpanels": 50},
    "neighbourhood2": {"evadoptation": 70, "solarpanels": 50},
    "heatholon": True,
    "windholon": False,
}


results = handle_request(mock_request)
