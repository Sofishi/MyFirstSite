from django.contrib.admin import AdminSite
from django.contrib.sites.admin import SiteAdmin
from django.contrib.sites.models import Site


class SofiaAdminSite(AdminSite):
    site_header = 'Sofia administration'
    site_title = 'Sofia site admin'

    def __init__(self, name='admin'):
        super().__init__(name)

    def has_permission(self, request):
        return request.user.is_superuser


admin_site = SofiaAdminSite(name='admin')

admin_site.register(Site, SiteAdmin)