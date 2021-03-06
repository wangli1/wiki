# Generated by Django 2.1.7 on 2019-04-26 09:12

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnapp', '0002_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', DjangoUeditor.models.UEditorField(verbose_name='文章')),
                ('author', models.CharField(max_length=30, verbose_name='作者')),
            ],
        ),
        migrations.DeleteModel(
            name='article',
        ),
    ]
