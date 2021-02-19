#! /usr/bin/python3
import json
import datetime
from algorithms import mod_11_algorithm
import uuid

DONOR_SOURCE = '/Users/rob/PycharmProjects/updateDonors/venv/data/donors-source/db.json'
DONOR_DESTINATION = '/Users/rob/PycharmProjects/updateDonors/venv/data/db.json'
LAST_NAME_BOUND = 4
SSN_LAST = -4 # last four makes the most sense; this has potential for bleeding sensitive data
DIGITS = 12
SUBSTITUTION_CHARACTER = 'X'

DONATION_SITES = ['WAILUKU', 'WAILEA', 'WAIMEA-HAWAII', 'WAIMEA-KAUAI', 'KOHALA', 'PAHOA', 'KONA', 'HONOLULU', 'KAILUA', 'WAIANAE']


DONOR_ID = 'donor_id'
DONOR_ORIGINAL_INDEX = "donor_original_index"
DONOR_SSN = 'ssn'
DONOR_ISSN = 'issn'
HOME_DONATION_SITE = 'home_donation_site'

donorUpdatedOutput = {}
uuids = []
"""
"""
def createDonorIdentifier(donorRecord):
    try:
        date = datetime.datetime.strptime(donorRecord['dob'], '%d %b %Y')
        firstInitial = donorRecord['first_name'][0].upper()
        lastName = donorRecord['surname'].upper() if len(donorRecord['surname']) >= LAST_NAME_BOUND else donorRecord['surname'].ljust(
            LAST_NAME_BOUND, SUBSTITUTION_CHARACTER).upper()
        lastSSNDigits = donorRecord['ssn'][SSN_LAST:].replace('-', '')
        donorIdentifier = f"{lastName[0:LAST_NAME_BOUND]}{firstInitial}{date.strftime('%Y%m%d')}{lastSSNDigits}"

        #return the check digit from the string of digits
        check_digit = mod_11_algorithm(donorIdentifier[-DIGITS:])
        #the check digit is one character by design
        return f'{donorIdentifier}{check_digit}'
    except Exception as ex:
        raise Exception(f'Exception occurred in createDonorIdentifier {ex}')

"""
"""
def updateDonorId(donorRecord, donorId):
    donorRecord[DONOR_ID] = donorId

"""
"""
def updateHomeDonationSite(donorRecord):
    index = int(donorRecord[DONOR_ORIGINAL_INDEX]) % len(DONATION_SITES)
    donorRecord[HOME_DONATION_SITE] = DONATION_SITES[index]

"""
"""
def updateDonorOriginalIndex(donorRecord, index):
    if not (isinstance(index, int) or index.isnumeric()):
        raise Exception(f'Update Donor Original Index NaN: Index Must Be a Number {index}')
    donorRecord[DONOR_ORIGINAL_INDEX] = index
"""
"""
def updateISSN(donorRecord):
    if len(donorRecord[DONOR_SSN]) < 11:
        raise Exception(f'Donor SSN Is Incomplete {donorRecord[DONOR_SSN]}')
    donorRecord[DONOR_ISSN] = donorRecord[DONOR_SSN].replace('-', '')

def getUUID():
    uuid4 = uuid.uuid4()
    while uuid4 in uuids:
        uuid4 = uuid.uuid4()
    uuids.append(uuid4)
    return uuid4


def main():
    with open(DONOR_SOURCE, "r+") as fp:
        parsedData = json.load(fp)
        for index, record in enumerate(parsedData):
            try:
                updateDonorId(record, createDonorIdentifier(record))
                updateDonorOriginalIndex(record, index)
                updateHomeDonationSite(record)
                updateISSN(record)
                uuid4 = getUUID()

                donorUpdatedOutput[str(uuid4)] = record
            except Exception as ex:
                print(f'Exception Occurred in Record {index} {ex}')

        with open(DONOR_DESTINATION, "w+", encoding='UTF-8') as ofp:
            ofp.write(json.dumps(donorUpdatedOutput, indent=4))

if __name__ == '__main__':
    main()
