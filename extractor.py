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

#emails 
print(f'Emails({len(emails)}):')
if emails == []:
    print('none')
else:
    for i in emails:
        print(f'\t{i}')

#phone numbers
print(f'Phone Numbers({len(phone_numbers)}):')
if phone_numbers == []:
    print('none')
else:
    for i in phone_numbers:
        print(f'\t{i}')

#urls
print(f'URLs({len(urls)}):')
if urls == []:
    print('none')
else:
    for i in urls:
        print(f'\t{i}')

#dates
print(f'Dates({len(dates)}):')
if dates == []:
    print('none')
else:
    for i in dates:
        print(f'\t{i}')

#times
print(f'Times({len(times)}):')
if times == []:
    print('none')
else:
    for i in times:
        print(f'\t{i}')


