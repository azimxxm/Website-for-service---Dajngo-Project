# Generated by Django 3.2.7 on 2021-09-27 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('info_title', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='Home/%Y/%M/')),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modal_texnology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_types', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service_about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('info_title', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='Service/%Y/%M/')),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service_about2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('info_title', models.TextField(max_length=200)),
                ('happy_customers', models.IntegerField(default=0)),
                ('issues_solved', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='Service_about2/%Y/%M/')),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('work_types', models.CharField(max_length=50)),
                ('comments', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='Testimonials/%Y/%M/')),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work_tpye',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_type_name', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service_modal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=50)),
                ('info_title1', models.TextField(max_length=200)),
                ('title2', models.CharField(max_length=50)),
                ('info_title2', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='Service_modal/%Y/%M/')),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('texnology', models.ManyToManyField(to='web.Modal_texnology')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50)),
                ('service_info', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=50)),
                ('color_icon', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('advantages', models.ManyToManyField(to='web.Advantages')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('info_title', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='Projects/%Y/%M/')),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('project_types', models.ManyToManyField(to='web.Projects_type')),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=12)),
                ('plan_price', models.BigIntegerField(default=0)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('plan_types', models.ManyToManyField(to='web.Plan_type')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('message', models.TextField(max_length=300)),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('work_tpye', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.work_tpye')),
            ],
        ),
    ]
