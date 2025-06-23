from django.urls import path
from .views import CreateStudentView, DepartmentListAPIView, MajorListAPIView, StudentListView, AllStudentGetListView, create_student

urlpatterns = [
    path('api/students/', CreateStudentView.as_view(), name='create_student'),
    path('api/departments/all/', DepartmentListAPIView.as_view(), name='get-list-department'),
    path('api/majors/all/', MajorListAPIView.as_view(), name='get-list-major'),
    path('api/accounts/students/all', StudentListView.as_view(), name='get-student-by-account-id'),
    path('api/students/list-all', AllStudentGetListView.as_view(), name='get-list-all-student'),
    path('api/students/acreated', create_student, name='acreated-student'),
]