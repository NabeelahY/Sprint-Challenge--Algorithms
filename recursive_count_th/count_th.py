'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count=0):
    # check if 'th' is in word
    if 'th' not in word:
        return count
    # check if word has letters
    if len(word) == 0:
        return count
    # if 'th' is in word
    elif 'th' in word:
        # increment count
        count += 1
        # replace 'th' with space and call function on it
        return count_th(word.replace('th', ' ', 1), count)
