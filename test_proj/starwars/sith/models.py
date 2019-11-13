from django.db import models


class Planet(models.Model):
    name = models.CharField('Название', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Планета'
        verbose_name_plural = 'Планеты'

    def __str__(self):
        return self.name


class Sith(models.Model):
    name = models.CharField('Имя', max_length=255)
    planet = models.ForeignKey(Planet,
                               on_delete=models.PROTECT,
                               verbose_name='Планета',
                               related_name='siths')

    class Meta:
        verbose_name = 'Ситх'
        verbose_name_plural = 'Ситхи'

    def __str__(self):
        return self.name


class Recruter(models.Model):
    name = models.CharField('Имя', max_length=255)
    planet = models.ForeignKey(Planet,
                               on_delete=models.PROTECT,
                               verbose_name='Планета',
                               related_name='recruters')
    age = models.PositiveIntegerField('Возраст')
    email = models.EmailField('Email', null=True, blank=True)
    sith = models.ForeignKey(Sith,
                             on_delete=models.CASCADE,
                             verbose_name='Ситх',
                             related_name='recruters',
                             null=True)

    class Meta:
        verbose_name = 'Рекрутер'
        verbose_name_plural = 'Рекрутеры'

    def __str__(self):
        return self.name


class TestExam(models.Model):
    orden_code = models.CharField('Код ордена', max_length=10, unique=True)

    class Meta:
        verbose_name = 'Тестовое испытание'
        verbose_name_plural = 'Тестовые испытания'

    def __str__(self):
        return self.orden_code


class Question(models.Model):
    content = models.TextField('Содержание вопроса')
    test_exam = models.ForeignKey(TestExam,
                                  on_delete=models.CASCADE,
                                  verbose_name='Тестовое испытание',
                                  related_name='questions')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.content


class Answer(models.Model):
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 verbose_name='Вопрос',
                                 related_name='answers')
    result = models.BooleanField('Да')
    recruter = models.ForeignKey(Recruter,
                                 on_delete=models.CASCADE,
                                 verbose_name='Рекрутер',
                                 related_name='answers')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return '{}:{}({})'.format(self.question.content[:30],
                                  self.result,
                                  self.recruter.name)
