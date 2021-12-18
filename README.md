# RestAPITutorial
 Building a Rest API in Python

Python Rest API Crash course
Link: https://www.youtube.com/watch?v=qbLc5a9jdXo&list=PLj_dto2iVEP6eWSYjbBzhFccqy4u2HO52&index=5&t=51s

# How to use
    1) Open a terminal and run the activate.bat
    2) Open the ip address provided
    3) In a seperate terminal run the dbLayer.py python script
        - you will see data added in {ip}/drinks
        - if it existed prior remove the data.db file
        - alternitivly you can requests.delete one by one for the drinks
        - or change the values or the drinks
    4) Finally you can run the client.py that will send post request then delete
    
    
    Notes: obviously you need to have a python env set up with the required modules

## Rest API Notes
	- API - Aplication Programming Interface
	- Server and client
		- Client process can request from the server process
		- server process (app layer) will connect to db
	- JSON - JavaScript Object Notation
		- standard for API
		- key value pairs, like dictionaries
	- API end points - defines what you can request
		- different end points
        	- mainly GET, POST, DELETE, PUT
	-  REST - Representational State Transfer
		- request type : web
	- why not directly go from App to DB?
		- main concern is securitry
		- can go from web to moble easily
		- Modularity : can change tech and as long as the endpoint is the same it'll work
		- interoperability
	- OAUTH2 - security
	
	- Main commands
		- GET - retrive
		- POST - write new data
		- DELETE - delete
		- PUT - update data
			- post not garunteed, put can be ran multiple time (idempotent) 
			

