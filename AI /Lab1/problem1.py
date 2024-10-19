class TransportationMDP(object):
    def __init__(self, N):
        # N = number of blocks
        self.N = N
    
    def discount(self):
        return 1.0

    def startState(self):
        return 1

    def isEnd(self, state):
        return state == self.N

    def actions(self, state):
        # return list of valid actions
        result = []
        if state + 1 <= self.N:
            result.append('walk')
        if state * 2 <= self.N:
            result.append('tram')
        return result

    def succProbReward(self, state, action):
        # return list of (newState, prob, reward) triples
        result = []
        if action == 'walk':
            result.append((state + 1, 1.0, -1.0))  # (newState, probability, reward)
        elif action == 'tram':
            result.append((state * 2, 0.5, -2.0))  # (newState, probability, reward)
            result.append((state, 0.5, -2.0))     # Sometimes tram fails, stay at the same state
        return result

    def states(self):
        return range(1, self.N + 1)

# Example usage:
mdp = TransportationMDP(N=10)
print(mdp.actions(3))  # Should print the available actions at state 3
print(mdp.succProbReward(3,'walk'))
print(mdp.succProbReward(3,'tram'))