# Generated by Django 3.1.1 on 2020-11-05 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_api_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='image_url',
            new_name='background_image',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='api_id',
            new_name='game_id',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='platform',
            new_name='platforms',
        ),
        migrations.RemoveField(
            model_name='game',
            name='category',
        ),
        migrations.RemoveField(
            model_name='game',
            name='score',
        ),
        migrations.AddField(
            model_name='game',
            name='background_image_additional',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='dominant_color',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='released',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='saturated_color',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
