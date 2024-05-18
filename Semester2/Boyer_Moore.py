class last_occurrence(object):

    def __init__(self, pattern, alphabet):
        self.occurrences = dict()
        for letter in alphabet:
            self.occurrences[letter] = pattern.rfind(letter)

    def __call__(self, letter):
        return self.occurrences.get(letter, -1)


def boyer_moore_match(text, pattern):
    alphabet = set(text)
    last = last_occurrence(pattern, alphabet)
    m = len(pattern)
    n = len(text)
    i = m - 1  # text index
    j = m - 1  # pattern index
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            l = last(text[i])
            i = i + m - min(j, 1 + l)
            j = m - 1
    return -1


if __name__ == '__main__':

    def show_match(text, pattern):
        print('Text:  %s' % text)
        p = boyer_moore_match(text, pattern)
        if p != -1:
            print('Match: %s%s' % ('.' * p, pattern))
        else:
            print('No match found')


    text3 = 'abcdefghij'
    pattern3 = 'def'
    show_match(text3, pattern3)
    print()
