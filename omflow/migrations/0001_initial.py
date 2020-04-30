# Generated by Django 2.2.4 on 2020-04-30 16:36

from django.db import migrations, models
import django.db.models.deletion
import omflow.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('omformflow', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueueData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('queue_id', models.TextField(blank=True, null=True, verbose_name='佇列編號')),
                ('name', models.CharField(max_length=50, verbose_name='名稱')),
                ('module_name', models.TextField(blank=True, null=True, verbose_name='模組名稱')),
                ('method_name', models.TextField(blank=True, null=True, verbose_name='方法名稱')),
                ('input_param', models.TextField(blank=True, null=True, verbose_name='輸入參數')),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SystemSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名稱')),
                ('value', models.TextField(verbose_name='值')),
                ('description', models.TextField(blank=True, null=True, verbose_name='說明')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='更新時間')),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='TempFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=omflow.models.get_file_path)),
                ('size', models.IntegerField(blank=True, verbose_name='大小')),
                ('file_name', models.TextField(blank=True, null=True, verbose_name='檔案名稱')),
                ('mapping_id', models.TextField(blank=True, null=True, verbose_name='對照編號')),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Scheduler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('exec_time', models.DateTimeField(blank=True, null=True, verbose_name='執行時間')),
                ('every', models.CharField(blank=True, max_length=50, null=True, verbose_name='每次')),
                ('cycle', models.CharField(blank=True, choices=[('ONCE', '執行一次'), ('SECONDLY', '每秒鐘'), ('MINUTELY', '每分鐘'), ('HOURLY', '每小時'), ('DAILY', '每天'), ('WEEKLY', '每週'), ('MONTHLY', '每月')], max_length=50, null=True, verbose_name='週期')),
                ('cycle_date', models.CharField(blank=True, max_length=50, null=True, verbose_name='週期執行日期')),
                ('exec_fun', models.CharField(max_length=50, verbose_name='執行功能')),
                ('input_param', models.TextField(verbose_name='輸入參數')),
                ('is_active', models.BooleanField(default=True, verbose_name='啟用/停用')),
                ('last_exec_time', models.TextField(blank=True, null=True, verbose_name='上次執行時間')),
                ('next_exec_time', models.TextField(blank=True, null=True, verbose_name='下次執行時間')),
                ('type', models.TextField(blank=True, null=True, verbose_name='分類')),
                ('flowactive', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specific_flowactive', to='omformflow.FlowActive')),
            ],
            options={
                'default_permissions': (),
            },
        ),
    ]
