from django.contrib.auth.mixins import UserPassesTestMixin

class StaffRequiredMixin(UserPassesTestMixin):
    """
    Mixin to restrict access to staff users only.
    """
    def test_func(self):
        return self.request.user.is_staff