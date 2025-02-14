# Generated by Django 3.2.16 on 2025-01-10 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Бокс для машины',
                'verbose_name_plural': 'Боксы для машины',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='ФИО')),
                ('discount', models.PositiveSmallIntegerField(default=0, verbose_name='Процент скидки')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.', unique=True, verbose_name='Идентификатор')),
                ('is_shown', models.BooleanField(default=True, verbose_name='Показывать услуги на главной странице')),
                ('name', models.CharField(max_length=256, verbose_name='ФИО')),
                ('photo', models.ImageField(blank=True, upload_to='master_images', verbose_name='Фото мастера')),
            ],
            options={
                'verbose_name': 'мастер',
                'verbose_name_plural': 'Мастера',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Время начала оказания услуги')),
            ],
            options={
                'verbose_name': 'временной слот',
                'verbose_name_plural': 'Временные слоты',
                'ordering': ('start_time',),
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.', unique=True, verbose_name='Идентификатор')),
                ('is_shown', models.BooleanField(default=True, verbose_name='Показывать услуги на главной странице')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Цена')),
                ('duration', models.DurationField(verbose_name='Продолжительность оказания')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='service.master', verbose_name='Мастер')),
            ],
            options={
                'verbose_name': 'услуга',
                'verbose_name_plural': 'Услиги',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='service.box', verbose_name='Бокс для машины')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='service.customer', verbose_name='Клиент')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='service.service', verbose_name='Услуга')),
                ('time_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='service.timeslot', verbose_name='Временной слот')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.AddField(
            model_name='master',
            name='slots',
            field=models.ManyToManyField(blank=True, null=True, related_name='masters', to='service.TimeSlot', verbose_name='Временной слот'),
        ),
        migrations.AddField(
            model_name='box',
            name='slots',
            field=models.ManyToManyField(blank=True, null=True, related_name='boxes', to='service.TimeSlot', verbose_name='Временной слот'),
        ),
    ]
