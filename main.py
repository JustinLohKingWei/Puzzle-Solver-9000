from heuristics import a_star, best_first, breakfast_search, depth_first_search, generate_success_State, ham_distance, move

goalState = ["1","2","3","8","B","4","7","6","5"]

# initial_State = ["2","3","4","1","8","5","7","6","B"]

# initial_State = ["5","1","4","7","B","6","3","8","2"]

initial_State = ["3","5","B","2","1","4","8","7","6"]

if __name__ == '__main__':
     # print(generate_success_State(goalState))
     # print(depth_first_search(initial_State,goalState))
     print(breakfast_search(initial_State,goalState))
     # print(best_first(ham_distance,initial_State,goalState))
     # print(a_star(ham_distance,initial_State,goalState))

