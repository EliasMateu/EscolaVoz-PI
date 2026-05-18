from django.urls import path
from .views import (
    DashboardStatsView,
    DashboardByCategoryView,
    DashboardBySchoolView,
    DashboardExportView
)

urlpatterns = [
    path('stats/', DashboardStatsView.as_view(), name='dashboard-stats'),
    path('by-category/', DashboardByCategoryView.as_view(), name='dashboard-by-category'),
    path('by-school/', DashboardBySchoolView.as_view(), name='dashboard-by-school'),
    path('export/', DashboardExportView.as_view(), name='dashboard-export'),
]