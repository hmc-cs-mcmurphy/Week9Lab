# Pig Latin Python translation from C
# (First lab version with bugs added)
#
# for HMC CS181Q
# Copyright 2019 Anderson MacKay
# MIT Licensed
#
"""
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""


import sys
import string

vowels = "aeiou"

# Check a word for a couple of important
# transform characteristics.  Takes in a single word
# and returns the tuple (beginsvowel, allupper, firstupper)
# beginswowel: true when the word begins with a vowel
# allupper: true if the word is all uppercase
# firstupper: true if the word's first character is uppercase
def pig_checkword(word):
    if word == word.upper():
        allupper = True
        firstupper = False
    elif word[0] == word[0].upper():
        allupper = False
        firstupper = True
    else:
        allupper = False
        firstupper = False

    if word[0].lower() in vowels:
        beginsvowel = True
    else:
        beginsvowel = False

    return (beginsvowel, allupper, firstupper)
   

# Do the Pig Latin transform on a single word,
# transformed word is returned
def pig_latinize(buf):
    (beginsvowel, allupper, firstupper) = pig_checkword(buf)

    # normalize to lowercase
    outbuf = buf.lower()
        
    # settle on a suffix
    if beginsvowel:
        suffix = "way"
    else:
        suffix = "ay"

    # reorder, for words not starting with a vowel
    if not beginsvowel:
        split_index = 0
        for ch in outbuf:
            if ch in vowels:
                break
            split_index = split_index + 1
        if split_index < len(buf):
            outbuf = outbuf[split_index:] + outbuf[:split_index]

    # add the suffix
    outbuf = "%s%s" % (outbuf, suffix)
            
    # if we started out Capitalized or ALL CAPS, fix back up
    if allupper:
        outbuf = outbuf.upper()
    elif firstupper:
        outbuf = outbuf.capitalize()

    return outbuf

def main():
    inbuf = sys.stdin.readline()
    while inbuf and len(inbuf) > 0:
        word = None
        for ch in inbuf:
            if not ch.isalnum():
                if word:
                    sys.stdout.write(pig_latinize(word))
                    word = None
                sys.stdout.write(ch) 
            else:
                if not word:
                    word = ""
                word = word + ch
        if word:
            sys.stdout.write(pig_latinize(word))
            word = None
        inbuf = sys.stdin.readline()

if __name__ == "__main__":
    main()
