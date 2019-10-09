from django.conf.urls import url, include

from project_superlists.lists import views as lists_views

urlpatterns = [
    url(r"^$", lists_views.home_page, name="home"),
    url(r"^lists/the-only-list-in-the-world/$", lists_views.view_list, name="view_list"),
]
