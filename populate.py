# -*- coding: utf-8 -*-
import requests, csv, os

output_file = os.getcwd() + 'output.csv'

def get_legislators():
    api_key = 'e863c0d4cf794dc4a33419c6c79ee84c'
    url = 'http://openstates.org/api/v1//legislators/?active=true&apikey=' + api_key

    response = requests.get(url)
    response = response.json()

    return response

def transform_data(data):
    output = []
    for i, leg in enumerate(data):
        new_row = [i,
                   leg['last_name'],
                   leg['updated_at'],
                   leg['full_name'],
                   leg['id'],
                   leg['first_name'],
                   leg['middle_name'],
                   leg['district'] if 'district' in leg.keys() else '',
                   leg['office_address'] if 'office_address' in leg.keys() else '',
                   leg['state'].upper(),
                   leg['votesmart_id'] if 'votesmart_id' in leg.keys() else '',
                   'LC' if 'chamber' in leg.keys() and leg['chamber'] == 'lower' else 'UC' if 'chamber' in leg.keys() and leg['chamber'] == 'upper' else '',
                   leg['party'] if 'party' in leg.keys() else '',
                   leg['offices'][0]['email'] if len(leg['offices']) > 0 and 'email' in leg['offices'][0].keys()else '',
                   '',
                   leg['leg_id'],
                   1,
                   leg['transparencyleg_id'] if 'transparencyleg_id' in leg.keys() else '',
                   leg['photo_url'] if 'photo_url' in leg.keys() else '',
                   leg['offices'][0]['fax'] if len(leg['offices']) > 0 and 'fax' in leg['offices'][0].keys() else '',
                   leg['offices'][0]['phone'] if len(leg['offices']) > 0 and 'phone' in leg['offices'][0].keys() else '',
                   leg['url'] if 'url' in leg.keys() else '',
                   leg['country'] if 'country' in leg.keys() else '',
                   leg['created_at'],
                   leg['level'] if 'level' in leg.keys() else '',
                   leg['office_phone'] if 'office_phone' in leg.keys() else '',
                   leg['suffixes']
                   ]
        output.append(new_row)
    
    return output

def write_to_csv(data):
    with open(output_file, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',quotechar='"')
        for row in data:
            writer.writerow([item.encode('utf-8') if isinstance(item, basestring) else item for item in row])

    return True

def client():
    data = get_legislators()
    write_to_csv(transform_data(data))
    return True

if __name__ == '__main__':
    client()