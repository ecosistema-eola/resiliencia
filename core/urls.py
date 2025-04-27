from django.urls import path
from django.http import HttpResponse
from . import views

def healthz(request):
    return HttpResponse("OK")

urlpatterns = [
    # endpoint de health check para Railway (o cualquier orquestador)
    path('healthz/', healthz, name='healthz'),

    # rutas de tu app
    path('signup/',            views.signup,                       name='signup'),
    path('',                   views.dashboard,                    name='dashboard'),
    path('proposal/new/',      views.create_proposal,             name='create_proposal'),
    path('risks/',             views.list_risks,                   name='list_risks'),
    path('risks/new/',         views.upload_risk,                  name='upload_risk'),
    path('territory-risks/',   views.territory_risks_list,         name='territory_risks_list'),
    path('indicators/',        views.resilience_indicators_list,   name='resilience_indicators_list'),
    path('indicators/new/',    views.add_resilience_indicator,     name='add_resilience_indicator'),
    path('projects/',          views.project_list,                 name='project_list'),
    path('projects/new/',      views.create_project,               name='create_project'),
    path('intermediaries/',    views.list_intermediaries,          name='intermediary_list'),
    path('admin-dashboard/',   views.platform_admin_dashboard,     name='platform_admin_dashboard'),
]
