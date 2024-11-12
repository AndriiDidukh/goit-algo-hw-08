
import heapq


def min_cost_to_connect_cables(cable_lengths):
    heapq.heapify(cable_lengths)
    total_cost = 0
    while len(cable_lengths) > 1:
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        cost = first + second
        total_cost += cost
        heapq.heappush(cable_lengths, cost)
        print(
            f"Cable connect {first} and {second} with cost {cost}. Total cost: {total_cost}"
        )
        print(f"Current heap: {cable_lengths}")

    return total_cost


if __name__ == "__main__":
    cable_lengths = [14, 3, 7, 9, 5, 2]
    min_cost = min_cost_to_connect_cables(cable_lengths)
    print("Minimal cost to connect cables:", min_cost)
