Endpoint URLs:
    http://localhost:8000
    http://localhost:8000/search_name?name=name
    http://localhost:8000/search_iata?code=code

**Installation instructions for Debain/Ubuntu (with docker):**

If you have docker installed, you can open project directory in terminal and run this command:
    sudo docker compose up -d

Once it's completed, Now open browser and go to http://localhost:8000

You will get this output: {"message":"Welcome to the airport search API"}

To search airport with name (replace 'berlin' with any name of your choice):
    http://localhost:8000/search_name?name=berlin

To search airport with iata code (replace 'sfx' with any code of your choice):
    http://localhost:8000/search_iata?code=sfx



**Installation Instructions for Debain/Ubuntu (without docker):**
1. Install python 3.8 or up.
2. Install pip-python
To install python3 and pip:
    sudo apt update
    sudo apt install python3-pip

3. Install python libraries written in 'requirements.txt'
-> To install libraries directly from requirements.txt (make sure you're in same directory as the requirements.txt) run:
    pip3 install -r ./requirements.txt

4. Run server using:
    uvicorn app.main:app --host 0.0.0.0 --port 8000

*Wait for a while till server starts*
5. Now open browser and go to http://localhost:8000
or if you have curl installed, run this command in terminal:
    curl http://localhost:8000

You will get this output: {"message":"Welcome to the airport search API"}

To search airport with name (replace berlin with any name of your choice):
    http://localhost:8000/search_name?name=berlin
    
    or with curl:
    curl -X 'GET' 'http://localhost:8000/search_name?name=berlin' -H 'accept: application/json'


To search airport with iata code (replace sfx with any code of your choice):
    http://localhost:8000/search_iata?code=sfx

    or with curl:
    curl -X 'GET' 'http://localhost:8000/search_iata?code=sfx' -H 'accept: application/json'