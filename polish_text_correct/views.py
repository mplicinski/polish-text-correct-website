from django.http.response import HttpResponseRedirect
from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import TextForm
from .algorithm import TextCorrect


class HomeView(FormView):
    template_name = 'home.html'
    form_class = TextForm
    success_url = reverse_lazy('home')


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

    def form_valid(self, form, **kwargs):
        text = form.cleaned_data['text']
        
        text_correct = TextCorrect()
        new_text = text_correct.run_correct(text)

        return self.render_to_response(
            self.get_context_data(
                form=form, 
                text=new_text,
                corrected="1"
            )
        )




