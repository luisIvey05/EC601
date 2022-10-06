from google.cloud import language_v1
#export GOOGLE_APPLICATION_CREDENTIALS="PATH"

client = language_v1.LanguageServiceClient()

text_content = 'I am so happy and joyful.'

# Available types: PLAIN_TEXT, HTML
type_ = language_v1.Document.Type.PLAIN_TEXT

# Optional. If not specified, the language is automatically detected.
# For list of supported languages:
# https://cloud.google.com/natural-language/docs/languages
language = "en"
document = {"content": text_content, "type_": type_, "language": language}

# Available values: NONE, UTF8, UTF16, UTF32
encoding_type = language_v1.EncodingType.UTF8

response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
# Get overall sentiment of the input document
print(u"Document sentiment score: {}".format(response.document_sentiment.score))
print(u"Document sentiment magnitude: {}".format(response.document_sentiment.magnitude))