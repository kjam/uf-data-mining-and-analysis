all_tags = set(itertools.chain(*stories.tags.values.ravel()))

print('c' in all_tags)

def clean_text(sentence):
    words = re.findall("\w+", sentence.lower())
    return [word for word in words if
            word not in stop_words.ENGLISH_STOP_WORDS
            and (len(word) > 1 or word in all_tags)
           ]

clean_text("I don't like watching TV News.")
