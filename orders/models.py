from django.db import models


# Order - заявка
# Actor - заявитель
# Position - должность заявителя
# Department - отдел заявителя


class Order(models.Model):
    """ заявка """
    title = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    actors = models.ManyToManyField('Actor', max_length=150, verbose_name="Заявитель")
    position = models.ManyToManyField('Position', max_length=150, verbose_name="Должность")
    department = models.ManyToManyField('Department', max_length=150, verbose_name="Отдел заявителя")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Actor(models.Model):
    """ Заявитель """
    name = models.CharField(max_length=150, verbose_name="ФИО")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заявитель"
        verbose_name_plural = "Заявители"


class Position(models.Model):
    """ Должность заявителя """
    title = models.CharField(max_length=150, verbose_name="Должность")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


class Department(models.Model):
    """ Отдел """
    title = models.CharField(max_length=150, verbose_name="Отдел")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"
