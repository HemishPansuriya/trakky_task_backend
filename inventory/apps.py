from django.apps import AppConfig


class InventoryConfig(AppConfig):
    # This sets the default primary key field type for models in this app
    # BigAutoField means Django will use a large auto-incrementing integer as the primary key
    default_auto_field = 'django.db.models.BigAutoField'

    # This is the name of the Django app
    name = 'inventory'

    def ready(self):
        # The ready() method runs when the Django app is fully loaded
        # It is commonly used to import signals so that they get registered
        # when Django starts the application.

        # This line imports the signals.py file from the inventory app
        # Without this import, the signals inside signals.py will not run
        import inventory.signals
