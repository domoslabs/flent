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


    fields = [
            ["BATCH_TITLE"],
            ["SERIES_META", "TCP download sum","MEAN_VALUE"],
            ["SERIES_META", "VoIP","PACKET_LOSS_RATE"],
            ["SERIES_META", "VoIP","RTT_MEAN"],
            ["SERIES_META", "VoIP","RTT_PERCENTILE90"],
            ["SERIES_META", "VoIP","RTT_PERCENTILE99"],
            ["SERIES_META", "Ping (ms) UDP BE","RTT_MEAN"],
            ["SERIES_META", "Ping (ms) UDP BE","RTT_PERCENTILE90"],
            ["SERIES_META", "Ping (ms) UDP BE","RTT_PERCENTILE99"],
            ["SERIES_META", "Ping (ms) UDP BK","RTT_MEAN"],
            ["SERIES_META", "Ping (ms) UDP BK","RTT_PERCENTILE90"],
            ["SERIES_META", "Ping (ms) UDP BK","RTT_PERCENTILE99"],
            ["SERIES_META", "Ping (ms) UDP BK","RTT_MEAN"],
            ["SERIES_META", "Ping (ms) UDP VI","RTT_PERCENTILE90"],
            ["SERIES_META", "Ping (ms) UDP VI","RTT_PERCENTILE99"],
            ["SERIES_META", "Ping (ms) UDP VI","RTT_MEAN"],
            ["SERIES_META", "Ping (ms) UDP VO","RTT_PERCENTILE90"],
            ["SERIES_META", "Ping (ms) UDP VO","RTT_PERCENTILE99"]]
    # print csv header
    header = ""
    for field in fields:
        header = header + get_name(field)+","
    header = header[:-1]
    print(header)
    for subdir, dirs, files in os.walk(inputfile):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".gz"):
                with gzip.open(filepath, "rb") as f:
                    data = f.read()
                    #print(data)
                    flent_data = json.loads(data)
                    metadata = flent_data["metadata"]
                    csv_line = ""
                    for field in fields:
                        csv_line = csv_line + str(get_value(field,metadata)) + ","
                    csv_line = csv_line[:-1]
                    print(csv_line)

def get_name(field):
    o = ""
    for subfield in field:
        if subfield != "SERIES_META":
            o = o + subfield + " "
    return o

def get_value(field, metadata):
    o = metadata
    for subfield in field:
        o = o[subfield]
    return o

if __name__ == "__main__":
    main(sys.argv[1:])