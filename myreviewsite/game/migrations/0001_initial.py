# Generated by Django 4.0.1 on 2023-03-02 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('comment', models.TextField(default='無し')),
                ('main_category', models.CharField(choices=[('シューティング', 'シューティング'), ('アクション', 'アクション'), ('ロールプレイング', 'ロールプレイング'), ('アドベンチャー', 'アドベンチャー'), ('レース', 'レース'), ('シミュレーション', 'シミュレーション'), ('ホラー', 'ホラー・サスペンス・推理'), ('サンドボックス', 'サンドボックス'), ('音楽', '音楽'), ('テーブル', 'テーブル'), ('その他', 'その他')], max_length=100)),
                ('score', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game_Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('score', models.IntegerField()),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]