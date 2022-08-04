from task.code_refactoring import Postman

if __name__ == '__main__':

    gmail_smtp = "smtp.gmail.com"
    gmail_imap = "imap.gmail.com"
    login = "login@gmail.com"
    password = "qwerty"

    mail_1 = Postman(gmail_smtp, gmail_imap, login, password)

    recipients = ["vasya@email.com", "petya@email.com"]
    subject = 'Subject'
    message = 'Message'

    # mail_1.send_message(recipients, subject, message)

    header = None

    mail_1.recieve(header)
