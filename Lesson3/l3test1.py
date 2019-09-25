import requests
import collections
import matplotlib as mpl

searchCriteriaFirst = '<div id="chapter1"'
searchCriteriaSecond = '<div class="center">'
searchCriteria_div = '</div>'
searchCriteriaThird = '<div class="illustration">'
searchCriteriaFour = '<div class="docfoot">'
searchCriteriaFive = '<div id'
searchCriteriaSix = '<p class="dropcap">'


def parseHTML(text, one, two):
    i = text.count(one)
    if two=='</html>':
        k=7
    else:
        k = 6
    for j in range(i):
        temp_index_one = text.find(one)
        temp_index_two = text.find(two, temp_index_one)
        text = text.replace(text[temp_index_one:temp_index_two + k], "")
    return text

def parseHTMLSecond(text, one):
    i = text.count(one)
    for j in range(i):
        text = text.replace(one, "")
    return text

def mainParser():
    try:
        response = requests.get(
            'https://ebooks.adelaide.edu.au/c/carroll/lewis/alice/chapter1.html')  # , timeout=(10, 0.0001))
        textBase = response.text
        one = textBase.find(searchCriteriaFirst)
        textOne = textBase[one:]
        textTwo = parseHTML(textOne, searchCriteriaSecond, searchCriteria_div)
        textThree = parseHTML(textTwo, searchCriteriaThird, searchCriteria_div)
        textFour = parseHTML(textThree, searchCriteriaFour, '</html>')
        textFive = parseHTML(textFour, searchCriteriaFive, searchCriteria_div)
        textSix = textFive.replace(searchCriteriaSix, "")
        textSeven = parseHTMLSecond(textSix, '<p>')
        textEight = parseHTMLSecond(textSeven, '</p>')
        textNine = parseHTMLSecond(textEight, '<em>')
        textTen = parseHTMLSecond(textNine, '</em>')
        textTen = parseHTMLSecond(textTen, '</div>')
        textTen = parseHTMLSecond(textTen, '?')
        textTen = parseHTMLSecond(textTen, '!')
        textTen = parseHTMLSecond(textTen, ',')
        textTen = parseHTMLSecond(textTen, '.')
        textTen = parseHTMLSecond(textTen, '’')
        textTen = parseHTMLSecond(textTen, '‘')
        textTen = parseHTMLSecond(textTen, ';')
        textTen = parseHTMLSecond(textTen, ':')
        textTen = parseHTMLSecond(textTen, '(')
        textTen = parseHTMLSecond(textTen, ')')
        textTen = parseHTMLSecond(textTen, '*')
        # textTen = parseHTMLSecond(textTen, '-')
        textTen = parseHTMLSecond(textTen, '_')
        textTen = parseHTMLSecond(textTen, '\n')
        textTen = parseHTMLSecond(textTen, '“')
        textTen = parseHTMLSecond(textTen, '”')
        textTen = parseHTMLSecond(textTen, '—')
        # textTen = parseHTMLSecond(textTen, 'ing')
        #         # textTen = parseHTMLSecond(textTen, 'ed')
        return textTen
    except requests.exceptions.ReadTimeout:
        print('Oops. Read timeout occured')
    except requests.exceptions.ConnectTimeout:
        print('Oops. Connection timeout occured!')

if __name__ == '__main__':
    richText = mainParser()
    richText= richText.split(' ')
    # print(richText)
    finalDict = {}

    for s in richText:
        if s in finalDict:
            finalDict[s] = finalDict[s] + 1
        else:
            finalDict[s] = 1
    # finalDict = sorted(finalDict.items())
    # sorted_dict = collections.OrderedDict(finalDict)
    sorted_dict = sorted(finalDict.items(), key=lambda kv: kv[1])
    sorted_dict.reverse()
    print(sorted_dict)
    for k, v in sorted_dict:
        print(f'слово {k} встретилось {v} раз')





