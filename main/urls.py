from django.urls import path
from .import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('details/<int:id>/', views.detail, name="detail"),
    path('addbooks/', views.add_books, name="add_books"),
    path('editbooks/<int:id>/', views.edit_books, name="edit_books"),
    path('deletebooks/<int:id>/', views.delete_books, name="delete_books"),
    path('addreview/<int:id>/', views.add_review, name="add_review"),
    path('editreview/<int:book_id>/<int:review_id>/', views.edit_review, name="edit_review"),
    path('deletereview/<int:book_id>/<int:review_id>/', views.delete_review, name="delete_review"),
]
