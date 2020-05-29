from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='geocoder_finder_utsw')

# opens a specified txt file and returns a dictionary of addresses
# INPUT
# file_name: txt file with patient id followed by a space and address
# OUTPUT
# address_dict: dictionary where key is patient id, value is address


def read_file(file_name):
    address_dict = {}
    with open(file_name, 'r') as file:
        line_list = file.read().splitlines()
        for i in range(len(line_list)):
            split_line = line_list[i].split(' ', 1)
            address_dict[split_line[0]] = split_line[1]
    file.close()
    return (address_dict)


# takes a dictionary of addresses and returns a dictionary of respective geocodes
# INPUT
# address_dict: dictionary where key is patient id, value is address
# OUTPUT
# geocode_dict: dictionary where key is patient id, value is geocode of latitude and longitude seperated by a space
def find_geocode(address_dict):
    geocode_dict = {}
    for pat_id, address in address_dict.items():
        location = geolocator.geocode(address)
        geocode_dict[pat_id] = str(
            location.latitude) + ' ' + str(location.longitude)
    return (geocode_dict)

# takes a dictionary of geocodes and writes it into a txt file
# INPUT
# geocode_dict: dictionary where key is patient id, value is geocode of latitude and longitude seperated by a space
# OUTPUT
# geocode_output.txt: txt file with patient id followed by a space and geocode


def write_output(geocode_dict):
    output_file = open('geocode_output.txt', 'w+')
    for pat_id, geocode in geocode_dict.items():
        output_file.write(pat_id + ' ' + geocode + '\n')
    output_file.close()

# print(read_file('address.txt'))
# print(find_geocode(read_file('address.txt')))


def main():
    write_output(find_geocode(read_file('address.txt')))


main()
