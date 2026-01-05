from django.contrib import admin
from .models import Area, Categoria, Projeto, Material

# --- Configuração do Projeto ---
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    # Campos que aparecem na lista de projetos no Admin
    list_display = ('nome', 'responsavel', 'estado', 'receita', 'custos', 'lucro_display')
    list_filter = ('estado', 'responsavel', 'data_inicio')
    search_fields = ('nome', 'descricao')
    
    # Organização do formulário (Layout por secções)
    fieldsets = (
        ('Informação Básica', {
            'fields': ('nome', 'descricao', 'responsavel', 'estado', 'ativo')
        }),
        ('Prazos', {
            'fields': ('data_inicio', 'data_fim')
        }),
        ('Financeiro', {
            'fields': ('orcamento', 'custos', 'receita')
        }),
        ('Campos Personalizados (Utilizador)', {
            'fields': ('campo_custom_1', 'campo_custom_2', 'campo_custom_3', 'campo_custom_4'),
            'description': 'Espaços para personalização do utilizador.'
        }),
    )

    # Cálculo do lucro para exibição na lista
    def lucro_display(self, obj):
        return f"{obj.lucro}€"
    lucro_display.short_description = 'Lucro (Rec - Cust)'


# --- Configuração da Biblioteca ---
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'area', 'categoria', 'ano', 'ativo')
    list_filter = ('area', 'categoria', 'ativo')
    search_fields = ('titulo', 'autor')


# --- Registos Simples ---
admin.site.register(Area)
admin.site.register(Categoria)