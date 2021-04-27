

cipher_num = int(input('What is your cipher number? '))
message = input('What is your message? ')
real_message = list(message)
letters = 'abcdefghijklmnopqrstuvwxyz'
letters_lower = list(letters)
upper = letters.upper()
letters_upper = list(upper)


if should_encode:
  for m in range(len(real_message)):

    if real_message[m] == '!':
      real_message[m] = 33
    if real_message[m] == '-':
      real_message[m] = 45
    if real_message[m] == '"':
      real_message[m] = 34
    if real_message[m] == ' ':
      real_message[m] = 32
    if real_message[m] == ',':
      real_message[m] = 44
    if real_message[m] == '.':
      real_message[m] = 46

    if real_message[m] in letters_upper:
      real_message[m] = (ord(real_message[m]) + cipher_num)

      if real_message[m] > 90:
        real_message[m] =  (real_message[m] - 90) + 64


    if real_message[m] in letters_lower:
      real_message[m] = (ord(real_message[m]) + cipher_num)

      if real_message[m] > 122:
        real_message[m] =  (real_message[m] - 122) + 96

    real_message[m] = chr(real_message[m]) 
  final_message = ''.join(real_message)
  print(final_message.upper())


