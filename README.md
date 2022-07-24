## ZMQ Library Setup
The following instructions assume that the necessary ZMQ library has been setup, and provide
sample code in Python, adapted from that available at https://zeromq.org/languages/python/.
For details regarding how to import the ZMQ library, view language-specific
instructions accessible from: https://zeromq.org/get-started/.
## Server Setup
Run flashcard_search_server.py (this server process loops infinitely until killed).
## Client Code
Initially connect to the socket bound by the server at port number 7077 as follows: 
~~~
import zmq
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:7077")
~~~
## Requesting Service and Receiving Response
After connecting to the server, send a request as follows:
~~~
socket.send_json(message)
~~~
where message is an ojbect (in this case a Python object) conforming to the structure
outlined in this [diagram](uml_message_structure.jpeg). After a request has been sent, the
client should wait for a response from the server as follows:
~~~
response = socket.recv_json()
~~~
Please note that recv_json() is a blocking function. After a response has been received, the server
will again be ready to receive any additional request(s). A UML sequence diagram representing the full
sequence communication between the microservice server is viewable [here](uml_sequence_diagram.jpeg).