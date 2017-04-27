from django.shortcuts import render
from django.views.generic import FormView
from django import forms
from django.http import JsonResponse


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'message': self.success_message,
            }
            return JsonResponse(data)
        else:
            return response


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField()


class ContactFormView(AjaxableResponseMixin, FormView):
    form_class = ContactForm
    success_message = "I will be contacting you shortly!"
    success_url = "/"

    def form_valid(self, form):
        from django.core.mail import send_mail
        message = "%s\n\n%s" % (form.cleaned_data['message'], form.cleaned_data['name'])
        send_mail(
            "New Inquiry: %s" % form.cleaned_data['subject'],
            message,
            form.cleaned_data['email'],
            ['hello@derricksee.me'],
            fail_silently=False,
        )
        return super(ContactFormView, self).form_valid(form)
