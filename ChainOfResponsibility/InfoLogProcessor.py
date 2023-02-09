from LogProcessor import LogProcessor

class InfoLogProcessor(LogProcessor):
    def log(self,loglevel, message):
        print(loglevel)
        if loglevel == super().INFO:
            print(f"INFO - {message}")
        else:
            super().log(loglevel, message)