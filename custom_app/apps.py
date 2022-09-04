from django.apps import AppConfig


class CustomAppConfig(AppConfig):
    name = 'custom_app'
    label = name
    verbose_name = 'LROSE Workflow App'
    fa_icon_class = 'fa-comment'
    url_home = 'custom_app:hello'
