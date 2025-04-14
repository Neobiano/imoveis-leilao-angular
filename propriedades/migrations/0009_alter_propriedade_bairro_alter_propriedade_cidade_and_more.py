# Generated by Django 5.0.1 on 2025-04-11 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propriedades', '0008_propriedade_analise_matricula_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propriedade',
            name='bairro',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='cidade',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='codigo',
            field=models.CharField(db_index=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='desconto',
            field=models.DecimalField(blank=True, db_index=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='estado',
            field=models.CharField(db_index=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='latitude',
            field=models.DecimalField(blank=True, db_index=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='longitude',
            field=models.DecimalField(blank=True, db_index=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='quartos',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='tipo',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='tipo_imovel',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='valor',
            field=models.DecimalField(db_index=True, decimal_places=2, max_digits=12),
        ),
        migrations.AddIndex(
            model_name='propriedade',
            index=models.Index(fields=['estado', 'cidade'], name='propriedade_estado_569b46_idx'),
        ),
        migrations.AddIndex(
            model_name='propriedade',
            index=models.Index(fields=['estado', 'cidade', 'bairro'], name='propriedade_estado_9aeb2e_idx'),
        ),
        migrations.AddIndex(
            model_name='propriedade',
            index=models.Index(fields=['tipo_imovel', 'valor'], name='propriedade_tipo_im_f2dc39_idx'),
        ),
        migrations.AddIndex(
            model_name='propriedade',
            index=models.Index(fields=['desconto', 'valor'], name='propriedade_descont_85c0a3_idx'),
        ),
    ]
