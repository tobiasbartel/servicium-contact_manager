from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.template import Context, Template
from django import template
from models import ContactOptions
from main.settings import TEMPLATE_NAME
from pprint import pprint


def contact_box(request, list_of_contacts):
    output = ''
    for assigned_contact in list_of_contacts:
        my_contact_options = ContactOptions.objects.all().filter(contact = assigned_contact.contact)
        html = render_to_string('%s/contact_box.tpl.html' % TEMPLATE_NAME,
                                  {'my_contact': assigned_contact.contact, 'my_contact_options': my_contact_options,
                                   'my_role': assigned_contact.role, }, request=request)
        output += html.replace('\n', '').replace('\r', '')
        pprint(assigned_contact.contact.name)
    return output