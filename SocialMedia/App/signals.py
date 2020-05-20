from django.dispatch import Signal

new_notification = Signal(providing_args=["sendRequest"])