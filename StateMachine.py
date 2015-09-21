class StateMachine:
    def __init__(self,initial_state,transition_table,final_states):
        self.state = initial_state
        self.transition_table = transition_table
        self.final_states = final_states
    
    def ndfsa(self,tape):
        agenda = [[self.state,0]]
        temp = agenda.pop()
        current_state, index = temp[0], temp[1]
        while True:
            if index == len(tape) - 1 and current_state in self.final_states:
                return True
            else:
                agenda = agenda + self.new_states(current_state,index,tape)
                if not agenda:
                    return False
                else:
                    temp = agenda.pop()
                    current_state, index = temp[0], temp[1]
        
        if accept_state(current_state):
            return True
        else:
            return False

    def new_states(self,current_state,index,tape):
        agenda = []
        for state in self.transition_table[current_state][tape[index]]:
            agenda.append([state,index+1])
        for state in self.transition_table[current_state]['E']:
            if state != '-1':
            	agenda.append([state,index])
        
        return agenda

initial_state = 0
final_states = [4]
transition_table = {0:{'b':[1],'a':-1,   '!':-1, 'E':'-1'},
                    1:{'b':-1, 'a':[2],  '!':-1, 'E':'-1'},
                    2:{'b':-1, 'a':[2,3],'!':-1, 'E':'-1'},
                    3:{'b':-1, 'a':-1,   '!':[4],'E':'-1'},
                    4:{'b':-1, 'a':-1,   '!':-1, 'E':'-1'}}
tape = "baaaa!"
sm = StateMachine(initial_state,transition_table,final_states)
accepted = sm.ndfsa(tape)
print accepted
