def find_pair(a, m):
    parlor = []
    tree = None
    def add_parlor(i, v):
        item = {'index': i, 'value': v}
        parlor.append(item)
        return item
    def add_2_tree(node, item):
        if not node:
            return {'data': item}
        if item['value'] <= node['data']['value']:
            node['left'] = add_2_tree(node.get('left'), item)
        else:
            node['right'] = add_2_tree(node.get('right'), item)
        return node
    def find_in_tree(node, item, value):
        if not node:
            return None
        if node['data']['value'] == value and node['data'] != item:
            return node['data']
        elif node['data']['value'] < value:
            return find_in_tree(node.get('right'), item, value)
        else:
            return find_in_tree(node.get('left'), item, value)
    for i in range(len(a)):
        v = a[i]
        if v < m:
            item = add_parlor(i+1, v)
            tree = add_2_tree(tree, item)
    for item in parlor:
        item2 = find_in_tree(tree, item, m-item['value'])
        if item2:
            return item['index'], item2['index']
    return None, None

t = int(raw_input().strip())
for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    v1, v2 = find_pair(a, m)
    print '%s %s' % (v1, v2)
