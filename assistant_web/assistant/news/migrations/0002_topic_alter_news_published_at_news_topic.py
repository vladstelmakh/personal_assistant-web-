# Generated by Django 4.2.6 on 2023-10-23 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='published_at',
            field=models.CharField(max_length=30),
        ),
        migrations.AddField(
            model_name='news',
            name='topic',
            field=models.ForeignKey(default=100, on_delete=django.db.models.deletion.CASCADE, to='news.topic'),
        ),
    ]
