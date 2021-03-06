# Generated by Django 4.0.2 on 2022-02-19 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workoutdate', models.DateField()),
                ('instructor', models.CharField(max_length=50)),
                ('classlength', models.IntegerField()),
                ('title', models.CharField(max_length=250)),
                ('classdate', models.DateField()),
                ('totoutput', models.IntegerField()),
                ('avgoutput', models.IntegerField()),
                ('avgresistance', models.DecimalField(decimal_places=2, max_digits=2)),
                ('avgcadence', models.IntegerField()),
                ('distance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.CharField(max_length=500)),
            ],
        ),
    ]
