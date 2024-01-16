from django.urls import path
from .views import DepartmentView


urlpatterns = [
    path('/department', DepartmentView.as_view()),
    path('/department/<str:id>',DepartmentView.as_view()),
]