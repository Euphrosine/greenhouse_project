from django.urls import path
from . import views


urlpatterns ={
    path('dashboard/', views.display_chart_data, name='display_chart_data'),
    path('api/', views.chart_data_view, name='chart_data_view'),
    path('', views.add_temp, name="add_temperature"),
    
}