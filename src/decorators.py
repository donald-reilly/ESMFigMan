def validate(func):
    def wrapper(self, value):
        if self._feature_flags:
            for feature in self._feature_flags:
                if feature(value):
                    return func(self, value)
                else:
                    raise ValueError(f"Invalid value: {value} for feature: {feature.__name__}")
        else:
            return func(self, value)
    return wrapper
def serialize(*upperargs):
    def serialize_class(func):
        def wrapper(self, *args, **kwargs):
            self._serialized_state = {arg: getattr(self, arg) for arg in upperargs}
            func(self, *args, **kwargs)
            return self._serialized_state
        return wrapper
    return serialize_class