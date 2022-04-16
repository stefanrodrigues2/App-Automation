
from time import sleep
import os
import mysql.connector
import socket
import sh
import time
import unittest
import logging
import datetime
import sys
import ConfigParser
from appium import webdriver
import requests
import smtplib



class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        self.screenshotDir = './Test1'
        self.udid = sys.argv[1]
		self.os = 'Android'
        desired_caps = {}
        desired_caps['platformName'] = self.os
        desired_caps['udid'] = self.udid
        desired_caps['deviceName'] = self.udid
        desired_caps['appPackage'] = "com.spotify.music"
        desired_caps['appActivity'] = ".MainActivity"
        desired_caps['noReset'] = 'True'
        self.device_id = self.udid
		
        self.appium_port = "4723"
        self.url = 'http://127.0.0.1:' + self.appium_port + '/wd/hub'
        self.driver = webdriver.Remote(self.url, desired_caps)

	

		self.start_app = int(round(time.time() * 1000))
		self.status = "Fail_launch"
		self.app_launch_time = 0
		self.search_time = 0	
		self.play_time = 0
		self.pass_count = 0
    	self.fail_count = 0
		self.timestamp =  int(round(time.time() * 1000))

    def tearDown(self):
		
		print("Pass count is %s", %self.pass_count)
        if self.pass_count!=3:
                self.fail_count = 3 - self.pass_count
        else:
                self.fail_count = 0
        print("Fail count is %s ",%self.fail_count)

		self.driver.quit()

    def test_login(self):
		
	
        self.driver.implicitly_wait(30)
        #Launching app
		home_bar = self.driver.find_element_by_id("com.spotify.music:id/home_tab")
        launched_app = int(round(time.time() * 1000))
        self.app_launch_time = launched_app - self.start_app
        print ("App Launch Time is %s ms" %self.app_launch_time)
		self.pass_count = 1
		#Search
		sleep(2)
		self.status = "Fail_search"
		search_bar = self.driver.find_element_by_id("com.spotify.music:id/search_tab")
		search_bar.click()
		new_releases = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("New Releases")')	
		new_releases.click()
		start_search = int(round(time.time() * 1000))
		self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("New releases")')
		end_search = int(round(time.time() * 1000))
		self.search_time = end_search - start_search
		print("Search time is %s ms",%self.search_time)
		self.pass_count = 2 
	
		#Play Music
		song_thumb = self.driver.find_elements_by_id("android:id/icon")
		song_thumb[0].click()
		self.status = "Fail_play_music"
		play_button = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("SHUFFLE PLAY")')
		play_button.click()
		start_play = int(round(time.time() * 1000))
		pause_button = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("PAUSE")')
		end_play = int(round(time.time() * 1000))
		self.play_time = end_play - start_play
		print("Play time is %s ms",%self.play_time)
		self.pass_count = 3
		pause_button.click()
		sleep(2)
	
	
		self.status = "Pass"



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)





