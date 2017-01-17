"""Object_from_dict had to be called from inside every class, to be converted from dict.
Should use python magic on that."""


def object_from_dict(obj, settings):
    for key in obj.__dict__.keys():  # fill only above mentioned names
        if key in settings:
            setattr(obj, key, settings[key])
    return obj
