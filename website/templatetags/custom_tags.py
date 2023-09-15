from django import template
from ..models import Patient,Medicinelist

register = template.Library()

@register.filter(name='dugtong')
def dugtong(a,b):
    return f"{a} at {b}"

@register.simple_tag
def testing1(pk):
    medicine_record = Medicinelist.objects.get(id=pk)
    return medicine_record.medicine_name