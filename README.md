# PyChat

PyChat is an easy to use chat server coded in python. When started the user can enter a username and address to connect with or can press to host button to allow for other users to connect to them. It is easy to host on a local network and with a bit of knowledge you can port forward to chat anytime.

## Getting Started
These instructions will help you get a copy of this project up and running on your local machine for development, testing, or general use.

### Prerequisites
To use this program you must have a working copy of Python 3 or higher with the standard library installed. You can download the latest version of python here: [Python.org](https://www.python.org/downloads/)

### Installation
To install this code onto your machine simply download the repository as a zip and then unzip it. Or if you are using a Linux machine you can use the following:
```
sudo git clone https://github.com/EdChSk/PyChat
sudo unzip [FILENAME]
```
### Running the code
You can run the code directly from python's IDLE. In addition to this you can run it from CMD or Terminal by changing directory into the main folder and running:

Windows (CMD): *(You will need to accept a security warning to allow the use of the socket)*
```
python3 main.py
```
Linux (Terminal):
```
sudo python3 main.py
```
This will then ask you what mode you would like to use. Client is a command line client, ClientG is a GUI client, and Server will run a server. Alternatively you can use the command line arguments. For a list of the possable arguments run:

Windows (CMD):
```
python3 main.py -h
```
Linux (Terminal):
```
sudo python3 main.py -h
```


### Hosting a server
To host a server for other people to connect to just run the main.py (explained above) and then type 'Server' when prompted. This will then host a server from your local machene and sometimes ask permission through your firewall :). After botting it will display a IP address for your clients to connect to. (The port is 9009 by default unless you changed it)

### Connecting To A Server
To connect to a server run 'main.py' (explained above), type 'Client' or 'ClientG' when prompted for a mode, enter a username, and then enter the servers IP address and port. Click login and you should connect. A notification will apear if your username is allready taken.

## Features:

Below is a list of the program's features and what version the program is. 
*'-' represents already in the projects and '+' indicates an addition to the project.*
### Version 0.2
  - Commands
    - /exit -- [Client] disconnects from server -
  - Multiple users
    + Multiple users can connect and chat at any one time (FIXED) +
  - Usernames
    - User chooses a username on login so that other users can identify them easily -
    + Checks username is not taken before login +
  - Command line interface +
    + Added command line client +
    + Added command line server +
    + Added GUI client +
    + Added command line arguments +

### Version Checking
To check the version of your code run:
```
python main.py -v
```
or
```
python main.py --version
```


## License
This project is licensed under the GNU Lesser General Public License v3.0 - See the [LICENCE](LICENSE) file for more details

## Authors
* **EdChSk** - *Initial work* - [Github Profile](https://github.com/EdChSk)

**Any ideas / suggestions / bugs please let me know as this is very much still a WIP**

:)
