import numpy

__author__ = 'xx'

if __name__ == '__main__':
    states = ['hot', 'cold']
    observation_options = ['1', '2', '3']
    start_transitions = [.8, .2]  # start -> hot, cold
    transitions = [[.7, .3],  # hot -> hot, cold
                   [.4, .6]]  # cold -> hot, cold
    observation_probs = [[.2, .4, .4],  # hot -> 1, 2, 3
                         [.5, .4, .1]]  # cold -> 1, 2, 3

    observations = ['3', '1', '3']

    probability_matrix = numpy.zeros((len(states), len(observations)))

    for state, state_name in enumerate(states):
        probability_of_state = start_transitions[state]
        probability_of_observation = observation_probs[state][observation_options.index(observations[0])]
        probability_matrix[state][0] = probability_of_state * probability_of_observation

    for observation, observation_name in enumerate(observations[1:], start=1):  # already did obs 1 above
        for state, state_name in enumerate(states):
            probability = 0
            for previous, previous_name in enumerate(states):
                probability_of_state = probability_matrix[previous, observation - 1] * transitions[previous][state]
                probability_of_observation = observation_probs[state][observation_options.index(observation_name)]
                probability_of_observation_at_state = probability_of_state * probability_of_observation
                probability += probability_of_observation_at_state
            probability_matrix[state][observation] = probability

    probability = probability_matrix[:, len(observations) - 1].sum()

    print(probability_matrix)
    print(probability)

