from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from Station.models import ChargeType
from account.managers import CustomUserManager


class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('user', 'regular user'), ('staff', 'member of staff'), ('admin', 'administrator')
    )

    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(unique=True, blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    activation_code = models.CharField(max_length=255, default='waiting for confirmation')
    avatar = models.ImageField(upload_to='avatars', blank=True, default='avatar/default_avatar.jpg')
    balance = models.IntegerField(default=0)
    bonuses = models.IntegerField(default=0)
    role = models.CharField(choices=ROLE_CHOICES, default='User')
    charge_types = models.ManyToManyField(ChargeType, related_name='customusers', blank=True)

    is_active = models.BooleanField(
        _("active"),
        default=True,  # False for confirmation by email
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.username}'

    def create_activation_code(self):
        code = str(uuid4())
        self.activation_code = code
