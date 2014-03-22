emailsender
===========

It's a simple python program for the teacher to send score to every student via email. It can read data from a xls file and modify the template easily.


Steps:
===========
1. You should get your smtp account from your email service provider and modify the mail_account.conf in the directory.
2. Set up the python enviroment for your computer. You may get more help from Google ^.^
3. Install xlrd mod for your computer.
    3.1 open a cmd/terminal and cd into the "xlrd-0.9.2"
    3.2 run the command "python setup.py install"
4. Modify the template.txt as you like and you can even add more tags.
5. Copy the data to the data.xls file, you can add more fields as your need.
6. Run the emailsender.py in the cmd/terminal
7. Check the log.txt for more detail.

tips:
===========
the tags in the template.txt and fields in the data.xls must be the same!!