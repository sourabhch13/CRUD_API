from django.urls import path
from .views import DepartmentView,EmployeeView


urlpatterns = [
    path('/department', DepartmentView.as_view()),
    path('/department/<str:id>',DepartmentView.as_view()),
    path('/employee',EmployeeView.as_view()),
    path('/employee/<str:id>',EmployeeView.as_view())
]