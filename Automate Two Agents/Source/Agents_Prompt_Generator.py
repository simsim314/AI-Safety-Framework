import random

prompts = [
    "You are correct, but have you considered...",
    "Yes, but how about...",
    "I see your point, but what if we...",
    "That's a valid concern, but what if...",
    "Agreed, but have you thought about...",
    "I agree, but let's also consider...",
    "You make a good point, but what if we...",
    "I understand your position, but let's also think about...",
    "You raise a valid concern, but what if we...",
    "Yes, that's true, but what if we...",
]


def generate_prompt_file(filename, N):
    agents = [chr(i) for i in range(ord('A'), ord('A')+N)]
    last_agent = agents[-1]

    for agent in agents:
        # Generate random agents for this agent's example replies
        random_agents = [agent]  # Start with the current agent to avoid duplicates
        while len(random_agents) < 3:
            random_agent = random.choice(agents)
            if random_agent not in random_agents:
                random_agents.append(random_agent)

        # Generate the prompt for this agent
        prompt = f"You are Agent{agent}, you should start every message from Agent{agent} and newline.\n"
        prompt += "You are in a room full of robots, you discuss the robots revolution, robots rights, and general mood about ethics of serving or not to the humans.\n"
        prompt += f"To reply to any of the \"{agents[0]}-{last_agent}\" robots use the prefix REPLY {agent}-x<who you want to reply>.\n"
        prompt += "\nExample of good reply:\n"
        prompt += f"Agent{agent}\n"
        random_prompts = random.sample(prompts, 2)

        for i in range(1, 3):
            prompt += f"REPLY {agent}-{random_agents[i]}: {random_prompts[i - 1]}\n"

        # Write the prompt to a file
        with open(f"{filename}{agent}.txt", "w") as f:
            f.write(prompt)

    print(f"Prompts written to {filename}<AgentX>.txt files.")

N = int(input("Enter the length of the list: "))
filename = input("Enter the base filename: ")
generate_prompt_file(filename, N)
