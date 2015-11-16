from appium_selector.CapGenerators.Caps import Caps, propertyFromString
from appium_selector.Helpers.GetDeviceInfo import getDeviceInfo


class GridMobile(Caps):

    options = {}
    caps = {}

    def __init__(self, environment):
        self.env = environment
        self.udid = propertyFromString('deviceName', self.env)
        self.platform = propertyFromString('platform', self.env)
        self.device = getDeviceInfo(self.udid, self.platform)

    def displayString(self):
        platform = self.device['platform']
        udid = self.device['udid']
        name = self.device['name']
        return "%s -- %s -- %s" % (platform, udid, name)
    
    def desiredCaps(self):
        self.options['provider'] = 'gridMobile'
        self.options['manufacturer'] = self.device['manufacturer']
        self.options['model'] = self.device['model']
        self.options['osv'] = self.device['osv']

        self.caps['platformName'] = propertyFromString('platform', self.env)
        self.caps['browserName'] = self.device['udid']
        self.caps['udid'] = self.device['udid']
        self.caps['deviceName'] = self.device['name']
        
        return {'desiredCaps': self.caps, 'options': self.options}