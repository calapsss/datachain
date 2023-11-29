from datachain_backend.sqlchain import SQLChain
from datachain_backend.utils.settings import openai_settings_from_dot_env

sqlchain = SQLChain()  # create an instance of SQLChain
sqlchain.connect()  # call the connect method on the instance

api_key = openai_settings_from_dot_env()
print("Connecting to OpenAI with key: "+ api_key)