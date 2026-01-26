import datetime

class BudgetLogger:
    # en class för att kunna hantera loggning till fil.
    
    def __init__(self, log_file):
        self.log_file = log_file
        
    def log_event(self, message, level="INFO"):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"[{timestamp}] [{level}] {message}\n"
        
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(formatted_message)
            
    def log_error(self, error_message):
        self.log_event(error_message, level="ERROR")