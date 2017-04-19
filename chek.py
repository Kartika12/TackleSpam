import imaplib
import email
import email.header
import classify
import classify1
import re

def read(username, password):

    #Decoding uid
    pattern_uid = re.compile(b'\d+ \(UID (?P<uid>\d+)\)')
    def parse_uid(data):
        match = pattern_uid.match(data)
        return match.group('uid')

    # Login to INBOX
    imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    imap.login(username, password)
    imap.select('INBOX')

    # Searching for unread emails
    status, response = imap.search('INBOX', '(UNSEEN)')
    unread_msg_nums = response[0].split()

    # Print the count of all unread messages
    print(len(unread_msg_nums))
    dat=[]
    # Read all unread messages
    status, response = imap.search(None, '(UNSEEN)')
    unread_msg_nums = response[0].split()
    result = []
    c=0
    for e_id in unread_msg_nums:
        _, response = imap.fetch(e_id, '(UID BODY[TEXT])')
        msg = email.message_from_bytes(response[0][1])
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                #Reading content of email
                body = part.get_payload()
                dat.append(body)
                #Classifying content and storing in result
                result.append(classify.classif(body))
                print(result)
                c=c+1
    print(unread_msg_nums)
    # Move according to classifier result
    c = 0
    for e_id in unread_msg_nums:
        _, response = imap.fetch(e_id, "(UID)")

        msg_uid = parse_uid(response[0])
        print(msg_uid)
        if(result[c]=='negative'):
            result1=classify1.classif1(body)

            if(result1=='Forgery/Lottery'):
                apply_lbl_msg = imap.uid('COPY', msg_uid, 'spamm/forgery')
                if apply_lbl_msg[0] == 'OK':
                    x , var = imap.uid('STORE', msg_uid , '-FLAGS', '(\Seen)') #Mark as Unseen
                    x , var = imap.uid('STORE', msg_uid , '+FLAGS', '(\Deleted)')

                    imap.expunge()
                    print('moved')
                    break
            else:
                apply_lbl_msg = imap.uid('COPY', msg_uid, 'spamm/advertisement')
                if apply_lbl_msg[0] == 'OK':
                    x , var = imap.uid('STORE', msg_uid , '-FLAGS', '(\Seen)') #Mark as Unseen
                    x , var = imap.uid('STORE', msg_uid , '+FLAGS', '(\Deleted)')

                    imap.expunge()
                    print('moved')
                    break
        else:
            x,var=imap.uid('STORE',msg_uid,'-FLAGS','(\Seen)')#Mark as Unseen
            print('not moved')
        c=c+1

read('project6589@gmail.com','dontspam')

