from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class DevotionPage(Page):
    date = models.DateField(auto_now=True)
    scripture = models.CharField(max_length=50)
    observation = models.TextField()
    application = models.TextField()
    prayer = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('scripture'),
        FieldPanel('observation'),
        FieldPanel('application'),
        FieldPanel('prayer'),
    ]
