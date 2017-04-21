from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel




class HomePage(Page):
    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="180x220"
    )
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="650x450"
    )
    profile_text = models.TextField()
    feature_title = models.TextField()
    feature_text = models.TextField()


    content_panels = Page.content_panels + [
        ImageChooserPanel('profile_image'),
        ImageChooserPanel('background_image'),
        FieldPanel('profile_text'),
        FieldPanel('feature_title'),
        FieldPanel('feature_text'),
    ]
