from database.DAO import DAO as DAO
import networkx as nx

class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        self.id_map = {}

    def get_years(self):
        return DAO.get_years()

    def get_shapes(self, year):
        return DAO.get_shapes_year(year)

    def crea_graph(self, anno, forma):
        self._grafo.clear()
        for s in DAO.get_nodes(anno, forma):
            self._grafo.add_node(s)
            self.id_map[s.id] = s

        temp_archi = DAO.get_archi(anno, forma)
        for a in temp_archi:
            if self._grafo.has_node(self.id_map[a.id1]) & self._grafo.has_node(self.id_map[a.id2]):
                self._grafo.add_edge(self.id_map[a.id1],self.id_map[a.id2], weight=a.peso)

    def get_top_edges(self):
        sorted_edges = self._grafo.edges
        sorted_edges = sorted(sorted_edges(data=True), key=lambda edge: edge[2].get('weight'), reverse=True)
        return sorted_edges[0:5]

    def get_num_of_nodes(self):
        return len(self._grafo.nodes)

    def get_num_of_edges(self):
        return len(self._grafo.edges)
