import os
import http.client
import urllib.parse
import re


def result(r):
    pattern = "<div class=\"tool-results\">(.*?)<div class=\"bodypagenav\">  "
    pattern2 = "<div class=\"tool-results\">"
    pattern3 = "<div >"
    pattern4 = "</div>"
    pattern5 = "<span class=\"label\">"
    pattern6 = "<span class=\"value\">"
    pattern7 = "</span>"
    pattern8 = ":&nbsp;"
    pattern9 = "<div class=\"bodypagenav\"> "
    pattern10 = "\t"
    pattern11 = "<br/>"
    pattern12 = '<pre>'
    pattern13 = "</pre>"

    tmp = ""

    for valid in re.finditer("<strong>Sorry, there was a problem.</strong>", r, re.S):
        print("Sorry, there was a problem")

    for filter in re.finditer(pattern, r, re.S):
        tmp += filter.group()

    tmp2 = tmp.replace(pattern2, "")
    tmp3 = tmp2.replace(pattern3, "")
    tmp4 = tmp3.replace(pattern4, "")
    tmp5 = tmp4.replace(pattern5, "")
    tmp6 = tmp5.replace(pattern6, "")
    tmp7 = tmp6.replace(pattern7, "")
    tmp8 = tmp7.replace(pattern8, "")
    tmp9 = tmp8.replace(pattern9, "")
    tmp10 = tmp9.replace(pattern10, "")
    tmp11 = tmp10.replace(pattern11, "")
    tmp12 = tmp11.replace(pattern12, "")
    tmp13 = tmp12.replace(pattern13, "")
    print(tmp13)


def query(q):
    try:
        print("Please, wait...")
        conn = http.client.HTTPSConnection("www.ultratools.com")
        params = urllib.parse.urlencode({'ipWhoisLookupForm': '', 'ipAddress': q, 'submit': 'IP Lookup'})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn.request("POST", "/tools/ipWhoisLookupResult", params, headers)
        r = conn.getresponse().read().decode('utf-8')
        result(r)
        conn.close()


    except:
        print("Error")


r = open("include/about.txt", "r")
print(r.read())
ip = input("Enter IPv4, IPv6 or Domain Name \n")
if ip == "":
    print("Input is blank")
else:
    query(ip)





