##PART 3:

part3.py just creates an instance and passes json, python script to run in vm1 to launch vm2, startup script of vm1 and vm2 as metadata.

Start up script:
- create files from the metadata(config,python,startup-script{for 2nd vm})
- Run the python script to 
	:launch new vm and run flask there

Python file is same as that we used for part1 except that it uses Service Account through the config passed to it.
Once VM 2 is launched it runs startup script to install and run flask app.

Instructions to run:
   python part3.py

For this part I have used code given in https://github.com/GoogleCloudPlatform/python-docs-samples as suggested by the professor for creation and wait.