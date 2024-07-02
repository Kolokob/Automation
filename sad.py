# import imaplib
# import email
# import re
# from email.header import decode_header
# from concurrent.futures import ThreadPoolExecutor, as_completed
# import email.utils
# import datetime
# import time
#
#
# def get_link_from_email(self):
#     username = "automation.senpex@outlook.com"
#     password_for_email = "A27011975a"
#     link = None
#
#     mail = imaplib.IMAP4_SSL("outlook.office365.com", 993)
#     try:
#         mail.login(username, password_for_email)
#         print("Login successful!")
#     except imaplib.IMAP4.error as e:
#         print(f"Failed to login: {e}")
#         exit(1)
#
#     mail.select("inbox")
#
#     status, messages = mail.search(None, '(FROM "noreply@senpex.com")')
#     email_ids = messages[0].split()
#
#     if email_ids:
#         email_date_pairs = []
#         for email_id in email_ids:
#             res, msg = mail.fetch(email_id, "(BODY[HEADER.FIELDS (DATE)])")
#             for response_part in msg:
#                 if isinstance(response_part, tuple):
#                     msg_date = email.message_from_bytes(response_part[1])["Date"]
#                     email_date_pairs.append((email_id, msg_date))
#
#         email_date_pairs.sort(key=lambda x: email.utils.parsedate_to_datetime(x[1]), reverse=True)
#
#         for email_id, _ in email_date_pairs:
#             res, msg = mail.fetch(email_id, "(RFC822)")
#             for response_part in msg:
#                 if isinstance(response_part, tuple):
#                     msg = email.message_from_bytes(response_part[1])
#                     subject, encoding = decode_header(msg["Subject"])[0]
#                     if isinstance(subject, bytes):
#                         subject = subject.decode(encoding if encoding else "utf-8")
#                     from_ = msg.get("From")
#
#                     print("Subject:", subject)
#                     print("From:", from_)
#                     print("=" * 100)
#
#                     if msg.is_multipart():
#                         for part in msg.walk():
#                             content_type = part.get_content_type()
#                             content_disposition = str(part.get("Content-Disposition"))
#
#                             try:
#                                 body = part.get_payload(decode=True).decode()
#                             except:
#                                 pass
#
#                             if content_type == "text/plain" and "attachment" not in content_disposition:
#                                 print("Body:", body)
#                                 match = re.search(r'Please use the link below to process payment\s*(https?://\S+)', body)
#                                 if match:
#                                     link = match.group(1)
#                                     print(f"Extracted link: {link}")
#                                     break
#                     else:
#                         body = msg.get_payload(decode=True).decode()
#                         print("Body:", body)
#                         match = re.search(r'Please use the link below to process payment\s*(https?://\S+)', body)
#                         if match:
#                             link = match.group(1)
#                             print(f"Extracted link: {link}")
#                             break
#             if link:
#                 break
#     else:
#         print("No emails found from noreply@senpex.com")
#
#     mail.close()
#     mail.logout()
#
#     return link
# # Example usage
# if __name__ == "__main__":
#     link = get_link_from_email(2)
#     if link:
#         print(f"Found link: {link}")
#     else:
#         print("No link found.")

import imaplib
import email
import re
from email.header import decode_header
from email.utils import parsedate_to_datetime
import time


def get_link_from_email():
    username = "automation.senpex@outlook.com"
    password_for_email = "A27011975a"
    link = None

    start_time = time.time()

    mail = imaplib.IMAP4_SSL("outlook.office365.com", 993)
    try:
        mail.login(username, password_for_email)
        print("Login successful!")
    except imaplib.IMAP4.error as e:
        print(f"Failed to login: {e}")
        return None

    mail.select("inbox")

    status, messages = mail.search(None, '(FROM "noreply@senpex.com")')
    email_ids = messages[0].split()
    email_ids = [eid.decode() for eid in email_ids]  # декодируем идентификаторы

    if email_ids:
        # Получаем заголовки всех сообщений
        result, headers = mail.fetch(','.join(email_ids), '(BODY[HEADER.FIELDS (DATE SUBJECT FROM)])')
        email_date_pairs = []

        for msg_part in headers:
            if isinstance(msg_part, tuple):
                msg = email.message_from_bytes(msg_part[1])
                msg_date = msg["Date"]
                email_id = msg_part[0].decode().split()[0]
                email_date_pairs.append((email_id, msg_date))

        email_date_pairs.sort(key=lambda x: parsedate_to_datetime(x[1]), reverse=True)

        for email_id, _ in email_date_pairs:
            result, msg_data = mail.fetch(email_id, "(RFC822)")
            for msg_part in msg_data:
                if isinstance(msg_part, tuple):
                    msg = email.message_from_bytes(msg_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")
                    from_ = msg.get("From")

                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))

                            try:
                                body = part.get_payload(decode=True).decode()
                            except:
                                continue

                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                match = re.search(r'Please use the link below to process payment\s*(https?://\S+)',
                                                  body)
                                if match:
                                    link = match.group(1)
                                    break
                    else:
                        body = msg.get_payload(decode=True).decode()
                        match = re.search(r'Please use the link below to process payment\s*(https?://\S+)', body)
                        if match:
                            link = match.group(1)
                            break
            if link:
                break
    else:
        print("No emails found from noreply@senpex.com")

    mail.close()
    mail.logout()

    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    return link


link = get_link_from_email()
print(f"Extracted link: {link}")
