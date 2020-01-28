import os
import json
from google.cloud import pubsub_v1
from FactivaStreams.listener import Listener
from FactivaStreams import logger


def main():
    gcp_project_id = os.getenv('GCP_PROJECT_ID', None)
    gcp_pubsub_topic = os.getenv('GCP_PUBSUB_TOPIC', None)
    gcp_creds = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', None)

    if gcp_project_id is not None and gcp_pubsub_topic is not None and gcp_creds is not None:
        logger.info("Sending messages to Pub/Sub topic {} in the GCP project {}".format(gcp_pubsub_topic, gcp_project_id))
        listener = Listener()
        ps_publisher = pubsub_v1.PublisherClient()
        topic_path = ps_publisher.topic_path(gcp_project_id, gcp_pubsub_topic)

        def callback(message, subscription_id, file_handle=None):
            callback.counter += 1
            logger.info("ACTION: {}, AN: {}".format(message['action'], message['an']))
            m_data = json.dumps(message, ensure_ascii=False).encode("utf-8")
            ps_publisher.publish(topic_path, data=m_data)
            return True

        callback.counter = 0
        listener.listen(callback)
    else:
        print("[ERROR]: Required ENV variables not set")
        if gcp_project_id is None:
            print("    - GCP_PROJECT_ID: GCP Project ID")
        if gcp_pubsub_topic is None:
            print("    - GCP_PUBSUB_TOPIC: GCP Pub/Sub Topic Name")
        if gcp_creds is None:
            print("    - GOOGLE_APPLICATION_CREDENTIALS: Path to Service Account JSON Credentials File")


if __name__ == '__main__':
    main()
