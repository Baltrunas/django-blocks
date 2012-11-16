# -*- utf-8 -*-
# import and register template library
from django import template
register = template.Library()

# import models
from blocks.models import Block
from blocks.models import URL
# import regex
import re


@register.simple_tag(takes_context=True)
def blocks_block(context, slug):
	request = context['request']

	block = False

	try:
		for url in URL.objects.all():
			if url.regex:
				url_re = re.compile(url.url)
				if url_re.findall(request.url):
					block = Block.objects.get(public=True, sites=request.site, urls=url, slug=slug)
			else:
				block = Block.objects.get(public=True, sites=request.site, urls__url=request.url, slug=slug)
	except:
		pass

	tpl = template.loader.get_template('blocks/block.html')
	return tpl.render(template.Context({'block': block}))
