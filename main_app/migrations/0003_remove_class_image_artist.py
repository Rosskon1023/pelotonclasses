# Generated by Django 4.0.2 on 2022-02-28 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_class_avgresistance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='image',
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=100)),
                ('pelclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.class')),
            ],
            options={
                'ordering': ('-artist',),
            },
        ),
    ]
