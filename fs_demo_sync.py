import json
from FactivaStreams.listener import Listener
from FactivaStreams import logger


def main():
    logger.info("*** Starting {} ***".format(__file__))
    listener = Listener()

    def callback(message, subscription_id, file_handle=None):
        callback.counter += 1
        logger.info("ACTION: {}, AN: {}".format(message['action'], message['an']))
        if file_handle is not None:
            file_handle.writelines(["{}\n".format(json.dumps(message))])
        return True

    callback.counter = 0
    listener.listen(callback, maximum_messages=20)


if __name__ == '__main__':
    main()
