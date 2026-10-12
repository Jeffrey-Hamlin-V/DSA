from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words):
        graph = {char:set() for word in words for char in word}; degree = {char:0 for char in graph}
        for first, second in zip(words, words[1:]):
            if len(first) > len(second) and first.startswith(second): return ''
            for a,b in zip(first, second):
                if a != b:
                    if b not in graph[a]: graph[a].add(b); degree[b] += 1
                    break
        queue = deque(char for char in degree if degree[char] == 0); result = []
        while queue:
            char = queue.popleft(); result.append(char)
            for neighbor in graph[char]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0: queue.append(neighbor)
        return ''.join(result) if len(result) == len(graph) else ''
