msf6 > use auxiliary/scanner/smtp/smtp


Matching Modules
================

   #  Name                                     Disclosure Date  Rank    Check  Description
   -  ----                                     ---------------  ----    -----  -----------
   0  auxiliary/scanner/smtp/smtp_version                       normal  No     SMTP Banner Grabber
   1  auxiliary/scanner/smtp/smtp_ntlm_domain                   normal  No     SMTP NTLM Domain Extraction
   2  auxiliary/scanner/smtp/smtp_relay                         normal  No     SMTP Open Relay Detection
   3  auxiliary/scanner/smtp/smtp_enum                          normal  No     SMTP User Enumeration Utility




msf6 auxiliary(scanner/smtp/smtp_enum) > use 2
msf6 auxiliary(scanner/smtp/smtp_relay) > show options

Module options (auxiliary/scanner/smtp/smtp_relay):

   Name      Current Setting     Required  Description
   ----      ---------------     --------  -----------
   EXTENDED  false               yes       Do all the 16 extended checks
   MAILFROM  sender@example.com  yes       FROM address of the e-mail
   MAILTO    target@example.com  yes       TO address of the e-mail
   RHOSTS                        yes       The target host(s), see https://docs.metasploit.com/docs/using-metaspl
                                           oit/basics/using-metasploit.html
   RPORT     25                  yes       The target port (TCP)
   THREADS   1                   yes       The number of concurrent threads (max one per host)


View the full module info with the info, or info -d command.

msf6 auxiliary(scanner/smtp/smtp_relay) > set RHOSTS 192.168.86.129
RHOSTS => 192.168.86.129

msf6 auxiliary(scanner/smtp/smtp_relay) > show options

Module options (auxiliary/scanner/smtp/smtp_relay):

   Name      Current Setting     Required  Description
   ----      ---------------     --------  -----------
   EXTENDED  false               yes       Do all the 16 extended checks
   MAILFROM  sender@example.com  yes       FROM address of the e-mail
   MAILTO    target@example.com  yes       TO address of the e-mail
   RHOSTS    192.168.86.129      yes       The target host(s), see https://docs.metasploit.com/docs/using-metaspl
                                           oit/basics/using-metasploit.html
   RPORT     25                  yes       The target port (TCP)
   THREADS   1                   yes       The number of concurrent threads (max one per host)


msf6 auxiliary(scanner/smtp/smtp_relay) > run

[+] 192.168.86.129:25     - SMTP 220 metasploitable.localdomain ESMTP Postfix (Ubuntu)\x0d\x0a
[*] 192.168.86.129:25     - No relay detected
[*] 192.168.86.129:25     - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed

