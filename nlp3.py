from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk_sents
from extractText import extractText
#with open('sample.txt', 'r') as f:
 #   sample = f.read().decode('utf-8')

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names


def get_entity_names(text, stoplist):
    entity_names = []
    sentences = sent_tokenize(text)
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = ne_chunk_sents(tagged_sentences, binary=True)

    for tree in chunked_sentences:
        # Print results per sentence
        # print extract_entity_names(tree)
        
        entity_names.extend(extract_entity_names(tree))

# Print all entity names
# print entity_names
# return unique entity names
    #return set(entity_names)

    # clean entity names
    with open(stoplist, 'r') as f:
        stopwords = set(f.read().lower().split('\n'))
    newentitylist = [word for word in set(entity_names) if word.lower() not in stopwords]
    #newentitylist = set(entity_names) - set(stopwords)
    return newentitylist


# get sentences in which the person appears
def sentextract(text, entity, max_value):
    entity = entity.lower()
    sentences = sent_tokenize(text)
    n_sent = []
    count = 0
    for sent in sentences:
        if count > (max_value - 1):
            break
        if entity in sent.lower():
            n_sent.append(sent)
            count += 1
    return n_sent








