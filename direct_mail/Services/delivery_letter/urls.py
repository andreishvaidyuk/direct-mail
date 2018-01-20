from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.TypeListView.as_view(),
        name='type-list'
    ),
]
