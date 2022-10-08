import streamlit as st
import cohere
from cohere.classify import Example 

NoLinesDisplayed = 8
NoLinesUsed = 2
co = cohere.Client(st.secrets["cohere_api"])

emotions = [
    Example("The order came 5 days early", "positive"), Example("The item exceeded my expectations", "positive"), 
    Example("I ordered more for my friends", "positive"), Example("I would buy this again", "positive"), 
    Example("I would recommend this to others", "positive"), Example("The package was damaged", "negative"), 
    Example("The order is 5 days late", "negative"), Example("The order was incorrect", "negative"), 
    Example("I want to return my item", "negative"), Example("The item\'s material feels low quality", "negative")]

st.title('Cohere.ai Demo')

if 'chat_conv' not in st.session_state:
    st.session_state['chat_conv'] = ['Bot: Start typing below to chat with me.\n']

conv = st.session_state['chat_conv']

container_top = st.empty()
container_top.text(''.join(conv[-1*NoLinesDisplayed:]))

container_bottom = st.empty()
input = container_bottom.text_input("Your Message",value="",key="msg")

#container_emotion = st.empty()
#container_emotion.text("---")

if input != '':
    conv.append('You: '+input+'\n')
    chat_conv = conv[-1*NoLinesUsed:]
    # response = "Hello, I am a bot. I am here to help you. How can I help you?"
    response = co.generate(
        prompt=''.join(chat_conv)+"\Bot:",
        model='xlarge', max_tokens=20,   temperature=1.2,   k=0,   p=0.75,
        frequency_penalty=0,   presence_penalty=0, return_likelihoods='NONE',
        stop_sequences=["User:", "\n"]
    ).generations[0].text.strip()
 
    conv.append('Bot: '+response+'\n')
    container_top.text(''.join(conv[-1*NoLinesDisplayed:]))
    input = container_bottom.text_input("Your Message",value="",key="placeholder")
    st.session_state['chat_conv'] = conv[-1*NoLinesDisplayed:]

    #emotion = co.classify( model='large', inputs=[input], examples=emotions) 
    #e0 = emotion.classifications[0].confidence[0]
    #e1 = emotion.classifications[0].confidence[1]
    #container_emotion.text(e0.label+":"+str(e0.confidence)+" - "+e0.label+":"+str(e0.confidence))
   
#st.write(response.generations[0].text)
