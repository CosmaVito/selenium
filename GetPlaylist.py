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

        x=0
        while (x<5):
            title = browser.find_element_by_xpath('.//raw[1]/div[1]/div[4]/h2').text
            artista = browser.find_element_by_xpath('.//raw[1]/div[1]/div[4]/h3/a').text
            print title
            print artista
            x=x+1


#mod


myClassObject = GetPlaylist()
myClassObject.getTopSongs()


