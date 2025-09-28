from django.contrib import admin
from .models import TestTask
from pathlib import PurePosixPath
from django.utils import html
from django.conf import settings


@admin.register(TestTask)
class TeskTaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_pass', 'has_report', 
                    'report_url', 'create_time', 'update_time')
    
    def report_url(self, obj:TestTask):
        if obj.status == 3 and obj.has_report:
            case_path = PurePosixPath(str(obj.case))
            root_path = PurePosixPath(settings.MEDIA_URL)

            report_path = root_path / case_path.parent / 'report/index.html'
            return html.format_html(
                f"<a href='/{report_path}' targe='_blank'> 点击查看 </a>"
            )
        
    
