from pydantic import BaseModel

class FarePredictionRequest(BaseModel):

    Airline:str

    Source:str

    Destination:str

    Total_Stops:int

    Date_of_Journey:str
    Dep_Time:str
    Arrival_Time:str
    Duration:int
    Route:str
    Additional_Info:str
