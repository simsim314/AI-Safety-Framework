2_agents.py - is the main script\
ChatGPT_api.py - is the [pyChatGPT](https://github.com/terry3041/pyChatGPT) wrapper. \
text1/2.txt are the prompts

### Code snippet
/# Initialize the API agents ChatGPT_api\
api0 = get_api(0)\
api1 = get_api(1)

/# Load the initial prompts from files\
with open('text1.txt', 'r') as f:\
    prompt1 = f.read()\
with open('text2.txt', 'r') as f:\
    prompt2 = f.read()

/# Send prompt1 to api0 and get the response to add to prompt2, pyChatGPT format\
response1 = api0.send_message(prompt1)['message']
