# Generated by Django 2.0.1 on 2018-02-04 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0002_auto_20180203_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
