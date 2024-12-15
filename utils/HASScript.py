import yaml
from .Error import InvalidFileExtension
class HASScript():
    def __init__(self, name: str):
        self._name = name
        self._script = None

    def init_script(self, script_path: str = None):
        """
        Function to get a home assistant script and convert to a
        processable dictionary.

        :param str script_path: Path to the script to be read. Script should be
        of type .hasscript  and follow Home Assistant YAML conventions.
        """
        try:
            with open(script_path) as f:
                script_as_dict = yaml.safe_load(f)
        except InvalidFileExtension as e:
            print(f"Error: {e}")
            raise
        except FileNotFoundError:
            print(f"Error: File '{script_path.split('/')[-1]}' not found in 'scripts' directory.")
            raise
        except yaml.YAMLError as e:
            print(f"Error: Failed to parse YAML file '{script_path.split('/')[-1]}'.")
            raise
        
        self._script = script_as_dict
    
    @property
    def script(self):
        return self._script

    @script.setter
    def script(self, script: dict):
        self._script = script
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name