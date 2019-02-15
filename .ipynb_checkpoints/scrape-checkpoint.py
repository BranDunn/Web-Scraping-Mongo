{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 1 - Scraping"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.\n",
    "\n",
    "\n",
    "Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.\n",
    "\n",
    "\n",
    "\n",
    "NASA Mars News\n",
    "\n",
    "\n",
    "Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import dependencies\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "import time\n",
    "from time import sleep\n",
    "import pandas as pd\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def init_browser():\n",
    "    executable_path = {\"executable_path\": 'chromedriver'}\n",
    "    return Browser(\"chrome\", **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA's MAVEN Spacecraft Shrinking its Mars Orbit to Prepare for Mars 2020 Rover\n",
      "The MAVEN spacecraft today is starting a campaign to tighten its orbit around Mars to prepare to serve as a data-relay satellite for NASA’s Mars 2020 rover, which launches next year.\n"
     ]
    }
   ],
   "source": [
    "#scrape Mars New site\n",
    "\n",
    "browser = init_browser()\n",
    "url = \"https://mars.nasa.gov/news/\"\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "title = soup.find('div', class_=\"content_title\").get_text()\n",
    "paragraph = soup.find('div', class_=\"article_teaser_body\").get_text()\n",
    "browser.quit()\n",
    "\n",
    "print(title)\n",
    "print(paragraph)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Example:\n",
    "news_title = \"NASA's Next Mars Mission to Investigate Interior of Red Planet\"\n",
    "\n",
    "news_p = \"Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast.\"\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "JPL Mars Space Images - Featured Image\n",
    "\n",
    "\n",
    "Visit the url for JPL Featured Space Image here.\n",
    "Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.\n",
    "Make sure to find the image url to the full size .jpg image.\n",
    "Make sure to save a complete url string for this image."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "MaxRetryError",
     "evalue": "HTTPConnectionPool(host='127.0.0.1', port=59274): Max retries exceeded with url: /session/9fb673019bf5a0e622295f5cea4f6c5d/elements (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x00000230A0E8F898>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it',))",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mConnectionRefusedError\u001b[0m                    Traceback (most recent call last)",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connection.py\u001b[0m in \u001b[0;36m_new_conn\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    140\u001b[0m             conn = connection.create_connection(\n\u001b[1;32m--> 141\u001b[1;33m                 (self.host, self.port), self.timeout, **extra_kw)\n\u001b[0m\u001b[0;32m    142\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\util\\connection.py\u001b[0m in \u001b[0;36mcreate_connection\u001b[1;34m(address, timeout, source_address, socket_options)\u001b[0m\n\u001b[0;32m     82\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0merr\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 83\u001b[1;33m         \u001b[1;32mraise\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     84\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\util\\connection.py\u001b[0m in \u001b[0;36mcreate_connection\u001b[1;34m(address, timeout, source_address, socket_options)\u001b[0m\n\u001b[0;32m     72\u001b[0m                 \u001b[0msock\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msource_address\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 73\u001b[1;33m             \u001b[0msock\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msa\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     74\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0msock\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mConnectionRefusedError\u001b[0m: [WinError 10061] No connection could be made because the target machine actively refused it",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mNewConnectionError\u001b[0m                        Traceback (most recent call last)",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    600\u001b[0m                                                   \u001b[0mbody\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbody\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 601\u001b[1;33m                                                   chunked=chunked)\n\u001b[0m\u001b[0;32m    602\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36m_make_request\u001b[1;34m(self, conn, method, url, timeout, chunked, **httplib_request_kw)\u001b[0m\n\u001b[0;32m    356\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 357\u001b[1;33m             \u001b[0mconn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mhttplib_request_kw\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    358\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\http\\client.py\u001b[0m in \u001b[0;36mrequest\u001b[1;34m(self, method, url, body, headers, encode_chunked)\u001b[0m\n\u001b[0;32m   1238\u001b[0m         \u001b[1;34m\"\"\"Send a complete request to the server.\"\"\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1239\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_send_request\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mencode_chunked\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1240\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\http\\client.py\u001b[0m in \u001b[0;36m_send_request\u001b[1;34m(self, method, url, body, headers, encode_chunked)\u001b[0m\n\u001b[0;32m   1284\u001b[0m             \u001b[0mbody\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_encode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbody\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'body'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1285\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mendheaders\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbody\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mencode_chunked\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mencode_chunked\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1286\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\http\\client.py\u001b[0m in \u001b[0;36mendheaders\u001b[1;34m(self, message_body, encode_chunked)\u001b[0m\n\u001b[0;32m   1233\u001b[0m             \u001b[1;32mraise\u001b[0m \u001b[0mCannotSendHeader\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1234\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_send_output\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmessage_body\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mencode_chunked\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mencode_chunked\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1235\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\http\\client.py\u001b[0m in \u001b[0;36m_send_output\u001b[1;34m(self, message_body, encode_chunked)\u001b[0m\n\u001b[0;32m   1025\u001b[0m         \u001b[1;32mdel\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_buffer\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1026\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmsg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1027\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\http\\client.py\u001b[0m in \u001b[0;36msend\u001b[1;34m(self, data)\u001b[0m\n\u001b[0;32m    963\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mauto_open\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 964\u001b[1;33m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    965\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connection.py\u001b[0m in \u001b[0;36mconnect\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    165\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 166\u001b[1;33m         \u001b[0mconn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_new_conn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    167\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_prepare_conn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mconn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connection.py\u001b[0m in \u001b[0;36m_new_conn\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    149\u001b[0m             raise NewConnectionError(\n\u001b[1;32m--> 150\u001b[1;33m                 self, \"Failed to establish a new connection: %s\" % e)\n\u001b[0m\u001b[0;32m    151\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNewConnectionError\u001b[0m: <urllib3.connection.HTTPConnection object at 0x00000230A0E8F898>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mMaxRetryError\u001b[0m                             Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-79fa4971d3c3>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     14\u001b[0m \u001b[1;31m# time.sleep(5)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     15\u001b[0m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 16\u001b[1;33m \u001b[0mfeatured_image_url\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_by_tag\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'img'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'src'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     17\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     18\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\driver\\webdriver\\__init__.py\u001b[0m in \u001b[0;36mfind_by_tag\u001b[1;34m(self, tag)\u001b[0m\n\u001b[0;32m    440\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    441\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mfind_by_tag\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtag\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 442\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_by\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_elements_by_tag_name\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mtag\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    443\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    444\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mfind_by_value\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\driver\\webdriver\\__init__.py\u001b[0m in \u001b[0;36mfind_by\u001b[1;34m(self, finder, selector, original_find, original_query)\u001b[0m\n\u001b[0;32m    400\u001b[0m         \u001b[1;32mwhile\u001b[0m \u001b[0mtime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtime\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m<\u001b[0m \u001b[0mend_time\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    401\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 402\u001b[1;33m                 \u001b[0melements\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfinder\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mselector\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    403\u001b[0m                 \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0misinstance\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0melements\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlist\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    404\u001b[0m                     \u001b[0melements\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[0melements\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mfind_elements_by_tag_name\u001b[1;34m(self, name)\u001b[0m\n\u001b[0;32m    544\u001b[0m             \u001b[0melements\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_elements_by_tag_name\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'h1'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    545\u001b[0m         \"\"\"\n\u001b[1;32m--> 546\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_elements\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mby\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mBy\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mTAG_NAME\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    547\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    548\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mfind_element_by_class_name\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mfind_elements\u001b[1;34m(self, by, value)\u001b[0m\n\u001b[0;32m   1005\u001b[0m         return self.execute(Command.FIND_ELEMENTS, {\n\u001b[0;32m   1006\u001b[0m             \u001b[1;34m'using'\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mby\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1007\u001b[1;33m             'value': value})['value'] or []\n\u001b[0m\u001b[0;32m   1008\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1009\u001b[0m     \u001b[1;33m@\u001b[0m\u001b[0mproperty\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[1;34m(self, driver_command, params)\u001b[0m\n\u001b[0;32m    317\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    318\u001b[0m         \u001b[0mparams\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_wrap_value\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 319\u001b[1;33m         \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    320\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    321\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\selenium\\webdriver\\remote\\remote_connection.py\u001b[0m in \u001b[0;36mexecute\u001b[1;34m(self, command, params)\u001b[0m\n\u001b[0;32m    372\u001b[0m         \u001b[0mdata\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mutils\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdump_json\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    373\u001b[0m         \u001b[0murl\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'%s%s'\u001b[0m \u001b[1;33m%\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_url\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpath\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 374\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_request\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcommand_info\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    375\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    376\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_request\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\selenium\\webdriver\\remote\\remote_connection.py\u001b[0m in \u001b[0;36m_request\u001b[1;34m(self, method, url, body)\u001b[0m\n\u001b[0;32m    395\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    396\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mkeep_alive\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 397\u001b[1;33m             \u001b[0mresp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_conn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbody\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    398\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    399\u001b[0m             \u001b[0mstatuscode\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mresp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstatus\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\request.py\u001b[0m in \u001b[0;36mrequest\u001b[1;34m(self, method, url, fields, headers, **urlopen_kw)\u001b[0m\n\u001b[0;32m     68\u001b[0m             return self.request_encode_body(method, url, fields=fields,\n\u001b[0;32m     69\u001b[0m                                             \u001b[0mheaders\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 70\u001b[1;33m                                             **urlopen_kw)\n\u001b[0m\u001b[0;32m     71\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     72\u001b[0m     def request_encode_url(self, method, url, fields=None, headers=None,\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\request.py\u001b[0m in \u001b[0;36mrequest_encode_body\u001b[1;34m(self, method, url, fields, headers, encode_multipart, multipart_boundary, **urlopen_kw)\u001b[0m\n\u001b[0;32m    146\u001b[0m         \u001b[0mextra_kw\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murlopen_kw\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    147\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 148\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mextra_kw\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\poolmanager.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, redirect, **kw)\u001b[0m\n\u001b[0;32m    319\u001b[0m             \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mconn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkw\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    320\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 321\u001b[1;33m             \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mconn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mu\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequest_uri\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkw\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    322\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    323\u001b[0m         \u001b[0mredirect_location\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mredirect\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_redirect_location\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    666\u001b[0m                                 \u001b[0mtimeout\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpool_timeout\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mpool_timeout\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    667\u001b[0m                                 \u001b[0mrelease_conn\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mrelease_conn\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbody_pos\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbody_pos\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 668\u001b[1;33m                                 **response_kw)\n\u001b[0m\u001b[0;32m    669\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    670\u001b[0m         \u001b[1;32mdef\u001b[0m \u001b[0mdrain_and_release_conn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    666\u001b[0m                                 \u001b[0mtimeout\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpool_timeout\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mpool_timeout\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    667\u001b[0m                                 \u001b[0mrelease_conn\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mrelease_conn\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbody_pos\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbody_pos\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 668\u001b[1;33m                                 **response_kw)\n\u001b[0m\u001b[0;32m    669\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    670\u001b[0m         \u001b[1;32mdef\u001b[0m \u001b[0mdrain_and_release_conn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    666\u001b[0m                                 \u001b[0mtimeout\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpool_timeout\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mpool_timeout\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    667\u001b[0m                                 \u001b[0mrelease_conn\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mrelease_conn\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbody_pos\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbody_pos\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 668\u001b[1;33m                                 **response_kw)\n\u001b[0m\u001b[0;32m    669\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    670\u001b[0m         \u001b[1;32mdef\u001b[0m \u001b[0mdrain_and_release_conn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    637\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    638\u001b[0m             retries = retries.increment(method, url, error=e, _pool=self,\n\u001b[1;32m--> 639\u001b[1;33m                                         _stacktrace=sys.exc_info()[2])\n\u001b[0m\u001b[0;32m    640\u001b[0m             \u001b[0mretries\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    641\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\util\\retry.py\u001b[0m in \u001b[0;36mincrement\u001b[1;34m(self, method, url, response, error, _pool, _stacktrace)\u001b[0m\n\u001b[0;32m    386\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    387\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mnew_retry\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mis_exhausted\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 388\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mMaxRetryError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0m_pool\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merror\u001b[0m \u001b[1;32mor\u001b[0m \u001b[0mResponseError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcause\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    389\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    390\u001b[0m         \u001b[0mlog\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Incremented Retry for (url='%s'): %r\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mnew_retry\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mMaxRetryError\u001b[0m: HTTPConnectionPool(host='127.0.0.1', port=59274): Max retries exceeded with url: /session/9fb673019bf5a0e622295f5cea4f6c5d/elements (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x00000230A0E8F898>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it',))"
     ]
    }
   ],
   "source": [
    "#visit https://www.jpl.nasa.gov/spaceimages/\n",
    "#use splinter to navigate site, find and assign (fullsize) url string to variable\n",
    "\n",
    "url = 'https://www.jpl.nasa.gov/spaceimages'\n",
    "\n",
    "browser = init_browser()\n",
    "\n",
    "browser.visit(url)\n",
    "time.sleep(2)\n",
    "#click 'full image'\n",
    "browser.click_link_by_id('full_image')\n",
    "# time.sleep(5)\n",
    "# browser.click_link_by_partial_text(' actual ')\n",
    "# time.sleep(5)\n",
    "browser.quit()\n",
    "featured_image_url = browser.find_by_tag('img')['src']\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov/assets/images/logo_nasa_trio_black@2x.png\n"
     ]
    }
   ],
   "source": [
    "print(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Example:\n",
    "featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Mars Weather\n",
    "\n",
    "\n",
    "Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2019-01-28 through 02-03 via MRO/Marci \n",
      "• dust storms north of Alba Patera\n",
      "• lee wave clouds near Tempe Terra & Deuteronilus Mensae\n",
      "• H2O ice clouds over Arsia Mons \n",
      "• dust haze hides Valles Marineris floor\n",
      "• seasonally high dust over Opportunity, Curioisty, & Insightpic.twitter.com/awlKHfgac2\n"
     ]
    }
   ],
   "source": [
    "#scrape mars weather twitter\n",
    "url = \"https://twitter.com/MarsWxReport\"\n",
    "\n",
    "#open browser\n",
    "browser = init_browser()\n",
    "\n",
    "browser.visit(url)\n",
    "\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "# time.sleep(2)\n",
    "mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').get_text()\n",
    "# time.sleep(2)\n",
    "browser.quit()\n",
    "\n",
    "print(mars_weather)\n",
    "\n",
    "      \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Example:\n",
    "mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Mars Facts\n",
    "\n",
    "\n",
    "Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.\n",
    "Use Pandas to convert the data to a HTML table string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{\"0\":\"Equatorial Diameter:\",\"1\":\"6,792 km\"},{\"0\":\"Polar Diameter:\",\"1\":\"6,752 km\"},{\"0\":\"Mass:\",\"1\":\"6.42 x 10^23 kg (10.7% Earth)\"},{\"0\":\"Moons:\",\"1\":\"2 (Phobos & Deimos)\"},{\"0\":\"Orbit Distance:\",\"1\":\"227,943,824 km (1.52 AU)\"},{\"0\":\"Orbit Period:\",\"1\":\"687 days (1.9 years)\"},{\"0\":\"Surface Temperature:\",\"1\":\"-153 to 20 \\u00b0C\"},{\"0\":\"First Record:\",\"1\":\"2nd millennium BC\"},{\"0\":\"Recorded By:\",\"1\":\"Egyptian astronomers\"}]\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.42 x 10^23 kg (10.7% Earth)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.52 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-153 to 20 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      0                              1\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.42 x 10^23 kg (10.7% Earth)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.52 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                  -153 to 20 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#use pandas to scrape table Mars Facts page\n",
    "url = 'https://space-facts.com/mars/'\n",
    "response = requests.get(url)\n",
    "soup = BeautifulSoup(response.content,'lxml')\n",
    "table = soup.find('table', class_='tablepress tablepress-id-mars')\n",
    "df = pd.read_html(str(table))\n",
    "print(df[0].to_json(orient='records'))\n",
    "df = df[0]\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<table border=\"1\" class=\"dataframe\">\n",
      "  <thead>\n",
      "    <tr style=\"text-align: right;\">\n",
      "      <th></th>\n",
      "      <th>0</th>\n",
      "      <th>1</th>\n",
      "    </tr>\n",
      "  </thead>\n",
      "  <tbody>\n",
      "    <tr>\n",
      "      <th>0</th>\n",
      "      <td>Equatorial Diameter:</td>\n",
      "      <td>6,792 km</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>1</th>\n",
      "      <td>Polar Diameter:</td>\n",
      "      <td>6,752 km</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>2</th>\n",
      "      <td>Mass:</td>\n",
      "      <td>6.42 x 10^23 kg (10.7% Earth)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>3</th>\n",
      "      <td>Moons:</td>\n",
      "      <td>2 (Phobos &amp; Deimos)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>4</th>\n",
      "      <td>Orbit Distance:</td>\n",
      "      <td>227,943,824 km (1.52 AU)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>5</th>\n",
      "      <td>Orbit Period:</td>\n",
      "      <td>687 days (1.9 years)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>6</th>\n",
      "      <td>Surface Temperature:</td>\n",
      "      <td>-153 to 20 °C</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>7</th>\n",
      "      <td>First Record:</td>\n",
      "      <td>2nd millennium BC</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>8</th>\n",
      "      <td>Recorded By:</td>\n",
      "      <td>Egyptian astronomers</td>\n",
      "    </tr>\n",
      "  </tbody>\n",
      "</table>\n"
     ]
    }
   ],
   "source": [
    "#use pandas to convert data to HTML table string\n",
    "html_table = df.to_html()\n",
    "print(html_table)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Mars Hemispheres\n",
    "\n",
    "\n",
    "Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.\n",
    "You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.\n",
    "Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.\n",
    "Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#create empty list to append with dicts\n",
    "hemisphere_image_urls = []\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "ename": "ElementDoesNotExist",
     "evalue": "no elements could be found with link by text \"Cerberus Hemisphere Enhanced\"",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, index)\u001b[0m\n\u001b[0;32m     39\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 40\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0msuper\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mElementList\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__getitem__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     41\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mIndexError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mElementDoesNotExist\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-24-f6aeeb9cd13e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     13\u001b[0m \u001b[1;31m#hemi1 - cerb\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     14\u001b[0m \u001b[0mtime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 15\u001b[1;33m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclick_link_by_text\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Cerberus Hemisphere Enhanced'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfirst\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     16\u001b[0m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclick_link_by_href\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhref\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     17\u001b[0m \u001b[0mcerb_url\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msoup\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'img'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstyle_\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'-webkit-user-select: none;cursor: zoom-out;'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'src'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\driver\\__init__.py\u001b[0m in \u001b[0;36mclick_link_by_text\u001b[1;34m(self, text)\u001b[0m\n\u001b[0;32m    388\u001b[0m         \u001b[0mClicks\u001b[0m \u001b[1;32min\u001b[0m \u001b[0ma\u001b[0m \u001b[0mlink\u001b[0m \u001b[0mby\u001b[0m \u001b[0mits\u001b[0m\u001b[0;31m \u001b[0m\u001b[0;31m`\u001b[0m\u001b[0;31m`\u001b[0m\u001b[0mtext\u001b[0m\u001b[0;31m`\u001b[0m\u001b[0;31m`\u001b[0m\u001b[1;33m.\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    389\u001b[0m         \"\"\"\n\u001b[1;32m--> 390\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_link_by_text\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfirst\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    391\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    392\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mclick_link_by_partial_text\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpartial_text\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36mfirst\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m     53\u001b[0m             \u001b[1;33m>>\u001b[0m\u001b[1;33m>\u001b[0m \u001b[1;32massert\u001b[0m \u001b[0melement_list\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m==\u001b[0m \u001b[0melement_list\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfirst\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     54\u001b[0m         \"\"\"\n\u001b[1;32m---> 55\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     56\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     57\u001b[0m     \u001b[1;33m@\u001b[0m\u001b[0mproperty\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, index)\u001b[0m\n\u001b[0;32m     42\u001b[0m             raise ElementDoesNotExist(\n\u001b[0;32m     43\u001b[0m                 u'no elements could be found with {0} \"{1}\"'.format(\n\u001b[1;32m---> 44\u001b[1;33m                     \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_by\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mquery\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     45\u001b[0m                 )\n\u001b[0;32m     46\u001b[0m             )\n",
      "\u001b[1;31mElementDoesNotExist\u001b[0m: no elements could be found with link by text \"Cerberus Hemisphere Enhanced\""
     ]
    }
   ],
   "source": [
    "#open browser\n",
    "browser = init_browser()\n",
    "\n",
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "\n",
    "# click each of the links to the hemispheres in order to find the image url to the full resolution image\n",
    "# browser.visit(url)\n",
    "\n",
    "# #BeautifulSoupification...\n",
    "# html = browser.html\n",
    "# soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "# #hemi1 - cerb\n",
    "# time.sleep(2)\n",
    "# browser.click_link_by_text('Cerberus Hemisphere Enhanced').first.click()\n",
    "# browser.click_link_by_href(href=\"http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg\")\n",
    "# cerb_url = soup.find('img', style_='-webkit-user-select: none;cursor: zoom-out;')['src']\n",
    "# cerb_url\n",
    "\n",
    "#navigate back to hemispheres page\n",
    "\n",
    "\n",
    "#close browser\n",
    "browser.quit()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Use a Python dictionary to store the data using the keys img_url and title\n",
    "\n",
    "#Append the dictionary with the image url string and the hemisphere title to a list\n",
    "#Save both the image url string for the full resolution hemisphere image, \n",
    "#and the Hemisphere title containing the hemisphere name.\n",
    "\n",
    "\n",
    "\n",
    "#create empty list to append with dicts\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "#open browser\n",
    "browser = init_browser()\n",
    "\n",
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "\n",
    "products = soup.find(\"div\", class_ = \"result-list\") \n",
    "\n",
    "hemispheres = products.find_all(\"div\", class_=\"item\")\n",
    "\n",
    "for hemisphere in hemispheres:\n",
    "    title = hemisphere.find(\"h3\").text\n",
    "    title = title.replace(\"Enhanced\", \"\")\n",
    "    end_link = hemisphere.find(\"a\")[\"href\"]\n",
    "    image = \"https://astrogeology.usgs.gov/\" + end_link    \n",
    "    browser.visit(image)\n",
    "    html = browser.html\n",
    "    soup=BeautifulSoup(html, \"html.parser\")\n",
    "    downloads = soup.find(\"div\", class_=\"downloads\")\n",
    "    image_url = downloads.find(\"a\")[\"href\"]\n",
    "    hemisphere_image_urls.append({\"title\": title, \"img_url\": image_url})\n",
    "    \n",
    "browser.quit()\n",
    "\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Example:\n",
    "hemisphere_image_urls = [\n",
    "    {\"title\": \"Valles Marineris Hemisphere\", \"img_url\": \"...\"},\n",
    "    {\"title\": \"Cerberus Hemisphere\", \"img_url\": \"...\"},\n",
    "    {\"title\": \"Schiaparelli Hemisphere\", \"img_url\": \"...\"},\n",
    "    {\"title\": \"Syrtis Major Hemisphere\", \"img_url\": \"...\"},\n",
    "]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 2 - MongoDB and Flask Application"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.\n",
    "\n",
    "\n",
    "Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.\n",
    "\n",
    "Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.\n",
    "\n",
    "\n",
    "Store the return value in Mongo as a Python dictionary.\n",
    "\n",
    "\n",
    "Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.\n",
    "Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "#convert mission_to_mars.ipynb to scrape_mars.py \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#scrape_mars.py will have a function added, called scrape, that will execute all of your scraping code from above and\n",
    "#return one Python dictionary containing all of the scraped data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#use MongoDB with Flask Templating to create new HTML page to display all scraped data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#create route called /scrape to import scrape_mars.py and call function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#store return value in Mongo as python dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#create root route that queries the MongoDB and pass mars data into an HTML template to display data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#create HTML template called index.HTML that takes mars data dict and displays all data in HTML elements"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Hints"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.\n",
    "Use Pymongo for CRUD applications for your database. For this homework, you can simply overwrite the existing document each time the /scrape url is visited and new data is obtained.\n",
    "Use Bootstrap to structure your HTML template."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:PythonData]",
   "language": "python",
   "name": "conda-env-PythonData-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
