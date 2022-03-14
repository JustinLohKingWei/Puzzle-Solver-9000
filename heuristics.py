from h_node import h_node, move_node


def move(initial_state, move):
    blank_Position = initial_state.index('B')
    swap_position_index = 0

    if(move == "down"):
        swap_position_index = blank_Position+3
        swap_item = initial_state[swap_position_index]
    elif(move == "up"):
        swap_position_index = blank_Position-3
    elif(move == "left"):
        swap_position_index = blank_Position-1
    elif(move == "right"):
        swap_position_index = blank_Position+1

    next_State = initial_state.copy()

    swap_item = initial_state[swap_position_index]
    next_State[blank_Position] = swap_item
    next_State[swap_position_index] = "B"

    return(next_State)


def generate_success_State(initial_state):
    blank_Position = initial_state.index('B')+1

    node = h_node(initial_state)

    if blank_Position < 7:
        node.setDownMove(move(initial_state, "down"))
    if blank_Position > 3:
        node.setUpMove(move(initial_state, "up"))
    if blank_Position not in [1, 4, 7]:
        node.setLeftMove(move(initial_state, "left"))
    if blank_Position % 3 != 0:
        node.setRightMove(move(initial_state, "right"))

    # State order is [down up left right]
    return node


def perm_inversion(state, goalstate):
    perm_sum = 0
    for i in state:
        currentIndex = state.index(i)
        realIndex = goalstate.index(i)
        diff = realIndex-currentIndex
        if(diff < 0):
            diff = 0
        perm_sum += diff
    return perm_sum


def man_distance(state, goalstate):
    manhattan_distance = 0
    for val1, val2 in zip(state, goalstate):
        if(val1 == "B"):
            val1 = 9
        if(val2 == "B"):
            val2 = 9
        manhattan_distance += abs(int(val1)-int(val2))

    return manhattan_distance


def ham_distance(state, goalstate):
    # Hamming distance = number of misplaced tiles
    hammingDistance = 0

    for i in range(len(state)):
        if state[i] != goalstate[i]:
            hammingDistance += 1

    return hammingDistance


def depth_first_search(start_state, goal_state):
    # use a node object and do DFS on each of its children and so on
    print("Using Depth First 2")
    openList = []
    closedList = []
    path = []

    openList.append(move_node(start_state, []))

    while(openList != []):
        current_Node = openList.pop()
        if(current_Node.getCurrent() == goal_state):
            closedList.append(current_Node)
            print("Search Path Cost:", len(closedList))
            count = 0
            indexedNode = closedList[-1]
            while(indexedNode.getPrev() != []):
                path.append(indexedNode.getCurrent())
                indexedNode = indexedNode.getPrev()
                count += 1
            print("Search Path Length:", count)
            # Uncomment this to print
            # print("Search Path:",path)
            return True
        else:
            sucess_states = generate_success_State(current_Node.getCurrent())
            closedList.append(current_Node)
            nextmoves = sucess_states.getMoves()
            for move in nextmoves:
                if(move != []):
                    i = move_node(move, current_Node)
                    if (i not in openList and i not in closedList):
                        openList.append(i)
    return False


def breadth_first_search(start_state, goal_state):
    print("Using breadth first")

    openList = []
    closedList = []
    path = []

    openList.append(move_node(start_state, []))

    while(openList != []):
        current_Node = openList.pop(0)
        if(current_Node.getCurrent() == goal_state):
            closedList.append(current_Node)
            print("Search Path Cost:", len(closedList))
            count = 0
            indexedNode = closedList[-1]
            while(indexedNode.getPrev() != []):
                path.append(indexedNode.getCurrent())
                indexedNode = indexedNode.getPrev()
                count += 1
            print("Search Path Length:", count)
            # Uncomment this to print
            # print("Search Path:",path)
            return True
        else:
            sucess_states = generate_success_State(current_Node.getCurrent())
            closedList.append(current_Node)
            nextmoves = sucess_states.getMoves()
            for move in nextmoves:
                if(move != []):
                    i = move_node(move, current_Node)
                    if (i not in openList and i not in closedList):
                        openList.append(i)
    return False


def best_first(h_func, start_state, goal_state):
    print("Using best first v2")

    openList = []
    closedList = []
    path = []

    openList.append(move_node(start_state, []))

    while(openList != []):
        current_Node = openList.pop(0)
        if(current_Node.getCurrent() == goal_state):
            closedList.append(current_Node)
            print("Search Path Cost:", len(closedList))
            count = 0
            indexedNode = closedList[-1]
            while(indexedNode.getPrev() != []):
                path.append(indexedNode.getCurrent())
                indexedNode = indexedNode.getPrev()
                count += 1
            print("Search Path Length:", count)
            print("Search Path:", path)
            return True
        else:
            sucess_states = generate_success_State(current_Node.getCurrent())
            closedList.append(current_Node)
            nextmoves = sucess_states.getMoves()
            for move in nextmoves:
                if(move != []):
                    i = move_node(move, current_Node)
                    if (i not in openList and i not in closedList):
                        # sort based on h_func
                        openList.append(i)
                        # implement f(n) here
                        sortedOpenList = sorted(
                            openList, key=lambda x: h_func(x.getCurrent(), goal_state))
                        openList = sortedOpenList
    return False


def a_star(h_func, start_state, goal_state):
    print("Using A*")

    openList = []
    closedList = []
    path = []

    openList.append(move_node(start_state, []))
    cost = 0

    while(openList != []):
        current_Node = openList.pop(0)
        if(current_Node.getCurrent() == goal_state):
            closedList.append(current_Node)
            print("Search Path Cost:", len(closedList))
            count = 0
            indexedNode = closedList[-1]
            while(indexedNode.getCurrent() != start_state):
                path.append(indexedNode.getCurrent())
                indexedNode = indexedNode.getPrev()
                count += 1
            print("Search Path Length:", count)
            print("Search Path:", path)
            return True
        else:
            sucess_states = generate_success_State(current_Node.getCurrent())
            closedList.append(current_Node)
            nextmoves = sucess_states.getMoves()
            cost += 1
            for move in nextmoves:
                if(move != []):
                    i = move_node(move, current_Node)
                    # i not in openList and
                    if (i not in closedList):
                        # sort based on h_func
                        openList.append(i)
                        # implement f(n) here
                        sortedOpenList = sorted(
                            openList, key=lambda x: h_func(x.getCurrent(), goal_state)+cost)

                        openList = sortedOpenList
    return False
