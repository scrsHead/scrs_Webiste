# Generated by Django 2.0.2 on 2018-06-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='summary',
            field=models.TextField(),
        ),
    ]