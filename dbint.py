
def get_database():
    from pymongo import MongoClient
    

    
    CONNECTION_STRING = "mongodb+srv://auth:RG5nr9eC8bVimJpP@arbxbet.35ttpip.mongodb.net/?retryWrites=true&w=majority"

    
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)
    return client['test']

    
