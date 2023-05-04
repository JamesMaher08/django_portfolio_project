from django.urls import path
from .views import TransactionListView, TransactionDetailView, TransactionCreateView, TransactionUpdateView, TransactionDeleteView
from . import views

urlpatterns = [
    path('', TransactionListView.as_view(), name="portfolio-home"),
    path('transaction/<int:pk>/', TransactionDetailView.as_view(), name="transaction-detail"),
    path('transaction/new/', TransactionCreateView.as_view(), name="transaction-create"),
    path('transaction/<int:pk>/update/', TransactionUpdateView.as_view(), name="transaction-update"),
    path('transaction/<int:pk>/delete/', TransactionDeleteView.as_view(), name="transaction-delete"),
    path('about/', views.about, name="portfolio-about"),
]

