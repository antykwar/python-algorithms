class IndirectUnweightedGraph:
    def __init__(self):
        self._nodes_count = 0
        self._neighbours = {}

    def add_vertex(self, value):
        if value not in self._neighbours:
            self._neighbours[value] = set()
            self._nodes_count += 1

    def add_edge(self, *args):
        if len(args) != 2:
            return

        root_node = args[0]
        connected_node = args[1]

        if root_node not in self._neighbours or connected_node not in self._neighbours:
            return

        self._neighbours[root_node].add(connected_node)
        self._neighbours[connected_node].add(root_node)

    def remove_vertex(self, value):
        if value not in self._neighbours:
            return

        del self._neighbours[value]

        for root_node, connected_nodes in self._neighbours.items():
            connected_nodes.discard(value)
            self._neighbours[root_node] = connected_nodes

    def remove_edge(self, *args):
        if len(args) != 2:
            return

        root_node = args[0]
        connected_node = args[1]

        if root_node not in self._neighbours or connected_node not in self._neighbours:
            return

        self._neighbours[root_node].discard(connected_node)
        self._neighbours[connected_node].discard(root_node)

    def show_connections(self):
        return [f'{node} -> {sorted(connected_nodes)}' for node, connected_nodes in sorted(self._neighbours.items())]
