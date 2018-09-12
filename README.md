# maccvecheck
Checks the CVE database for any macOS Vulnerabilities

Run the command with no $1 and it will return empty braces if no vulnerabilities are found. For example:

cvecheck.py 10.13.6

Will result in:

[]

Supplying no $1 will result in checking the current operating system and outputing information about that OS. 
