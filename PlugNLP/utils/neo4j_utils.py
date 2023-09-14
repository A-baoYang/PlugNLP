import logging
import os
from tqdm import tqdm
from py2neo import Graph
from py2neo.bulk import merge_nodes, merge_relationships

logger = logging.getLogger(__name__)


class NEO4JConnector:
    def __init__(self, hostname: str, database_name: str):
        """從環境變數取得 Neo4j 身份認證帳密"""
        self.HOSTNAME = hostname
        self.USERNAME = os.environ.get("NEO4J_USERNAME", None)
        self.PASSWORD = os.environ.get("NEO4J_PASSWORD", None)
        self.DATABASE = database_name
        if [i for i in [self.HOSTNAME, self.USERNAME, self.PASSWORD] if i is None]:
            raise Exception(
                "Neo4j authentication haven't set in environment variables yet."
            )
        else:
            logger.info("Get authentication from environment variables successfully.")
        if not self.DATABASE:
            raise Exception("Neo4j target database not set yet.")
        else:
            logger.info(f"Target Neo4j database: {self.DATABASE}")

    def connect(self):
        """向 Neo4j 建立連線"""
        self.conn = Graph(
            host=self.HOSTNAME, auth=(self.USERNAME, self.PASSWORD), name=self.DATABASE
        )
        logger.info(f"Connected to Neo4j database on {self.HOSTNAME}/{self.DATABASE}.")
        return self.conn

    def run_cypher(self, query: str):
        logger.info(f"Run cypher: {query}")
        graph = self.connect()
        cursor = self.conn.run(query)
        return cursor.data()

    def update_nodes(self, name_correction_dict: dict, no_tqdm: bool = False):
        for k, v in tqdm(name_correction_dict.items(), no_tqdm=no_tqdm):
            if v:
                query = 'MATCH (n {name: "%s"}) SET n.name = "%s"' % (k, v)
            else:
                query = 'MATCH (n {name: "%s"}) DETACH DELETE n'

            self.run_cypher(query)

    def __del__(self):
        logger.info("Neo4j connection closed.")
