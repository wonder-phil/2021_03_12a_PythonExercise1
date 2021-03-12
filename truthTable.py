def truthtable (n):
  if n < 1:
    return [[]]
  subtable = truthtable(n-1)
  return [ row + [v] for row in subtable for v in [True,False] ]



#def my_tt(n):

def ttable(n): 
  if n < 1:
    yield []
    return
  subtable = ttable(n-1)
  for row in subtable:
    for v in [True,False]:
      yield row + [v]


def ttable1(vars,n): 
  if n < 1:
    yield []
    return
  subtable = ttable1(vars,n-1)
  for row in subtable:
    for v in vars:
      for w in [True,False]:
        yield row + [v] + [w]      

#    
# [[True, True], [True, False], [False, True], [False, False]]
# [['x', 'y'], ['x', 'y'], ['x', 'y'], ['x', 'y'] ]
#
# [x for x in ttable(1)]
# [[True], [False]]
#
#
#
# [[True, True]] x [['x', 'y']]
# 
# [ [['x', True], ['y', True]] ]
#
#

#
# combine(['x','y'],[[True,True],[False, False]])
#

def combine(myVars, truthTable):
  r_value = []
  for c in truthTable:
    for v in myVars:
      for item in c:
        r_value = r_value.append([v + item])
  return r_value

    
