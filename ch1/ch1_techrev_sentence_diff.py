############################################
# NLTK Sentence Segmenter

# 1. Import the nltk package:
import nltk
# 2. Read in the book text:
filename = "sherlock_holmes_1.txt"
file = open(filename, "r", encoding="utf-8")
text = file.read()
# 3. Replace newlines with spaces:
text = text.replace("\n", " ")
# 4. Initialize an NLTK tokenizer. This uses the Punkt model we downloaded previously:
tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
# 5. Divide the text into sentences:
sentences = tokenizer.tokenize(text)

# In [2]: sentences
# Out[2]:
# ['To Sherlock Holmes she is always _the_ woman.',
#  'I have seldom heard him mention her under any other name.',
#  'In his eyes she eclipses and predominates the whole of her sex.',
#  'It was not that he felt any emotion akin to love for Irene Adler.',
#  'All emotions, and that one particularly, were abhorrent to his cold, precise but admirably balanced mind.',
#  'He was, I take it, the most perfect reasoning and observing machine that the world has seen, but as a lover he would have placed himself in a false position.',
#  'He never spoke of the softer passions, save with a gibe and a sneer.',
#  'They were admirable things for the observer—excellent for drawing the veil from men’s motives and actions.',
#  'But for the trained reasoner to admit such intrusions into his own delicate and finely adjusted temperament was to introduce a distracting factor which might throw a doubt upon all his mental results.',
#  'Grit in a sensitive instrument, or a crack in one of his own high-power lenses, would not be more disturbing than a strong emotion in a nature such as his.',
#  'And yet there was but one woman to him, and that woman was the late Irene Adler, of dubious and questionable memory.']

sentences_nltk = sentences

# NLTK Sentence Segmenter
############################################


############################################
# SpaCy Small Sentence Segmenter

# 1. Import the spacy package:
import spacy
# 2. Read in the book text:
filename = 'sherlock_holmes_1.txt'  # ”->''
file = open(filename, "r", encoding="utf-8")
text = file.read()
# 3. Replace newlines with spaces:
text = text.replace("\n", " ")
# 4. Initialize the spaCy engine:
nlp = spacy.load("en_core_web_sm")
# 5. Divide the text into sentences:
doc = nlp(text)
sentences = [sentence.text for sentence in doc.sents]

# In [2]: sentences
# Out[2]:
# ['To Sherlock Holmes she is always _the_ woman.',
#  'I have seldom heard him mention her under any other name.',
#  'In his eyes she eclipses and predominates the whole of her sex.',
#  'It was not that he felt any emotion akin to love for Irene Adler.',
#  'All emotions, and that one particularly, were abhorrent to his cold, precise but admirably balanced mind.',
#  'He was, I take it, the most perfect reasoning and observing machine that the world has seen, but as a lover he would have placed himself in a false position.',
#  'He never spoke of the softer passions, save with a gibe and a sneer.',
#  'They were admirable things for the observer—excellent for drawing the veil from men’s motives and actions.',
#  'But for the trained reasoner to admit such intrusions into his own delicate and finely adjusted temperament was to introduce a distracting factor which might throw a doubt upon all his mental results.',
#  'Grit in a sensitive instrument, or a crack in one of his own high-power lenses, would not be more disturbing than a strong emotion in a nature such as his.',
#  'And yet there was but one woman to him, and',
#  'that woman was the late Irene Adler, of dubious and questionable memory.']

sentences_spacy = sentences

# SpaCy Small Sentence Segmenter
############################################

############################################
# SpaCy Small vs NLTK Sentence Segmenter

all(ss == sn for ss, sn in zip(sentences_spacy, sentences_nltk))
# Out[7]: False

[ss == sn for ss, sn in zip(sentences_spacy, sentences_nltk)]
# Out[8]: [True, True, True, True, True, True, True, True, True, True, False]

sentences_nltk[-1]
# Out[9]:
# 'And yet there was but one woman to him, and that woman was the late Irene Adler, of dubious and questionable memory.'

sentences_spacy[-2:]
# Out[6]:
# ['And yet there was but one woman to him, and',
#  'that woman was the late Irene Adler, of dubious and questionable memory.']

# SpaCy Small vs NLTK Sentence Segmenter
############################################


############################################
# SpaCy Medium Sentence Segmenter

# 4. Initialize the spaCy engine:
nlp = spacy.load("en_core_web_md")
# 5. Divide the text into sentences:
doc = nlp(text)
sentences = [sentence.text for sentence in doc.sents]


sentences_spacy_md = sentences

# Medium is no better than Small for this sentence...

# In [8]: sentences_spacy_md[-2:]
# Out[8]:
# ['And yet there was but one woman to him, and',
#  'that woman was the late Irene Adler, of dubious and questionable memory.']

# SpaCy Medium Sentence Segmenter
############################################


############################################
# SpaCy Large Sentence Segmenter
#  fixes poor sentence segementation in small and medium

# 4. Initialize the spaCy engine:
nlp = spacy.load("en_core_web_lg")
# 5. Divide the text into sentences:
doc = nlp(text)
sentences = [sentence.text for sentence in doc.sents]


# In [8]: sentences_spacy_md[-2:]
# Out[8]:
# ['And yet there was but one woman to him, and',
#  'that woman was the late Irene Adler, of dubious and questionable memory.']

# SpaCy Large Sentence Segmenter
############################################
