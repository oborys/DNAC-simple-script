import requests
from requests.exceptions import Timeout
import base64

requests.packages.urllib3.disable_warnings()

USER_DNA = "devnetuser"
PASSWORD_DNA = "Cisco123!"
DEF_TIMEOUT = 10

tokenDNA = ''

def main():
    API_Server = "https://sandboxdnac.cisco.com/"
    #  functions
    sandboxAvailability(API_Server)
    checkSimpleRequest(API_Server)
    networkHealth(API_Server)



def sandboxAvailability(API_Server):
    response = requests.get(API_Server, verify=False)
    if response.status_code != 200:
        #send notification to bot
        print("Error", response.status_code)
        exit()
    print("response.status_code (HTTP Status code): ", response.status_code)
    #print("response.content: ", response.content[:50])
    #print("response.text: ", response.text[:50])
    return (response.status_code)

def checkSimpleRequest(API_Server):
    global tokenDNA
    API_Endpoint = API_Server + "api/system/v1/"
    Path = "auth/token"
    API_Resource =  API_Endpoint + Path
    usrPasDna = USER_DNA + ":" + PASSWORD_DNA
    basicDNA = base64.b64encode(usrPasDna.encode()).decode()
    HTTP_Request_header = {"Authorization": "Basic %s" % basicDNA,
                "Content-Type": "application/json;"}
    body_json = ""

    try:
        # API Operation
        response = requests.post(API_Resource, data=body_json, headers=HTTP_Request_header, verify=False, timeout=DEF_TIMEOUT)
    except Timeout as e:
        raise Timeout(e)
    tokenDNA = response.json()['Token']
    urlSimpleDNA = API_Server + "api/v1/network-device/"
    urlSimpleDNAerror = API_Server + "api/v1/network-devic/"
    HTTP_Request_header = {'x-auth-token': tokenDNA}
    try:
        response = requests.get(urlSimpleDNA, headers=HTTP_Request_header, verify=False)
        print ("\n API Operation: GET https://sandboxdnac.cisco.com/api/v1/network-device/ response JSON:\n", response.json())
        print ("\n Extract related information from JSON:\n")
        for item in response.json()['response']:
            print("ID: ", item['id'], " Hostname ", item['hostname'], " Management IP Address ", item['managementIpAddress'], " Serial Number ", item['serialNumber'])
        if response.status_code == 429:
            retry_after = response.getheader("Retry-After")
            time.sleep(retry_after)
            #time.sleep(30)
        if response.status_code != 200:
            print("Error SimpleRequest status_code != 200")
            exit()
    except Timeout as e:
        raise Timeout(e)

def networkHealth(API_Server):
    API_Endpoint = API_Server + 'dna/intent/api/v1/'
    Path = "network-health"
    API_Resource =  API_Endpoint + Path
    usrPasDna = USER_DNA + ":" + PASSWORD_DNA
    basicDNA = base64.b64encode(usrPasDna.encode()).decode()
    HTTP_Request_header = {'x-auth-token': tokenDNA}
    try:
        # API Operation
        response = requests.get(API_Resource, headers=HTTP_Request_header, verify=False, timeout=DEF_TIMEOUT)
        print('\n')
        for networkhealth in response.json()['response']:
            print('Health Score {0}, Total Count: {1}'.format(networkhealth['healthScore'], networkhealth['totalCount']))
        for hd in response.json()["healthDistirubution"]:
            print('Category {0}, Health Score: {1}'.format(hd["category"], hd['healthScore']))
    
    except Timeout as e:
        raise Timeout(e)

if __name__ == "__main__":
    main()
