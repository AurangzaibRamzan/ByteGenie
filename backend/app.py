import uvicorn

from config.index import PORT
from scripts.load_data_from_csv import load_data_from_csv
from server import server

if __name__ == "__main__":
    print("Server Started", "success")
    load_data_from_csv()
    uvicorn.run(server, host="localhost", port=int(PORT))
