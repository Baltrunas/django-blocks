# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _


class URL(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=256)
	url = models.CharField(verbose_name=_('URL or URL RegEx'), max_length=2048)
	regex = models.BooleanField(verbose_name=_('RegEx'), default=False)

	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['-created_at']
		verbose_name = _('URL')
		verbose_name_plural = _('URLs')


class Block(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=256)
	text = models.TextField(verbose_name=_('Text'), blank=True, null=True)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, help_text=_('A slug is the part of a URL which identifies a page using human-readable keywords'))

	PLACE_CHOICES = (
		('header', _('header')),
		('aside', _('aside')),
		('footer', _('footer')),
	)
	place = models.CharField(verbose_name=_('Place'), max_length=20, choices=PLACE_CHOICES)

	sites = models.ManyToManyField(Site, related_name='site_bloks', verbose_name=_('Sites'), null=True, blank=True)
	urls = models.ManyToManyField(URL, related_name='url_bloks', verbose_name=_('URLs'), null=True, blank=True)

	order = models.PositiveSmallIntegerField(verbose_name=_('Order'), default=500)

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['-created_at']
		verbose_name = _('Block')
		verbose_name_plural = _('Blocks')