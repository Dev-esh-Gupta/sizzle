# Generated by Django 5.1.4 on 2025-01-06 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sizzle', '0003_alter_booktable_name_alter_feedback_user_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='image',
            field=models.ImageField(blank=True, upload_to='items/'),
        ),
    ]