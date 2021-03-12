#
# CNF-SAT
#
# not(x) is written ~x
# only variables can have NOTs
#
# listOfClauses: [['x', 'y', 'z', 'x2'], ['a', 'b', 'x'] ['x2', 'y']...
# truthAssignment: [[x True] [x2 False] [y True] ...
#    assumes each variable occurs exactly once
#


#
# clause = ['x1', 'x2']
# truthAssignment: [['x1', True], ['x2', False]]
#
# orClause(['x1', 'x2'], [['x1', False], ['x2', False]])
# orClause(['x1', 'x2'], [['x1', True], ['x2', False]])
# orClause(['~x1', 'x2'], [['x1', True], ['x2', False]])
# orClause(['~x1', '~x2'], [['x1', True], ['x2', False]])
#
def orClause(clause, truthAssignment):
    if len(clause) == 0:
      return False
    for c in clause:
      t_value = findTruthValue(removeNot(clause[0]), truthAssignment)
      if hasNot(clause[0]):
        t_value = not(t_value)
      return t_value or orClause(clause[1:], truthAssignment)


#
# [['x1', 'y', 'z', 'x2'], ['a', 'b', 'x'] ['x2', 'y']...
# listOfClauses [['~x1', 'x2'], ['x1', '~x2']]
# truthAssignments [['x1', True], ['x2', False]]
# satExpression([['~x1', 'x2']], [['x1', False], ['x2', False]])
# satExpression([['~x1', 'x2'], ['x1', '~x2']], [['x1', True], ['x2', False]])
# satExpression([['~x1', 'x2'], ['x1', '~x2']], [['x1', False], ['x2', False]])
# 

def satExpression(listOfClauses, truthAssignment):
  if len(listOfClauses) == 0:
    return True
  else:
    for c in listOfClauses:
        t_value = orClause(listOfClauses[0], truthAssignment)
        return t_value and satExpression(listOfClauses[1:], truthAssignment)
    
#
# '~x'
# hasNot('~x')
# hasNot('x3')
#
def hasNot(var):
  return var[0] == "~"

#
# removeNot('~x')
# removeNot('xy3')
#
def removeNot(var):
  if hasNot(var):
    return var[1:];
  else:
    return var;

def findTruthValue(stringVariable, truthAssignment):
  s_var = removeNot(stringVariable)
  pair = next(filter(lambda truthAssignment: truthAssignment[0] ==  s_var, truthAssignment), None)
  if (pair == None):
    return False
  else:
    return pair[1]

