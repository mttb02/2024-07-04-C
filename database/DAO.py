from database.DB_connect import DBConnect
from model.state import State
from model.sighting import Sighting
from model.arco import Arco


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_all_states():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select * 
                    from state s"""
            cursor.execute(query)

            for row in cursor:
                result.append(
                    State(row["id"],
                          row["Name"],
                          row["Capital"],
                          row["Lat"],
                          row["Lng"],
                          row["Area"],
                          row["Population"],
                          row["Neighbors"]))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_sightings():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select * 
                    from sighting s 
                    order by `datetime` asc """
            cursor.execute(query)

            for row in cursor:
                result.append(Sighting(**row))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_years():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT YEAR(`datetime`) as anno
                    FROM new_ufo_sightings.sighting"""
            cursor.execute(query,)

            for row in cursor:
                result.append(row["anno"])
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_shapes_year(anno):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT shape
                        FROM new_ufo_sightings.sighting
                        WHERE YEAR(datetime) = %s
                        ORDER BY shape"""
            cursor.execute(query, (anno,))

            for row in cursor:
                if row["shape"]!="":
                    result.append(row["shape"])
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_nodes(year, shape):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select * 
                        from sighting s
                        where YEAR(datetime) = %s
                        AND shape = %s 
                        order by `datetime` asc """
            cursor.execute(query, (year, shape,))

            for row in cursor:
                result.append(Sighting(**row))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_archi(anno, forma):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select s1.id as id1, s2.id as id2, ABS(s1.longitude - s2.longitude) as peso
                        FROM new_ufo_sightings.sighting as s1, new_ufo_sightings.sighting as s2
                        WHERE YEAR(s1.datetime) = YEAR(s2.datetime)
                        AND YEAR(s1.datetime) = %s
                        AND s1.shape = s2.shape
                        AND s1.shape = %s
                        AND s1.state = s2.state
                        AND s1.longitude < s2.longitude  """
            cursor.execute(query, (anno, forma,))

            for row in cursor:
                result.append(Arco(**row))
            cursor.close()
            cnx.close()
        return result