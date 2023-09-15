import pandas as pd
import xml.etree.ElementTree as ET
import os
import gc
from tqdm.auto import tqdm

df = pd.DataFrame()
group_names = ["Page1", "Blocks05"]#, "Blocks05"

field_types = ["DEN_BillProvAddr1","DEN_BillProvAddr2", "DEN_BillProvCity", "DEN_BillProvPostCode", "DEN_BillProvState", \
               "DEN_BillProvOrgName", "DEN_BillProvFullName", "DEN_BillProvLName", "DEN_BillProvFName" ] 


def XML_to_OCR_output(file):
    df = pd.DataFrame()
    row = 0
    counter = 0
    data_g = ''
    l = []
    l2 = []
    if ".TRANS" in file:
        tree = ET.parse(file)
        root = tree.getroot()
        groupNames = root.findall("./FldColls/FldSet")
        w_h = root.find("./Imgs/Img")
        for gn in groupNames:
            if gn.attrib["Nm"] in group_names:
                fields = gn.findall("./Fld")
                for field in fields:
                    if field.attrib["Typ"] == "GROUP":
                        field_t = field.findall("./Ln/Clm")
                        for f in field_t:
                            if f.attrib["Nm"] in field_types:
                                l.append(f.attrib["Nm"])
                                work_g = f.findall("./Ln/Work")
                                history_g = f.findall("./Ln/Hstry")
                                if len(work_g) == 0:
                                    work_g = f.findall("./Work")
                                    history_g = f.findall("./Hstry")
                                    
                                for k in range(len(work_g)):
                                    data_g = work_g[k].findall("./Data")
                                
                                for dataa_g in data_g:
                                    df.loc[row, "Ground_truth"] = dataa_g.text
                                
                                for k in range(len(history_g)):
                                    data_h = history_g[k].findall("./Data")
                                    cords = work_g[k].find("./Crds")
                                    df.loc[row, "File_Name"] = file
                                    df.loc[row, "Group_name"] = gn.attrib["Nm"]
                                    df.loc[row, "Image_width"] = w_h.attrib["w"]
                                    df.loc[row, "Image_height"] = w_h.attrib["h"]
                                    df.loc[row, "Field_Name"] = f.attrib["Nm"]
                                    df.loc[row, "x1"] = cords.attrib["x1"]
                                    df.loc[row, "x2"] = cords.attrib["x2"]
                                    df.loc[row, "y1"] = cords.attrib["y1"]
                                    df.loc[row, "y2"] = cords.attrib["y2"]
                                    for dataa_h in data_h:
                                        if dataa_h.attrib["Src"] == "OCR_OM":
                                            df.loc[row, "OCR_OMNI"] = dataa_h.text

                                        if dataa_h.attrib["Src"] == "OCROptimizer":
                                            df.loc[row, "OCR_Optimizer"] = dataa_h.text
                                            df.loc[row, "Ground_truth"] = dataa_h.text
                                      
                                row += 1
                    elif field.attrib["Typ"] == "SINGLE":
                        field_name = field.find("./Nm").text
                        if field_name in field_types:
                            l2.append(field_name)
                            work = field.findall("./Ln/Work")
                            history = field.findall("./Ln/Hstry")
                            if len(work) == 0:
                                work = field.findall("./Ln/Clm/Work")
                                history = field.findall("./Ln/Clm/Hstry")
                            for k in range(len(work)):
                                data = work[k].findall("./Data")
                            
                            for dataa in data:
                                df.loc[row, "Ground_truth"] = dataa.text 
                                
                                
                            for k in range(len(history)):
                                data = history[k].findall("./Data")
                                cords = work[k].find("./Crds")
                                df.loc[row, "File_Name"] = file
                                df.loc[row, "Group_name"] = gn.attrib["Nm"]
                                df.loc[row, "Image_width"] = w_h.attrib["w"]
                                df.loc[row, "Image_height"] = w_h.attrib["h"]
                                df.loc[row, "Field_Name"] = field_name
                                df.loc[row, "x1"] = cords.attrib["x1"]
                                df.loc[row, "x2"] = cords.attrib["x2"]
                                df.loc[row, "y1"] = cords.attrib["y1"]
                                df.loc[row, "y2"] = cords.attrib["y2"]
                                for dataa in data:
                                    if dataa.attrib["Src"] == "OCR_OM":
                                        df.loc[row, "OCR_OMNI"] = dataa.text

                                    if dataa.attrib["Src"] == "OCROptimizer":
                                        df.loc[row, "OCR_Optimizer"] = dataa.text
                                        df.loc[row, "Ground_truth"] = dataa.text
                            row += 1
            counter += 1
    return df