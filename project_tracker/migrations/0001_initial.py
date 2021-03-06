# Generated by Django 3.1.1 on 2021-12-10 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import project_tracker.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTracker',
            fields=[
                ('id', models.CharField(default=project_tracker.models.project_tracker_generate_id, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('excavation', models.FloatField()),
                ('foundation', models.FloatField()),
                ('plinth_stage', models.FloatField()),
                ('gf_brick_work', models.FloatField()),
                ('gf_slab', models.FloatField()),
                ('first_floor_brick_work', models.FloatField()),
                ('first_slab', models.FloatField()),
                ('electrical_works', models.FloatField()),
                ('plumbing_works', models.FloatField()),
                ('wood_grill_works', models.FloatField()),
                ('internal_plastering', models.FloatField()),
                ('external_plastering', models.FloatField()),
                ('flooring_tiling', models.FloatField()),
                ('painting', models.FloatField()),
                ('finishing', models.FloatField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projecttracker', to='accounts.projectdetails')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_tracker', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Project Tracker',
            },
        ),
    ]
