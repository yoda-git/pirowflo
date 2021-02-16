import configparser

class globalParameterBuilder():
    def __init__(self):
        #Software-wide public variables
        self.counter = 0
        self.trigger = False
        self.oldcounter = -1
        self.activemenu = 0 #defaults is currently main menu needed to scroll through the menus
        self.oldactivemenu = -1 #needes for update thread needed to scroll through the menus
        self.blackscreen = False
        ########

        #Load Config
        print("Load configuration file")
        self.config = configparser.ConfigParser() # initiloze the configerparger module
        self.config.read("settings.ini") # reads the setting file with the settings

        #Set fonts
        print("Loading font configuration")
        self.font_icons = self.config.get('Fonts', 'icons') # those are for icons fonts "Font awesome for example
        self.font_text = self.config.get('Fonts', 'text') # normal text must be open source for the project
        #self.font_clock = self.config.get('Fonts', 'clock') # normal text must be open source for the project

        #Set PiRowFlo setting
        self.SmartRowOn = 0
        self.S4MonitorOn = 1
        self.BluetoothOn = 1
        self.AntplusOn = 0

    def setScreen(self, screenid,counter=0):
        self.activemenu = screenid
        self.counter = counter # position of the curser in the menu page
        self.oldcounter = -1

globalParameters = globalParameterBuilder()