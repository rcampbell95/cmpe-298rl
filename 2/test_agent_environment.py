from environment import Environment
from agent import Agent

#import gym

if __name__ == "__main__":
    env = Environment()
    test_agent = Agent()

    while not env.is_done():
        test_agent.step()

    print("Total rewards: {}".format(test_agent.total_reward))



