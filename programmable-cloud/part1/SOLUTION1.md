##PART 1:

I have changed the code to specify the image family, ptoject, machine type while creating the instance.

Also I am recording the time it starts creating the instance and time it finishes. This info is stored in TIMING.md

while creating this instance I also provide the startup script to install and run flask application.

I have created firewall using the api to to accept any ip by giving 0.0.0.0/0, add tag alloW-5000 and for tcp protocol port 5000

Then I add the firewal tag to the instace as well. Hence I was able to access flask app useing its external ip with port 5000.

Start up script:
- Install all packages/flask
- Run the flask app

Instructions to run:
   python part1.py

For this part I have used code given in https://github.com/GoogleCloudPlatform/python-docs-samples as suggested by the professor for creation and wait.