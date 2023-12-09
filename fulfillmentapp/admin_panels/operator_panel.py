from django.contrib import admin


class OperatorPanel(admin.AdminSite):
    """Сайт оператора"""
    site_header = 'Fast Way'
    site_title = 'Fast Way'
    index_title = 'Главная страница'


operator_panel = OperatorPanel(name='operator_panel')
