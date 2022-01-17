import pandas as pd

def roster_data(league_number):
    #https://towardsdatascience.com/read-data-from-google-sheets-into-pandas-without-the-google-sheets-api-5c468536550
    url = f"https://ottoneu.fangraphs.com/{league_number}/rosterexport"

    rosters = pd.read_csv(url)

    return(rosters)

def player_values(sheet_id, sheet_name):
    # TODO: Figure out league type by league number

    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    values = pd.read_csv(url)

    return(values)