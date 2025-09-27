from django.utils import html
from django.contrib import admin
from .models import Task
from pathlib import Path


# 注册 Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "status", "report_url")

    def save_model(self, request, obj: Task, form, change):
        super().save_model(request, obj, form, change)

        test_dir = Path(str(obj.case)).parent
        if obj.status == 1:
            # print("需要执行用例")
            # print("测试的存放路径", obj.case)
            # print("测试目录", test_dir)

            report_dir = test_dir / 'report'
            report_dir.mkdir(parents=True, exist_ok=True)
            index_path = report_dir / 'index.html'

            obj.status = 2
            try:
                with open(index_path, "w") as f:
                    f.write("hello world")
            except Exception as e:
                pass
            obj.status = 3  
            obj.save() 

    
    @admin.display(description="测试报告")
    def report_url(self, obj: Task):
        if obj.status == 3:
            report_url = Path(str(obj.case)).parent / 'report' / 'index.html'
            return html.format_html(
                f"<a href='/{report_url}' targe='_blank'> 点击查看 </a>"
            )
        else:
            return '-'