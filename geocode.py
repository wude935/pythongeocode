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
            if line_list[i] != '':
                split_line = line_list[i].split(' ', 1)
                # print(split_line)
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
        try:
            location = geolocator.geocode(address)
            # print(location)
            geocode_dict[pat_id] = str(
                location.latitude) + ' ' + str(location.longitude)
        except AttributeError as error:
            print(error)
            print('Unable to find Geocode for the address ' + address +
                  '. Make sure that the address is valid (check spacing or abbreviations) or try a different Geocode API.')
        except Exception as error:
            print(error)
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


# takes a input file and creates an output file:
# INPUT
# file_name: txt file with patient id followed by a space and address
# OUTPUT
# geocode_output.txt: txt file with patient id followed by a space and geocode
def main_function(file_name):
    write_output(find_geocode(read_file(file_name)))


def main():
    main_function('example_input.txt')


main()
