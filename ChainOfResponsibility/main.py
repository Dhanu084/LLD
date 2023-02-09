from InfoLogProcessor import InfoLogProcessor
from DebugLogProcessor import DebugLogProcessor
from ErrorLogProcessor import ErrorLogProcessor
from LogProcessor import LogProcessor

if __name__ == "__main__":
    logProcessor = InfoLogProcessor(DebugLogProcessor(ErrorLogProcessor()))
    logProcessor.log(LogProcessor.INFO, "sampleInfo")
    logProcessor.log(LogProcessor.ERROR, "sample error")