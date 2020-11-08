# Generated by Django 3.1.3 on 2020-11-06 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='collections')),
                ('owner_id', models.CharField(max_length=100)),
                ('is_disabled', models.BooleanField(default=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=100)),
            ],
        ),
    ]