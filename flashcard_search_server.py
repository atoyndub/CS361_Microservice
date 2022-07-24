#****************
#   SERVER
#****************

#   adapted from demo code retrieved from https://zeromq.org/languages/python/

import zmq

PORT_NUM = 7077

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.bind("tcp://*:" + str(PORT_NUM))

while True:
    msg = socket.recv_json() #blocks till message received
    print("\nSERVER - received message from client successfully")

    response = {"status":"done", "search term":"", "data":{}}

    #message validation
    if not "search term" in msg or msg["search term"] == "":
        socket.send_json(response)
        print("SERVER - sent response to client successfully")
        continue
    
    response["search term"] = msg["search term"]
    if not "data" in msg or not "status" in msg or msg["status"] != "run":
        socket.send_json(response)
        print("SERVER - sent response to client successfully")
        continue

    for collectionName in msg["data"]:
        collection = msg["data"][collectionName]

        for key in collection:
            value = collection[key]

            #key or value doesn't contain the search term
            if key.find(msg["search term"]) == -1 and value.find(msg["search term"]) == -1:
                continue

            #add the collection to the response object if not previously added
            if collectionName not in response["data"]:
                response["data"][collectionName] = {}
            response["data"][collectionName][key] = value #add the key/value pair to the response collection
    
    socket.send_json(response)
    print("SERVER - sent response to client successfully")
