from django.contrib.auth.models import User
import ldap
from rest_framework import authentication, exceptions

USERNAME = 'username'
PASSWORD = 'password'


class UniventionAuth(authentication.BasicAuthentication):

    def authenticate_credentials(self, userid, password, request=None):
        """
        Authenticate the userid and password against username and password
        with optional request for context.
        """

        # For ldap debugging, set trace_level=2
        l = ldap.initialize('ldaps://turing.cs.sunyit.edu')
        l.protocol_version = ldap.VERSION3
        username = f"cn={userid},cn=users,dc=cs,dc=sunyit,dc=edu"
        try:
            l.simple_bind_s(username, password)
            user = User.objects.get(username=userid)
        except ldap.INVALID_CREDENTIALS:
            raise exceptions.AuthenticationFailed('Invalid username/password.')
        except User.DoesNotExist:
            user = User.objects.create_user(username=userid, password=password)

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return user, None
