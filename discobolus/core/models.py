from django.db import models

# Create your models here.

class BaseModel(models.Model):

    class Meta:
        abstract = True

    def get_model_attrs(self, filter_fields=['id', 'pk', 'user']):
        for field in self._meta.fields:
            if field.name not in filter_fields:
                if field.choices:
                    yield field.name, getattr(self, 'get_%s_display' % field.name)
                else:
                    yield field.name, getattr(self, field.name)
