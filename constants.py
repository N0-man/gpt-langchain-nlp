ASTRA_DB_SECURE_BUNDLE_PATH="<<secure bundle path>>"
ASTRA_DB_TOKEN_JSON_PATH="<<your token json path>>"
ASTRA_DB_KEYSPACE="<<your keyspace name>>"
OPENAI_API_KEY="<<your openai api key>>"

# These are used to authenticate with Astra DB
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Vector support using Langchain, Apache Cassandra (Astra DB is built using
# Cassandra), and OpenAI (to generate embeddings)
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores.cassandra import Cassandra

import json

cloud_config = {
    'secure_connect_bundle': ASTRA_DB_SECURE_BUNDLE_PATH
}

with open(ASTRA_DB_TOKEN_JSON_PATH) as f:
    secrets = json.load(f)
ASTRA_DB_APPLICATION_TOKEN = secrets["token"] # token is pulled from your token json file
# DataStax Astra DB is a cloud-native, scalable Database-as-a-Service built on Apache Cassandra
auth_provider=PlainTextAuthProvider("token", ASTRA_DB_APPLICATION_TOKEN)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
astra_session = cluster.connect()

llm = OpenAI(openai_api_key=OPENAI_API_KEY)
chat_model = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
myEmbedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

myCassandraVStore = Cassandra(
    embedding=myEmbedding,
    session=astra_session,
    keyspace=ASTRA_DB_KEYSPACE,
    table_name="phrases_search"
)