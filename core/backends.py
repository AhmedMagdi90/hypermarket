from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class PhoneOrUsernameModelBackend(ModelBackend):
    """
    Authenticate using username or phone number.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = None
        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)

        # Try username first
        try:
            user = User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            # Try phone search in UserProfile
            from .models import UserProfile
            try:
                profile = UserProfile.objects.get(phone=username)
                user = profile.user
            except UserProfile.DoesNotExist:
                return None

        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
