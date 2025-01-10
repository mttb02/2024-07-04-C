from database.DAO import DAO as DAO
import networkx as nx

class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        self.id_map = {}

    def crea_graph(self, anno, forma):
        self._grafo.clear()
        for s in self.temp_sightings:
            if s.datetime.year == anno and s.shape == forma:
                self._grafo.add_node(s)
                self.id_map[s.id] = s

        temp_archi = DAO.get_archi(anno, forma)
        for a in temp_archi:
            if self._grafo.has_node(self.id_map[a.id1]) & self._grafo.has_node(self.id_map[a.id2]):
                self._grafo.add_edge(self.id_map[a.id1],self.id_map[a.id2], weight=a.peso)

    def get_cinque_preso_maggiore(self):
        sorted_edges = self._grafo.edges
        sorted_edges = sorted(sorted_edges(data=True), key=lambda edge: edge[2].get('weight'), reverse=True)
        return sorted_edges

    def get_num_of_nodes(self):
        return len(self._grafo.nodes)

    def get_num_of_edges(self):
        return len(self._grafo.edges)

    def get_years(self):
        self.temp_sightings = DAO.get_all_sightings()
        temp_anni = []
        for s in self.temp_sightings:
            if s.datetime.year not in temp_anni:
                temp_anni.append(s.datetime.year)
        temp_anni.sort()
        return temp_anni

    def get_shapes(self, year):
        temp_shapes = []
        for s in self.temp_sightings:
            temp_year = s.datetime.year
            if temp_year == year:
                if s.shape not in temp_shapes and s.shape != "":
                    temp_shapes.append(s.shape)
        temp_shapes.sort()
        return temp_shapes
