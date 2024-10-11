import heapq

def dijkstra(graph, source):
    # Create a distance array to store the shortest distance from the source node to all other nodes
    distance = [float('inf')] * len(graph)
    distance[source] = 0

    # Create a priority queue to store the nodes to be processed
    priority_queue = [(0, source)]

    while priority_queue:
        # Extract the node with the minimum distance from the queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Update the distance array by considering the shortest path from the source node to the current node
        for neighbor, weight in enumerate(graph[current_node]):
            if weight > 0 and distance[neighbor] > current_distance + weight:
                distance[neighbor] = current_distance + weight
                heapq.heappush(priority_queue, (distance[neighbor], neighbor))

    return distance

# Example usage:
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]
source_node = 0
print("Shortest distances from node", source_node, ":")
print(dijkstra(graph, source_node))

