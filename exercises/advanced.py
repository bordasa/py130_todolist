# #Problem Overview
# # Input: text
# # Output: longest sentence by words. Also, the number of words in it
# # Rules: Sentences end in '.', '!', '?'
#     # words = any seq of chars not spaces or sentence ends

# #Examples

# #Data Structure: Dictionary? Tuple of just the current max?

# #Algorithm
#     #1. Look at all chars in text
#     #2. Track # of words (sentence word count)
#     #3. if end of sentence, compare current sentence word count to max
#     #4. Update max as needed. Save sentence
#     #5. finish going through all chars
#     #Alt
#     #1. Split text by spaces and save to list
#     #2. Look through all elements in list
#     #3. Find where sentences end and measure the length of each sentence
#     #4. Update max as needed

def longest_sentence(text):
    sentence_endings = '.!?'

    index_L = 0
    index_R = 0

    curr_word_count = 0
    max_word_count = 0
    max_sentence = ''

    for i in range(len(text)):
        char = text[i]

        if char.isspace():
            if i != 0 and text[i-1] not in sentence_endings:
                curr_word_count += 1
    
        if char in sentence_endings:
            curr_word_count += 1
            index_R = i + 1

            if curr_word_count > max_word_count:
                max_word_count = curr_word_count
                max_sentence = text[index_L: index_R]
            
            curr_word_count = 0
            index_L = index_R + 1 #Account for space after punctuation
                                    #This is the start of next word
    
    print(max_sentence)
    # print()
    print(f'The longest sentence has {max_word_count} words.')
    print('---------')

# def longest_sentence(text):
#     sentence_endings = '.!?'

#     text_list = text.split(' ')
#     current_len = 0
#     current_sentence = []
#     max_len = 0
#     max_sentence = []

#     for word in text_list:
#         current_len += 1
#         current_sentence.append(word)

#         if word[-1] in sentence_endings:
#             if current_len > max_len:
#                 max_len, max_sentence = current_len, current_sentence
            
#             current_len, current_sentence = 0, []
    
#     print(' '.join(max_sentence))
#     print()
#     print(f'The longest sentence has {max_len} words.')
#     print()

long_text = (
    'Four score and seven years ago our fathers brought forth on this '
    'continent a new nation, conceived in liberty, and dedicated to the '
    'proposition that all men are created equal. Now we are engaged in a '
    'great civil war, testing whether that nation, or any nation so '
    'conceived and so dedicated, can long endure. We are met on a great '
    'battlefield of that war. We have come to dedicate a portion of that '
    'field, as a final resting place for those who here gave their lives '
    'that that nation might live. It is altogether fitting and proper that '
    'we should do this.'
)

longer_text = long_text + (
    'But, in a larger sense, we can not dedicate, we can not consecrate, '
    'we can not hallow this ground. The brave men, living and dead, who '
    'struggled here, have consecrated it, far above our poor power to add '
    'or detract. The world will little note, nor long remember what we say '
    'here but it can never forget what they did here. It is for us the '
    'living, rather, to be dedicated here to the unfinished work which '
    'they who fought here have thus far so nobly advanced. It is rather '
    'for us to be here dedicated to the great task remaining before us -- '
    'that from these honored dead we take increased devotion to that '
    'cause for which they gave the last full measure of devotion -- that '
    'we here highly resolve that these dead shall not have died in vain '
    '-- that this nation, under God, shall have a new birth of freedom -- '
    'and that government of the people, by the people, for the people, '
    'shall not perish from the earth.'
)

longest_sentence(long_text)
# Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.
#
# The longest sentence has 30 words.

longest_sentence(longer_text)
# It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.
#
# The longest sentence has 86 words.

longest_sentence("Where do you think you're going? What's up, Doc?")
# Where do you think you're going?
#
# The longest sentence has 6 words.

longest_sentence("To be or not to be! Is that the question?")
# To be or not to be!
#
# The longest sentence has 6 words.

