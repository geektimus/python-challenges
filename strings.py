def reverse_string(s):
    return s[::-1]


def reverse_string_without_slicing(s):
    return ''.join(reversed(s))


def reverse_string_without_slicing_and_join(s):
    return ''.join(s[i] for i in range(len(s)-1, -1, -1))
