# Это реализация алгоритма BFS (Breadth-First Search)
# Пример работы из книги "Грокаем алгоритмы"
from collections import deque

def person_is_seller(person):
    if person[:-1] == "m":
        return True
    return False

def search(name):
    q = deque()
    q += graph[name]
    searched = set()
    while q:
        person = q.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is seller!")
                return True
            else:
                q += graph[person]
                searched.add(person)
    return False


