
import oracledb as orc
#from ..utils import translate_to_dict


class OracleConnection:
    """
    Oracle connection class to get data from oracle db.
    """

    # def __init__(self, user, password, name, ip, port):
    #     self.user = user
    #     self.password = password
    #     self.name = name
    #     self.ip = ip
    #     self.port = port
    #     self.uri = "oracle+cx_oracle://%s:%s@%s:%s/%s" % (user, password, ip, port, name)

    def __init__(self, dsn):
        self.dsn = dsn

    def initialize_connection(self):
        """
        Initialize connection to oracle db.
        """
        dsn = orc.makedsn(host='10.45.46.40', port='1521', service_name=self.dsn, config_dir='/opt/oracle/instantclient_19_22/network/admin')
        orc.init_oracle_client()
        connection = orc.connect(dsn=dsn)
        return connection


    def get_data(self, query: str):
        """
        Run the query with application_id.
        """
        connection = self.initialize_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        translate_to_dict(cursor, data)
        cursor.close()




