from django.urls import path
from .views import DepartmentView,EmployeeView


urlpatterns = [
    path('/department', DepartmentView.as_view()),
    path('/department/<int:id>',DepartmentView.as_view()),
    path('/employee',EmployeeView.as_view()),
    path('/employee/<int:id>',EmployeeView.as_view())
]