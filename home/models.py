from __future__ import unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
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
        InlinePanel('services', label="Services"),
    ]


class ServicePage(Orderable):
    page = ParentalKey(HomePage, related_name='services')
    title = models.TextField()
    text = models.TextField()
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1150x580"
    )

    panels = Page.content_panels + [
        FieldPanel('text'),
        ImageChooserPanel('image'),
    ]
