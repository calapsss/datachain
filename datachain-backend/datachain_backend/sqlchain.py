import psycopg2
import openai
import datachain_backend.openai_loader as openai_loader


class SQLChain:
    functions = [
        {
            "type": "function",
            "function": {
                "name": "create_table",
                "description": "Create a Query to create a table based on the csv file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "csv": {
                            "type": "string",
                            "description": "The first three lines of the csv file.",
                        }
                    },
                    "required": ["csv"],
                },
            }
        },
    ]

    def __init__(self):
        # Initialize any necessary variables or connections here
        self.database = "datachain-test"
        self.host = "localhost"
        self.user = "postgres"
        self.password = "password"
        self.port = "5432"
        self.connection = None

    def connect(self):
        # Connect to the database
        try:
            print("Trying to Connect...")
            self.conn = psycopg2.connect(
                database=self.database, 
                user=self.user, 
                password=self.password, 
                host=self.host,
                port=self.port)
            print("Connected to database")
        except psycopg2.Error as e:
            print(f"Unable to connect to the database: {e}")

    def create_table(self, csv):
       
        # Create a query with openai
        prompt = """Based on the first two lines of csv below, write a query to create a table:
        {csv}"""

        messages = [] 
        messages.append({"role": "user", "content": prompt})

        pass


    
    def execute_query(self, query):
        # Execute a query
        pass


    def disconnect(self):
        # Disconnect from the database
        pass

    
    # Add more methods as needed
