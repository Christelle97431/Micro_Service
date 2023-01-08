# Micro_Service
An API microservice to register and connect. A User microservice to return data from the API

## General Information
With Flask and Python3, this application allows to create an API (CRUD User) on a server and to return the data on the client side, on another server.  


# Technologies  
List of technologies used in this project :   
  
<img src="https://static.javatpoint.com/python/images/tkinter-tutorial.png" width="90" alt="Python Logo"> 

1. [installation Python](https://www.pythontutorial.net/getting-started/install-python/) : Version 3+  

2. [documentation Python](https://docs.python.org/3.11/)  

3. [documentation pip](https://help.dreamhost.com/hc/en-us/articles/115000699011-Using-pip3-to-install-Python3-modules)   




<img src="https://www.fullstackpython.com/img/logos/flask.jpg" width="90" alt="Flask Logo">  
4. [library flask](https://flask.palletsprojects.com/en/2.2.x/) : Version 2.2.x  



<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT15d13IJ7gtixCZJXH-N-EctmRjvZyI8yw6BcbTX7A-g&s" width="90" alt="MySQL Logo">  
5. [MySQL](https://upload.wikimedia.org/wikipedia/commons/0/0a/MySQL_textlogo.svg) : Version 5.7  



<img src="https://www.wampserver.com/wp-content/themes/wampserver/img/logo.png" width="150" alt="WampServer Logo">
6. [WampServer](https://www.wampserver.com/) : Version 3.2


# Installation  

WARNING !  
Requires prior installation of WampServer (Windows version)  
[WampServer](https://www.wampserver.com/)  


After cloning the project, type the following shell commands:   

1. Check if Python 3 is installed   
`python --version`  

2. Otherwise, install Python 3   
`cf. installation in technologies`   

3. check is pip is installed  
`pip show package_name`  

4. Oterwise, install   
`pip install package_name`  

5. Install Flask  
`python3 -m pip install flask`  

6. Import db in MySQL  
Start the Apache server.    
Import the file flask.sql   
Change if necessary your connections in the app.py file :  
app.config['MYSQL_USER'] = 'your MySQL user'  
app.config['MYSQL_PASSWORD'] = 'your MySQL password'  

7. Install MySQL  
`pip install flask-mysql`  

8. To Start the API server    
`python3 app.py run`  

9. To Start the user server    
`python3 client.py run`  
 
  
# License
This application is open-source under the [MIT license](https://opensource.org/licenses/MIT).  
