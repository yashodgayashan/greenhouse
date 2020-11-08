# Generated by Django 3.1.3 on 2020-11-06 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('site_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('api_key', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='units')),
                ('is_disabled', models.BooleanField(default=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=100)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_app.collection')),
            ],
        ),
    ]