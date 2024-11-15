# Generated by Django 4.2.16 on 2024-11-15 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_fname', models.CharField(max_length=50)),
                ('act_gemder', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mov_title', models.CharField(max_length=50)),
                ('mov_year', models.IntegerField()),
                ('mov_time', models.IntegerField()),
                ('mov_lang', models.CharField(max_length=50)),
                ('mov_dl_rel', models.DateField()),
                ('mov_rel_country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev_starts', models.IntegerField()),
                ('num_o_ratings', models.IntegerField()),
                ('mov_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.movie')),
                ('rev_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.reviewer')),
            ],
        ),
        migrations.CreateModel(
            name='MovieCast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=30)),
                ('act_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.actor')),
                ('mov_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen_title', models.CharField(max_length=20)),
                ('mov_id', models.ManyToManyField(to='api.movie', verbose_name='movie')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dir_fname', models.CharField(max_length=50)),
                ('dir_lname', models.CharField(max_length=50)),
                ('mov_id', models.ManyToManyField(to='api.movie', verbose_name='Director movie')),
            ],
        ),
    ]