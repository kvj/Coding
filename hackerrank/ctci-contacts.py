root = None
def add_node(n, data):
    if not n:
        return dict(data=data)
    if n['data'] > data:
        n['left'] = add_node(n.get('left'), data)
    else:
        n['right'] = add_node(n.get('right'), data)
    return n

def find_all(n, data):
    if not n:
        return 0
    ndata = n['data']
    result = 0
    if ndata.startswith(data):
        # count
        return 1 + find_all(n.get('right'), data) + find_all(n.get('left'), data)
    if ndata > data:
        return find_all(n.get('left'), data)
    else:
        return find_all(n.get('right'), data)

n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op == 'add':
        root = add_node(root, contact)
    if op == 'find':
        num = find_all(root, contact)
        print num
