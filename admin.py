from django.contrib import admin
from models import  *
from guardian.admin import GuardedModelAdmin
from reversion_compare.admin import CompareVersionAdmin

class option_to_contact(admin.TabularInline):
    model = ContactOptions
    fk_name = 'contact'
    extra = 1

class ContactRoleAdmin(CompareVersionAdmin):
    pass
admin.site.register(ContactRole, ContactRoleAdmin)

class ContactAdmin(CompareVersionAdmin):
    inlines = (option_to_contact, )
admin.site.register(Contact, ContactAdmin)

class ContactMethodAdmin(CompareVersionAdmin):
    pass
admin.site.register(ContactMethod, ContactMethodAdmin)

class ContactTypeAdmin(CompareVersionAdmin):
    pass
admin.site.register(ContactType, ContactTypeAdmin)