from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from account.managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(blank=True, unique=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    activation_code = models.CharField(max_length=255, default='waiting for confirmation')
    avatar = models.ImageField(upload_to='avatars', blank=True, default='avatar/default_avatar.jpg')
    balance = models.IntegerField(default=0)
    bonuses = models.IntegerField(default=0)
    # charge_type =
    # role =

    is_active = models.BooleanField(
        _("active"),
        default=True,  # False for confirmation by email
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = CustomUserManager()
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}'

    def create_activation_code(self):
        code = str(uuid4())
        self.activation_code = code


# TODO: dohuya
