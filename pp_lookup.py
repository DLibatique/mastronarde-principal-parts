# all principal parts from Mastronarde's master list

from greek_accentuation.characters import *
import re

character_map = {
    'a': 'α',
    'b': 'β',
    'g': 'γ',
    'd': 'δ',
    'e': 'ε',
    'z': 'ζ',
    'h': 'η',
    'q': 'θ',
    'i': 'ι',
    'k': 'κ',
    'l': 'λ',
    'm': 'μ',
    'n': 'ν',
    'c': 'ξ',
    'o': 'ο',
    'p': 'π',
    'r': 'ρ',
    's': 'σ',
    't': 'τ',
    'u': 'υ',
    'f': 'φ',
    'x': 'χ',
    'y': 'ψ',
    'w': 'ω',
}

# master verb list
verbs = [
    ['ἀγγέλλω', 'ἀγγελέω', 'ἤγγειλα', 'ἤγγελκα', 'ἤγγελμαι', 'ἠγγέλθην'],
    ['ἀγνοέω', 'ἀγνοήσω', 'ἠγνόησα', 'ἠγνόηκα', 'ἠγνόημαι', 'ἠγνοήθην'],
    ['ἄγω', 'ἄξω', 'ἤγαγον', 'ἦχα', 'ἦγμαι', 'ἤχθην'],
    ['ἀδικέω', 'ἀδικήσω', 'ἠδίκησα', 'ἠδίκηκα', 'ἠδίκημαι', 'ἠδικήθην'],
    ['ἁθροίζω', 'ἁθροίσω', 'ἥθροισα', 'ἥθροικα', 'ἥθροισμαι', 'ἡθροίσθην'],
    ['αἱρέω', 'αἱρήσω', 'εἷλον (ἑλ-)', 'ᾕρηκα', 'ᾕρημαι', 'ᾑρέθην'],
    ['αἰσθάνομαι', 'αἰσθήσομαι', 'ᾐσθόμην', '', 'ᾔσθημαι', ''],
    ['αἰτέω', 'αἰτήσω', 'ᾔτησα', 'ᾔτηκα', 'ᾔτημαι', 'ᾐτήθην'],
    ['αἰτιάομαι', 'αἰτιάσομαι', 'ᾐτιασάμην', '', 'ᾐτίαμαι', 'ᾐτιάθην'],
    ['ἀκούω', 'ἀκούσομαι', 'ἤκουσα', 'ἀκήκοα', '', 'ἠκούσθην'],
    ['ἁλίσκομαι', 'ἁλώσομαι', 'ἑάλων/ἥλων', 'ἑάλωκα/ἥλωκα', '', ''],
    ['ἀλλάττω', 'ἀλλάξω', 'ἤλλαξα', 'ἤλλαχα', 'ἤλλαγμαι', 'ἠλλάχθην/ἠλλάγην'],
    ['ἁμαρτάνω', 'ἁμαρτήσομαι', 'ἥμαρτον', 'ἡμάρτηκα', 'ἡμάρτημαι', 'ἡμαρτήθην'],
    ['ἀξιόω', 'ἀξιώσω', 'ἠξίωσα', 'ἠξίωκα', 'ἠξίωμαι', 'ἠξιώθην'],
    ['ἀπαντάω', 'ἀπαντήσομαι', 'ἀπήντησα', 'ἀπήντηκα', '', ''],
    ['γράφω', 'γράψω', 'ἔγραψα', 'γέγραφα', 'γέγραμμαι', 'ἐγράφην'],
    ['ἀποθνῄσκω', 'ἀποθανέομαι', 'ἀπέθανον', 'τέθνηκα', '', ''],
    ['ἀποκτείνω', 'ἀποκτενέω', 'ἀπέκτεινα', 'ἀπέκτονα', '', ''],
    ['ἀπόλλυμι', 'ἀπολέω', 'ἀπώλεσα/ἀπωλόμην', 'ἀπολώλεκα/ἀπόλωλα', '', ''],
    ['ἀπολογέομαι', 'ἀπολογήσομαι', 'ἀπελογησάμην', '', 'ἀπολελόγημαι', ''],
    ['ἀπορέω', 'ἀπορήσω', 'ἠπόρησα', 'ἠπόρηκα', 'ἠπόρημαι', 'ἠπορήθην'],
    ['λύω', 'λύσω', 'ἔλυσα', 'λέλυκα', 'λέλυμαι', 'ἐλύθην'],
]

# get list of unaccented first principal parts
stripped_1st_pps = []
for x in verbs:
    pp1_stripped = ''
    for letter in x[0]:
        pp1_stripped += base(letter)
    stripped_1st_pps.append(pp1_stripped)

request = input("For what verb would you like the principal parts?")

def get_stripped_1st_pp(requested_verb):

    '''
    input: string (either in latin or greek alphabet)
    output: string (in greek alphabet, no accents)
    '''

    if re.search('[a-z]', requested_verb):
        request_stripped = ''
        for letter in request:
            request_stripped += character_map[str(letter)]
    else:
        request_stripped = ''
        for letter in request:
            request_stripped += base(letter)

    return request_stripped

if get_stripped_1st_pp(request) not in stripped_1st_pps:
    print('verb not found!')
else:
    for x in verbs:
        pp1_stripped = ''
        for letter in x[0]:
            pp1_stripped += base(letter)
        if request == x[0] or get_stripped_1st_pp(request) == pp1_stripped:
            print(x)
        else:
            pass
