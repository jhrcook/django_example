# Generated by Django 2.2 on 2019-04-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20190407_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='website_images/Unknown.png', upload_to='projects/static/projects/img'),
        ),
    ]
