from queue import PriorityQueue
from h_node import move_node
from heuristics import a_star, best_first, best_first2, breakfast_search, breakfast_search2, depth_first_search, depth_first_search2, ham_distance, man_distance, perm_inversion

goalState = ["1", "2", "3", "8", "B", "4", "7", "6", "5"]

initial_State2 = ["2", "3", "4", "1", "8", "5", "7", "6", "B"]

initial_State3 = ["5", "1", "4", "7", "B", "6", "3", "8", "2"]

initial_State = ["3", "5", "B", "2", "1", "4", "8", "7", "6"]

if __name__ == '__main__':
#     # print(generate_success_State(goalState))
#     print(depth_first_search2(initial_State,goalState))
#     print(breakfast_search2(initial_State,goalState))
#     print(best_first2(ham_distance,initial_State3,goalState))
    print(a_star(ham_distance,initial_State3,goalState))


#     list1 = PriorityQueue()
#     list1.put((1,"PHAT ASS"))
#     list1.put((3,"PHAT ASS3"))
#     list1.put((2,"PHAT ASS2"))
#     list1.put((8,"PHAT ASS8"))

#     print(list1.get(1))