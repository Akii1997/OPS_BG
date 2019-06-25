import pygsheets

gc = pygsheets.authorize(client_secret='pyg_authentication_file.json')


def push_df(df, id1, sheet1):
    sheet = gc.open_by_key(id1)
    worksheet = sheet.worksheet_by_title(sheet1)
    worksheet.clear()
    worksheet.set_dataframe(df, start='A1')


def get_df(id1, sheet1):
    sheet = gc.open_by_key(id1)
    worksheet = sheet.worksheet_by_title(sheet1)
    wrk = worksheet.get_all_values()
    return wrk
