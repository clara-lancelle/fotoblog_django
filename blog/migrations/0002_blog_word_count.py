# Generated by Django 4.2.1 on 2023-06-15 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='word_count',
            field=models.IntegerField(null=True),
        ),
    ]