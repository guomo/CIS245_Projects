import urllib.request
import json
from pathlib import Path

def parseRouterLog(filename):
    
    # open the file and read the lines into a list
    file_obj = open(Path(filename))
    lines =  file_obj.readlines()

    # dictoninary to hold the counts
    addressDict = {}
    # iterate over each line
    for line in lines :
        words = line.split() # separate on space to get each word
        if(len(words) > 3 and words[0].startswith('0')):
            # remember third column is the source ip address; for readabilty assign to var
            ip_addr = words[2] 
            # The log file truncates the ipv6 addresses so filter those out
            if ip_addr.find(':') != -1:
                continue
            count = addressDict.get(ip_addr)
            if not count:
                addressDict[ip_addr] = 1
            else:
                addressDict[ip_addr] = count+1
    return addressDict

def getGeoLocation(ip_addr):
    """   Call a web service that returns the geolocation of an ip address as json like so
        {   "status":"success",
            "data":{    "ipv4":"45.129.33.84",
                        "continent_name":"Africa",
                        "country_name":"South Africa",
                        "subdivision_1_name":"Gauteng",
                        "subdivision_2_name":null,
                        "city_name":"Johannesburg",
                        "latitude":"-26.23090","longitude":"28.05830"
                    }
        }
    """
    try:
        with urllib.request.urlopen(f'https://ipvigilante.com/{ip_addr}') as response:
            # fetch the response
            raw_resp = response.read()
    except:
        print(f"error requesting location for ip {ip_addr}")
    else:
        # parse the json into a Python dictionary; convert the binary data returned to a string
        geo_loc = json.loads(raw_resp.decode("utf-8"))
        return f"{geo_loc['data']['city_name']}, {geo_loc['data']['subdivision_1_name']}, {geo_loc['data']['country_name']}"


        


addrs = parseRouterLog('/Users/gman/Desktop/logs.txt')
for ip in addrs:
    print(f"{addrs[ip]} request(s) {ip} from {getGeoLocation(ip)}")
