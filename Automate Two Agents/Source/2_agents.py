from ChatGPT_api import *

def run_api_loop():
    # Initialize the API agents
    api0 = get_api(0)
    api1 = get_api(1)
    
    # Load the initial prompts from files
    with open('text1.txt', 'r') as f:
        prompt1 = f.read()
    with open('text2.txt', 'r') as f:
        prompt2 = f.read()

    # Send prompt1 to api0 and get the response to add to prompt2
    response1 = api0.send_message(prompt1)['message']
    prompt2 += '\n' + response1
    
    print(prompt2)
    
    # Loop until a termination condition is met
    while True:
        # Send prompt2 to api1 and get the response
        response2 = api1.send_message(prompt2)['message']
        
        # Print response2 and append it to prompt1 for the next iteration
        print(response2)
        
        response1 = api0.send_message(response2)['message']
        prompt2 = response1
        print(prompt2)
        