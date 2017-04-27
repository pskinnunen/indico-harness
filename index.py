# Key is located in:
# ~/.indicorc
# [auth]
# api_key = YOUR_API_KEY

import indicoio

# single_sentiment
indico_sentiment = indicoio.sentiment("Let's write some code!")
print("Sentiment: {}".format(indico_sentiment))

# single_language detection
lang_rec_dict = indicoio.language("Let's write some code!") # dozens of languages
language_max = max(lang_rec_dict, key=lang_rec_dict.get) # get max prediction
print("Language: {}".format([language_max, lang_rec_dict[language_max]]))

# batch examples
batch_sentiments = indicoio.sentiment([
    "It's the best day ever.",
    "Spent a whole two hours just tying my shoe."
])
print("Batch Setiments: {}".format(batch_sentiments))

# Image recognition example
image_url = "http://cdn3-www.dogtime.com/assets/uploads/gallery/goldendoodle-dog-breed-pictures/puppy-4_1.jpg"
image_rec_dict = indicoio.image_recognition(image_url) # list of ~1k possible images
image_max = max(image_rec_dict, key=image_rec_dict.get)
print("Image Recognition: {}".format([image_max, image_rec_dict[image_max]]))
