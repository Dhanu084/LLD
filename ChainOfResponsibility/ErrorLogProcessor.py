from LogProcessor import LogProcessor

class ErrorLogProcessor(LogProcessor):

    def log(self,loglevel, message):
        if loglevel == super().ERROR:
            print(f"ERROR - {message}")
        else:
            super().log(loglevel, message)