def main():
  myMessage = 'Common sense is not so common.'
  myKey = 8

  ciphertext = encryptMessage(myKey, myMessage)
  print(ciphertext + '|')

def encryptMessage(key, message):
# each string in ciphertext represents a column in the grid:
  ciphertext = [''] * key

  for column in range(key):
    currentIndex = column

    # Keep looping until currentIndex goes past the message length:
    while currentIndex < len(message):
      # Place the character at currentIndex in message at the
      # end of the current column in the ciphertext list:
      ciphertext[column] += message[currentIndex]

      # Move currentIndex over:
      currentIndex += key

  return ''.join(ciphertext)


# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function:

if __name__=='__main__':
  main()
