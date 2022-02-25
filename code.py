import numpy as np

class Node:
	def __init__(self,data,index,parent):
		self.Node_State_i = data
		self.Node_Index_i = index
		self.Parent_Node_Index_i = parent

def blank_tile(state):
	for i,e in enumerate(state):
		for j,ee in enumerate(e):
			if ee == 0:
				b = [i,j]
	a = [b[0],b[1]]
	return a

def ActionMoveLeft(state):
	global C
	new_State = np.copy(state.Node_State_i)
	a = blank_tile(new_State)
	i,j = a[0],a[1]
	C += 1
	if j > 0:
		
		temp = new_State[i,j-1]
		new_State[i,j-1] = 0
		new_State[i,j] = temp
		New_Node = Node(new_State,C,state)
		
		return New_Node.Node_State_i,New_Node
	else:
		return state.Node_State_i,state

def ActionMoveRight(state):
	global C
	new_State = np.copy(state.Node_State_i)
	a = blank_tile(new_State)
	i,j = a[0],a[1]
	C += 1
	if j < 2:		
		temp = new_State[i,j+1]
		new_State[i,j+1] = 0
		new_State[i,j] = temp
		New_Node = Node(new_State,C,state)
		
		return New_Node.Node_State_i,New_Node
	else:
		return state.Node_State_i,state

def ActionMoveUp(state):
	global C
	new_State = np.copy(state.Node_State_i)
	a = blank_tile(new_State)
	i,j = a[0],a[1]
	C += 1
	if i > 0:
		temp = new_State[i-1, j]
		new_State[i-1,j] = 0
		new_State[i,j] = temp
		New_Node = Node(new_State,C,state)
		
		return new_State,New_Node
	else:
		return state.Node_State_i,state

def ActionMoveDown(state):
	global C
	new_State = np.copy(state.Node_State_i)
	a = blank_tile(new_State)
	i,j = a[0],a[1]
	C += 1
	if  i < 2:
		temp = new_State[i+1, j]
		new_State[i+1,j] = 0
		new_State[i,j] = temp
		New_Node = Node(new_State,C,state)
		
		return New_Node.Node_State_i,New_Node
	else:
		return state.Node_State_i,state

def action(i,curr_node):
	if i == 1:
		New_State,New_Node = ActionMoveUp(curr_node)
		return New_State,New_Node
	elif i == 2:
		New_State,New_Node = ActionMoveDown(curr_node)
		return New_State,New_Node
	elif i == 3:
		New_State,New_Node = ActionMoveLeft(curr_node)
		return New_State,New_Node
	elif i == 4:
		New_State,New_Node = ActionMoveRight(curr_node)
		return New_State,New_Node

def write_to_nodes(state):
	with open('Nodes.txt','a') as f:
		state.ravel()
		for i in state:
			f.write(str(i)[1:-1])
			f.write(' ')
		f.write('\n')

def write_nodes_info(node_index,parent_node_index):
	with open('NodesInfo.txt','a') as f:
		f.write(str(node_index))
		f.write('\t')
		f.write(str(parent_node_index))
		f.write('\n')

def generate_path(node):
	path = []
	path = [node]
	while node.Parent_Node_Index_i != None:
		node = node.Parent_Node_Index_i
		path.append(node)
	path.reverse()

	with open('nodePath.txt','w') as f:
		for i in path:
			state = i.Node_State_i
			state.ravel()
			for j in state:
				f.write(str(j)[1:-1])
				f.write(' ')
			f.write('\n')


def BFS(initial,goal):
	
	global C

	queue = []
	visited = []
	backtracking = []
	curr_node = Node(initial,0,None)
	visited.append(curr_node.Node_State_i.tolist())
	queue.append(curr_node)

	while queue:
		Q = queue.pop(0)
		if(Q.Node_State_i.tolist() != goal_state.tolist()):
			for i in range(1,5):
				NewState,NewNode = action(i,Q)
				
				if NewState.tolist() not in visited:
					visited.append(NewState.tolist())
					queue.append(NewNode)
					
					write_nodes_info(C,NewNode.Parent_Node_Index_i.Node_Index_i)

					write_to_nodes(NewState)
					
					if(NewNode.Node_State_i.tolist() == goal_state.tolist()):
						print("reached")
						print(NewNode.Node_Index_i)
						return NewNode
				else:
					C = C-1

if '__name__ ==__main__':

	C = 0
	with open('NodesInfo.txt','w') as f:
		f.write('Node Index \t Parent Index')
		f.write('\n')
	f.close()
	initial_state = np.array([[4,7,0],[1,2,8],[3,5,6]])
	goal_state = np.array([[1,4,7],[2,5,8],[3,6,0]])

	initial = Node(initial_state.T,0,None)
	last_node = BFS(initial_state,goal_state.T)
	generate_path(last_node)



