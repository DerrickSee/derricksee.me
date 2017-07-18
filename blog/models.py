from django.db import models
from django.utils.timezone import now

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, InlinePanel,
                                                MultiFieldPanel,
                                                PageChooserPanel, StreamFieldPanel)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
import secretballot

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class BlogPage(Page):
    date = models.DateField("Post date")
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1920x1080"
    )
    thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="800x600"
    )
    intro = models.TextField()
    summary = models.TextField()
    rating = models.DecimalField(decimal_places=1, max_digits=2, default=1)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('hero_image'),
        ImageChooserPanel('thumbnail'),
        FieldPanel('intro'),
        FieldPanel('summary'),
        StreamFieldPanel('body'),
    ]


secretballot.enable_voting_on(BlogPage)


class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
    ]

    class Meta:
        abstract = True


# Related links
class RelatedLink(LinkFields):
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


class BlogIndexPage(Page):
    paginate_by = 10
    intro = RichTextField(blank=True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1600x1000"
    )

    @property
    def blogs(self):
        blogs = BlogPage.objects.live().filter(
            date__lte=now().date()).descendant_of(self)
        blogs = blogs.order_by('-date')
        return blogs

    def get_context(self, request):
        blogs = self.blogs
        page = request.GET.get('page')
        paginator = Paginator(blogs, self.paginate_by) #count pages to display
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        context = super(BlogIndexPage, self).get_context(request)
        context['blogs'] = blogs
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        ImageChooserPanel('hero_image'),
    ]
