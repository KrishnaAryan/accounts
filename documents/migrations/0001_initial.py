# Generated by Django 3.1.1 on 2021-12-10 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import documents.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.CharField(default=documents.models.gallery_generate_id, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('project_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='accounts.projectdetails')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Gallery Image',
            },
        ),
        migrations.CreateModel(
            name='WorkingDrawings',
            fields=[
                ('id', models.CharField(default=documents.models.working_drawings_generate_id, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('open_schedule', models.ImageField(upload_to='image/')),
                ('joinery_details', models.ImageField(upload_to='image/')),
                ('plumbing_details', models.ImageField(upload_to='image/')),
                ('electrical', models.ImageField(upload_to='image/')),
                ('section', models.ImageField(upload_to='image/')),
                ('section_elevation', models.ImageField(upload_to='image/')),
                ('toilet_detailing', models.ImageField(upload_to='image/')),
                ('brick_work_layout', models.ImageField(upload_to='image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workingdrawings', to='accounts.projectdetails')),
            ],
            options={
                'verbose_name_plural': 'working Drawing',
            },
        ),
        migrations.CreateModel(
            name='TwoD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('two_d', models.ImageField(upload_to='two_d/')),
                ('gallery_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='two_d', to='documents.galleryimage')),
            ],
            options={
                'verbose_name_plural': 'Two-D',
            },
        ),
        migrations.CreateModel(
            name='ThreeDModel',
            fields=[
                ('id', models.CharField(default=documents.models.three_generate_id, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('three_d_elevation', models.ImageField(upload_to='image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='three_d', to='accounts.projectdetails')),
            ],
            options={
                'verbose_name_plural': 'Three-D Image',
            },
        ),
        migrations.CreateModel(
            name='ThreeD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('three_d', models.ImageField(upload_to='three_d/')),
                ('gallery_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='three_d', to='documents.galleryimage')),
            ],
            options={
                'verbose_name_plural': 'Three-D',
            },
        ),
        migrations.CreateModel(
            name='StructuralDrawings',
            fields=[
                ('id', models.CharField(default=documents.models.structural_drawing_generate_id, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('center_line_plan', models.ImageField(upload_to='image/')),
                ('footing_layout', models.ImageField(upload_to='image/')),
                ('column_details', models.ImageField(upload_to='image/')),
                ('plinth_beam_details', models.ImageField(upload_to='image/')),
                ('beam_layout', models.ImageField(upload_to='image/')),
                ('beam_details', models.ImageField(upload_to='image/')),
                ('slab_details', models.ImageField(upload_to='image/')),
                ('staircase_details', models.ImageField(upload_to='image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='structural_drawings', to='accounts.projectdetails')),
            ],
            options={
                'verbose_name_plural': 'structural Drawing',
            },
        ),
        migrations.CreateModel(
            name='OutsideImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outside', models.ImageField(upload_to='outside/')),
                ('gallery_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outside', to='documents.galleryimage')),
            ],
            options={
                'verbose_name_plural': 'Outside Image',
            },
        ),
        migrations.CreateModel(
            name='InsideImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inside', models.ImageField(upload_to='inside/')),
                ('gallery_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inside', to='documents.galleryimage')),
            ],
            options={
                'verbose_name_plural': 'Inside Image',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.CharField(default=documents.models.document_generate_id, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('boq', models.ImageField(upload_to='image/')),
                ('payments', models.ImageField(upload_to='image/')),
                ('projects_schedule', models.ImageField(upload_to='image/')),
                ('quality_checkList', models.ImageField(upload_to='image/')),
                ('specifications', models.ImageField(upload_to='image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='accounts.projectdetails')),
            ],
            options={
                'verbose_name_plural': 'document',
            },
        ),
        migrations.CreateModel(
            name='ConceptPlans',
            fields=[
                ('id', models.CharField(default=documents.models.concept_plan_generate_id, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('concept_plans', models.ImageField(upload_to='image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concept_plans', to='accounts.projectdetails')),
            ],
            options={
                'verbose_name_plural': 'concept Plan',
            },
        ),
        migrations.CreateModel(
            name='Agreements',
            fields=[
                ('id', models.CharField(default=documents.models.agreement_generate_id, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('booking_agreements', models.ImageField(upload_to='image/')),
                ('main_agreements', models.ImageField(upload_to='image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agreements', to='accounts.projectdetails')),
            ],
            options={
                'verbose_name_plural': 'agreement',
            },
        ),
    ]