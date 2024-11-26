Setting up a new project to experiment with serving an ML model through a web app.

This app will take selected birds and generate new dawn choruses from those bird combinations.

Starting with serving the model as a local api, to eventually move to some sort of cloud hosted service. More to come, stay tuned.


Steps to run the app locally

1. clone the repo
```git clone https://github.com/```

2. install virtual environment
```
pip install virtualenv
virtualenv <ENV-NAME>
source <ENV-NAME>/bin/activate
```

3.Install the required dependencies
```pip install -r requirements.txt```

4. Activate Streamlit and run app.py
```streamlit run app.py --server.port 8080```