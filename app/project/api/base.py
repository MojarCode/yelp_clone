from rest_framework.exceptions import NotFound


class GetObjectMixin(object):
    @staticmethod
    def get_object_by_model(model, **kwargs):
        try:
            obj = model.objects.get(**kwargs)
        except model.DoesNotExist:
            raise NotFound(f'Object not found with params {kwargs} on model {model.__name__}')
        return obj
