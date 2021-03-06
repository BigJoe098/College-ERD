# Generated by Django 3.2.9 on 2022-01-12 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='class_model',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('semester', models.CharField(max_length=200)),
                ('section', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=200)),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('dob', models.DateField()),
                ('sex', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Other')], default=1, max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='create.department')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('USN', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('dob', models.DateField()),
                ('sex', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Other')], default=1, max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('class_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='create.class_model')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='create.course')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='create.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='create.department'),
        ),
        migrations.AddField(
            model_name='class_model',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='create.department'),
        ),
    ]
