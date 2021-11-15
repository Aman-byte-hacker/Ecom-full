from django import template
from ecommerceapp.models import Product
register = template.Library()

@register.filter(name='wholeprice')
def wholeprice(product):
    return product.price - ((product.price*product.discount)/100)

