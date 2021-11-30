from challenges.graph_depth_first.graph_depth_first import Graph
import pytest


def test_graph_depth_first(graph_vertix):
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    actual = graph_vertix[1].depth_first(graph_vertix[0])
    assert actual == expected


def test_graph_depth_first2(graph_vertix):
    expected = 'B'
    actual = graph_vertix[1].depth_first(graph_vertix[0])[1]
    assert actual == expected


@pytest.fixture
def graph_vertix():
    graph = Graph()
    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    e = graph.add_node('E')
    f = graph.add_node('F')
    g = graph.add_node('G')
    h = graph.add_node('H')

    graph.add_edge(a,b)
    graph.add_edge(a,d)
    graph.add_edge(b,c)
    graph.add_edge(b,d)
    graph.add_edge(c,g)
    graph.add_edge(d,e)
    graph.add_edge(d,h)
    graph.add_edge(d,f)
    graph.add_edge(f,h)

    return a,graph
