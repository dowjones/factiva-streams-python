How To Use
----------

This library is for Dow Jones customers consuming a Dow Jones Factiva Streams.

This project is designed for clone > set env variables > run. See details below.


Auth
-----------

There are two ways to authenticate.

- Your User Key

- UserId, ClientId and Password


Configuring
___________

To run this code, you need to provide credentials from one of the authentication methods and your subscriptions. There are 3 ways to do this. You can either set environment variables or you can use a configuration file.

1. Set environment variables.
###################################################################

To set your service account credentials, set either:

- An environment variable named 'USER_KEY'.
- Three environment variable named 'USER_ID', 'CLIENT_ID', and 'PASSWORD'.

To set your subscription ID, simply set an environment variable named 'SUBSCRIPTION_ID' like so

.. code-block::

    export SUBSCRIPTION_ID="ABC1234567889"


To be clear, the code above is the command line expression for setting this environment variable on Mac OSX. Other operating systems might have a slightly different techniques for setting environment variables on the command line.

2. Using the configuration file.
###################################################################

In this codebase you will find a file named 'customer_config.json'. You are not required to use this file. If you prefer to use this configuration file, follow these directions: Open this file and add your service account credentials. Then add your subscription IDs. Remember that this is a JSON file so follow basic JSON formatting and syntax conventions.

3. Pass in variables as function arguments.
###################################################################

You may pass your service account credentials (user_id, client_id, and password) to the Listener constructor like so:

.. code-block:: python

    from FactivaStream.listener import Listener
    # User key authentication
    listener = Listener(user_key=<YOUR USER KEY>)

    # UserId, ClientId and Password authentication
    listener = Listener(user_id=<YOUR USER ID>, client_id=<YOUR_CLIENT_ID>, password=<YOUR_PASSWORD>)


Or you may use the environment variables.
Remember that passing credentials and subscription ID(s) in this way will override the environment variable and the config file settings.

.. code-block:: python

    from FactivaStream.listener import Listener

    listener = Listener()


4. Listening to messages
###################################################################

You may want to listen messages synchronously like so:

.. code-block:: python

    def callback(message, subscription_id, file_handle=None):
        print("ACTION: {}, AN: {}".format(message['action'], message['an']))
        return True

    listener.listen(callback)


This method is implemented in the script fs_demo_sync.py.

You may want to listen messages asynchronously like so:

.. code-block:: python

    def callback(message, subscription_id):
        print("ACTION: {}, AN: {}".format(message['action'], message['an']))

    future = listener.listen_async(callback)
    # After calling `listen_async` you need to keep the main thread alive.

    for count in range(0, 5):
        sleep(1)

    # Stop receiving messages after 5 seconds
    if future.running():
        future.cancel()

This method is implemented in the script fs_demo_async.py.

Log Files
_________

Minimal logging is written to the path 'logs'. This log can be configured with multiple levels and messages are appended across executions, so it is a good idea to have log maintenance procedures in production environments.


Running the Demonstration Code/Development
__________________________________________

If you are enhancing this codebase (and not just using it as a library), follow these example MacOS steps:

1. Checkout the Project from Git.
###################################################################

2. Go to the Project Root.
###################################################################

3. Create a Virtual Environment.
###################################################################

.. code-block::

    virtualenv venv


4. Then activate the virutal environment by executing this command:
###################################################################

.. code-block::

    source ./venv/bin/activate


5. Install the Dependencies
###################################################################

.. code-block::

    pip install -r requirements.txt


6. Set the Configuration Variables
###################################################################

See the config section.

7. Run the Demo Code
###################################################################

Execute the following at the project root:

.. code-block::

    python fs_demo_sync.py

Or

.. code-block::

    python fs_demo_async.py

