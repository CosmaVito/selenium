import re
import mechanize
from selenium  import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
class GetPlaylist(object):

    def getTopSongs(self):
        print "working billboard"
        browser = webdriver.Firefox()
        browser.get('http://www.billboard.com/charts/rock-songs')
        time.sleep(5)


        title = browser.find_element_by_xpath('.//article[contains(@class,"chart-raw")]/div[contains(@class,"raw-title")]/h2').text
        print title



#mod


myClassObject = GetPlaylist()
myClassObject.getTopSongs()


