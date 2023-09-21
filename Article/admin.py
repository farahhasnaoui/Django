from django.contrib import admin, messages

from Article.models import Article


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'reporter', 'pub_date', 'pub_date', 'created_at', 'updated_at', 'est_valide')
    '''fields = (
        ('headline','reporter'),
        ('pub_date','created_at','updated_at','est_valide')
    )'''
    fieldsets = (
        (None, {'fields': ('headline', 'reporter')}),
        ('Dates', {'fields': ('pub_date', 'created_at', 'updated_at')}),
        ('State', {'fields': ('est_valide',)})
    )
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ['headline']
    list_filter = ('headline', 'pub_date')
    actions = ['set_to_valid', 'set_to_not_valid']

    def set_to_valid(self, request, queryset):
        queryset.update(est_valide=True)

    set_to_valid.short_description = 'validate'

    def set_to_not_valid(self, request, queryset):
        row_no_valid = queryset.filter(est_valide=False)
        if row_no_valid.count() > 0:
            messages.error(request, '%s this article is not valid' % row_no_valid.count())
        else:
            rows_update = queryset.update(est_valide=False)
            if rows_update == 1:
                message = "1 article was successfully updated"
            else:
                message = '%s articles were' % rows_update
            self.message_user(request, level='success', message='%s successfully marked as not valid' % message)
    # radio_fields = {'reporter':admin.VERTICAL}
# admin.site.register(Article,ArticleAdmin)
