#****************
#   CLIENT
#****************

#   adapted from demo code retrieved from https://zeromq.org/languages/python/

import zmq

PORT_NUM = 7077

msgTests = []
rspnsTests = []

msgTests.append(
    {
        "status": "run",
        "search term": "benkyou",
        "data":
        {
            "japanese": {"benkyou": "study", "noboru": "to climb"}, 
            "japanese2": {"benkyou suru": "to study"}, 
            "cs 361": {"CSH": "Cognitive Style Heuristics", "UML": "Unified Modelling Language"}
        }
    }
)
rspnsTests.append(
    {
        "status": "done",
        "search term": "benkyou",
        "data":
        {
            "japanese": {"benkyou": "study"}, 
            "japanese2": {"benkyou suru": "to study"} 
        }
    }
)

msgTests.append(
    {
        "status": "run",
        "search term": "n a",
        "data":
        {
            "A1": {"been apt": "study", "noboru": "to climb"}, 
            "A2": {"benkyou suru": "ran about"}, 
            "turn about": {"CSH": "Cognitive Style Heuristics", "UML": "Unified Modelling Language"}
        }
    }
)
rspnsTests.append(
    {
        "status": "done",
        "search term": "n a",
        "data":
        {
            "A1": {"been apt": "study"}, 
            "A2": {"benkyou suru": "ran about"}
        }
    }
)

msgTests.append(
    {
        "status": "run",
        "search term": "",
        "data":
        {
            "japanese": {"benkyou": "study", "noboru": "to climb"}, 
            "japanese2": {"benkyou suru": "to study"}, 
            "cs 361": {"CSH": "Cognitive Style Heuristics", "UML": "Unified Modelling Language"}
        }
    }
)
rspnsTests.append(
    {
        "status": "done",
        "search term": "",
        "data": {}
    }
)

msgTests.append(
    {
        "status": "run",
        "search term": "A",
        "data":
        {
            "A1": {}, 
            "A2": {}, 
            "A3": {}
        }
    }
)
rspnsTests.append(
    {
        "status": "done",
        "search term": "A",
        "data": {}
    }
)

msgTests.append(
    {
        "status": "run",
        "search term": "4",
        "data":
        {
            "A1": {"10":"11", "11":"12", "12":"13"}, 
            "A2": {"20":"21", "21":"22", "22":"23"}, 
            "A3": {"30":"31", "31":"32", "32":"33"}
        }
    }
)
rspnsTests.append(
    {
        "status": "done",
        "search term": "4",
        "data": {}
    }
)

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:" + str(PORT_NUM))

for i in range(len(msgTests)):

    socket.send_json(msgTests[i]) #send the test message
    print("\nCLIENT - sent message to server successfully")

    response = socket.recv_json() #blocks till message received
    print("CLIENT - received response from server successfully")

    if response == rspnsTests[i]: #compare to the expected response
        print("CLIENT - Response as expected")
    else:
        print("CLIENT - Response not as expected:\n" + str(response))

print("\nCLIENT - all tests completed")
