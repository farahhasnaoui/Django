from django.contrib import admin,messages
from datetime import datetime

# Register your models here.

from .models import *

class ParticipationInline(admin.StackedInline):
    model=Participation
    readonly_fields=('date_participation',)
    can_delete=False;

class ParticipantFilter(admin.SimpleListFilter):

    title='participant'
    parameter_name='nbe_participant'
    def lookups(self, request,AdminModel):
        return (
                 ('0','0 participant',),
                ('more','more participant')
        
        )

    def queryset(self, request, queryset):
        if self.value()=='0':
            return queryset.filter(nbe_participant__exact= 0)
        if self.value()== 'more':
            return queryset.filter(nbe_participant__gte = 0)


class DateFilter(admin.SimpleListFilter):

    title='Event Date'
    parameter_name='evt_date'
    def lookups(self, request,queryset):
          return (
                 ('Post Event','Post Event',),
                ('Today Event','Today participant'),
                ('upcoming Event',' upcoming participant')
        
        )

    def queryset(self, request, queryset):
        if self.value()=='Post Event':
            return queryset.filter(evt_date__lt = datetime.today)
        if self.value()== 'Today Event':
            return queryset.filter(evt_date__exact = datetime.today)
        if self.value()== 'upcoming Event':
            return queryset.filter(evt_date__gte = datetime.today)
    


def UpdateState(ModelAdmin,request,queryset) :   
    
    rows_update = queryset.update(state=False)
    if  rows_update == 1:
        msg='1 seule evenement'
    else :
        msg='plusieur'

        return  messages.success(request,message='%s modifier' % msg)    


UpdateState.short_description='refuse' 

def accept(obj,request,queryset):
        rows_update=queryset.update(state=True)
        if  rows_update == 1:
                msg='1 seule evenement'
        else :
                msg='plusieur'

        return  messages.success(request,message='%s modifier' % msg)    




# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
  
    def Participant_number(self,obj):
        val=obj.subscription.count()
        return val
    list_display=['title','category','state','Participant_number','created_at','evt_date']
    list_filter=['state','category',ParticipantFilter,DateFilter]
    search_fields=['title','category']
    list_per_page= 5
    ordering=['-title','-created_at','-evt_date']
    
    readonly_fields=['updated_at','created_at']
    autocomplete_fields=['organizer']

    fieldsets = [
        ['Event State',{
            'fields':['state',]
        } ],

        ['About' , {
            'classes':['collapse'],
            'fields':('title','description','image','category','nbe_participant'  , 'organizer')
        }],

        ['Date' , {
            'fields':['evt_date','updated_at','created_at']
        }]
    ]
    
    # pour afficher dans le dashboard ajouter des particiapnts en associaction avec levent lfouk hatina extra =1 ppour afficher une seule sinon il affiche par defaut 3 
    inlines=[ParticipationInline]
    actions=[UpdateState,accept]
    actions_on_bottom=True
    actions_on_top=False
class ParticipationEvent(admin.ModelAdmin):
    admin.site.register(Participation)
