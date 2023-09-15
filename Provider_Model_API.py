import gc
import json
import os
import pandas as pd
import warnings, logging
import xml.etree.ElementTree as ET
from Provider_XML_DF import *
from df_to_address_distances import *
from Provider_utils import *
from tqdm import tqdm
from Levenshtein import distance
from fuzzywuzzy import fuzz
from XML_to_OCR_output import *
from flask import Flask, jsonify, request, make_response
from tqdm import tqdm
from pathlib import Path


gc.collect()
app = Flask(__name__)
warnings.simplefilter('ignore')


def clean_df(df):
    df = df.loc[df['OfcAddr1'].notna() | df['OfcAddr2'].notna() | df['OfcCity'].notna() | df['OfcState'].notna() | df['OfcZip'].notna() |\
                df['Address1'].notna() | df['Address2'].notna() | df['City'].notna() | df['State'].notna() | df['ZipCode'].notna() ]
    return df


@app.route('/Provider_Matching', methods=['GET', 'POST'])
def Provider_Matching():
    if request.method == 'POST':
        data = request.get_json(force=True)
        file_name = data['file_name']
        # print(file_name)
        prepared_data = provider_xml_to_df(file_name)
        prepared_data = clean_df(prepared_data)
        prepared_data["LastName_"], prepared_data["FirstName_"] = prepared_data["FirstName_"], prepared_data["LastName_"]
        file_name = Path(file_name)
        filename_without_extension = file_name.stem.replace("_BillingProvider", "")
        XML_file_name = file_name.parent/'000000'/(filename_without_extension+".TRANS")
        data = XML_to_OCR_output(str(XML_file_name))
        ProvOrgName, ProvFullName, ProvLName, ProvFName, ProvAddr1, ProvAddr2, ProvCity, ProvState, ProvPostCode = "","", "", "", "","","", "", ""
        ProvOrgName, ProvFullName, ProvLName, ProvFName, ProvAddr1, ProvAddr2, ProvCity, ProvState, ProvPostCode = extract_address_from_df(data)
        # print(ProvOrgName, ProvFullName, ProvLName, ProvFName, ProvAddr1, ProvAddr2, ProvCity, ProvState, ProvPostCode)
        
        if prepared_data.shape[0] > 0:
            Relevant_DF = df_to_address_distances(prepared_data, ProvCity, ProvState, ProvOrgName, ProvAddr1)
        
        if Relevant_DF.shape[0] > 0:
            return json.dumps({"Lookup": True, "Record": str(Relevant_DF.iloc[0]["QueryNumber"]+"_"+Relevant_DF.iloc[0]["id"])})
        else:
            return json.dumps({"Lookup": False})

if __name__ == '__main__':
    app.run(host='localhost',port='5001',debug=True)
