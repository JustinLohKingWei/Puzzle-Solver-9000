from heuristics import a_star, best_first, breadth_first_search, depth_first_search, ham_distance, man_distance, perm_inversion

goalState = ["1", "2", "3", "8", "B", "4", "7", "6", "5"]

initial_State1 = ["5", "1", "4", "7", "B", "6", "3", "8", "2"]

initial_State2 = ["3", "5", "B", "2", "1", "4", "8", "7", "6"]

initial_State3 = ["2", "8", "3", "1", "6", "4", "7", "B", "5"]

if __name__ == '__main__':

    # Uncomment for DFS, BFS
    # print(depth_first_search(initial_State, goalState))
    # print(breadth_first_search(initial_State, goalState))

    print(best_first(ham_distance, initial_State3, goalState))
    print(a_star(ham_distance, initial_State3, goalState))
    print(best_first(man_distance, initial_State3, goalState))
    print(a_star(man_distance, initial_State3, goalState))
    print(best_first(perm_inversion, initial_State3, goalState))
    print(a_star(perm_inversion, initial_State3, goalState))
