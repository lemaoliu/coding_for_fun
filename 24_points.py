class Node:

  def __init__(self, val, opt=None,l=None,r=None):
    self.val = val
    self.opt = opt
    self.lch = l
    self.rch = r

  def add(self, x, y):
    return Node(x.val+y.val, '+', x, y)

  def minus(self, x, y):
    return Node(x.val-y.val, '-', x, y)

  def mul(self, x, y):
    return Node(x.val*y.val, '*', x, y)

  def div(self, x, y):
    assert y.val != 0, 'error'
    return Node(x.val/y.val, '/', x, y)

  def __str__(self):
    if self is None:
      return ""
    if self.opt is None:
      return '%d'%self.val
    else:
      return "(%s %s %s)" % (self.lch.__str__(),
          self.opt, self.rch.__str__())

def solve(a):
  if len(a) == 1:
    flag = 1 if abs(a[0].val-tot) < 1e-5 else 0
    return flag, a[0]
  expr = None
  find_res = False
  for i, x in enumerate(a):
    for j in xrange(i+1,len(a)):
      y = a[j]
      res = [a[k] for k in xrange(len(a)) if k != i and k !=j ]
      array = [(x,x.add,y),(x,x.minus,y),(x,x.mul,y),
                   (x,x.div,y),(y,x.minus,x),(y,x.div,x)]
      for u,opt,w in array:
        if opt == x.div:
          if w.val == 0 or u.val % w.val != 0:
            continue
        find_res, expr = solve(res+[opt(u,w)])
        if find_res:
          break
    if find_res:
      break
  return find_res, expr
 
a = [1,2,2,6]
a = [1,3,5,7]
a = [4,5,8,7]
a = [6,1,7,8]
a = [13, 3, 2, 10, 1]
a = [4,6,7,9]
nodes = [Node(x) for x in a]
ans, tree = solve(nodes)
if ans:
  print tree, '= %d'%tot
else:
  print 'invalid expr'
