1. Go to sinch sms developer portal and create an account( There are two portal from sinchsms, you have to go to sinchsms developer portal)
2. Go to APPs tab from left panel and create an APP(key and secret are the one we need)
3. Go to your linux system! And install python sinchsms module through this:
	pip install sinchsms
4. Now you have to write code for sending an sms through python!(search 'send sms python sinchsms'! Also I will attach a screenshot of the code!, You can also check the attached code! sms.py)
5. Now add rule in udev:
	-> cd /etc/udev/rules.d/
	-> vim anyname.rules
	-> ACTION=="add", SUBSYSTEM=="usb"   RUN=="path_to_your_python_file"
	    Make sure your python has executable, so 
	             -> chmod +x yourfile.py

YOU ARE DONE
-------------
Just attach pendrive and you will get a SMS!
Make sure you are connected to internet before attaching pendrive!

