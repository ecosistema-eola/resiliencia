from django.contrib import admin
from .models import Indicator, ProjectProposal

@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'value', 'updated_at')

@admin.register(ProjectProposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('title', 'proposer', 'created_at')
    search_fields = ('title', 'proposer__username')
