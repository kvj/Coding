class Graph:
    def __init__(self, size):
        self.a = []
        self.m = []
        self.size = size
        for i in range(size):
            self.a.append([])
            self.m.append(False)
    
    def connect(self, u, v):
        self.a[u].append(v)
        self.a[v].append(u)
        
    def _find_distance(self, tasks, g):
        new_tasks = []
        for t in tasks:
            u,d = t
            au = self.a[u]
            if g in au:
                return d+1, []
            for v in au:
                if not self.m[v]:
                    self.m[v] = True
                    new_tasks.append([v, d+1])
        return 0, new_tasks
            
    def find_all_distances(self, s):
        result = []
        for i in range(self.size):
            if i == s:
                continue
            for j in range(self.size):
                self.m[j] = False
            self.m[i] = True
            tasks = [[i, 0]]
            l = None
            while len(tasks):
                l, tasks = self._find_distance(tasks, s)
                if l:
                    break
            result.append(l*6 if l else -1)
        print ' '.join(map(str, result))

def input():
    return int(raw_input().strip())
    
t = input()
for i in range(t):
    n,m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for i in xrange(m):
        x,y = [int(x) for x in raw_input().split()]
        graph.connect(x-1,y-1) 
    s = input()
    graph.find_all_distances(s-1)
