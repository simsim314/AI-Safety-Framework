from ChatGPT_api import *

N = 3  # number of agents
agents = [chr(i) for i in range(ord('A'), ord('A')+N)]
    
def run_api_loop():
    # Initialize the API agents
    apis = [get_api(i) for i in range(N)]

    # Load the initial prompts from files
    prompts = []
    for i in range(N):
        with open(f'text{agents[i]}.txt', 'r') as f:
            prompts.append(f.read())
    
    responses = []
    for i in range(N):
        input_str = '\n'.join(responses)
        response = apis[i].send_message(prompts[i] + '\n' + input_str)['message']
        print(response)
        
        responses.append(response)

    # Loop until a termination condition is met
    while True:
        # Print the responses
        for i in range(N):
            # Send the inputs to the corresponding agents and get the responses
            input_str = '\n'.join(responses[-N:])
            response = apis[i].send_message(input_str)['message']
            print(response)
            responses.append(response)
run_api_loop()
