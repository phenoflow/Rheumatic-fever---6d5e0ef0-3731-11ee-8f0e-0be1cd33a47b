# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"14A1.00","system":"readv2"},{"code":"100051.0","system":"med"},{"code":"101539.0","system":"med"},{"code":"105615.0","system":"med"},{"code":"14840.0","system":"med"},{"code":"20246.0","system":"med"},{"code":"23619.0","system":"med"},{"code":"24636.0","system":"med"},{"code":"34916.0","system":"med"},{"code":"36886.0","system":"med"},{"code":"44756.0","system":"med"},{"code":"48099.0","system":"med"},{"code":"48189.0","system":"med"},{"code":"5326.0","system":"med"},{"code":"59942.0","system":"med"},{"code":"63252.0","system":"med"},{"code":"64799.0","system":"med"},{"code":"68849.0","system":"med"},{"code":"69995.0","system":"med"},{"code":"72936.0","system":"med"},{"code":"73540.0","system":"med"},{"code":"764.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('rheumatic-fever-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["fever---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["fever---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["fever---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
