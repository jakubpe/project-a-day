def shift_list(list, shift_number):
    list_shifted = []
    for char in range(shift_number, len(list)):
        list_shifted.append(list[char])
    for char in range(0, shift_number):
        list_shifted.append(list[char])
    return list_shifted


def encrypt(message, list_shifted, list_not_shifted):
    message_encrypted = []
    for char in message:
        if char in list_not_shifted:
            position = list_not_shifted.index(char)
            message_encrypted.append(list_shifted[position])
        else:
            message_encrypted.append(char)
    word = ''.join(message_encrypted)
    return word


def decrypt(message, list_shifted, list_not_shifted):
    message_decrypted = []
    for char in message:
        if char in list_not_shifted:
            position = list_shifted.index(char)
            message_decrypted.append(list_not_shifted[position])
        else:
            message_decrypted.append(char)
    word = ''.join(message_decrypted)
    return word

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
work = True

while work:
    what_to_do = input("To encrypt wirte E, to decrypt D\n")
    text = input("Message: ").lower()
    shift = int(input("By how many shift the code?\n")) % 32
    alphabet_shifted = shift_list(alphabet, shift)
    if what_to_do == 'E':
        print("Coded message is: {}".format(encrypt(text, alphabet_shifted, alphabet)))
    elif what_to_do == 'D':
        print("Coded message is: {}".format(decrypt(text, alphabet_shifted, alphabet)))
    else:
        print("Wrong instruction provided")
    if input("To continue type 'Y', to end type 'N'\n") == 'N':
        work = False
