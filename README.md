emailsender
===========

It's a simple python program for the teacher to send score to every student via email. It can read data from an xls file and you can modify the template easily.


Steps:
===========
1. You should get your smtp account from your email service provider and modify the mail_account.conf in the directory.
2. Set up the python enviroment for your computer. You may get more help from Google ^.^
3. download the xlrd mod from https://pypi.python.org/pypi/xlrd/0.9.2
4. open a cmd/terminal and cd into the "xlrd-0.9.2"
5. run the command "python setup.py install"
6. Modify the template.txt as you like and you can even add more tags.
7. Copy the data to the data.xls file, you can add more fields as your need.
8. Run the emailsender.py in the cmd/terminal
9. Check the log.txt for more detail.

tips:
===========
the tags in the template.txt and fields in the data.xls must be the same!!
