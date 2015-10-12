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

    most_likely_sequence = [None] * len(observations)

    current_most_likely_probability = 0
    current_most_likely = ''
    previous_state = -1

    for state, state_name in enumerate(states):
        probability = start_transitions[state] * observation_probs[state][observation_options.index(observations[0])]
        if probability > current_most_likely_probability:
            current_most_likely_probability = probability
            current_most_likely = state_name
            most_likely_sequence[0] = state_name
            previous_state = state

    for observation, observation_names in enumerate(observations[1:], start=1):
        current_most_likely_probability = 0
        current_most_likely = ''

        for state, state_name in enumerate(states):
            probability = transitions[previous_state][state] * observation_probs[state][observation]
            if probability > current_most_likely_probability:
                current_most_likely_probability = probability
                current_most_likely = state_name
                most_likely_sequence[observation] = state_name
        previous_state = states.index(current_most_likely)

    print(most_likely_sequence, current_most_likely_probability)
