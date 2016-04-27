<!--
@Author: Guan Gui <guiguan>
@Date:   2016-04-27T11:24:57+10:00
@Email:  root@guiguan.net
@Last modified by:   guiguan
@Last modified time: 2016-04-28T02:08:16+10:00
-->

# Problem Summary
An online class is in session while the video chat server is suddenly overloaded.  Video quality has downgraded severely, you need to implement a fall-back plan that utilizes commercial video application to continue the class session.   Examples of commercial video app ,  Skype, QQ,  WeChat, facetime and etc.

# Features
1. The fall-back video chat is implemented using WebRTC, which is a distributed P2P realtime video chat mechanism.
2. <del>Database is implemented using PouchDB, where each client has a local in-browser copy that can sync automatically with the central database. This can potentially make the system more scalable and support a better offline experience.</del> Unfortunately, at the moment, `pouchdb-server` is buggy, where it cannot keep a stable live connection between database and clients (precisely, always got ETIMEOUT error), and therefore no server-push is possible. I am using a very naive polling approch to get newest updates from database.
3. Fluid and mobile friendly user interfaces.

# Server Setup
1. Make sure python 2 is installed, which is the dependency required to run a simple https server hosting the web interfaces.
2. Make sure `pouchdb-server` is installed using `npm install -g pouchdb-server`, which is the central database to store client's information.
3. Type `python server.py` in terminal to start the https server. Assume the host ip address is **IP_HOST**.
4. Type `sh run_database.sh` in terminal to start the central database on the same machine as the https server.

# Client Usage
* For teacher, open Google Chrome and visit https://IP_HOST:4443/?role=teacher.
* For student, open Google Chrome and visit https://IP_HOST:4443/?role=student or simply https://IP_HOST:4443/.
* *NOTE*: you may need to trust the self-signed certificate for the app to work properly. Also, you may need to force Chrome to allow mixed-content by clicking the shield icon on the right hand side of the address bar.
