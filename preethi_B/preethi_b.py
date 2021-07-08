#purpose of the script
###################################################################################################################
#This script has been designed to read from a text file that byte count and
#Write to output count on greater than 5000 records and sum of records which is greater than 5000.

###################################################################################################################
#Below points has been considered in the list
###################################################################################################################

#1. Read fro input files row wise and output writing based on condition

#2. A log file has been created with the current date time stamp along with the message specified .

#3. Script has  been written to exit out errorneous condition.
import logging
import sys
logging.basicConfig(filename='preethi.log',format='%(asctime)s %(message)s',filemode='w',level=logging.INFO)
#Declaring a empty list and opening a file and opening the file in read console.
with open('in.txt','r') as inp_file:
    lst=[]
    for lines in inp_file.readlines():
        words=lines.split()
        lst.append(words[-1])
lst=list(int(byte)for byte in lst)
#################################################################################################################
lst1=[]
try:
    #Max length of lst to count the byte records
    if len(lst)<2*pow(10,5):
        sum=0
        #Loop to check the records which are greater than 5000
        for i in lst:
            if i>5000:
                lst1.append(i)
                sum+=i
        print(lst1,sum)
        #To print the byte count in output file
        byte_count='Records of byte count which is greater than 5000:{}'.format(len(lst1))
        #To print the sum of byte counts greater than 5000 in output file
        total_sum='Total sum of Records of byte countwhich is greater than 5000 is: {}'.format(sum)

    try:
        #Max length of lst to print sum of total bytes which are greater than 5000
        if sum <pow(10,12):
            with open('ot.txt','w') as ot_file:
                ot_file.write(byte_count + '\n' + total_sum)
                logging.info(byte_count)
                logging.info(total_sum)

    except:
        with open('ot.txt','w') as ot_file:
            ot_file.write("byte counts are greater")
            logging.info("Byte count does not match to the given condition")
            sys.exit()

except:
    with open('ot.txt','w') as ot_file:
            ot_file.write("records doesn't match to the given condition")
            logging.info("Too many line sin the file")
            sys.exit()

