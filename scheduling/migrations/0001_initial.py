# Generated by Django 4.1.7 on 2023-04-19 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LearningGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scheduling.language')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_teacher', models.BooleanField()),
                ('learning_groups', models.ManyToManyField(to='scheduling.learninggroup')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('description', models.CharField(max_length=200)),
                ('learning_group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scheduling.learninggroup')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='scheduling.userprofile')),
            ],
        ),
    ]
