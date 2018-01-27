from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.TypeListView.as_view(),
        name='type-list'
    ),
    url(
        regex=r'^delivery/$',
        view=views.LetterFormView.as_view(),
        name='delivery'
    ),
    url(
        regex=r'^only_delivery/$',
        view=views.LetterOnlyDeliveryFormView.as_view(),
        name='only_delivery'
    ),
]
