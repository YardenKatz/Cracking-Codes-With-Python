import random
import sys
import transpositionEncrypt
import transpositionDecrypt


def main():
    random.seed(42)

    for i in range(20):
        # Generate a random message to test
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        # Convert to list to shuffle message
        message = list(message)
        random.shuffle(message)
        # Reconvert to string
        message = ''.join(message)

        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        # Check all possible keys for each message
        for key in range(1, int(len(message) / 2)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()

    print('Transposition cipher test passed.')


if __name__ == '__main__':
    main()
