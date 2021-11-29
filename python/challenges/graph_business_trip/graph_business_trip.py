from Data_structure.graph.graph import Graph

def business_trip(graph,cites):
    """
    A function that return true if there is direct flight for input list cities
    and flight cost.
    -------
    Arguments: graph, array of city names
    Return: boolean, cost or null
    """
    trip = True
    cost = 0
    for i in range(len(cites)-1):
        for city_path in graph.get_neighbors(cites[i]):
            if cites[i+1]==city_path.vertex:
                cost+=city_path.weight
    if cost == 0:
        trip = False
    return trip, '$'+str(cost)


if __name__ == '__main__':
    graph = Graph()
    pandora= graph.add_node('Pandora')
    arendelle= graph.add_node('Arendelle')
    metroville= graph.add_node('Metroville')
    narina= graph.add_node('Narina')
    naboo= graph.add_node('Naboo')
    manstropolis= graph.add_node('Manstropolis')

    graph.add_edge(pandora,arendelle,150)
    graph.add_edge(pandora,metroville,82)
    graph.add_edge(arendelle,pandora,150)
    graph.add_edge(arendelle,metroville,99)
    graph.add_edge(arendelle,manstropolis,42)
    graph.add_edge(metroville,pandora,82)
    graph.add_edge(metroville,arendelle,99)
    graph.add_edge(metroville,manstropolis,105)
    graph.add_edge(metroville,naboo,26)
    graph.add_edge(metroville,narina,37)
    graph.add_edge(narina,metroville,37)
    graph.add_edge(narina,naboo,250)
    graph.add_edge(naboo,narina,250)
    graph.add_edge(naboo,metroville,26)
    graph.add_edge(naboo,manstropolis,73)
    graph.add_edge(manstropolis,naboo,73)
    graph.add_edge(manstropolis,arendelle,42)
    graph.add_edge(manstropolis,metroville,105)

    print(business_trip(graph,[arendelle,manstropolis, naboo]))
