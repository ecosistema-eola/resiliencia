from django.shortcuts            import render, redirect
from django.contrib.auth         import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import (
    Indicator,
    ProjectProposal,
    Risk,
    ResilienceIndicator,
    Project,
    Profile
)
from .forms import (
    IndicatorForm,
    ProposalForm,
    SignUpForm,
    RiskForm,
    ResilienceIndicatorForm,
    ProjectForm
)

@login_required
def dashboard(request):
    # ————— Gestión del indicador base —————
    indicator, created = Indicator.objects.get_or_create(user=request.user)
    if created:
        indicator.value = 0
        indicator.save()

    if request.method == 'POST':
        form = IndicatorForm(request.POST, instance=indicator)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = IndicatorForm(instance=indicator)

    # ————— Obtención de propuestas —————
    proposals = ProjectProposal.objects.all()

    # Contexto común
    context = {
        'indicator': indicator,
        'form': form,
        'proposals': proposals,
    }

    # ————— Selección de plantilla según rol —————
    role = request.user.profile.role
    if role == 'company_small':
        template = 'core/dashboard_company_small.html'
    elif role == 'company_large':
        template = 'core/dashboard_company_large.html'
    elif role == 'environmental_intermediary':
        template = 'core/dashboard_intermediary.html'
    else:
        template = 'core/dashboard.html'

    return render(request, template, context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

@login_required
def list_risks(request):
    risks = Risk.objects.filter(owner=request.user, is_territory=False)
    return render(request, 'core/risk_list.html', {'risks': risks})

@login_required
def upload_risk(request):
    if request.method == 'POST':
        form = RiskForm(request.POST, request.FILES)
        if form.is_valid():
            risk = form.save(commit=False)
            risk.owner = request.user
            risk.save()
            return redirect('list_risks')
    else:
        form = RiskForm()
    return render(request, 'core/risk_form.html', {'form': form})

@login_required
def territory_risks_list(request):
    risks = Risk.objects.filter(is_territory=True)
    return render(request, 'core/territory_risk_list.html', {'risks': risks})

@login_required
def resilience_indicators_list(request):
    indicators = ResilienceIndicator.objects.all().order_by('risk_focus', 'year_target')
    return render(request, 'core/resilience_indicator_list.html', {'indicators': indicators})

@login_required
def add_resilience_indicator(request):
    if request.user.profile.role != 'admin_territorial':
        return redirect('dashboard')
    if request.method == 'POST':
        form = ResilienceIndicatorForm(request.POST)
        if form.is_valid():
            indicator = form.save(commit=False)
            indicator.uploaded_by = request.user
            indicator.save()
            return redirect('resilience_indicators_list')
    else:
        form = ResilienceIndicatorForm()
    return render(request, 'core/resilience_indicator_form.html', {'form': form})

@login_required
def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'core/project_list.html', {'projects': projects})

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.proposer = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'core/project_form.html', {'form': form})

@login_required
def list_intermediaries(request):
    intermediaries = Profile.objects.filter(role='environmental_intermediary')
    return render(request, 'core/intermediary_list.html', {'intermediaries': intermediaries})

@login_required
def platform_admin_dashboard(request):
    # Solo el Administrador de Plataforma puede acceder
    if request.user.profile.role != 'platform_admin':
        return redirect('dashboard')

    context = {
        'users':          User.objects.all(),
        'risks':          Risk.objects.all(),
        'indicators':     ResilienceIndicator.objects.all(),
        'projects':       Project.objects.all(),
        'intermediaries': Profile.objects.filter(role='environmental_intermediary'),
    }
    return render(request, 'core/platform_admin_dashboard.html', context)


@login_required
def create_proposal(request):
    if request.method == 'POST':
        form = ProposalForm(request.POST)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.proposer = request.user
            proposal.save()
            return redirect('dashboard')
    else:
        form = ProposalForm()

    return render(request, 'core/proposal_form.html', {'form': form})
