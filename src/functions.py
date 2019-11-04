import re

def sex_filter(text):
    dictionary = {'.':"Unknown", 
                'F':'F',
                'M':'M',
                'M ':'M',
                'N':"Unknown",
                'lli':"Unknown"}
    return dictionary.get(text,text)

def fatal_filter(text):
    dictionary = {'F':'Y',
                'Y':'Y',
                'UNKNOWN':'Unknown',
                ' N':'N',
                'Unknown':'Unknown',
                'N':'N',
                'N ':'N'}
    return dictionary.get(text,text)

def space_cleaner(text):
    return text.strip()

def age_cleaner(text):
    dictionary = {'"middle-age"':25,
                '"young"':25,
                ' ':"Unknown",
                '  ':"Unknown",
                "middle-age":30,
                "young":25,
                '(adult)':30,
                '10 or 12':11,
                '12 or 13':12,
                '13 or 18':16,
                '16 to 18':17,
                '17 & 16':16,
                '17 & 35':26,
                '18 months':1,
                '18 or 20':19,
                '18 to 22':20,
                '2 to 3 months':0,
                '20?':20,
                '20s':20,
                '21 & ?':21,
                '21 or 26':23,
                '21, 34,24 & 35':28,
                '23 & 20':21,
                '23 & 26':24,
                '25 or 28':26,
                '25 to 35':30,
                '28 & 26':27,
                '28, 23 & 30':27,
                '30 & 32':31,
                '30 or 36':33,
                '30s':30,
                '31 or 33':32,
                '32 & 30':31,
                '33 & 26':29,
                '33 & 37':35,
                '33 or 37':35,
                '34 & 19':26,
                '36 & 23':29,
                '36 & 26':31,
                '37, 67, 35, 27,  ? & 27':39,
                '40s':40,
                '46 & 34':40,
                '50 & 30':40,
                '50s':50,
                "60's":60,
                '60s':60,
                '6½':6,
                '7      &    31':19,
                '7 or 8':7,
                '8 or 10':9,
                '9 & 12':10,
                '9 months':1,
                '9 or 10':9,
                '>50':55,
                '?    &   14':14,
                '? & 19':19,
                'A.M.':"Unknown",
                'Both 11':"Unknown",
                'Ca. 33':33,
                'Elderly':80,
                'F':"Unknown",
                'MAKE LINE GREEN':"Unknown",
                'Teen':15,
                'Teens':15,
                'Unknown':"Unknown",
                'X':"Unknown",
                'adult':35,
                'mid-20s':25,
                'mid-30s':35,
                'teen':15,
                'young':20,
                '\xa0 ':"Unknown",
                'M':"Unknown",
                "13 or 14":13}
    return dictionary.get(text,text)


def integer(text):
    return int(text)


