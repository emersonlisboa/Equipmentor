# Generated by Django 3.2 on 2021-05-31 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_equipment_fabricante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('time', models.IntegerField(help_text='Tempo em (min)')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('status', models.CharField(blank=True, choices=[('a', 'Ativo'), ('i', 'Inativo')], default='a', help_text='Equipamento availability', max_length=1)),
            ],
            options={
                'verbose_name_plural': 'Atividades',
            },
        ),
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('createdAt', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Corporação',
                'ordering': ['name', 'country'],
            },
        ),
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('status', models.CharField(blank=True, choices=[('a', 'Ativo'), ('i', 'Inativo')], default='a', max_length=1)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamento',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Employeer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('registerNumber', models.BigIntegerField()),
                ('status', models.CharField(blank=True, choices=[('a', 'Ativo'), ('i', 'Inativo')], default='a', max_length=1)),
                ('cargo', models.CharField(blank=True, choices=[('t', 'Técnico SMT'), ('e', 'Engenheiro SMT')], default='t', max_length=1)),
                ('departament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.departament')),
            ],
            options={
                'verbose_name': 'Colaborador',
                'verbose_name_plural': 'Colaborador',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('status', models.CharField(blank=True, choices=[('a', 'Ativo'), ('i', 'Inativo')], default='a', max_length=1)),
            ],
            options={
                'verbose_name': 'Fabricante',
                'verbose_name_plural': 'Fabricante',
                'ordering': ['name', 'country'],
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('status', models.CharField(blank=True, choices=[('a', 'Ativo'), ('i', 'Inativo')], default='a', max_length=1)),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Local',
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='book',
        ),
        migrations.DeleteModel(
            name='MyModelName',
        ),
        migrations.AlterModelOptions(
            name='equipment',
            options={'verbose_name': 'Equipamento', 'verbose_name_plural': 'Equipamento'},
        ),
        migrations.AddField(
            model_name='equipment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Ativo'), ('i', 'Inativo')], default='a', help_text='Equipamento availability', max_length=1),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.AddField(
            model_name='corporation',
            name='local',
            field=models.ManyToManyField(to='catalog.Local'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='local',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.local'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='fabricante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.factory'),
        ),
    ]
