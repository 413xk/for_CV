# создаем хэш таблицы стоимости ребер
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

infinity = float('inf') # конечный узел стоит бесконечность
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:  # перебираем все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  # если это узел с наименьшей стоимостью из уже виденных и он еще не был обработан
            lowest_cost = cost  # ...он назначается новым узлом с наименьшей стоимостью
            lowest_cost_node = node
        return lowest_cost_node


node = find_lowest_cost_node(costs) # найти узел с наименьшей стоимостью среди необработанных
while node is not None: # если обработаны все узлы, цикл завершен
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # пеберать всех соседей текущего узла
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: # если к соседу можно добраться быстрее через текущий узел...
            costs[n] = new_cost # ...обновить стоимость для этого узла
            parents[n] = node # этот узел становится новым родителем для соседа

    processed.append(node) # узел помечается как обработанный
    node = find_lowest_cost_node(costs) # найти следующий узел для обработки и повторить цикл

print(cost)