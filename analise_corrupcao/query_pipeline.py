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
        sys.exit(0)

    return conn



def query_on_database(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


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

    if len(cpf_cnpj) < 14:
        cpf_cnpj = f"***{cpf_cnpj[3:9]}**"


    query = f"""SELECT {fields} FROM socio s
                WHERE s.cnpj LIKE '{cpf_cnpj}'
                  OR  s.cnpj_cpf_do_socio LIKE '{cpf_cnpj}' {limit};"""

    LOGGER.info(f"Running query:\n{query}")


    for row in query_on_database(conn, query):
        yield row


def query_cpf_cnpj_from_election(conn:sqlite3.Connection, cpf_cnpj:str, fields:list=[], limit:int=-1):
    fields = '*' if len(fields)==0 else ",".join(fields)
    limit  = ""  if limit == -1 else f"LIMIT {limit}"

    cpf_cnpj = cpf_cnpj.strip('*')
    query = f"""SELECT {fields} FROM receita r
                WHERE r.cpf_cnpj_doador like '{cpf_cnpj}' {limit}"""


    LOGGER.info(f"Running query:\n{query}")

    for row in query_on_database(conn, query):
        yield row


def main():
    config_file = sys.argv[1]
    configs = toml.load(config_file)

    business_part_db_file  = configs["databases"]["socios_file"]
    elections_db_file = configs["databases"]["eleicoes_file"]

    business_part_db_conn  = create_sqlite_connection(business_part_db_file)
    election_db_conn = create_sqlite_connection(elections_db_file)


    #  cpf = "04160131000197"
    cpf = "58560432272"
    with business_part_db_conn as conn:
        fields = ["cnpj", "nome_socio", "cnpj_cpf_do_socio"]
        for business_part in query_cpf_cnpj_from_socios(conn, cpf, fields,  5):
            print(business_part)


    print('\n\n')

    with election_db_conn as conn:
        fields = ['cpf_cnpj_doador', 'setor_economico_doador', 'data', 'tipo_recurso', 'valor', 'descricao']
        for donation in query_cpf_cnpj_from_election(conn, cpf, fields):
            print(donation)


if __name__ == "__main__":
    main()
