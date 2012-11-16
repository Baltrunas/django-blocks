# django-blocks

## Required
* https://github.com/glavit/django-seo

## Install
* Add to INSTALLED_APPS 'blocks',
* ./manage.py syncdb

## How To Use
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

## Futures
* Model optimization:
** Block: area -> ???
** Add variants or make foregin key or just input for AREA_CHOICES

## I think about
Mmm... Donation...

## Changelog
### 2012.11.16
#### Add
* show_title
* Template Tag for block
* Render block
* Template Tag for area
* Clear template
* Translations
* Update README.md
* Add context to render

#### Fix
* Rename place to area
* Delete context_processors
* Model optimization
** URL: name -> title
** Block: text -> content
** PLACE_CHOICES -> AREA_CHOICES

### 2012.11.15
#### Add
* Start develop
