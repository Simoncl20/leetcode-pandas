import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    
    # Get the shape of the dataframe (rows, columns)
    rows, columns = players.shape
    
    # Return as a list of integers [rows, columns]
    return [rows, columns]