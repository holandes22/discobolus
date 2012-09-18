from django.db import models
from django.db.models import permalink

DATE_FORMAT = '%m/%d/%Y'

@permalink
def get_permalink(name, *args):
    return (name, args)

def make_custom_field_callback(field):
    """
    Callback to make field customization. This is useful to midifiy the elements of a form, for example
    a custom class to a date field so it can be identified by Jquery UI datepicker in the template
    """
    formfield = field.formfield()
    if formfield:
        formfield.widget.attrs.update({'title': field.help_text})
    if isinstance(field, models.DateField):
        formfield.widget.format = DATE_FORMAT
        formfield.widget.attrs.update({'class': 'date-picker', 'readonly': 'true'})
    return formfield


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
