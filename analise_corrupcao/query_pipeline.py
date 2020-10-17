import sqlite3, sys, os, toml, logging
from sqlite3 import Error

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
LOGGER = logging.getLogger(__name__)


def create_sqlite_connection(db_file:str):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        LOGGER.info(f"Database {db_file} connected successfully")
    except Exception as e:
        LOGGER.error(f"Error while trying to connect to database {db_file}.\n{e}")

    return conn


def query_cpf_cnpj_from_socios(conn:sqlite3.Connection, cpf_cnpj:str, fields:list=[], limit:int=-1):
    """ Create a generator that iterates through all business partners with a
        cpf/cnpj value from `conn` database.
    :conn:     Connection object from sqlite3
    :cpf_cnpj: String containing a cpf or cnpj to search for
    :fields:   Optional list of fiels in `socio` table to return. If empty,
               returns all fields from table
    :limit:    Integer indicating a limit of rows to query. Default to -1, returns
               all rows.

    :return:   Generator object returning all rows from query result.
    """

    fields = '*' if len(fields)==0 else ",".join(fields)
    limit  = ""  if limit == -1 else f"LIMIT {limit}"

    query = f"""SELECT {fields} FROM socio s
                WHERE s.cnpj_cpf_do_socio LIKE '{cpf_cnpj}' {limit};"""

    LOGGER.info(f"Running query:\n{query}")

    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        yield row


def main():
    config_file = sys.argv[1]
    configs = toml.load(config_file)

    socios_db_file = configs["databases"]["socios_file"]

    socios_db_conn = create_sqlite_connection(socios_db_file)

    with socios_db_conn as conn:
        for socio in query_cpf_cnpj_from_socios(conn, "***019378**", ["cnpj", "nome_socio", "cnpj_cpf_do_socio"], 5):
            print(socio)


if __name__ == "__main__":
    main()
