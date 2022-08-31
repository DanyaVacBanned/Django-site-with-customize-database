from django.db import models

class Table(models.Model):
    division = models.CharField('Подразделение', max_length=40)
    subject = models.CharField('Сотрудник', max_length=40)
    fiz_face = models.CharField('Физ.лицо', max_length=40)
    tabel_time = models.IntegerField('Табель учёта времени')

    class Meta:
        verbose_name='Табель учёта рабочего времени'

    def get_absolute_url(self):
        return 'input/'
