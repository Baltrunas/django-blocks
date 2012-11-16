django-blocks
=============

# Required
* https://github.com/glavit/django-seo

# Install
* Add to INSTALLED_APPS 'blocks',
* ./manage.py syncdb

# How To Use
* Show all area blocks

```html
{% load blocks_area %}
{% blocks_area 'area_name' %}
```

* Show one block

```html
{% load blocks_block %}
{% blocks_block 'block_slig' %}
```

# Futures
* Translations
* Update readme
* Add context to render

# Changelog
## 2012.11.16
### Add
* show_title
* Template Tag for block
* Render block
* Template Tag for area
* Clear template

### Fix
* Rename place to area
* Delete context_processors

## 2012.11.15
### Add
* Start develop
