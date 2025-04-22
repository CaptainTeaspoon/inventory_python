from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import Users, UserProfile, Usergroups

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Use 'name' field instead of 'username'
            custom_user = Users.objects.get(name=username)
            
            # Simple password comparison (NOT SECURE FOR PRODUCTION)
            if custom_user.password == password:
                # Get or create a corresponding Django User
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    # Create a new Django User if one doesn't exist
                    user = User.objects.create_user(
                        username=username,
                        email=custom_user.email,
                        password=None  # Don't set password here as we'll use custom auth
                    )
                    user.set_unusable_password()  # We'll use our custom auth, not Django's password
                    user.save()
                
                # Make sure there's a UserProfile for this user
                try:
                    UserProfile.objects.get(user=user)
                except UserProfile.DoesNotExist:
                    UserProfile.objects.create(
                        user=user, 
                        Usergroup=custom_user.usergroup
                    )
                
                return user
            return None
        except Users.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
