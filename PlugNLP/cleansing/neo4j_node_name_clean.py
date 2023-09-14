from PlugNLP.PlugNLP.cleansing.base import TextCleanser
from PlugNLP.PlugNLP.utils.neo4j_utils import NEO4JConnector


class Neo4jTextCleanser(TextCleanser):
    def __init__(self, api_token: str = None, credential_file: str = None) -> None:
        super().__init__(api_token, credential_file)

    def neo4j_update(self, hostname: str, database_name: str):

        names_to_update = {
            k: v for k, v in self.default_dictionary.items() if k in self.inputs
        }

        n4j = NEO4JConnector(hostname=hostname, database_name=database_name)
        n4j.update_nodes(name_correction_dict=names_to_update)
