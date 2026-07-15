import re

phone_number = re.compile(r'''
(  
((\()|(\+1 ))?        #optional ( or +1
\d{3}           # 3 digits 
[\. -)]?               # optional . or - or space or )
\d{3}                      # 3 digits
[\. -]?                # optional . or - or space 
\d{4}               # 4 digits                                      
                          )''', re.X)

print(re.findall(phone_number, '111-222-3333'))