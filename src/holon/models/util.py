import json
from pathlib import Path
from typing import Union
from django.db import models, transaction
from django.db.models import Model
from django.db import models
from django.db.models.query import QuerySet
from django.db.migrations.operations.models import ModelOptionOperation
from polymorphic.managers import PolymorphicQuerySet
from polymorphic import utils as polymorphic_utils
import copy

base_path = Path(__file__).parent.parent / "services" / "jsons"
base_path.mkdir(exist_ok=True, parents=True)


def write_payload_to_jsons(payload_dict: dict, name: str) -> None:
    for key, json_output in payload_dict.items():
        variable_filename = f"{name}_{key}.json"
        fp = base_path / variable_filename
        with open(fp, "w") as outfile:
            json.dump(json_output, outfile, indent=2)


def all_subclasses(cls) -> set[Model]:
    return set(cls.__subclasses__()).union(
        [s for c in cls.__subclasses__() for s in all_subclasses(c)]
    )


def duplicate_model(obj, attrs={}):
    obj.pk = None
    obj.id = None

    # for copying polymorphic models with multiple levels of inheritance
    # https://stackoverflow.com/a/74999379/19602496
    for field in obj._meta.get_fields(include_parents=True):
        if not isinstance(field, models.OneToOneField):
            continue

        # Test this is a pointer to something in our own inheritance tree
        if not isinstance(obj, field.related_model):
            continue

        setattr(obj, field.attname, None)

    # modify attributes
    for key, value in attrs.items():
        setattr(obj, key, value)

    obj.save()
    return obj


def reset_obj(obj, attributes: dict = {}):
    """Reset an object"""
    obj.pk = None
    obj.id = None

    # for copying polymorphic models with multiple levels of inheritance
    # https://stackoverflow.com/a/74999379/19602496
    for field in obj._meta.get_fields(include_parents=True):
        if not isinstance(field, models.OneToOneField):
            continue

        # Test this is a pointer to something in our own inheritance tree
        if not isinstance(obj, field.related_model):
            continue

        setattr(obj, field.attname, None)

    # modify attributes
    for key, value in attributes.items():
        setattr(obj, key, value)

    return obj


def bulk_duplicate(queryset: PolymorphicQuerySet, attributes: dict = {}):
    """Duplicate multiple models at once. This invalidates the objects in the original queryset"""

    if not queryset:
        return

    class_types = set([model.__class__ for model in queryset])
    print(class_types)

    class_dict = dict.fromkeys(class_types, [])

    for obj in queryset:
        class_dict[obj.__class__].append(obj)

    print(class_dict)

    for class_type, objs in class_dict.items():
        objs = [reset_obj(obj, attributes) for obj in objs]

        class_type.objects.bulk_create(objs)


class RemoveModelBasesOptions(ModelOptionOperation):
    def __init__(self, name):
        super().__init__(name)

    def deconstruct(self):
        kwargs = {
            "name": self.name,
        }
        return (self.__class__.__qualname__, [], kwargs)

    def state_forwards(self, app_label, state):
        from ..models.filter import Filter

        model_state = state.models[app_label, self.name_lower]
        model_state.bases = (Filter,)
        state.reload_model(app_label, self.name_lower, delay=True)

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        pass

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        pass

    def describe(self):
        return "Remove bases from the model %s" % self.name

    @property
    def migration_name_fragment(self):
        return "remove_%s_bases" % self.name_lower


def is_exclude_field(field):
    if field.name.endswith("_ptr"):
        # Exclude iternal polymorphic attributes for CMS
        return True
    if field.is_relation and hasattr(field, "field") and field.field.name.endswith("_ptr"):
        # Exclude iternal polymorphic attributes of relations for CMS
        return True
    else:
        return False
