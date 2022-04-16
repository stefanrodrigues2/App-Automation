## arguments - argv[1]: device id, argv[2]: appium port eg.4723,    argv[3]: location
import socket
import os
from time import sleep
import sys
import time
import unittest
import logging
import datetime
import sh
import mysql.connector

 
from appium import webdriver
device_serial=sys.argv[1]



class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
		self.started_1_millis = int(round(time.time() * 1000))
	
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['udid'] = device_serial
		desired_caps['deviceName'] = device_serial
        desired_caps['appPackage'] = 'com.google.android.youtube'
        desired_caps['appActivity'] = 'com.google.android.apps.youtube.app.WatchWhileActivity'
        desired_caps['noReset'] = True
		
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
		self.status = "Fail"
        self.FailReason=""
		self.g_started_millis = 0
		self.g_search_millis = 0
		self.g_launch_millis = 0
		self.g_city = sys.argv[3]


    def tearDown(self):
        # end the session
	
		self.driver.quit()

    def test_login(self):

 		self.FailReason="Fail_Loadingapp"
		search_button = self.driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("Search")')
        started_millis = int(round(time.time() * 1000))
		self.g_started_millis = str(started_millis - self.started_1_millis)	        

		self.driver.implicitly_wait(50)
      
        self.FailReason = "Fail_beforeSearch"
	
		search_button = self.driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("Search")')
		search_button.click()
        edit_text = self.driver.find_element_by_id('com.google.android.youtube:id/search_edit_text')
        edit_text.set_value("The Smurfs")
        self.driver.press_keycode(66)
        self.FailReason = "Fail_search_vid"
        self.driver.implicitly_wait(50)
        search_result = self.driver.find_elements_by_id('com.google.android.youtube:id/video_info_view')
        search_millis = int(round(time.time() * 1000))
        self.g_search_millis = str(search_millis - started_millis)
        search_result[1].click()
        
        self.driver.implicitly_wait(50)
        

	    ImageViewElements = self.driver.find_elements_by_class_name('android.widget.ImageView')
	    ImageViewElementsLength = len(ImageViewElements)
        self.FailReason = "Fail_LoadVideo"
        if ImageViewElementsLength > 4:
            self.FailReason = "Pass"
            self.status="Pass"
            load_millis = int(round(time.time() * 1000))
            self.g_launch_millis = str(load_millis-search_millis)
            print ImageViewElementsLength
            break
        else:
            sleep(1)
		print "Launched time: "
		print self.g_started_millis
		print "Search time: "
		print self.g_search_millis
		print "Video load time: "
		print self.g_launch_millis
	

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
