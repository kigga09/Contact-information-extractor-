import re
import patterns as pat

txt = input('Enter your text: \n')

#email, phone number, url, date, time

emails = re.findall(pat.email, txt)
phone_numbers = re.findall(pat.phone_number, txt)
urls = re.findall(pat.url, txt)
dates = re.findall(pat.date, txt)
times = re.findall(pat.time, txt)

print('\n---Results---:\n')




#print(f'phone numbers: {phone_numbers}')
#print(f'emails: {emails}')
#print(f'urls: {urls}')
#print(f'dates: {dates}')
#print(f'times: {times}')

