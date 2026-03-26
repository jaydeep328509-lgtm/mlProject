import sys
from logger import logging # Assumes your previous logging code is saved in logger.py

def error_message_detail(error, error_detail: sys):
    # exc_info() returns (type, value, traceback)
    _, _, exc_tb = error_detail.exc_info()
    
    # Extracting the file name and line number from the traceback
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Initialize the base Exception class
        super().__init__(error_message)
        # Override the error message with our detailed custom string
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
    
if __name__=="__main__":
    try:
        a = 1 / 0
    except Exception as e:
        # 1. Create the custom exception object first
        custom_error = CustomException(e, sys)
        
        # 2. Log the detailed custom error message to your file
        # We use logging.error() instead of info() since it's an actual failure
        logging.error(custom_error) 
        
        # 3. Finally, crash the program and print to the console
        raise custom_error