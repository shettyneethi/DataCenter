sudo apt-get update
sudo apt-get install -y python3 python3-pip git

STARTUP_SCRIPT=$(curl http://metadata/computeMetadata/v1/instance/attributes/startupscript -H "Metadata-Flavor: Google")
S_ACCOUNT_JSON=$(curl http://metadata/computeMetadata/v1/instance/attributes/serviceaccountjson -H "Metadata-Flavor: Google")
PYTHON_SCRIPT=$(curl http://metadata/computeMetadata/v1/instance/attributes/pythonscript -H "Metadata-Flavor: Google")

mkdir supportFiles
cd supportFiles

echo -e "$STARTUP_SCRIPT" > startup-script.sh
echo -e "$PYTHON_SCRIPT" > part3B.py
echo -e "$S_ACCOUNT_JSON" > service-credentials.json

sudo pip3 install google-api-python-client
sudo python3 part3B.py