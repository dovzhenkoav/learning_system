from django.urls import path

from lms.views import ProductListView

app_name = 'lms'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
]
