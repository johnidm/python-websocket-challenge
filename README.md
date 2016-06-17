# Websocket challange

[![Deploy](http://www.herokucdn.com/deploy/button.png)](http://chat-room-interview.herokuapp.com/)

> HTTPS does not work in this project

#### Setup project
```
pyenv install 2.7.11
pyenv virutalenv 2.7.11 venv-2.7.11
pyenv activate venv-2.7.11
```

```
git clone git@github.com:johnidm/python-websocket-challenge.git
pip install -r requirements.txt
```

#### Run project
```
python app.py
````
or 
```
foreman start
```

Open the url [http://localhost:5000](http://localhost:5000) in many tabs and different browsers and enjoy yourself!

#### How project work

![](http://i.imgur.com/jgsaINw.gif)


#### References

I did not do this project alone, I researched and used many things that articles:

* http://codepen.io/supah/pen/jqOBqp
* https://www.fullstackpython.com/websockets.html
* https://github.com/tornadoweb/tornado/tree/master/demos/chat
* http://code.runnable.com/UqDMKY-VwoAMABDk/simple-websockets-chat-with-tornado-for-python
* http://www.jpablo128.com/multi-room-websockets-server-with-tornado-i-basic-chat-server/
* http://www.codecheese.com/2013/11/running-tornado-web-server-on-heroku/
