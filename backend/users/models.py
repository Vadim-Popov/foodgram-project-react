from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        'Email',
        max_length=settings.MAX_LENGTH_EMAIL,
        unique=True,)
    first_name = models.CharField(
        'Имя',
        max_length=settings.MAX_LENGTH_USER_NAME)
    last_name = models.CharField(
        'Фамилия',
        max_length=settings.MAX_LENGTH_USER_NAME)
    groups = models.ManyToManyField(Group, related_name='user_groups')
    user_permissions = models.ManyToManyField(Permission,
                                              related_name='user_permissions')
    subscribe = models.OneToOneField(
        'Subscribe',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Подписка',
        related_name='user_subscription',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('email',)

    def __str__(self):
        return self.email


class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор')
    created = models.DateTimeField(
        'Дата подписки',
        auto_now_add=True)

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ['user__username']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_subscription')]

    def __str__(self):
        return f'Пользователь {self.user} -> автор {self.author}'
