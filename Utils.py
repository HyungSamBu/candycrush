import ConfigParser

def scaler(OldMin, OldMax, NewMin, NewMax):
    def fn(OldValue):
        return (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
    return fn

def configfile(config_path):
    config = ConfigParser.ConfigParser(allow_no_value = True)
    config.read(config_path)
    return config
