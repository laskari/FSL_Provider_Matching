import pandas as pd
from Levenshtein import distance

def df_to_address_distances(provider_data, ProvCity, ProvState, ProvOrgName, ProvAddr1):
    Relevant_DF = pd.DataFrame()
    for i, row in provider_data.iterrows():
        
        is_LName_Match = False
        is_FName_Match = False
        is_TaxID_Match = False
        is_ZipCode_Match = False
        is_City_Match = False
        is_State_Match = False
        is_OrgName_Match = False
        is_Addrs1_Match = False
        is_Addrs2_Match = True

        FName_L_dist = 0
        LName_L_dist = 0
        TaxID_L_dist = 0
        ZipCode_L_dist = 0
        State_L_dist = 0
        Org_Name_L_dist = 0
        City_L_dist = 0
        Addr1_L_dist = 0
        
        substring_addrss = False
        substring_Orgname = False
        
        
        if pd.notna(row["LastName_"]):
            if pd.notna(row["ProviderLastName"]):
                if row["LastName_"] == row["LastName"] and row["LastName_"] == row["ProviderLastName"]:
                    is_LName_Match = True
                else:
                    LName_L_dist = distance(row["LastName_"], row["ProviderLastName"])
                    is_LName_Match = False
            elif pd.notna(row["ProvLastName"]):
                if row["LastName_"] == row["LastName"] and row["LastName_"] == row["ProvLastName"]:
                    is_LName_Match = True
                else:
                    LName_L_dist = distance(row["LastName_"], row["ProvLastName"])
                    is_LName_Match = False
            else:
                is_LName_Match = False
        elif pd.isna(row["LastName_"]) and pd.isna(row["LastName"]) and \
            pd.isna(row["ProvLastName"]) and pd.isna(row["ProviderLastName"]):
            is_LName_Match = True
        else:
            LName_L_dist = distance(row["LastName_"], row["ProvLastName"])
            is_LName_Match = False
        
           
        if pd.notna(row["FirstName_"]):
            if pd.notna(row["ProviderFirstName"]):
                if row["FirstName_"] == row["FirstName"] and row["FirstName_"] == row["ProviderFirstName"]:
                    is_FName_Match = True
                else:
                    FName_L_dist = distance(row["FirstName_"], row["ProviderFirstName"])
                    is_FName_Match = False
            elif pd.notna(row["ProvFirstName"]):
                if row["FirstName_"] == row["FirstName"] and row["FirstName_"] == row["ProvFirstName"]:
                    is_FName_Match = True
                else:
                    FName_L_dist = distance(row["FirstName_"], row["ProvFirstName"])
                    is_FName_Match = False
            else:
                is_FName_Match = False
                FName_L_dist = distance(row["FirstName_"], row["ProvFirstName"])
        elif pd.isna(row["FirstName_"]) and pd.isna(row["FirstName"]) and \
            pd.isna(row["ProvFirstName"]) and pd.isna(row["ProviderFirstName"]):
            is_FName_Match = True
        
        if pd.notna(row["TaxID_"]):
            if row["TaxID_"] == row["TaxID"]:
                is_TaxID_Match = True
            else:
                TaxID_L_dist = distance(row["TaxID_"], row["TaxID"])
                is_TaxID_Match = False
        
        if pd.notna(row["Tin"]):
            if row["Tin_"] == row["Tin"]:
                is_TaxID_Match = True
            else:
                TaxID_L_dist = distance(row["Tin_"], row["Tin"])
                is_TaxID_Match = False
    
        if pd.notna(row["ZipCode_"]):
            if row["ZipCode_"] == row["ZipCode"]:
                is_ZipCode_Match = True
            else:
                ZipCode_L_dist = distance(row["ZipCode_"], row["ZipCode"])
                is_ZipCode_Match = False
        
        if pd.notna(row["OfcZip_"]):
            if row["OfcZip_"] == row["OfcZip"]:
                is_ZipCode_Match = True
            else:
                ZipCode_L_dist = distance(row["OfcZip_"], row["OfcZip"])
                is_ZipCode_Match = False
        
        
        if pd.notna(row["City"]):
            if ProvCity == row["City"]:
                is_City_Match = True
            else:
                City_L_dist = distance(ProvCity, row["City"])
                is_City_Match = False
        elif pd.notna(row["OfcCity"]):
            if ProvCity == row["OfcCity"]:
                is_City_Match = True
            else:
                City_L_dist = distance(ProvCity, row["OfcCity"])
                is_City_Match = False      
        
        
        if pd.notna(row["State"]):
            if ProvState == row["State"]:
                is_State_Match = True
            else:
                State_L_dist = distance(ProvState, row["State"])
                is_State_Match = False
        elif pd.notna(row["OfcState"]):
            if ProvState == row["OfcState"]:
                is_State_Match = True
            else:
                State_L_dist = distance(ProvState, row["OfcState"])
                is_State_Match = False
        
        
        if pd.notna(row["OfcName"]):
            if ProvOrgName == row["OfcName"]:
                is_OrgName_Match = True
                substring_Orgname = True
            else:
                Org_Name_L_dist = distance(ProvOrgName, row["OfcName"])
                if ProvOrgName.find(row["OfcName"]) != -1 or row["OfcName"].find(ProvOrgName) != -1:
                    substring_Orgname = True
                is_OrgName_Match = False
        
        
        if pd.notna(row["Address1"]):
            if ProvAddr1 == row["Address1"]:
                is_Addrs1_Match = True
                substring_addrss = True
            else:
                Addr1_L_dist = distance(ProvAddr1,row["Address1"] )
                if ProvAddr1.find(row["Address1"]) != -1 or row["Address1"].find(ProvAddr1) != -1:
                    substring_addrss = True
                is_Addrs1_Match = False
        elif pd.notna(row["OfcAddr1"]):
            if ProvAddr1 == row["OfcAddr1"]:
                is_Addrs1_Match = True
                substring_addrss = True
            else:
                Addr1_L_dist = distance(ProvAddr1,row["OfcAddr1"] )
                if ProvAddr1.find(row["OfcAddr1"]) != -1 or row["OfcAddr1"].find(ProvAddr1) != -1:
                    substring_addrss = True
                is_Addrs1_Match = False
        else:
            is_Addrs1_Match = True
                    
        row["LName_L_dist"] = LName_L_dist
        row["FName_L_dist"] = FName_L_dist
        row["TaxID_L_dist"] = TaxID_L_dist
        row["ZipCode_L_dist"] = ZipCode_L_dist
        row["State_L_dist"] = State_L_dist
        row["Org_Name_L_dist"] = Org_Name_L_dist
        row["City_L_dist"] = City_L_dist
        row["Addr1_L_dist"] = Addr1_L_dist
        row["substring_addrss"] = substring_addrss
        row["substring_Orgname"] = substring_Orgname

               
#         print(LName_L_dist, FName_L_dist, TaxID_L_dist, ZipCode_L_dist, State_L_dist,  Org_Name_L_dist, City_L_dist,  Addr1_L_dist)
        row["Total_distance"] = LName_L_dist + FName_L_dist + TaxID_L_dist + ZipCode_L_dist + State_L_dist + Org_Name_L_dist + City_L_dist + Addr1_L_dist
#         print(row["Total_distance"])

        print("LAST_NAME:", row["LastName_"], row["LastName"],row["ProviderLastName"],  row["ProvLastName"])
        print("FIRST_NAME:", row["FirstName_"], row["FirstName"], row["ProviderFirstName"], row["ProvFirstName"]) 
        print("TAX_ID:", row["TaxID_"], row["TaxID"], row["Tin_"], row["Tin"])
        print("ZIP_CODE: ",row["ZipCode_"], row["ZipCode"], row["OfcZip_"], row["OfcZip"])
        print("CITY:", ProvCity,":", row["City"],":",row["OfcCity"])
        print("STATE:", ProvState,row["State"], row["OfcState"] )
        print("ORG_NAME:", ProvOrgName, row["OfcName"])
        print("ADDRESS_1",ProvAddr1, row["Address1"], row["OfcAddr1"])    
        print("-"*80)
        print("LName: ", is_LName_Match,"FName: ",is_FName_Match,"Tax_ID:", is_TaxID_Match, "Zip:", is_ZipCode_Match, "City:",is_City_Match, "State:", is_State_Match)
        print("Org_Name:", is_OrgName_Match,"Address1:", is_Addrs1_Match)
        print("substring_Orgname: ", substring_Orgname, "substring_addrss",substring_addrss)
        print(".."*40)
        if is_LName_Match and is_FName_Match and is_TaxID_Match and is_ZipCode_Match and is_City_Match and is_State_Match:
            if is_OrgName_Match and is_Addrs1_Match:
                Relevant_DF = Relevant_DF.append(row)
#                 print("LAST_NAME:", row["LastName_"], row["LastName"],row["ProviderLastName"],  row["ProvLastName"])
#                 print("FIRST_NAME:", row["FirstName_"], row["FirstName"], row["ProviderFirstName"], row["ProvFirstName"]) 
#                 print("TAX_ID:", row["TaxID_"], row["TaxID"], row["Tin_"], row["Tin"])
#                 print("ZIP_CODE: ",row["ZipCode_"], row["ZipCode"], row["OfcZip_"], row["OfcZip"])
#                 print("CITY:", ProvCity,":", row["City"],":",row["OfcCity"])
#                 print("STATE:", ProvState,row["State"], row["OfcState"] )
#                 print("ORG_NAME:", ProvOrgName, row["OfcName"])
#                 print("ADDRESS_1",ProvAddr1, row["Address1"], row["OfcAddr1"])
            elif Org_Name_L_dist < 8  and Addr1_L_dist < 8:
                if substring_addrss or substring_Orgname:
                    Relevant_DF = Relevant_DF.append(row)
#                     print("LAST_NAME:", row["LastName_"], row["LastName"],row["ProviderLastName"],  row["ProvLastName"])
#                     print("FIRST_NAME:", row["FirstName_"], row["FirstName"], row["ProviderFirstName"], row["ProvFirstName"]) 
#                     print("TAX_ID:", row["TaxID_"], row["TaxID"], row["Tin_"], row["Tin"])
#                     print("ZIP_CODE: ",row["ZipCode_"], row["ZipCode"], row["OfcZip_"], row["OfcZip"])
#                     print("CITY:", ProvCity,":", row["City"],":",row["OfcCity"])
#                     print("STATE:", ProvState,row["State"], row["OfcState"] )
#                     print("ORG_NAME:", ProvOrgName, row["OfcName"])
#                     print("ADDRESS_1",ProvAddr1, row["Address1"], row["OfcAddr1"])
    return Relevant_DF