import requests
import os
import sys
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def main(addr):
    global ans
    try:
        ans = ("https://" + addr)
        r = requests.get(ans, timeout=2, verify = False)
        outpt(r)

    except requests.ConnectionError:
        try:
            ans = ("http://" + addr)
            r = requests.get(ans, timeout=2, verify = False)
            outpt(r)
            
        except requests.ConnectionError:
            connectionError()
        except:
            Error()

    except:
        Error()

def outpt(r):
    report = (ans + " | " +  str(r.status_code) + "\n")
    print (report[:-1])
    WriteReport = open('Report.txt', 'a')
    WriteReport.write(report)
    WriteReport.close()

def connectionError():
    report = (addr + " | Connection Error" + "\n")
    print(report[:-1])
    WriteReport = open('Report.txt', 'a')
    WriteReport.write(report)
    WriteReport.close()

def Error():
    report = (addr + " | Timeout " + "\n")
    print(report[:-1])
    WriteReport = open('Report.txt', 'a')
    WriteReport.write(report)
    WriteReport.close()

if __name__== "__main__":

    pathname = os.path.dirname(sys.argv[0])
    os.chdir(pathname)
    open('Report.txt', 'w').close()

    with open("domainlist.txt", "r") as file:   
        for line in file:
            addr = line.strip()
            if str(line[:4])== "http":
                try:
                    r = requests.get(addr, timeout=2, verify = False)
                    ans = addr
                    outpt(r)
                except requests.ConnectionError:
                    connectionError()
                except:
                    Error()
            else:
                main(addr)
            
