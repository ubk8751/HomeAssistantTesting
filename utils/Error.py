class HomeAssistantException(Exception):
    def __init__(self, message: str):
        self._message = message
        super().__init__(message)


class InvalidFileExtension(HomeAssistantException):
    def __init__(self, script_name: str):
        self._script_name = script_name
        _message = f"The file extension of {script_name} is incorrect. The correct extension is '.hasscript'"
        super().__init__(_message)
    
    def __str__(self):
        return self._message
