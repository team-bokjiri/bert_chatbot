from django.db import models
from django.conf import settings


# Create your models here.


class UserChat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    my_chat = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.user

class Seoul(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'seoul'


class Dobong(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'dobong'


class Gangnam(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'gangnam'


class Gangdong(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'gangdong'


class Gangbuk(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'gangbuk'

class Gangseo(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'gangseo'


class Gwanak(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'gwanak'


class Gwangjin(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'gwangjin'


class Guro(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'guro'


class Geumcheon(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'geumcheon'


class Nowon(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'nowon'


class Dongdaemun(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'dongdaemun'


class Dongjak(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'dongjak'


class Mapo(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'mapo'


class Seodaemun(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'seodaemun'


class Seocho(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'seocho'


class Seongdong(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'seongdong'


class Seongbuk(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'seongbuk'


class Songpa(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'songpa'


class Yangcheon(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'yangcheon'


class Yeongdeungpo(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'yeongdeungpo'


class Yongsan(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'yongsan'

class Eunpyeong(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'eunpyeong'

class Jongno(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'jongno'


class Junggu(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'junggu'

class Jungnang(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.ForeignKey('Seoul', models.DO_NOTHING, db_column='num', blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    target = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'jungnang'


