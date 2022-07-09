# Importing dependencies from transformers
from transformers import pipeline,PegasusForConditionalGeneration, AutoTokenizer 

model_name = "google/pegasus-arxiv"

model = PegasusForConditionalGeneration.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline("summarization",model=model,tokenizer=tokenizer)

# Load tokenizer 
# tokenizer = AutoTokenizer.from_pretrained("google/pegasus-xsum")


text ="""Abstract— an intelligent digital assistant who can interpret
the requests of the user via voice commands and can provide
thoughtful responses through its voice while also performing
the various functions.
Keywords—digital-assistant,interpret,requests,voice-commands,
responses,various-functions.
People living with disabilities - whether hidden or visible - have
hopes, dreams and frustrations just like everyone else.
There are many struggles people with disabilities go through.
Here are the few problems faced by the elderly and the disabled
people in their everyday life. A central promise of technology
and its advancements is to bring a better world through solving
inherent problems of human society and its individuals. The
above described issues are addressed using a cheap device
called the “Apthamitra”.
"""

result = classifier(text)

print(result)