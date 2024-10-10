from django.contrib import admin
from .models import Video
import subprocess
import os
import logging

logger = logging.getLogger(__name__)
# Register your models here.

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_file','id')
    search_fields=  ('title','id')
    list_filter= ('id','title')

    def get_search_results(self, request, queryset, search_term):
            queryset, use_distinct = super().get_search_results(request, queryset, search_term)
            if search_term.isdigit():
                queryset |= self.model.objects.filter(id=int(search_term))
            return queryset, use_distinct


