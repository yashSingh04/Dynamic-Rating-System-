# Generated by Django 3.0.4 on 2020-08-08 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('imdb_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=220)),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('kind', models.CharField(max_length=15, null=True)),
                ('cover_url', models.URLField(max_length=500)),
                ('episode_of', models.CharField(max_length=50, null=True)),
                ('season', models.PositiveSmallIntegerField(null=True)),
                ('episode', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
    ]
