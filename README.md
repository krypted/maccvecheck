#cvemacoscheck.py
Checks the CVE database for any macOS Vulnerabilities

Run the command with no $1 and it will return empty braces if no vulnerabilities are found. For example:

cvemacoscheck.py 10.13.6

Will result in:

[]

Supplying no $1 will result in checking the current operating system and outputing information about the OS version the tool is run on. 

#cveitunescheck.py
Checks the CVE database for any iTunes Vulnerabilities

Run the command with no $1 and it will return empty braces if no vulnerabilities are found. For example:

cveitunescheck.py 12.0

Will result in:

[]

Supplying no $1 will result in checking the current iTunes version and outputing information about the version currently installed on the system the tool is run on. 
