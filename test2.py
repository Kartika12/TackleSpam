import imaplib

import webbrowser

obj = imaplib.IMAP4_SSL('imap.gmail.com','993')

obj.login('project6589','dontspam')

obj.select()
unread = str(obj.search(None, 'UNSEEN'))

print(unread)

print(len(unread) - 13)

if (len(unread) - 13) > 0: webbrowser.open('http://gmail.com')