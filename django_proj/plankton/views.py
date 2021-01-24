from django.views import generic
from headlines.models import Headline  # bring News into the views


# class HomePageView(generic.ListView):
#     template_name = 'home.html'
#     context_object_name = 'articles'  # assign "News" object list to the object "articles"
#
#     # pass news objects as queryset for listview
#     def get_queryset(self):
#         return News.objects.all()

class HomePageView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'headlines'  # assign "Headline" object list to the object "headlines"

    # pass news objects as queryset for listview
    def get_queryset(self):
        return Headline.objects.all()

