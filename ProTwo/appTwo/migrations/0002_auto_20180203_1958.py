# Generated by Django 2.0.1 on 2018-02-04 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=128)),
                ('date_opened', models.CharField(max_length=128)),
                ('crew_list', models.CharField(max_length=128)),
                ('project_manager', models.CharField(max_length=128)),
                ('flowrate', models.CharField(max_length=128)),
                ('current_treatmant', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
