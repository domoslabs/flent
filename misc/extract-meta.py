#!/usr/bin/python
import os
import sys, getopt
import gzip
import json

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    for subdir, dirs, files in os.walk(inputfile):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".gz"):
                with gzip.open(filepath, "rb") as f:
                    data = f.read()
                    #print(data)
                    flent_data = json.loads(data)
                    smeta = flent_data["metadata"]["SERIES_META"]
                    print(os.path.basename(f.name) ,end =",")
                    print(smeta["Ping (ms) avg"]["MEAN_VALUE"] , end =",")
                    print(smeta["TCP download sum"]["MEAN_VALUE"],end =",")
                    #print(smeta["TCP upload sum"]["MEAN_VALUE"],end =",")
                    print(smeta["VoIP"]["PACKET_LOSS_RATE"],end =",")
                    print(smeta["VoIP"]["OWD_DOWN_MEAN"],end =",")
                    print(smeta["VoIP"]["OWD_UP_MEAN"],end =",")
                    print(smeta["VoIP"]["RTT_MEAN"])
    
if __name__ == "__main__":
    main(sys.argv[1:])