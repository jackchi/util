# /usr/bin/python
# Interview Question from Clever
# Jack Chi (github.com/jackchi)
# Python Request / Json
# REST API Parsing 
# String Formatter

"""
Sample Response
{
  "data": [
    {
      "data": {
        "course_name": "Group Guidance",
        "course_number": "101",
        "created": "2014-02-26T21:15:37.927Z",
        "district": "4fd43cc56d11340000000005",
        "grade": "10",
        "last_modified": "2014-11-14T15:06:55.544Z",
        "name": "Group Guidance - 101 - B. Greene (Section 1)",
        "period": "0",
        "school": "530e595026403103360ff9fd",
        "sis_id": "581",
        "students": [
          "530e5961049e75a9262d0010",
          "530e5961049e75a9262d004e",
          "530e5961049e75a9262d0080",
          "530e5962049e75a9262d0156",
          "530e5963049e75a9262d01b7",
          "530e5963049e75a9262d0253",
          "530e5966049e75a9262d0418",
          "530e5966049e75a9262d0475",
          "530e5966049e75a9262d04b4",
          "530e5967049e75a9262d0503",
          "530e5968049e75a9262d05e9",
          "530e5968049e75a9262d0632",
          "530e5968049e75a9262d0647"
        ],
        "subject": "homeroom/advisory",
        "teacher": "530e5955d50c310f36112c11",
        "teachers": [
          "530e5955d50c310f36112c11"
        ],
        "term": {
          "name": "Y1",
          "start_date": "2012-08-01",
          "end_date": "2013-06-01"
        },
        "id": "530e5979049e75a9262d0af2"
      },
      "uri": "/v1.1/sections/530e5979049e75a9262d0af2"
    }
  ],
  "paging": {
    "current": 1,
    "total": 379,
    "count": 379
  },
  "links": [
    {
      "rel": "self",
      "uri": "/v1.1/sections?limit=1"
    },
    {
      "rel": "next",
      "uri": "/v1.1/sections?limit=1&starting_after=530e5979049e75a9262d0af2"
    }
  ]
}
"""
import requests
import json
r = requests.get('https://api.clever.com/v1.1/sections', headers={'Authorization':'Bearer DEMO_TOKEN'})

print r.status_code

totalNumStudents = sum ([len(section['data']['students']) for section in r.json().get('data')])
print "Total Students: {0}".format(totalNumStudents)
print "Avg Student per Section: %s" % (totalNumStudents / len(r.json().get('data')))



	


