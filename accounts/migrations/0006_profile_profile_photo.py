# Generated by Django 4.1 on 2023-04-10 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_education_alter_profile_skill_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
