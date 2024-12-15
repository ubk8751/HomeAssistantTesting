# Home Assistant Test environment

## Initiate repo

1. Clone repo: `git clone git@github.com:ubk8751/HomeAssistantTesting.git` (for SSH)
2. Setup virtual environment: `python3 python3 -m venv [venv_name]`
3. Activate virtual environment: `source [venv_name]/bin/activate`
4. Install requirements: `pip install -r requirements.txt`

## Test scripts

To test a script, run:

    python main.py [--script SCRIPT_NAME] [--debug]

The script should be in the `CWD/scripts/` directory, be a YAML file that follows Home Assistant YAML conventions.
