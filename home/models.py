from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class HomePage(Page):
    hero_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1920x1080"
    )
    hero_heading = models.TextField()
    hero_subheading = models.TextField()
    # About Me
    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="600x600"
    )
    about_text = models.TextField()

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel('hero_background'),
                FieldPanel('hero_heading'),
                FieldPanel('hero_subheading'),
            ],
            heading="Hero",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel('profile_image'),
                FieldPanel('about_text'),
            ],
            heading="About Me",
            classname="collapsible"
        ),
    ]


# class ServicePage(Page):
#     text = models.TextField()
#
#     content_panels = Page.content_panels + [
#         FieldPanel('text'),
#     ]
