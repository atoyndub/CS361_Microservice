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
where message is a JSON ojbect conforming to the structure outlined in this [diagram](uml_message_structure.jpeg).
Below is an example of a message object which conforms to this structure:
~~~
{
	"status": "run",
	"search term": "3",
	"data":
	{
		"A1": {"10":"11", "11":"12", "12":"13"}, 
		"A2": {"20":"21", "21":"22", "22":"23"}, 
		"A3": {"30":"31", "31":"32", "32":"33"},
		"A33": {"40":"41", "41":"42"}
	}
}
~~~
Note that "status" should be "run" for any inbound request. After a request has been sent, the
client should wait for a response from the server via recv_json() as below. Please note that
recv_json() is a blocking method.
~~~
response = socket.recv_json()
~~~
The server will send a JSON object in response, conforming to the same structure as the request message.
An example response from the server, which would be sent based on the request above, is as follows:
~~~
{
	"status": "done",
	"search term": "3",
	"data":
	{
		"A1": {"12":"13"}, 
		"A2": {"22":"23"}, 
		"A3": {"30":"31", "31":"32", "32":"33"}
	}
}
~~~
Note that "status" in the response will be "done", "search term" will match the value of that sent
in the request, and data will consist of any Collection and contained NoteCard entries with a key or value
containing the search term. Note that whether the Collection name property contains the search value is
irrelevant.

After a response has been received, the server
will again be ready to receive any additional request(s). A UML sequence diagram representing the full
sequence communication between the microservice server is viewable [here](uml_sequence_diagram.jpeg).