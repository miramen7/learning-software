import argparse
import collections
import os
import json
import time
import datetime
import subprocess
import urllib2
import selenium
from selenium import webdriver


def main():
    driver = webdriver.Chrome('/Applications/chromedriver')
    driver.quit()


if __name__ == "__main__":
    main()
    

