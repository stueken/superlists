import requests
from django.contrib.auth import get_user_model
User = get_user_model()
# import sys
# from accounts.models import ListUser

PERSONA_VERIFY_URL = 'https://verifier.login.persona.org/verify'
DOMAIN = 'localhost'


class PersonaAuthenticationBackend(object):

    def authenticate(self, assertion):
        response = requests.post(
            PERSONA_VERIFY_URL,
            data={'assertion': assertion, 'audience': DOMAIN}
        )
        if response.ok and response.json()['status'] == 'okay':
            email = response.json()['email']
            try:
                return User.objects.get(email=email)
            except User.DoesNotExist:
                return User.objects.create(email=email)


# class PersonaAuthenticationBackend(object):

#     def authenticate(self, assertion):
#         # Send the assertion to Mozilla's verifier service.
#         data = {'assertion': assertion, 'audience': 'localhost'}
#         print('sending to mozilla', data, file=sys.stderr)
#         resp = requests.post(
#             'https://verifier.login.persona.org/verify', data=data
#         )
#         print('got', resp.content, file=sys.stderr)

#         # Did the verifier respond?
#         if resp.ok:
#             # Parse the response
#             verification_data = resp.json()

#             # Check if the assertion was valid
#             if verification_data['status'] == 'okay':
#                 email = verification_data['email']
#                 try:
#                     return self.get_user(email)
#                 except ListUser.DoesNotExist:
#                     return ListUser.objects.create(email=email)

#     def get_user(self, email):
#         return ListUser.objects.get(email=email)
