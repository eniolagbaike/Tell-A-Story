# Generated by Django 5.0.2 on 2024-03-07 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_book_book_cover_image_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='audio_file',
            new_name='audio',
        ),
    ]
