#!/usr/bin/python3
# 101- remove char from the string insert

def remove_char_at(charinsert, n):
    """Create a copy of the string without the character at position n."""
    if n < 0:
        return (charinsert)
    return (charinsert[:n] + charinsert[n+1:])
