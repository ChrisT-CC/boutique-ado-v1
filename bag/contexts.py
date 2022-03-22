"""Add functionality to track what's in the shopping bag"""
from decimal import Decimal
from django.conf import settings


def bag_contents(request):
    """
    This is what's known as a context processor.
    And its purpose is to make a dictionary available to all templates across
    the entire application due to the presence of the built-in request context
    processor.

    In order to make this context processor available to the entire application
    it needs to be added to the list of context processors in the templates
    variable in settings.py
    """

    # Initialize variables
    bag_items = []
    total = 0
    product_count = 0

    # In order to entice customers to purchase more, we're going to give them
    # free delivery if they spend more than the amount specified in
    # the free_delivery_threshold in settings.py
    if total < settings.FREE_DELIVERY_THRESHOLD:

        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

        # Create a variable called free_delivery_delta
        # Used to let the user know how much more they need to spend to get
        # a free delivery
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    # Calculate the grand total
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
