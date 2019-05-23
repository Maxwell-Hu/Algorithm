def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}

    # initialize base case in t = 0
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]] # V[t][y]表示t时刻，由 状态y 得到观测结果obs[t]的概率
        path[y] = [y]

    # iterable while t > 0
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        for y in states:
            (prob, state) = max([(V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states])
            V[t][y] = prob
            newpath[y] = path[state] + [y]
        
        path = newpath

    (prob, state) = max([(V[len(obs)-1][y], y) for y in states])
    return (path[state], prob)

if __name__ == '__main__':
    states = ('Healthy', 'Fever')
 
    observations = ('normal', 'cold', 'dizzy')
 
    start_probability = {'Healthy': 0.6, 'Fever': 0.4}
 
    transition_probability = {
    'Healthy' : {'Healthy': 0.7, 'Fever': 0.3},
    'Fever' : {'Healthy': 0.4, 'Fever': 0.6},
    }
    
    emission_probability = {
    'Healthy' : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
    'Fever' : {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
    }

    print(viterbi(observations, states, start_probability, transition_probability, emission_probability))