from LogProcessor import LogProcessor

class DebugLogProcessor(LogProcessor):

    def log(self,loglevel, message):
        if loglevel == super().DEBUG:
            print(f"DEBUG - {message}")
        else:
            super().log(loglevel, message)