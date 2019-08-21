from bs4 import BeautifulSoup, SoupStrainer
import httplib2


http = httplib2.Http()
status, response = http.request("http://vccs-web-dev-1715195167.eu-west-2.elb.amazonaws.com/vehicle_checkers/enter_details")

for link in BeautifulSoup(response, 'html.parser', parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        print(link['href'])