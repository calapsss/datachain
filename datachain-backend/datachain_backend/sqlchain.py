import psycopg2
import openai
import dotenv


class SQLChain:
    def __init__(self):
        # Initialize any necessary variables or connections here
        self.database = "datachain-test"
        self.host = "localhost"
        self.user = "postgres"
        self.password = "password"
        self.port = "5432"
        self.connection = None

        # Load the .env file
        dotenv.load_dotenv()
        

        

    def connect(self):
        # Connect to the database
        try:
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
        template = """Based on the first two lines of csv below, write a query to create a table:
        {csv}
        SQL Query:"""

        pass


    
    def execute_query(self, query):
        # Execute a query
        pass


    def disconnect(self):
        # Disconnect from the database
        pass

    
    # Add more methods as needed
