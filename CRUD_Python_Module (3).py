from pymongo import MongoClient

class AnimalShelter(object):
    """
    CRUD operations for Animal collection in MongoDB.
    This class connects to the AAC database and provides
    methods to create, read, update, and delete documents.
    """

    def __init__(self):
        """
        Initialize the MongoDB connection using authentication.
        """
        # Connection Variables
        USER = 'aacuser'
        PASS = 'Password123!'   # <-- my password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        try:
            # Create MongoDB client connection
            self.client = MongoClient(
                'mongodb://%s:%s@%s:%d/?authSource=admin' % (USER, PASS, HOST, PORT)
            )
            
            # Access database and collection
            self.database = self.client[DB]
            self.collection = self.database[COL]

        except Exception as e:
            print(f"Connection error: {e}")

    # CREATE (C in CRUD)
    def create(self, data):
        """
        Insert a document into the collection.

        :param data: dictionary containing document data
        :return: True if insert is successful, otherwise False
        """
        try:
            if data is not None:
                # Insert document into collection
                result = self.collection.insert_one(data)
                
                # Return True if insert succeeded
                return True if result.inserted_id else False
            else:
                return False

        except Exception as e:
            print(f"Create error: {e}")
            return False

    # READ (R in CRUD)
    def read(self, query):
        """
        Retrieve documents from the collection.

        :param query: dictionary specifying search criteria
        :return: list of matching documents, or empty list
        """
        try:
            if query is not None:
                # Execute query and convert cursor to list
                cursor = self.collection.find(query)
                return list(cursor)
            else:
                return []

        except Exception as e:
            print(f"Read error: {e}")
            return []

    # UPDATE (U in CRUD)
    def update(self, query, new_values):
        """
        Update existing documents in the collection.

        :param query: dictionary specifying documents to update
        :param new_values: dictionary of fields to update
        :return: number of documents modified
        """
        try:
            if query is not None and new_values is not None:
                # Update matching documents using $set
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            else:
                return 0

        except Exception as e:
            print(f"Update error: {e}")
            return 0

    # DELETE (D in CRUD)
    def delete(self, query):
        """
        Delete documents from the collection.

        :param query: dictionary specifying documents to delete
        :return: number of documents deleted
        """
        try:
            if query is not None:
                # Delete matching documents
                result = self.collection.delete_many(query)
                return result.deleted_count
            else:
                return 0

        except Exception as e:
            print(f"Delete error: {e}")
            return 0