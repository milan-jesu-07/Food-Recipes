from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from recipe.models import Recipe


class Home(TemplateView):
    context = {}
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        user = request.user.id
        if user:
            return redirect('user-home')
        date = Recipe.objects.all()
        self.context['date'] = date
        return render(request, self.template_name, self.context)