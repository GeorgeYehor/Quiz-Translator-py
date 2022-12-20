import random
import sys

word = 'a'
def words():
    global translate
    global word
    word = str(input('Enter a word:   '))
    if word == 'x':
        sys.exit('GoodBye!')
    elif word == '':
        while word == '':
            word = (input('Enter a word:   '))


    translate = (input('Enter a translate:   '))
    if word == 'q':
        translate == word
    elif translate == 'x':
        sys.exit('GoodBye!')
    elif translate == '':
        while translate == '':
            translate = str(input('Enter translation:   '))


    if word == 'q':
        print('\nExcellent! you wrote the words and their translations, now you can move on to learning :) \nWhen you '
              'want to exit, \npress \'x, ENTER\'\n')
    else:
        print('(' + word.lower() + ')' + '  -  ' + '(' + translate.lower() + ')' + '\n\nThe words are written down \nTo'
              ' start checking, write - \'q, ENTER, q, ENTER\'\nOr keep typing\n')


#Infinite loop, which ends after double clicking on "q"
dictionary_word = []
dictionary_translate = []
while word != 'q':
    words()
    dictionary_word.append(word.lower())
    dictionary_translate.append(translate.lower())

#Delate "q"
dictionary_word.remove('q')
dictionary_translate.remove('q')


#Naive solution
dic = {}
for i in range(0, len(dictionary_word)):
    dic[dictionary_word[i]] = dictionary_translate[i]
    dic[dictionary_translate[i]] = dictionary_word[i]

sum_words = dictionary_word + dictionary_translate

#Writing user-entered words to a separate file called "Dictionary.txt"

dictionary_txt = open('Dictionary.txt', 'a', encoding='utf-8')

dictionary_number = list(dictionary_word)
length = len(dictionary_number)

#line numbering in the "Dictionary.txt" file
number = sum(1 for line in open('Dictionary.txt', 'r', encoding='utf-8'))
while word != 'q':
    number += 1
num_line = number + 1
l = (list(range(num_line, 1000000)))
m = map(str, l)
num = list(m)
for index1, index2, index3 in zip((num), list(dictionary_word), list(dictionary_translate)):
    dictionary_txt.write(index1 + ': ' + index2 +' - ' +index3+'\n')


def funk():
    try:
       random_word = random.choice(sum_words)
       inf = input('Enter translation\n'+random_word+' - ')
    except IndexError:
        print('GoodBye')

#The function of exiting the program by pressing "ENTER" in the test block
    if inf == 'x':
           sys.exit('GoodBye!')


    while inf != dic[random_word]:
           inf = input('Wrong, try again\n'+ random_word +' - ')
           if inf == 'x':
               sys.exit('GoodBye!')

    while (dic[inf]) == random_word:
        print('Cool!\n')
        funk()
        words()

try:
   funk()
except NameError:
    print()
