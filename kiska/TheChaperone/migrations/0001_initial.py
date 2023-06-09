# Generated by Django 4.1.3 on 2023-05-25 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdStatus',
            fields=[
                ('id_AdStat', models.AutoField(primary_key=True, serialize=False)),
                ('name_AdStat', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'AdStatus',
            },
        ),
        migrations.CreateModel(
            name='Bodywork',
            fields=[
                ('id_Body', models.AutoField(primary_key=True, serialize=False)),
                ('name_Body', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Bodywork',
            },
        ),
        migrations.CreateModel(
            name='CarCat',
            fields=[
                ('id_CarCat', models.AutoField(primary_key=True, serialize=False)),
                ('name_Cat', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'CarCat',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id_City', models.AutoField(primary_key=True, serialize=False)),
                ('name_City', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'City',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id_Color', models.AutoField(primary_key=True, serialize=False)),
                ('name_Color', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Color',
            },
        ),
        migrations.CreateModel(
            name='DamageStatus',
            fields=[
                ('id_Dam', models.AutoField(primary_key=True, serialize=False)),
                ('name_Dam', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'DamageStatus',
            },
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id_Fuel', models.AutoField(primary_key=True, serialize=False)),
                ('name_Fuel', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'FuelType',
            },
        ),
        migrations.CreateModel(
            name='Handlebar',
            fields=[
                ('id_Hand', models.AutoField(primary_key=True, serialize=False)),
                ('name_Hand', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Handlebar',
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id_Mark', models.AutoField(primary_key=True, serialize=False)),
                ('name_Mark', models.CharField(max_length=50)),
                ('photo_Mark', models.ImageField(blank=True, null=True, upload_to='photo_mark')),
            ],
            options={
                'db_table': 'Mark',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id_Roles', models.AutoField(primary_key=True, serialize=False)),
                ('name_Roles', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id_Trans', models.AutoField(primary_key=True, serialize=False)),
                ('name_Trans', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Transmission',
            },
        ),
        migrations.CreateModel(
            name='TypeOfEngine',
            fields=[
                ('id_TypeEng', models.AutoField(primary_key=True, serialize=False)),
                ('name_TypeEng', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'TypeOfEngine',
            },
        ),
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('id_UserStat', models.AutoField(primary_key=True, serialize=False)),
                ('name_UserStat', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'UserStatus',
            },
        ),
        migrations.CreateModel(
            name='Wheeldrive',
            fields=[
                ('id_Wheel', models.AutoField(primary_key=True, serialize=False)),
                ('name_Wheel', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Wheeldrive',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_User', models.AutoField(primary_key=True, serialize=False)),
                ('log_User', models.CharField(max_length=50)),
                ('pass_User', models.CharField(max_length=50)),
                ('phone_User', models.CharField(max_length=50)),
                ('email_User', models.CharField(max_length=50)),
                ('name_User', models.CharField(max_length=50)),
                ('surname_User', models.CharField(max_length=50)),
                ('birth_User', models.DateField()),
                ('city_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.city')),
                ('role_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.roles')),
                ('status_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.userstatus')),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Models',
            fields=[
                ('id_Mod', models.AutoField(primary_key=True, serialize=False)),
                ('name_Mod', models.CharField(max_length=50)),
                ('name_Mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.mark')),
            ],
            options={
                'db_table': 'Models',
            },
        ),
        migrations.CreateModel(
            name='Metro',
            fields=[
                ('id_Met', models.AutoField(primary_key=True, serialize=False)),
                ('name_Met', models.CharField(max_length=50)),
                ('name_City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.city')),
            ],
            options={
                'db_table': 'Metro',
            },
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id_Engine', models.AutoField(primary_key=True, serialize=False)),
                ('name_Engine', models.CharField(max_length=50)),
                ('hp_Engine', models.IntegerField(default=1)),
                ('capacity_Engine', models.DecimalField(decimal_places=2, max_digits=20)),
                ('fuel_Engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.fueltype')),
                ('type_Engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.typeofengine')),
            ],
            options={
                'db_table': 'Engine',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id_Car', models.AutoField(primary_key=True, serialize=False)),
                ('vin_Car', models.CharField(max_length=50)),
                ('year_Car', models.DateField()),
                ('statenum_Car', models.CharField(max_length=50)),
                ('numown_Car', models.IntegerField(default=1)),
                ('mileage_Car', models.IntegerField(default=1)),
                ('photo_Car', models.ImageField(blank=True, null=True, upload_to='photo_сar')),
                ('body_Car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.bodywork')),
                ('cat_Car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.carcat')),
                ('color_Car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.color')),
                ('damage_Car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.damagestatus')),
                ('engine_Car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.engine')),
                ('handle_Car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.handlebar')),
                ('model_Car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.models')),
                ('trans_Car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.transmission')),
                ('user_Car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.user')),
                ('wheel_Car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.wheeldrive')),
            ],
            options={
                'db_table': 'Car',
            },
        ),
        migrations.CreateModel(
            name='Advertisment',
            fields=[
                ('id_Ad', models.AutoField(primary_key=True, serialize=False)),
                ('comm_Ad', models.CharField(max_length=280)),
                ('date_Ad', models.DateField()),
                ('price_Ad', models.DecimalField(decimal_places=2, max_digits=20)),
                ('contact_Ad', models.CharField(max_length=140)),
                ('car_Ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.car')),
                ('loc_Ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.metro')),
                ('status_Ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.adstatus')),
                ('user_Ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheChaperone.user')),
            ],
            options={
                'db_table': 'Advertisment',
            },
        ),
    ]
