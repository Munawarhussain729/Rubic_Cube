

import copy
from collections import deque

class RubicCube:
  __size = 3
  

  def __init__(self):
    __size = 3
    self.path = []
    self._front = [['R', 'R', 'R'],
            ['R', 'R', 'R'],
            ['R', 'R', 'R']]

    self._back = [['O', 'O', 'O'],
            ['O', 'O', 'O'],
            ['O', 'O', 'O'],]

    self._top = [['W', 'W', 'W'],
          ['W', 'W', 'W'],
          ['W', 'W', 'W']]

    self._bottom = [['Y', 'Y', 'Y'],
              ['Y', 'Y', 'Y'],
              ['Y', 'Y', 'Y']]

    self._left = [['G', 'G', 'G'],
            ['G', 'G', 'G'],
            ['G', 'G', 'G']]

    self._right = [['B', 'B', 'B'],
            ['B', 'B', 'B'],
            ['B', 'B', 'B']]
  
  def insertPath(self, path):
    self.path.append(path)

  def GetRight(self):
    return self._right
  
  def GetLeft(self):
    return self._left

  def GetTop(self):
    return self._top

  def GetBottom(self):
    return self._bottom

  def GetFront(self):
    return self._front

  def GetBack(self):
    return self._back

  def moveRight(self):
    dummy = [[]]
    dummy = copy.deepcopy(self._right)
    k = self.__size - 1
    for i in range(3):
      for j in range(3):
        dummy[j][k] = self._right[i][j]
      k = k-1
    self._right = copy.deepcopy(dummy)

    list1 = []
    for x in range(3):
      list1.insert(x, self._top[x][self.__size-1])

    for x in range(3):
      self._top[x][self.__size-1] = self._front[x][self.__size-1]
      self._front[x][self.__size-1] = self._bottom[x][self.__size-1]
      self._bottom[x][self.__size-1] = self._back[x][self.__size-1]
      self._back[x][self.__size-1] = list1[x]

  def moveLeft(self):
    dummy = [[]]
    dummy = copy.deepcopy(self._left)
    k = self.__size-1
    for i in range(3):
      for j in range(3):
        dummy[j][k] = self._left[i][j]
      k = k-1
    self._left = copy.deepcopy(dummy)

    list1 = []
    for x in range(3):
      list1.insert(x, self._top[x][0])

    for x in range(3):
      self._top[x][0] = self._front[x][0]
      self._front[x][0] = self._bottom[x][0]
      self._bottom[x][0] = self._back[x][0]
      self._back[x][0] = list1[x]

  def moveTop(self):
    dummy = [[]]
    dummy = copy.deepcopy(self._top)
    k = self.__size-1
    for i in range(3):
      for j in range(3):
        dummy[j][k] = self._top[i][j]
      k = k-1
    self._top = copy.deepcopy(dummy)

    list1 = []
    for x in range(3):
      list1.insert(x, self._front[0][x])

    for x in range(3):
      self._front[0][x] = self._right[0][x]
      self._right[0][x] = self._back[0][x]
      self._back[0][x] = self._left[0][x]
      self._left[0][x] = list1[x]

  def moveBottom(self):
    dummy = [[]]
    dummy = copy.deepcopy(self._bottom)
    k = self.__size-1
    for i in range(3):
      for j in range(3):
        dummy[j][k] = self._bottom[i][j]
      k = k-1
    self._bottom = copy.deepcopy(dummy)

    list1 = []
    for x in range(3):
      list1.insert(x, self._front[self.__size-1][x])

    for x in range(3):
      self._front[self.__size-1][x] = self._left[self.__size-1][x]
      self._left[self.__size-1][x] = self._back[self.__size-1][x]
      self._back[self.__size-1][x] = self._right[self.__size-1][x]
      self._right[self.__size-1][x] = list1[x]
 
  def PrintCube(self):
    print("Front is ", end=" ")
    print(self._front)
    print("Back is ", end=" ")
    print(self._back)
    print("Right is ", end=" ")
    print(self._right)
    print("Left is ", end=" ")
    print(self._left)
    print("Top is ", end=" ")
    print(self._top)
    print("Bottom is ", end=" ")
    print(self._bottom)

  def moveFront(self):
    dummy = [[]]
    dummy = copy.deepcopy(self._front)
    k = self.__size-1
    for i in range(3):
      for j in range(3):
        dummy[j][k] = self._front[i][j]
      #   print(dummy[j][k], end=" ")
      # print()
    k = k-1

    self._front = copy.deepcopy(dummy)
    list1 = []

    for x in range(3):
      list1.insert(x, self._top[self.__size-1][x])

    for x in range(3):
      self._top[self.__size-1][x] = self._left[self.__size-1][x]
      self._left[self.__size-1][x] = self._bottom[self.__size-1][x]
      self._bottom[self.__size-1][x] = self._right[self.__size-1][x]
      self._right[self.__size-1][x] = list1[x]
    

  def moveBack(self):
    dummy = [[]]
    dummy = copy.deepcopy(self._back)
    k = self.__size-1
    for i in range(self.__size ):
      for j in range(self.__size ):
        dummy[j][k] = self._back[i][j]
    k = k-1
    self._front = copy.deepcopy(dummy)
    list1 = []

    for x in range(3):
      list1.insert(x, self._top[0][x])

    for x in range(3):
      self._top[0][x] = self._right[0][x]
      self._right[0][x] = self._bottom[0][x]
      self._bottom[0][x] = self._left[0][x]
      self._left[0][x] = self._top[0][x]



  def print_phases(self):  # This Function Will Print the Rubic Cube Means all the Faces of Rubic cube
    print("Top Phase is: ")
    for x in self._top:
      for y in x:
        print(y, end="  ")
      print()

    print("Bottom Phase is: ")
    for x in self._bottom:
      for y in x:
        print(y, end="  ")
      print()

    print("Right Phase is: ")
    for x in self._right:
      for y in x:
        print(y, end="  ")
      print()

    print("Left Phase is: ")
    for x in self._left:
      for y in x:
        print(y, end="  ")
      print()

    print("Front Phase is: ")
    for x in self._front:
      for y in x:
        print(y, end="  ")
      print()

    print("Back Phase is: ")
    for x in self._back:
      for y in x:
        print(y, end="  ")
      print()
    
def Final_State(Rubic_cube):
  right_phase = Rubic_cube.GetRight()
  Left_phase = Rubic_cube.GetLeft()
  Top_phase = Rubic_cube.GetTop()
  Bottom_phase = Rubic_cube.GetBottom()
  Front_phase = Rubic_cube.GetFront()
  Back_phase = Rubic_cube.GetBack()

  for x in right_phase:
    for y in x:
      if y != 'B':
        # print( y )
        return -1
  
  for x in Left_phase:
    for y in x:
      if y != 'G':
        # print( y )
        return -1
  
  for x in Bottom_phase:
    for y in x:
      if y != 'Y':
        # print( y )
        return -1
    
  for x in Top_phase:
    for y in x:
      if y != 'W':
        # print( y )
        return -1

  for x in Back_phase:
    for y in x:
      if y != 'O':
        # print( y )
        return -1

  for x in Front_phase:
    for y in x:
      if y != 'R':
        # print( y )
        return -1
  Rubic_cube.PrintCube()
  print("Path is Given as : ", end=" ")
  print(Rubic_cube.path)
  return 1

 
def printLevelOrder( cube):
  if cube is None:
    return
  print("Starting Cube is ")
  cube.PrintCube()
  print()
  queue = deque()
  queue.append(cube)
  i = 1
  while(len(queue) > 0):
    node = queue.popleft()
    re_value = str(Final_State(node))
    i = i+1
    
    if re_value == '1':
      print("Solved Cube is ")
      node.PrintCube()
      print("Path is Given as : ", end=" ")
      print(node.path)
      return 

    else:
      cube_R = copy.deepcopy(node)
      cube_R.insertPath('R')
      cube_L = copy.deepcopy(node)
      cube_L.insertPath('L')
      cube_T = copy.deepcopy(node)
      cube_T.insertPath('T')
      cube_Bo = copy.deepcopy(node)
      cube_Bo.insertPath('Bo')
      cube_F = copy.deepcopy(node)
      cube_F.insertPath('F')
      cube_Ba = copy.deepcopy(node)
      cube_Ba.insertPath('Ba')

      cube_R.moveRight()
      cube_L.moveLeft()
      cube_T.moveTop()
      cube_Bo.moveBottom()
      cube_F.moveFront()
      cube_Ba.moveBack()
      if (( str(Final_State(cube_L)) == '1') or (( str(Final_State(cube_R)) == '1')) or (( str(Final_State(cube_T)) == '1'))):
        return 
      if(( str(Final_State(cube_Bo)) == '1') or ( str(Final_State(cube_F)) == '1') or ( str(Final_State(cube_Ba)) == '1')):
        return 
      queue.append(cube_R)
      queue.append(cube_Bo)
      queue.append(cube_F)
      queue.append(cube_L)
      queue.append(cube_T)
      queue.append(cube_Ba)
      


def main():
    print("Welcome to our Game ")
    dummyCube = RubicCube()
    dummyCube.moveRight()
    dummyCube.moveBottom()
    # dummyCube.moveBottom()
    # dummyCube.moveBack()
    dummyCube.PrintCube()
    print()
    printLevelOrder(dummyCube)


if __name__ == "__main__":
    main()
