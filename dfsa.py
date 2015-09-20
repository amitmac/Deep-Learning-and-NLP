def dfsa(tape,initial_state,final_states,transition_table):
    current_state = initial_state
    for index in range(0,len(tape)):
        if (transition_table[current_state][tape[index]] == -1):
            return False          
        current_state = transition_table[current_state][tape[index]]
        
    if (current_state in final_states):
        return True
    else:
        return False

initial_state = 0
final_states = [4]
transition_table = {0:{'b':1,'a':-1,'!':-1},
                    1:{'b':-1,'a':2,'!':-1},
                    2:{'b':-1,'a':3,'!':-1},
                    3:{'b':-1,'a':3,'!':4},
                    4:{'b':-1,'a':-1,'!':-1}}
tape = "baaaa!"                    
accepted = dfsa(tape,initial_state,final_states,transition_table)
print accepted
