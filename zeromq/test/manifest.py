
# TODO handle contents of excel files
# TODO handle contents of files that are neither excel or csv format

import os
import os.path
from datetime import datetime
import time
from stat import *
import pathlib
import json

def generateFileManifest(filename, manifest_filename=None):

    string = ""
    data = {}
    if os.path.isfile(filename):
        f = pathlib.Path(filename)  

        #* Extract contents of file into variable
        # csv file 
        if (os.path.splitext(filename)[1]).replace(".","") == "csv": 
            with open(filename) as open_file: 
                contents = open_file.readlines()
        # excel file
        elif (os.path.splitext(filename)[1]).replace(".","") == "xlsx": 
            contents = "TODO: CONTENTS OF EXCEL FILE"
        else: 
            contents = "TODO: CONTENTS OF NEITHER CSV OR EXCEL FILE"

        #* Construct message
        data[os.path.basename(filename)] = {
                    'purpose': ["data"], 
                    'type': [(os.path.splitext(filename)[1]).replace(".","")],
                    'ctime': [str(f.stat().st_ctime), str(datetime.fromtimestamp(f.stat().st_ctime))],
                    'mtime':[str(f.stat().st_mtime), str(datetime.fromtimestamp(f.stat().st_mtime))], 
                    'data': contents
                    }
        json_data = json.dumps(data)

        #* if specified, write contents of manifest to file
        if manifest_filename != None:
            with open(manifest_filename, "w+") as manifest_file:
                manifest_file.write(json_data)

    else:
        print ("skipping bad filename: {}".format(filename))

    return data