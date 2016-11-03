from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ContactMethod(models.Model):
    name = models.CharField(max_length=15, blank=False, null=False, db_index=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    url_pattern=models.CharField(max_length=200, blank=True, null=True, default=None, help_text="Use \"\%s\" where the value (Phone number, EMail address, ...) should be inserted.")
    human_pattern=models.CharField(max_length=200, blank=True, null=True, default=None, help_text="Use \"\%s\" where the value (Phone number, EMail address, ...) should be inserted.")

    def __unicode__(self):
        return self.name


class ContactType(models.Model):
    name = models.CharField(max_length=15, blank=False, null=False, db_index=True)
    image = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class ContactRole(models.Model):
    name = models.CharField(max_length=15, blank=False, null=False, db_index=True)
    image = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    type = models.ForeignKey(ContactType, blank=False, null=False)
    is_external = models.BooleanField(default=False)
    is_member_of = models.ForeignKey('self', related_name='member_of_team', limit_choices_to={'type__name': 'Team'}, blank=True, null=True, )

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class ContactOptions(models.Model):
    contact = models.ForeignKey(Contact, related_name='contact_to_option')
    method = models.ForeignKey(ContactMethod, related_name='method_to_option')
    value = models.CharField(max_length=100, blank=False, null=False)
    comment = models.CharField(max_length=200, blank=True, null=True)
    order = models.IntegerField(default=0)
    url = models.CharField(max_length=100, editable=False, blank=True, null=True)
    human_string = models.CharField(max_length=100, editable=False, blank=True, null=True)

    class Meta:
        ordering = ['order']
        unique_together = ('contact', 'method', 'value', )

    def save(self, *args, **kwargs):
        self.url = self.method.url_pattern.replace('%s', self.value)
        self.human_string = self.method.human_pattern.replace('%s',self.value)
        super(ContactOptions, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s: %s" % (self.contact.name, self.method.name)