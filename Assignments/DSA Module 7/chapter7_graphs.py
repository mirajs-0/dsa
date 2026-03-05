class MachineNetwork:
    def __init__(self):
        self.machine_links = {}

    def add_machine(self, machine):
        if machine not in self.machine_links:
            self.machine_links[machine] = []

    def add_link(self, m1, m2):
        self.add_machine(m1)
        self.add_machine(m2)

        if m2 not in self.machine_links[m1]:
            self.machine_links[m1].append(m2)
        if m1 not in self.machine_links[m2]:
            self.machine_links[m2].append(m1)

    def print_network(self):
        for machine in sorted(self.machine_links.keys()):
            neighbors = sorted(self.machine_links[machine])
            print(f"{machine} -> {neighbors}")

    def print_connected_machines(self, machine):
        if machine not in self.machine_links:
            print(f"Error: {machine} does not exist in the network.")
            return
        print(f"Machines connected to {machine}: {sorted(self.machine_links[machine])}")

    def bfs(self, start):
        if start not in self.machine_links:
            print(f"Error: {start} does not exist in the network.")
            return []

        visited = set([start])
        order = []
        queue = [start]

        while queue:
            current = queue.pop(0)
            order.append(current)

            for neighbor in self.machine_links[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    def dfs(self, start):
        if start not in self.machine_links:
            print(f"Error: {start} does not exist in the network.")
            return []

        visited = set()
        order = []
        stack = [start]

        while stack:
            current = stack.pop()
            if current in visited:
                continue

            visited.add(current)
            order.append(current)

            for neighbor in reversed(self.machine_links[current]):
                if neighbor not in visited:
                    stack.append(neighbor)

        return order


# Testing the code:
network = MachineNetwork()

network.add_link("Machine_A", "Machine_B")
network.add_link("Machine_A", "Machine_C")
network.add_link("Machine_B", "Machine_D")
network.add_link("Machine_C", "Machine_D")
network.add_link("Machine_C", "Machine_E")

network.print_network()
print()

network.print_connected_machines("Machine_C")
print()

print(network.bfs("Machine_A"))
print(network.dfs("Machine_A"))