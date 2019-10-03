import os

from django.conf import settings

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials, _GOOGLE_OAUTH2_TOKEN_ENDPOINT
from allauth.socialaccount.models import SocialToken


class YouTubeApi:

    def __init__(self, user):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        social_token = SocialToken.objects.filter(account__user=user).first()
        creds = Credentials(social_token.token, refresh_token=social_token.token_secret,
                            token_uri=_GOOGLE_OAUTH2_TOKEN_ENDPOINT,
                            client_id=social_token.app.client_id,
                            client_secret=social_token.app.secret)

        self.service = build('youtube', 'v3', credentials=creds)

        # self.youtube = googleapiclient.discovery.build(
        # api_service_name, api_version, credentials=credentials)

    def search(self):
        request = self.service.search().list(
            part="snippet",
            channelId="UCqrILQNl5Ed9Dz6CGMyvMTQ"
        )
        response = request.execute()

        print(response)

        return response['items']
