import unittest
from data_structures.indirect_unweighted_graph import *


class IndirectUnweightedGraphCase(unittest.TestCase):
    @staticmethod
    def _get_initial_graph():
        graph = IndirectUnweightedGraph()

        for i in range(0, 7):
            graph.add_vertex(i)

        edges_list = [(3, 1), (3, 4), (4, 2), (4, 5), (1, 2), (1, 0), (0, 2), (6, 5)]

        for edge in edges_list:
            graph.add_edge(*edge)

        return graph

    @staticmethod
    def _get_initial_graph_show_connections():
        return [
            '0 -> [1, 2]',
            '1 -> [0, 2, 3]',
            '2 -> [0, 1, 4]',
            '3 -> [1, 4]',
            '4 -> [2, 3, 5]',
            '5 -> [4, 6]',
            '6 -> [5]'
        ]

    @staticmethod
    def _get_vertex_remove_show_connections():
        return [
            '0 -> [2]',
            '2 -> [0, 4]',
            '4 -> [2, 5]',
            '5 -> [4, 6]',
            '6 -> [5]'
        ]

    @staticmethod
    def _get_edge_remove_show_connections():
        return [
            '0 -> [1, 2]',
            '1 -> [0, 2, 3]',
            '2 -> [0, 1, 4]',
            '3 -> [1, 4]',
            '4 -> [2, 3]',
            '5 -> []',
            '6 -> []'
        ]

    def test_graph_creation(self):
        graph = self._get_initial_graph()
        self.assertListEqual(self._get_initial_graph_show_connections(), graph.show_connections())

    def test_vertex_remove(self):
        graph = self._get_initial_graph()
        graph.remove_vertex(3)
        graph.remove_vertex(1)
        self.assertListEqual(self._get_vertex_remove_show_connections(), graph.show_connections())

    def test_edge_remove(self):
        graph = self._get_initial_graph()
        graph.remove_edge(4, 5)
        graph.remove_edge(5, 6)
        self.assertListEqual(self._get_edge_remove_show_connections(), graph.show_connections())
