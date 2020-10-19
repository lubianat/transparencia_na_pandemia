import sqlite3, sys, os, toml, logging, csv, tqdm
from sqlite3 import Error

logging.basicConfig(level=os.environ.get("LOGLEVEL", "ERROR"))
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


def get_business_part_of_company(conn:sqlite3.Connection, cpf_cnpj:str, fields:list=[], limit:int=-1):
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
                WHERE s.cnpj LIKE '{cpf_cnpj}' {limit};"""

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


def verify_match(elections, business_part, buys):
    company_ids_who_donated = []
    for buy in tqdm.tqdm(list(buys), ncols=50):
        company_id = buy['company_id']
        company_id_clean = company_id.strip(".-/")

        tqdm.tqdm.write(company_id)
        business_parners = get_business_part_of_company(business_part, company_id_clean, ["cnpj_cpf_do_socio"])
        for business_parner in business_parners:
            # If a company owns another company
            if len(business_parner) > 11:
                continue

            fields = ['cpf_cnpj_doador', 'setor_economico_doador', 'data', 'tipo_recurso', 'valor', 'descricao']
            donations = query_cpf_cnpj_from_election(elections, business_parner,fields, 1)
            if len(list(donations)) > 0:
                company_ids_who_donated.append(company_id)

    return company_ids_who_donated


def main():
    config_file = sys.argv[1]
    configs = toml.load(config_file)

    business_part_db_file  = configs["databases"]["socios_file"]
    elections_db_file = configs["databases"]["eleicoes_file"]

    business_part_db_conn  = create_sqlite_connection(business_part_db_file)
    election_db_conn = create_sqlite_connection(elections_db_file)


    buys_fd = open(configs['databases']['compras_csv'])
    buys_csv = csv.DictReader(buys_fd, delimiter=',', quotechar='"')

    print(verify_match(election_db_conn, business_part_db_conn, buys_csv))


if __name__ == "__main__":
    main()
