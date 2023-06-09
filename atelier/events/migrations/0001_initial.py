# Generated by Django 4.1.5 on 2023-02-03 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='TITLE')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('category', models.CharField(choices=[('Musique', 'Musique'), ('Cinema', 'Cinema'), ('Sport', 'Sport')], max_length=15)),
                ('state', models.BooleanField(default=False)),
                ('nbe_participant', models.IntegerField(default=0)),
                ('evt_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_participation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
