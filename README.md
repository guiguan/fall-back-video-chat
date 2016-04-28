<!--
@Author: Guan Gui <guiguan>
@Date:   2016-04-27T11:24:57+10:00
@Email:  root@guiguan.net
@Last modified by:   root
@Last modified time: 2016-04-28T23:39:31+08:00
-->

![Live Chat](https://raw.githubusercontent.com/guiguan/fall-back-video-chat/master/screen_shot_1.png)

![Session Doc](https://raw.githubusercontent.com/guiguan/fall-back-video-chat/master/screen_shot_2.png)

# Project Summary
An online class is in session while the video chat server is suddenly overloaded.  Video quality has downgraded severely, you need to implement a fall-back plan that utilizes commercial video application to continue the class session.   Examples of commercial video app ,  Skype, QQ,  WeChat, facetime and etc.

## Input Assumption
* The session start time is the time user starts their fall-back video chat
* The planned end time will be one hour after the session starts
* Session ID, student ID and teacher ID are provided via URL params, and all other info are provided in database or implicitly figured out by the interface
* Image and video URLs are provided in database

## System Output
* A web interface for student and teacher to continue their video chat session
* A summary with some statistics for a session when it is completed

# Features
1. The fall-back video chat is implemented using WebRTC, which is a realtime P2P realtime video chat approach.
2. <del>Database is implemented using PouchDB, where each client has a local in-browser copy that can sync automatically with the central database. This can potentially make the system more scalable and support a better offline experience.</del> Unfortunately, at the moment, `pouchdb-server` is buggy, where it cannot keep a stable live connection between database and clients (precisely, always got ETIMEOUT error), and therefore no server-push is possible. I am using a very naive polling approach to get newest updates from a single central database.
3. Fluid and mobile friendly user interfaces.

# Server Setup
1. Make sure `http-server` is installed using `npm install -g http-server`, which is a simple https server hosting the web interfaces.
2. Make sure `pouchdb-server` is installed using `npm install -g pouchdb-server`, which is a central database to store client's information.
3. Assume the host ip address is **IP_HOST**. Type `sh run_database.sh` in terminal to start the central database, then type `sh run_https_server.sh` in terminal to start the https server.
4. You may now access web interfaces at https://IP_HOST:9000. A database admin inteface can be accessed at `/_utils`. Client interfaces can be accessed as follows.

# Client Usage
* For **teacher**, open Google Chrome and visit https://IP_HOST:9000/?userID=2&sessionID=3
* For **student**, open Google Chrome and visit https://IP_HOST:9000/?userID=1&sessionID=3
* _**NOTES**_: Remember to use https secure connections. Newest version of Google Chrome is needed. Tested under Google Chrome Version 50.0.2661.86 (64-bit) for Mac OSX. For security reasons, you may need to trust the self-signed certificate for the app to work properly. Also, you may need to force Chrome to allow mixed-content by clicking the shield icon on the right hand side of the address bar.
