from django.db import models
import uuid
import os
from pathlib import Path
import pytest


def get_case_path(instance, filename):
    # save to 'tests/id/file'
    return os.path.join('tests', str(instance.id), filename)


class TestTask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)  # 主键不可编辑
    name = models.CharField('任务名称', max_length=100)
    case = models.FileField('用例文件', upload_to=get_case_path)

    status = models.IntegerField("测试状态", default=-1, choices=[
        (-2, '出现错误'),
        (-1, '初始化'),
        (0, '等待执行'),
        (1, '执行用例'),
        (2, '生成报告'),
        (3, '执行完毕'),
    ])

    is_processing = models.BooleanField('正在执行', default=False, editable=False)
    is_pass = models.BooleanField('是否通过', default=False, editable=False)
    has_report = models.BooleanField('拥有报告', default=False, editable=False)

    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('最后更新', auto_now=True)

    class Meta:  # 指定该模型在 Django 后台（Admin）中显示的单数和复数名称
        verbose_name_plural = verbose_name = '测试任务'
    
    def __str__(self):  # 定义模型实例的“字符串表示”
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status == 0 and self.is_processing is False:
            self.status = 1 
            self.is_processing = True
            self.save()  # 保存状态

            test_dir = Path(str(self.case.path)).parent
            ret = pytest.main_with(test_dir)

            if ret == pytest.ExitCode.OK:
                self.is_pass = True
            else:
                self.is_pass = False

            self.status = 2
            self.is_processing = True
            self.save()

            ret = os.system(f"allure generate -c -o {test_dir / 'report'} {test_dir / '.allure_results'}")

            if ret == 0:
                self.has_report = True
            else:
                self.has_report = False

            self.status = 3
            self.is_processing = False
            self.save()


