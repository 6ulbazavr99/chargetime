from django.contrib.auth.base_user import BaseUserManager

from charge.models import ChargeType


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        if not email:
            return ValueError('The given email must be set!')

        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        charge_types = kwargs.get('charge_types', [])

        # if charge_types:
        #     for charge_type in charge_types:
        #         charge_type = ChargeType.objects.get(pk=charge_type.id)
        #         user.charge_types.set(charge_type)
        if charge_types:
            charge_type_objects = ChargeType.objects.filter(pk__in=charge_types)
            user.charge_types.set(charge_type_objects)

        user.create_activation_code()
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('role', 'admin')
        kwargs.setdefault('balance', 9999)
        return self._create_user(email, password, **kwargs)
