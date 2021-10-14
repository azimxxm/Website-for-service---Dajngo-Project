from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import *

admin.site.site_header = "Hush kelibsiz Admin portalga!!!"
admin.site.site_title = "Sayt ma'muriyati"

admin.site.register(Advantages)
admin.site.register(Service)
admin.site.register(Home)
admin.site.register(Service_about)
admin.site.register(Modal_texnology)
admin.site.register(Service_modal)
admin.site.register(Service_about2)
admin.site.register(Projects_type)
admin.site.register(Projects)
admin.site.register(Testimonials)
admin.site.register(Plan_type)
admin.site.register(Pricing)
admin.site.register(Work_tpye)
admin.site.register(Contact)
