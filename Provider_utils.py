import pandas as pd
from Levenshtein import distance


def create_Addr_seq2(row):
    row = row.astype('str')
    sep ="[SEP]"
    sep =" "
    return (row['OfcAddr1'] + sep + \
        row['OfcAddr2'] + sep + \
        row['OfcCity'] + sep + \
        row['OfcState'] + sep + \
        row['OfcZip'] + sep + \
        row['Address1'] + sep + \
        row['Address2'] + sep + \
        row['City'] + sep + \
        row['State'] + sep + \
        row['ZipCode'])


def extract_address_from_df(df):
    ProvOrgName =  None
    ProvFullName =  None
    ProvLName =  None
    ProvFName =  None
    ProvAddr1 =  None
    ProvAddr2 =  None
    ProvCity =  None
    ProvState =  None
    ProvPostCode =  None

    for index, row in df.iterrows():
        # ground_truth_value = row['Ground_truth']
        ground_truth_value = row['OCR_OMNI']
        if pd.notna(ground_truth_value) and ground_truth_value is not None:
            if index == 0:
                ProvOrgName = ground_truth_value
            elif index == 1:
                ProvFullName = ground_truth_value
            elif index == 2:
                ProvLName = ground_truth_value
            elif index == 3:
                ProvFName = ground_truth_value
            elif index == 4:
                ProvAddr1 = ground_truth_value
            elif index == 5:
                ProvAddr2 = ground_truth_value
            elif index == 6:
                ProvCity = ground_truth_value
            elif index == 7:
                ProvState = ground_truth_value
            elif index == 8:
                ProvPostCode = ground_truth_value
        else:
            if index == 0:
                ProvOrgName = 'Missing'
            elif index == 1:
                ProvFullName = 'Missing'
            elif index == 2:
                ProvLName = 'Missing'
            elif index == 3:
                ProvFName = 'Missing'
            elif index == 4:
                ProvAddr1 = 'Missing'
            elif index == 5:
                ProvAddr2 = 'Missing'
            elif index == 6:
                ProvCity = 'Missing'
            elif index == 7:
                ProvState = 'Missing'
            elif index == 8:
                ProvPostCode = 'Missing'
    return ProvOrgName, ProvFullName, ProvLName, ProvFName, ProvAddr1, ProvAddr2, ProvCity, ProvState, ProvPostCode
