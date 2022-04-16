import os
from time import sleep
import time
import unittest
import logging
import datetime
import sys
import sh
import mysql.connector
import ConfigParser
import socket
from appium import webdriver


class SimpleAndroidTests(unittest.TestCase):


	
    def setUp(self):
		
		self.reference= str(int(round(time.time() * 1000)))
        self.device_id= sys.argv[1]
		self.udid = self.device_id
		self.os='Android'
		
		

    	desired_caps= {}
    	desired_caps['platformName']= self.os
        desired_caps['deviceName'] = self.device_id
        desired_caps['udid']= self.device_id
        desired_caps['appPackage']= "com.walmart.android"
        desired_caps['appActivity']= ".Settings"
        desired_caps['noReset'] = 'True'

		    
	    self.url= ('http://127.0.0.1:' + appium_input + '/wd/hub')
	       
		
	
		self.status = "Fail_Launch"
		self.app_launch_time = 0
		self.search_time = 0
	
		self.kpi_count = 2
		self.pass_count = 0
	    self.fail_count = 0
		
		self.driver = webdriver.Remote(self.url, desired_caps)
		

    def tearDown(self):
		
		print("Pass count is %s",%self.pass_count)
	    if self.pass_count!= self.kpi_count:
       		self.fail_count = self.kpi_count - self.pass_count
        else:
            self.fail_count = 0
        print("Fail count is %s ",%self.fail_count)

	       
		self.driver.quit()		

	
	def test_walmart(self):

		self.driver.implicitly_wait(50)
	

		#App launch
		app_launch_start=int(round(time.time() * 1000))
		nav_bar = self.driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("Open navigation drawer")')
		app_launch_end=int(round(time.time() * 1000))

		self.app_launch_time= app_launch_end- app_launch_start
		print('App launch time = ', self.app_launch_time)	
		self.pass_count += 1

		
		self.driver.implicitly_wait(60)
		


		#Item search
		self.status= "Search failed"
		search_box_text= self.driver.find_element_by_id('com.walmart.android:id/search_src_text')
		search_box_text.click()
		search_box_text= self.driver.find_element_by_id('com.walmart.android:id/search_src_text')
		search_box_text.set_value('iPhone 6s')
		self.driver.keyevent(66)
		search_start = int(round(time.time() * 1000))

		search_item= self.driver.find_element_by_id('com.walmart.android:id/shelf_item_view_title')
		search_end= int(round(time.time() * 1000))

		self.search_time= search_end-search_start
		print('search time= ',self.search_time)
		self.pass_count += 1

		self.status="Pass"

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)


