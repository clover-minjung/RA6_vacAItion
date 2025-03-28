from django.urls import path
from . import views


urlpatterns = [
    # 기본 CRUD 엔드포인트
    path('schedules/', views.ScheduleListCreateView.as_view(), name='schedule-list-create'),
    path('schedules/<int:pk>/', views.ScheduleDetailView.as_view(), name='schedule-detail'),
    path('add-recommended-place/', views.AddRecommendedPlaceView.as_view(), name='add-recommended-place'),
    path('recommended-places/', views.RecommendedPlaceListView.as_view(), name='recommended-place-list'),
    path('recommended-places/<int:pk>/', views.RecommendedPlaceDetailView.as_view(), name='recommended-place-detail'),
]