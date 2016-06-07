from nltk.tokenize.regexp import RegexpTokenizer

import nltk, re
import settings
import event_functions as ef

class Extract_event():
    """A class to extract events from a document."""
    
    def __init__(self, document):
        """Tokenize the text of the body."""
        self.settings = settings.Settings()
        self.tokeniser = RegexpTokenizer(self.settings.pattern)
        self.text = document['body']
        self.sentences = nltk.sent_tokenize(self.text)
        self.event = document['head']
        
    def info(self):
        """Print info regarding the event."""
        print(self.event)
        print(self.venue)
        
    def pos_tag(self):
        """Tag the words of the sentences."""
        self.sentences = ef.tokenize_sent(self.sentences, self.tokeniser)
        ef.clean_sentences(self.sentences)
        self.sentences = [nltk.pos_tag(sent) for sent in self.sentences]
        
    def extract_tag(self, tag):
        """Return a list containing words with the given tag."""
        relevant = []
        for sent in self.sentences:
            for word in sent:
                if word[1] == tag:
                    relevant.append(word[0])
        return relevant
        
    def extract_venue(self, venues):
        """Extract venue from the document."""
        relevant = self.extract_tag('NNP')
        self.venue = ef.check_venue(relevant, venues)
        
    def extract_time(self):
        """Extracts the date time from the mail."""
        self.time = ''
