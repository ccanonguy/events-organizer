import json
import dateutil.parser as datep

def clean_sentences(sentences):
    """Remove the whitespace at the ends of the words."""
    for sent in sentences:
        for count in range(len(sent)):
            sent[count] = sent[count].strip()
            
def tokenize_sent(sentences, tokeniser):
    """Tokenize the sentences using regexp."""
    sentences = [tokeniser.tokenize(sent) for sent in sentences]
    return sentences

def load_venues(path):
    """Load venues from a given file."""
    with open(path) as ft:
        venues = json.load(ft)
    return venues
    
def reduce_str(string):
    """Remove spaces, dots, hyphens, apostrophes and lower the string."""
    string = string.replace(' ', '').replace('.', '')
    string = string.replace('-', '').replace('\'', '')
    string = string.lower()
    return string

def match(str1, str2):
    """Check whether two strings are equal."""
    if reduce_str(str1) == reduce_str(str2):
        return True
    else:
        return False

def check_venue(relevant, venues):
    """Checks the venues in relevant against the venue list."""
    for word in relevant:
        for venue in venues['sn']:
            if match(word, venue):
                return venue
        for venue in venues['names']:
            if match(word, venue):
                return venue

def clean_relevant(relevant, skip_tag):
    """Removes the words in skip_tag from relevant."""
    for word in skip_tag:
        while(word in relevant):
            relevant.remove(word)

def check_time(text):
    """Checks the time from the text."""
    text = text.replace('.', ' ').replace('"', ' ').replace('\'', '')
    text = text.replace('?', ' ').replace('\n', ' ').replace('\t', ' ')
    try:
        event_time = datep.parse(text, fuzzy=True, dayfirst=True)
    except ValueError:
        event_time = 'Couldn\'t extract time properly.'
    return event_time
