# Generated by Django 2.1.7 on 2019-04-26 10:25

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learnapp', '0003_auto_20190426_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='page',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容'),
        ),
    ]
