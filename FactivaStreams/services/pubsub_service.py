from google.cloud.pubsub_v1 import SubscriberClient

from FactivaStreams.services import authentication_service
from FactivaStreams.services import credentials_service


def get_client(config):
    streaming_credentials = credentials_service.fetch_credentials(config)
    credentials = authentication_service.get_authenticated_oauth_credentials(streaming_credentials)

    return SubscriberClient(credentials=credentials)
