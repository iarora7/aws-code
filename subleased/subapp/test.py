from decimal import Decimal
import math

hospitallist = [{'rating': Decimal('4'), 'st_address': '1338 S Hope St', 'id': 5, 'city': 'Los Angles', 'name': 'Ca Hospital Medical Center', 'zip': '90015', 'state': 'California', 'category_type': 'Hospital', 'location': 'POINT(-118.266208 34.038906)', 'latitude': '34.038906', 'category_id': 3, 'longitute': '-118.266208'}, {'rating': Decimal('4'), 'st_address': '1513 S Grand Ave #400', 'id': 6, 'city': 'Los Angles', 'name': 'Los Angeles Center for Women Health', 'zip': '90015', 'state': 'California', 'category_type': 'Hospital', 'location': 'POINT(-118.266508 34.037519)', 'latitude': '34.037519', 'category_id': 3, 'longitute': '-118.266508'}, {'rating': Decimal('4'), 'st_address': '403 W Adams Blvd', 'id': 7, 'city': 'Los Angles', 'name': 'Orthopaedic Institute for Children', 'zip': '90007', 'state': 'California', 'category_type': 'Hospital', 'location': 'POINT(-118.273375 34.02877)', 'latitude': '34.02877', 'category_id': 3, 'longitute': '-118.273375'}]

houselist = [
    {
      "AptNo": 5, 
      "Available": True, 
      "City": "Los Angeles", 
      "Description": "Nearest to Campus", 
      "Distance": 0.187918524066387, 
      "EndDate": "Thu, 01 Jun 2017 00:00:00 GMT", 
      "Latitude": 34.029367, 
      "Longitude": -118.287419, 
      "PhoneNumber": "4086007283  ", 
      "Point": "POINT(-118.287419 34.029367)", 
      "Price": 2700.0, 
      "Spots": 2, 
      "StartDate": "Sat, 01 Apr 2017 00:00:00 GMT", 
      "State": "California", 
      "StreetAddress": "2827 Orchard Ave                                                                                    ", 
      "Title": "This is Sindhus house", 
      "Zip": 90007, 
      "id": 3, 
      "user_id": 1349781218406667
    }, 
    {
      "AptNo": 6, 
      "Available": True, 
      "City": "Los Angeles", 
      "Description": "Kahani ghar ghar ki", 
      "Distance": 0.0951896103868667, 
      "EndDate": "Thu, 01 Jun 2017 00:00:00 GMT", 
      "Latitude": 34.031053, 
      "Longitude": -118.288293, 
      "PhoneNumber": "4086007283  ", 
      "Point": "POINT(-118.288293 34.031053)", 
      "Price": 2700.0, 
      "Spots": 2, 
      "StartDate": "Sat, 01 Apr 2017 00:00:00 GMT", 
      "State": "California", 
      "StreetAddress": "2656 Ellendale Place                                                                                ", 
      "Title": "This is Patros house", 
      "Zip": 90007, 
      "id": 4, 
      "user_id": 1349781218406667
    }
  ]

first = houselist
second = houselist
combine = first + second
print(len(combine))
combine = list({v['id']:v for v in combine}.values())
print(len(combine))
