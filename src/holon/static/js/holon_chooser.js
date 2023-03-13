const interactiveTypeInput = "#panel-type-content #id_type";
const selectSection = "#panel-options-section";
const contiuousSection = "#panel-continuous_values-section";

const ruleModelTypeSelect = "";

$(document).ready(function () {
    function setModelSubtypeSelectors(model_type_select, data) {
        let model_type = model_type_select.val();

        const model_subtype_select = convertInputToSelect(
            $(model_type_select)
                .closest(".w-panel__content")
                .find("input[id$='-model_subtype']"),
            Object.keys(model_type ? data[model_type].model_subtype : []),
            true
        );
        $(model_type_select)
            .closest(".w-panel__content")
            .find("button[id$='-ADD'")
            .click(function (e) {
                setAssetAttributes(
                    model_type_select,
                    model_subtype_select,
                    data
                );
                setAssetTypes(model_type_select, model_subtype_select, data);
            });
        if (!model_subtype_select) return;
        setAssetAttributes(model_type_select, model_subtype_select, data);
        setAssetTypes(model_type_select, model_subtype_select, data);
        model_subtype_select.change(function (e) {
            updateAssetAttributes(
                model_type_select,
                model_subtype_select,
                data
            );
        });

        model_type_select.change(function (e) {
            const model_type = e.target.value;
            const model_type_select = $(this);
            let model_subtype_select;

            model_subtype_select =
                convertInputToSelect(
                    $(e.target)
                        .closest(".w-panel__content")
                        .find("input[id$='-model_subtype']"),
                    Object.keys(data[model_type].model_subtype),
                    true
                ) ||
                $(e.target)
                    .closest(".w-panel__content")
                    .find("select[id$='-model_subtype']");

            model_subtype_select.find("option").remove().end();
            if (!data[model_type]) return;

            updateOptions(
                model_subtype_select,
                Object.keys(data[model_type].model_subtype),
                true
            );
            updateAssetAttributes(
                model_type_select,
                model_subtype_select,
                data
            );
            model_subtype_select.change(function (e) {
                updateAssetAttributes(
                    model_type_select,
                    model_subtype_select,
                    data
                );
            });
        });
        // setAssetAttributes(select, data, model_type, select.target.value);
    }
    $.ajax({
        url: "/wt/cms/modelconfig",
        success: function (data, status) {
            $("select[id$='-model_type']").each(function () {
                setModelSubtypeSelectors($(this), data);
            });
            $("#id_rules-ADD").click(function (e) {
                $("select[id$='-model_type']").each(function () {
                    setModelSubtypeSelectors($(this), data);
                });
            });
        },
    });
    setVisibleElements($(interactiveTypeInput).val());

    $(interactiveTypeInput).change(function (e) {
        setVisibleElements($(this).val());
    });

    function setVisibleElements(type) {
        switch (type) {
            case "single_select":
            case "multi_select":
                $(selectSection).show();
                $(contiuousSection).hide();
                break;
            case "continuous":
                $(selectSection).hide();
                $(contiuousSection).show();
                break;
            default:
                $(selectSection).hide();
                $(contiuousSection).hide();
                break;
        }
    }

    var checkEverySeconds = 1;
    const interactiveElementInputs = {};

    if ($("#panel-child-content-storyline-heading")) {
        setInterval(function () {
            $("input[id$=-value-interactive_input]").each(function () {
                const element = $(this);
                if (!interactiveElementInputs[element.attr("id")]) {
                    interactiveElementInputs[element.attr("id")] = "";
                }
                if (
                    element.val() &&
                    interactiveElementInputs[element.attr("id")] !==
                        element.val()
                ) {
                    const defaultValueInput = $(element)
                        .closest(".w-panel__content")
                        .find(
                            "input[id$='-value-default_value'],select[id$='-value-default_value']"
                        );
                    const label = $(
                        "label[for='" + $(defaultValueInput).attr("id") + "']"
                    );

                    const interactiveElementName = $(element)
                        .closest(".w-panel__content")
                        .find("span.title")[0];

                    let name, type, options;
                    [name, type, options] =
                        interactiveElementName.innerText.split("|");
                    interactiveElementName.innerText = name;
                    if (type === "continuous") {
                        if (defaultValueInput.prop("tagName") !== "INPUT")
                            convertSelectToInput(defaultValueInput);
                        defaultValueInput.attr("type", "number");
                        defaultValueInput.attr("min", "0");
                        defaultValueInput.attr("max", "100");
                        label.text("Default value (between 0 and 100)");
                    } else {
                        convertInputToSelect(
                            defaultValueInput,
                            options.split(",")
                        );
                        label.text("Default value (choose one of the options)");
                    }

                    interactiveElementInputs[element.attr("id")] =
                        element.val();
                }
            });
        }, checkEverySeconds * 1000);
    }
});

function setAssetAttributes(model_type_select, model_subtype_select, data) {
    if (!model_subtype_select || model_type_select.val() === "") return;
    const model_type = model_type_select.val();
    const attributeInputs = model_subtype_select
        .closest(".w-panel__content")
        .find("input[id$='-asset_attribute'], input[id$='-model_attribute']");

    const options = model_subtype_select.val()
        ? data[model_type].model_subtype[model_subtype_select.val()]
        : data[model_type].attributes;

    attributeInputs.each(function () {
        convertInputToSelect($(this), options);
    });

    updateFilterInputs(model_type, model_subtype_select, data);
}

function setAssetTypes(model_type_select, model_subtype_select, data) {
    const assetTypeInputs = model_type_select
        .closest(".w-panel__content")
        .find("input[id$='-selected_asset_type']");

    const options = Object.keys(data["EnergyAsset"].model_subtype);

    assetTypeInputs.each(function () {
        convertInputToSelect($(this), options);
    });
}

function updateFilterInputs(model_type, model_subtype_select, data) {
    const filterInputs = model_subtype_select
        .closest(".w-panel__content")
        .find(" input[id$='-relation_field'], select[id$='-relation_field']");

    filterInputs.each(function () {
        const allowedRelations = Object.keys(data).map((key) =>
            key.toLowerCase()
        );
        const options = model_subtype_select.val()
            ? data[model_type].model_subtype[model_subtype_select.val()].filter(
                  (item) => allowedRelations.includes(item)
              )
            : data[model_type].attributes.filter((item) =>
                  allowedRelations.includes(item)
              );

        let select;
        if ($(this).prop("tagName") !== "SELECT") {
            select = convertInputToSelect($(this), options);
            if ($(this).val()) {
                convertInputToSelect(
                    select
                        .closest(".w-panel__content")
                        .find(" input[id$='-relation_field_subtype']"),
                    Object.keys(
                        data[
                            Object.keys(data).find(
                                (key) => key.toLowerCase() === $(this).val()
                            )
                        ].model_subtype
                    )
                );
            }
        } else {
            select = $(this);
            updateOptions(select, options);
            select.val("");
        }
        select.change(function (e) {
            const relation_type = e.target.value;
            const relation_subtype = $(this)
                .closest(".w-panel__content")
                .find("input[id$='-relation_field_subtype']");
            const options = Object.keys(
                data[
                    Object.keys(data).find(
                        (key) => key.toLowerCase() === relation_type
                    )
                ].model_subtype
            );
            let select = convertInputToSelect(relation_subtype, options, true);

            if (!select) {
                select = $(e.target)
                    .closest(".w-panel__content")
                    .find("select[id$='-relation_field_subtype']");

                updateOptions(select, options, true);
            }

            select.change(function (e) {
                const relation_subtype = e.target.value;
                const relation_type = $(this)
                    .closest(".w-panel__content")
                    .find("select[id$='-relation_field']")
                    .val();
                const options =
                    data[
                        Object.keys(data).find(
                            (key) => key.toLowerCase() === relation_type
                        )
                    ].model_subtype[relation_subtype];

                const attribute_select = $(this)
                    .closest(".w-panel__content")
                    .find("select[id$='-model_attribute']");
                updateOptions(attribute_select, options);
            });
        });
    });
}

function updateOptions(select, options, allowNull = false) {
    select.find("option").remove().end();
    for (const value of options) {
        select.append(
            $("<option>", {
                value: value,
                text: value,
            })
        );
    }

    if (allowNull) {
        select.append(
            $("<option>", {
                value: "",
                text: "----",
            })
        );
        select.val("").change();
    }
}

function updateAssetAttributes(model_type_select, model_subtype_select, data) {
    if (!model_subtype_select) return;
    const model_type = model_type_select.val();
    const attributeInputs = model_subtype_select
        .closest(".w-panel__content")
        .find("select[id$='-asset_attribute'], select[id$='-model_attribute']");

    attributeInputs.each(function () {
        const attribute_select = $(this);
        attribute_select.find("option").remove().end();

        const options = model_subtype_select.val()
            ? data[model_type].model_subtype[model_subtype_select.val()]
            : data[model_type].attributes;

        for (const value of options) {
            attribute_select.append(
                $("<option>", {
                    value: value,
                    text: value,
                })
            );
        }
    });

    updateFilterInputs(model_type, model_subtype_select, data);
}

function convertSelectToInput(select) {
    if (!select.length) return;
    const attributes = select.prop("attributes");

    const input = $("<input></input>");
    $.each(attributes, function () {
        $(input).attr(this.name, this.value);
    });
    select.replaceWith(input);
    return input;
}

function convertInputToSelect(input, options, allowNull = false) {
    if (!input.length) return;
    const attributes = input.prop("attributes");

    const select = $("<select></select>");

    $.each(attributes, function () {
        $(select).attr(this.name, this.value);
    });

    for (const value of options) {
        select.append(
            $("<option>", {
                value: value,
                text: value,
            })
        );
    }
    input.replaceWith(select);

    if (allowNull) {
        select.append(
            $("<option>", {
                value: "",
                text: "----",
            })
        );

        select.val("").change();
    }

    select.val(input.val()).change();

    return select;
}
