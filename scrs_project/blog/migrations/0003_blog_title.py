# Generated by Django 2.0.2 on 2018-06-06 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]