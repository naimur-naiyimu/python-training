words = {
            'one':'এক',
            'two': 'দুই',
            'three':'তিন',
            'four': 'চার',
            'five':'পাচঁ',
            'six':'ছয়',
            'seven':'সাত',
            'eight':'আট',
            'nine':'নয়',
            'ten':'দশ',
            'eleven':'এগারো',
            'twelve':'বারো',
            'therteen':'তেরো',
            'fourteen':'চৌদ্দ',
            'fifteen':'পনেরো',
            'sixteen':'ষোলো',
            'seventeen':'সতেরো',
            'eightteen':'আটারো',
            'nineteen':'ঊনিশ',
            'twenty':'বিশ',
            'twenty one':'একুশ',
            'twenty two':'বাইশ',
            'twenty three':'তেইশ',
            
    }
while True:
    word = input("enter a word: ")

    if word in words:
        print(words[word])
    else:
        print('not match')
        
    a = input("do you want to continue? if yes enter y else enter n: ")
    if  a =='y' or a =='Y':
        continue
    else:
        break
              
