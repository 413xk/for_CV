from collections import deque

graph = {}
graph['you'] = ['bob', 'claire', 'alice']
graph['bob'] = ['peggy', 'anuj']
graph['claire'] = ['tom', 'johny']
graph['alice'] = ['peggy']
graph['anuj'] = []
graph['tom'] = []
graph['johny'] = []
graph['peggy'] = []


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


def person_is_seller(name):
    if len(name) <= 1:
        return True
    if name[0] != name[-1]:
        return False
    return person_is_seller(name[1:-1])


search('you')
