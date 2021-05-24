# Generated by Django 3.2.3 on 2021-05-24 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_rename_mutualfundsscheme_mutualfundscode'),
    ]

    operations = [
        migrations.CreateModel(
            name='MutualFundsScheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_house', models.CharField(max_length=255)),
                ('scheme_type', models.CharField(max_length=255)),
                ('scheme_category', models.CharField(max_length=255)),
                ('scheme_name', models.TextField()),
                ('scheme_start_date', models.DateField()),
                ('scheme_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mutual_funds_schemes', to='basic_app.mutualfundscode')),
            ],
        ),
    ]
