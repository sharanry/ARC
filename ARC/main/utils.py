from __future__ import unicode_literals

from decimal import Decimal
from datetime import datetime, date
from django.utils import datetime_safe, timezone, six
from django.utils.encoding import smart_text
from django.utils.dateparse import parse_duration
from django.conf import settings
from import_export.widgets import Widget, ForeignKeyWidget
import time


class TimeWidget(Widget):
    """
    Widget for converting time fields.
    Takes optional ``format`` parameter.
    """

    def __init__(self, format=None):
        if format is None:
            if not settings.TIME_INPUT_FORMATS:
                formats = ("%H:%M:%S",)
            else:
                formats = settings.TIME_INPUT_FORMATS
        else:
            formats = (format,)
        self.formats = formats

    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return None
        for format in self.formats:
            print(format)
            try:
                time = float(value) * 24 * 60 * 60
                time = time % (24 * 3600)
                hour = time // 3600
                time %= 3600
                minutes = time // 60
                time %= 60
                seconds = time
                if hour < 12:
                    value = "%02d:%02d:%02d AM" % (hour, minutes, seconds)
                else:
                    value = "%02d:%02d:%02d PM" % (hour - 12, minutes, seconds)

                return datetime.strptime(value, format).time()
            except (ValueError, TypeError):
                print("2")
                continue
        raise ValueError("Enter a valid time.")

    def render(self, value, obj=None):
        if not value:
            return ""
        return value.strftime(self.formats[0])


class DateWidget(Widget):
    """
    Widget for converting date fields.
    Takes optional ``format`` parameter.
    """

    def __init__(self, format=None):
        if format is None:
            if not settings.DATE_INPUT_FORMATS:
                formats = ("%Y-%m-%d",)
            else:
                formats = settings.DATE_INPUT_FORMATS
        else:
            formats = (format,)
        self.formats = formats

    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return None
        if isinstance(value, date):
            return value
        for format in self.formats:
            try:
                return date(1900, 1, 1) + int(value)
            except (ValueError, TypeError):
                continue
        raise ValueError("Enter a valid date.")

    def render(self, value, obj=None):
        if not value:
            return ""
        try:
            return value.strftime(self.formats[0])
        except:
            return datetime_safe.new_date(value).strftime(self.formats[0])


class CompCodesWidget(ForeignKeyWidget):
    def __init__(self, model, field='pk', *args, **kwargs):
        super(CompCodesWidget, self).__init__(model, field, *args, **kwargs)

    def clean(self, value, row=None, *args, **kwargs):
        val = super(ForeignKeyWidget, self).clean(value)
        print(val[1:])
        if val:
            try:
                return self.get_queryset(value, row, *args, **kwargs).get(**{self.field: val[1:]})
            except: 
                return None
        else:
            return None
