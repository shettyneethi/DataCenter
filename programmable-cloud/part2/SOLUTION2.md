##PART 2:

I first created a snapshot of the disk(of instance created in part1)using the api and created 3 instances with allow-5000 tag using the snapshot. During each creation od each instance I have recorded the time in TIMING.md

It was found that time taken to create the instance from snapshop is lesser than creation of a new vm.

Start up script:
- Run the flask app (dont have to install as we copied the disk using snapshot)

Instructions to run:
   python part2.py

For this part I have used code given in https://github.com/GoogleCloudPlatform/python-docs-samples as suggested by the professor for creation and wait.