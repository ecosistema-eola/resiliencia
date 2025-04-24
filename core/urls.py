from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.dashboard, name='dashboard'),
    path('proposal/new/', views.create_proposal, name='create_proposal'),

    # Módulo 1: Riesgos particulares
    path('risks/', views.list_risks, name='list_risks'),
    path('risks/new/', views.upload_risk, name='upload_risk'),

    # Módulo 2: Riesgos generales del territorio
    path('territory-risks/', views.territory_risks_list, name='territory_risks_list'),

    # ✅ Módulo 3: Indicadores de resiliencia
    path('indicators/', views.resilience_indicators_list, name='resilience_indicators_list'),
    path('indicators/new/', views.add_resilience_indicator, name='add_resilience_indicator'),

    # Módulo 4: Proyectos
    path('projects/', views.project_list, name='project_list'),
    path('projects/new/', views.create_project, name='create_project'),

    # Módulo 5
    path('intermediaries/', views.list_intermediaries, name='intermediary_list'),

    # Dashboard de Plataforma
    path('admin-dashboard/',views.platform_admin_dashboard,name='platform_admin_dashboard'),



]


