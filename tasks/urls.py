from django.urls import path
from .views import (
    ListTasksView, CreateTaskView, DetailTaskView,
    UpdateTaskView, SetTaskReadyView, SetTaskIncompleteView, SetTaskCompletedView,
    ListIncompleteTasksView, ListUnReviewedTasksView, ListCompletedTasksView,
    ReportHomeView, TasksJsonView
)

app_name = 'tasks'

urlpatterns = [
    path('', ListTasksView.as_view(), name='list_tasks'),
    path('incomplete/', ListIncompleteTasksView.as_view(), name='list_incomplete_tasks'),
    path('completed/', ListCompletedTasksView.as_view(), name='list_completed_tasks'),
    path('unreviewed/', ListUnReviewedTasksView.as_view(), name='list_unreviewed_tasks'),
    path('create/', CreateTaskView.as_view(), name='create_task'),
    path('<int:pk>/', DetailTaskView.as_view(), name='task_detail'),
    path('<int:pk>/edit/', UpdateTaskView.as_view(), name='edit_task'),
    path('<int:pk>/incomplete/', SetTaskIncompleteView.as_view(), name='set_task_incomplete'),
    path('<int:pk>/ready/', SetTaskReadyView.as_view(), name='set_task_ready'),
    path('<int:pk>/complete/', SetTaskCompletedView.as_view(), name='set_task_complete'),
    path('report/', ReportHomeView.as_view(), name='report_home'),
    path('report/task_by_status/json', TasksJsonView.as_view(), name='task_by_status_json'),
]
