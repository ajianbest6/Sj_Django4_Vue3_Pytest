from django.db import models


class Task(models.Model):
    name = models.CharField("用例名称", max_length=20)
    case = models.FileField("用例文件", upload_to='tests/%Y_%m_%d_%H_%M_%S/')
    status = models.IntegerField("测试状态", choices=[
        (0, '未执行'),
        (1, '正在执行用例'),
        (2, '正在生成报告'),
        (3, '执行完毕')
    ])
