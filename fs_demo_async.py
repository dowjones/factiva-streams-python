from time import sleep
from FactivaStreams.listener import Listener
from FactivaStreams import logger


def main():
    logger.info("*** Starting {} ***".format(__file__))
    listener = Listener()
    max_secs = 5
    logger.info("Receiving messages (ASYNC) for the next {} seconds.".format(max_secs))

    def callback(message, subscription_id):
        callback.counter += 1
        logger.info("ACTION: {}, AN: {}".format(message['action'], message['an']))
        return True

    callback.counter = 0
    future = listener.listen_async(callback)

    # Stop receiving messages after 5 seconds
    for count in range(0, max_secs):
        sleep(1)

    if future.running():
        future.cancel()

    logger.warning("Stop receiving messages!.")


if __name__ == '__main__':
    main()
