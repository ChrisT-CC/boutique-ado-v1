"""Shopping bag package"""
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """Calculate shopping bag subtotal"""
    return price * quantity
