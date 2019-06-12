import json 
import requests                                    

ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')  
ottawa_wards_response.json()    

{'meta': {'previous': None,
  'next': '/boundaries/?sets=ottawa-wards&offset=20&limit=20',
  'offset': 0,
  'limit': 20,
  'related': {'centroids_url': '/boundaries/centroid?sets=ottawa-wards',
   'simple_shapes_url': '/boundaries/simple_shape?sets=ottawa-wards',
   'shapes_url': '/boundaries/shape?sets=ottawa-wards'},
  'total_count': 23},
 'objects': [{'name': 'Barrhaven',
   'external_id': '3',
   'url': '/boundaries/ottawa-wards/barrhaven/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'West Carleton-March',
   'external_id': '5',
   'url': '/boundaries/ottawa-wards/west-carleton-march/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'Somerset',
   'external_id': '14',
   'url': '/boundaries/ottawa-wards/somerset/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'Rideau-Goulbourn',
   'external_id': '21',
   'url': '/boundaries/ottawa-wards/rideau-goulbourn/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'Cumberland',
   'external_id': '19',
   'url': '/boundaries/ottawa-wards/cumberland/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'Orléans',
   'external_id': '1',
   'url': '/boundaries/ottawa-wards/orleans/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'Innes',
   'external_id': '2',
   'url': '/boundaries/ottawa-wards/innes/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'Rideau-Rockcliffe',
   'external_id': '13',
   'url': '/boundaries/ottawa-wards/rideau-rockcliffe/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'Rideau-Vanier',
   'external_id': '12',
   'url': '/boundaries/ottawa-wards/rideau-vanier/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'Stittsville',
   'external_id': '6',
   'url': '/boundaries/ottawa-wards/stittsville/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'Alta Vista',
   'external_id': '18',
   'url': '/boundaries/ottawa-wards/alta-vista/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'Gloucester-Southgate',
   'external_id': '10',
   'url': '/boundaries/ottawa-wards/gloucester-southgate/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'Kitchissippi',
   'external_id': '15',
   'url': '/boundaries/ottawa-wards/kitchissippi/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'Capital',
   'external_id': '17',
   'url': '/boundaries/ottawa-wards/capital/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'River',
   'external_id': '16',
   'url': '/boundaries/ottawa-wards/river/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'Knoxdale-Merivale',
   'external_id': '9',
   'url': '/boundaries/ottawa-wards/knoxdale-merivale/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'Kanata North',
   'external_id': '4',
   'url': '/boundaries/ottawa-wards/kanata-north/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'Gloucester-South Nepean',
   'external_id': '22',
   'url': '/boundaries/ottawa-wards/gloucester-south-nepean/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'College',
   'external_id': '8',
   'url': '/boundaries/ottawa-wards/college/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}},
  {'name': 'Beacon Hill-Cyrville',
   'external_id': '11',
   'url': '/boundaries/ottawa-wards/beacon-hill-cyrville/',
   'boundary_set_name': 'Ottawa ward',
   'related': {'boundary_set_url': '/boundary-sets/ottawa-wards/'}}]}


for object in ottawa_wards_response.json()["objects"]: 
    print(object["name"])
    Barrhaven
        West Carleton-March
        Somerset
        Rideau-Goulbourn
        Cumberland
        Orléans
        Innes
        Rideau-Rockcliffe
        Rideau-Vanier
        Stittsville
        Alta Vista
        Gloucester-Southgate
        Kitchissippi
        Capital
        River
        Knoxdale-Merivale
        Kanata North
        Gloucester-South Nepean
        College
        Beacon Hill-Cyrville

elections = requests.get(https://represent.opennorth.ca/elections/)
call = elections.json()

call.keys()

objects = call['objects']
objects.__class__
for a in objects:
    print(e['name'])