from environment import Environment
from agent import Agent

#import gym

if __name__ == "__main__":
    env = Environment()
    test_agent = Agent()

    steps = 0
    while not env.is_done():
        print ("Current step: {}".format(steps))
        test_agent.step(env)
        steps += 1

    print("Total rewards: {}".format(test_agent.total_reward))
