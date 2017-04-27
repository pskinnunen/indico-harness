# Indico.io Example Scripts

1. Get an API key: https://indico.io/pay-per-call

1. Create a file with your key in ~/.indicorc

  > [auth]  
  > api_key = YOUR_API_KEY

1. Create virtualenv

  `python3 -m venv env`

1. Activate

  `source env/bin/activate`

1. Install requirements

  `pip3 install -r requirements.pip`

1. Run entry script

  `python3 index.py`