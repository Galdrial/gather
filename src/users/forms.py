from django_registration.forms import RegistrationForm
from users.models import CustomUser

class CustomUserRegistrationForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = CustomUser
        