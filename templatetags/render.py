# -*- utf-8 -*-
from django.template import Context
from django.template import Template

from django import template
register = template.Library()


@register.simple_tag
def render(text):
	try:
		tpl = Template(text)
		# context = Context({'message': 'Your message'})
		context = Context({})
		return tpl.render(context)
	except:
		return 'Render Error'
