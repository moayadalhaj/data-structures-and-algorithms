from challenges.graph_breadth_first.graph_breadth_first import Graph
import pytest


def test_not_exist_node():
    expected = "This node does not exist"
    graph = Graph()
    a = 'a'
    actual = graph.breadth_first(a)
    assert actual == expected

def test_graph_breadth_first():
    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']
    graph = Graph()
    Pandora = graph.add_node('Pandora')
    Arendelle = graph.add_node('Arendelle')
    Metroville = graph.add_node('Metroville')
    Monstroplolis = graph.add_node('Monstroplolis')
    Narnia = graph.add_node('Narnia')
    Naboo = graph.add_node('Naboo')

    graph.add_edge(Pandora,Arendelle)
    graph.add_edge(Arendelle,Metroville)
    graph.add_edge(Arendelle,Monstroplolis)
    graph.add_edge(Metroville,Monstroplolis)
    graph.add_edge(Metroville,Narnia)
    graph.add_edge(Monstroplolis,Naboo)

    actual = graph.breadth_first(Pandora)
    assert actual == expected

def test_graph_breadth_first2():
    expected = 'Arendelle'
    graph = Graph()
    Pandora = graph.add_node('Pandora')
    Arendelle = graph.add_node('Arendelle')
    Metroville = graph.add_node('Metroville')
    graph.add_edge(Pandora,Arendelle)
    graph.add_edge(Arendelle,Metroville)

    actual = graph.breadth_first(Pandora)[1]
    assert actual == expected
