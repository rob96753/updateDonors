import pytest
import os
import json
import sys

sys.path.insert(1, '../src')

from algorithms import mod_11_algorithm


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

LIMIT_SSN_LAST = 4

from donorUpdate import SSN_LAST, createDonorIdentifier

def test_SSNLastNotTooLong():
    assert abs(SSN_LAST) <= LIMIT_SSN_LAST, "Extracting more than {LIMIT_SSN_LAST} digits from SSN Can Lead to Spillage of Sensitive Data"
