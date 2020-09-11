# Generated by Django 2.2 on 2020-09-11 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rs_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.EmailField(blank=True, max_length=120, null=True)),
                ('content', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]
