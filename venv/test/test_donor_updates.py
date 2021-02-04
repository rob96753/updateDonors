import pytest
import os
import json
import sys

sys.path.insert(1, '../src')
import donorUpdate

donorRecords = [
{
        "first_name": "KAMALA",
        "middle_name": "K",
        "surname": "Kaopua",
        "ssn": "903-20-0128",
        "issn": "903200128",
        "donor_id": "KAOPK1996012101289",
        "blood_type": "O Positive",
        "nationality": "United States of America",
        "home_donation_site": "WAILUKU",
        "ltowb": "N",
        "gender": "F",
        "race": "Pacific Islander",
        "dob": "21 JAN 1996",
        "last_donation": "14 Nov 2020",
        "donor_original_index": 0
    },
    {
        "first_name": "KAMALA",
        "middle_name": "K",
        "surname": "K",
        "ssn": "903-20-0128",
        "issn": "903200128",
        "donor_id": "KXXXK1996012101289",
        "blood_type": "O Positive",
        "nationality": "United States of America",
        "home_donation_site": "WAILUKU",
        "ltowb": "N",
        "gender": "F",
        "race": "Pacific Islander",
        "dob": "21 JAN 1996",
        "last_donation": "14 Nov 2020",
        "donor_original_index": 0
    }

]

def test_GetDonorIdentifier():
    for donorRecord in donorRecords:
        donorIdentifier = donorUpdate.createDonorIdentifier(donorRecord)
        assert donorIdentifier == donorRecord['donor_id'], "Donor ID computed incorrectly"

def test_updateDonorId():
    record = donorRecords[0]
    donorUpdate.updateDonorId(record, 'UPDATED_DONOR_ID')
    assert record['donor_id'] == 'UPDATED_DONOR_ID', 'Donor ID Didn''t Update As Was Expected'

def test_updateDonorOriginalIndex():
    record = donorRecords[0]
    donorUpdate.updateDonorOriginalIndex(record, 5999)
    assert record['donor_original_index'] == 5999, "Donor Original Index Didn't Update As Was Expected"


def test_updateDonorOriginalIndexNaN():
    record = donorRecords[0]
    with pytest.raises(Exception) as error_info:
        donorUpdate.updateDonorOriginalIndex(record, 'AA')

def test_updateHomeDonationSite():
    record = donorRecords[0]
    initialValue = record[donorUpdate.HOME_DONATION_SITE]
    donorUpdate.updateHomeDonationSite(record)
    assert initialValue != record[donorUpdate.HOME_DONATION_SITE], "Home Donation Site Wasn't Updated"

def test_updateDonorISSN():
    record = donorRecords[0]
    donorUpdate.updateISSN(record)
    assert record[donorUpdate.DONOR_ISSN] == record[donorUpdate.DONOR_SSN].replace('-',''), "Donor ISSN Wasn't Updated"
