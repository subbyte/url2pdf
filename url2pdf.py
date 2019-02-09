#!/usr/bin/env python

import sys
import validators
import pdfkit

def printUsage ():
    print ("Usage: url2pdf.py https://www.url.com output.pdf")

def validArgvs (a):
    return len(a) == 3 and validators.url(a[1]) and a[2][-4:] == ".pdf"

def main ():
    if validArgvs (sys.argv):
        src = sys.argv[1]
        dest = sys.argv[2]
        pdfkit.from_url(src, dest)
    else:
        printUsage()

if __name__ == "__main__":
    main()
