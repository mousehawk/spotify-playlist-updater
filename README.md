# Spotify Playlist Updater

Forked from https://github.com/aeriie/spotify-playlist-updater - installation instructions & full details there.


#### A Python script to check Spotify Playlist data every 1 minutes and restore it if missing.


## Description

An automatic playlist updater using Spotify API and Authorization code flow in Python to regularly check a playlist for changes and reset the title, description and cover image if they have been removed. 

## Getting Started
#### You will need Python to execute the script:

* Python 3
    * [Installation Link](https://www.python.org/downloads/)

#### Spotify Playlist Updater requires three dependencies: 

##### Pip

* A Package Management System for Python.
* [Installation Link](https://pip.pypa.io/en/stable/installation/)
* For Windows, you can run ```py -m ensurepip --upgrade``` in CMD to install. 

##### Schedule
* Python job scheduler to run the script on a timer.
* [Installation Link](https://schedule.readthedocs.io/en/stable/installation.html)
* For Windows, you can run ```-m pip install schedule --upgrade``` in CMD to install. 

##### A Web Domain

* No website required, only a web domain for redirecting the API request and retrieving the user authorization token. 
* If you don't already own a domain, you can create one at [https//wix.com](https://wix.com)

##### Spotipy
* Python library for the Spotify Web API
* [Installation Link](https://spotipy.readthedocs.io/en/2.19.0/#installation)
* For Windows, you can run ``` py -m pip install spotipy --upgrade ``` in CMD to install. 

#

### Set Up

##### Installing the Script

* Install the dependencies listed above. 
* Choose a location on your device (I'll refer to this as the working directory)
* Download the latest release of [spotify-playlist-updater](https://github.com/aeriie/spotify-playlist-updater/) to the working directory. 
* Save your playlist photo (if applicable) in the ``data`` folder of the working directory
    * The photo must be 150KB or less. If it is too large, resize the photo. 
    * You can use this website to resize your image: https://www.resizepixel.com/reduce-image-in-kb/

##### Set up Client ID, Client Secret and Redirect URI
* Login to Spotify Developer Account
    * Go to https://developer.spotify.com/dashboard/ and click Manage Dashboard. 
    * Then, sign in with your Spotify credentials and accept the latest Developer terms of service.
    * Note your Client ID, and Client Secret. 
* Create an App
    * In the Developer Dashboard, create an App. You can put whatever you'd like for the App name and description. 
    * Click Edit Settings. 
        * Add your domain address to the Redirected URI's field, and click Add. Make sure to Save. 

##### Adding your Playlist information
* Right click \spotify-playlist-updater.py from the working directory and edit it with a text editor.
   * Put your Playlist Image path in place of: ```` "C:\\Users\\Username\\Documents\\spotify-playlist-updater\\Data\\thumbnail.jpg" ````
   * Put your Spotify Username in place of: ```` 'username' ````
   * Put your Client ID in place of ```` 'clientid' ````
   * Put your Client Secret in place of ```` 'clientsecret' ````
   * Put your Web Domain Address in place of ```` 'http://yourdomain.com' ````
   * Put your Spotify Playlist Link in place of ```` 'https://open.spotify.com/playlist/0000000000000000000000' ````
   * Put your Playlist Description in place of ```` 'Playlist Name' ````
   * Put your Playlist Description in place of ```` 'Playlist Description' ````
* **Save the script once your changes are made.** 



### Running the Script

* Open Command Prompt.
* Navigate to the directory where your script is located, eg. ```` cd C:\Users\Username\Documents\spotify-playlist-updater ````
* Run the script by typing ```` python spotify-playlist-updater.py ````

The script checks the playlist every 1 minute, but only restores the details if they have been changed. You can adjust the update frequency by changing the number value for ```` schedule.every(1).minutes.do(func) ````





## Version History

* 0.1
    * Initial Release
   
* 0.2 
    * Conditional logic & timestamps added

* 0.3
    * Added a counter
