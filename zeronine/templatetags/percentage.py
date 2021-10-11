from django import template

register = template.Library()


@register.filter(name='percentage')
def percentage(product):
    total = product.get_total()
    target_price = product.target_price

    progress = str(int(min(500, total / target_price * 100)))

    return f'{progress}%'