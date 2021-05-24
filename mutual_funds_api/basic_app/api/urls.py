from django.urls import path
from basic_app.api.views import MutualFundsSchemeListAPIView, MutualFundsCodeListAPIView

urlpatterns = [
    path('schemes/', MutualFundsSchemeListAPIView.as_view(), name='scheme-list'),
    path('codes/', MutualFundsCodeListAPIView.as_view(), name='code-list'),
]
