from django import  template
from jalali_date import date2jalali , datetime2jalali

register = template.Library()


@register.filter(name='showDate')
def showDate(value):
    return date2jalali(value)


@register.filter(name='showDateTime')
def showDateTime(value):
    return datetime2jalali(value)



@register.filter(name='threeDigitsCurrency')
def threeDigitsCurrency(value:int):
    return '{:,}'.format(value)