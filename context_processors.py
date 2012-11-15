# -*- coding: utf-8 -*
# import models
from blocks.models import Block
from blocks.models import URL
# import regex
import re


def page_blocks(request):
	try:
		page_blocks = []
		for url in URL.objects.all():
			if url.regex:
				url_re = re.compile(url.url)
				if url_re.findall(request.url):
					regex_urls_blocks = Block.objects.filter(public=True, sites=request.site, urls=url)
					page_blocks += regex_urls_blocks
			else:
				plain_urls_blocks = Block.objects.filter(public=True, sites=request.site, urls__url=request.url)
				page_blocks += plain_urls_blocks
		page_blocks_ids = [block.id for block in list(set(page_blocks))]
		page_blocks = Block.objects.filter(pk__in=page_blocks_ids).order_by('order')
	except:
		page_blocks = False
	return {
		'page_blocks': page_blocks
	}
