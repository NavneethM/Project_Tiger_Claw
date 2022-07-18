import random
import ipaddress

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class QuestionBank:
    def randomloop1(mc):
        output3 = ""
        random.shuffle(mc)
        for choice in mc:
            output3 += "\n " + choice
        return output3

    #for future implementation
    #Adds letter choices to multiple choices
    def randomloop(mc):
        multChoice = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        i = 0

        output3 = ""
        random.shuffle(mc)
        for choice in mc:
            output3 += "\n " + multChoice[i] + " " + choice
            i += 1
        return output3
    
    #Random IP
    def rand_IP():
        iprand = str(ipaddress.IPv4Address(random.randint(1,2147483647))) + "/" +str(random.randint(10, 31))
        return iprand

    iplist = [
        rand_IP(),
        rand_IP(),
        rand_IP(),
        rand_IP(),
        rand_IP(),
    ]

    #Random binary generator
    def rand_bin():
        decInt = random.randint(1, 255)
        temp = bin(decInt)[2:]
    
        return temp

    #Random hexidecimal generator
    def rand_hex():
        decInt = random.randint(1, 255)
        temp = hex(decInt)[2:]
    
        return temp
    
    def rand_oct():
        decInt = random.randint(1, 255)
        temp = oct(decInt)[2:]
    
        return temp
    
    rlist = [
        (rand_bin()),
        (rand_hex()),
        (rand_oct()),
        (random.randint(1, 255)),
        (random.randint(1, 255)),
        (random.randint(1, 255))
    ]

    quiz_choices = [
        #this is a list of tuples. the first is what the user sees, the second is the name corresponding question list minus _question
        ("Ports", "port"),
        ("OSI Model", "osi"),
        ("Computery Things 1", "ct1"),
        ("Computery Things 2", "ct2"),
        ("Unix/Windows Things", "unix_windows1"),
        ("Computery Things 3", "ct3"),
        ("Storage and Memory", "storage_memory"),
        ("Domains, Logs, and a little Powershell", "domains_logs"),
        ("Networking", "networking"),
        ("Routing", "routing"),
        ("Linux Files", "linux_file"),
        ("Number Convertions", "number_conv"),
        ("Networking Commands", "networking_commands"),
        ("Security", "security"), 
        ("Subnetting", "subnetting"),
        ("TCP/IP", "tcp_ip"),
        ("More Ports", "more_ports"),
        ("Practicals", "practical"),
        ("More Networking", "more_networking"),
        ("Windows File System", "windows_filesys"),
        ("A Few Random Topics", "thingsigottoldlastminute")
    ]
        

    port_question_prompts = [
        "What service runs on TCP port 20?" + randomloop(["- FTP Data Transfer", "- FTP Control", "- SSH", "- SMTP"]) + "\n[+] Answer> ",
        "What service runs on TCP port 21?" + randomloop(["- FTP Data Transfer", "- RDP", "- FTP Control", "- IMAP"]) + "\n[+] Answer> ",
        "What service runs on TCP/UDP port 3389?" + randomloop(["- SUNRPC", "- RDP", "- NETBIOS", "- Datagram", "- SNMP"]) + "\n[+] Answer> ",
        "What service runs on TCP/UDP port 137?" + randomloop(["- DHCP", "- SYSLOG", "- NetBIOS Name", "- LDAPS"]) + "\n[+] Answer> ",
        "What service runs on TCP port 111?" + randomloop(["- SUNRPC", "- POP3", "- SSH", "- Telnet"]) + "\n[+] Answer> ",
        "What service runs on TCP port 445?" + randomloop(["- BOOTP", "- SYSLOG", "- SMB", "- NetBIOS Sessions" ]) + "\n[+] Answer> ",
        "What service runs on TCP port 110?" + randomloop(["- IMAP", "- LDAPS", "- DHCP", "- POP3"]) + "\n[+] Answer> ",
        "What service runs on UDP port 514?" + randomloop(["- NetBIOS Name", "- NetBIOS Datagram", "- SNMP", "- SYSLOG"]) + "\n[+] Answer> ",
        "What service runs on TCP/UDP port 138?" + randomloop(["- NetBIOS Datagram", "- FTP Control", "- HTTP", "- HTTPS"]) + "\n[+] Answer> ",
        "What NEWER service runs on UDP port 67 & 68?" + randomloop(["- SMB", "- RDP", "- DHCP", "- SQL"]) + "\n[+] Answer> ",
        "What service runs on TCP/UDP port 139?" + randomloop(["- LDAPS", "- NetBIOS Session", "- BOOTP", "- FTPS"]) + "\n[+] Answer> ",
        "What service runs on TCP port 143?" + randomloop(["- IMAP", "- POP3", "- SMB", "- NetBIOS Name"]) + "\n[+] Answer> ",
        "What service runs on TCP/UDP port 161/162?" + randomloop(["- RDP", "- FTP Control", "- SSH", "- SNMP"]) + "\n[+] Answer> ",
        "What service runs on TCP/UDP port 636?" + randomloop(["- SNMP", "- IMAP", "- LDAPS", "- FTP Data Transfer"]) + "\n[+] Answer> ",
        "What OLDER service runs on UDP port 67 & 68?" + randomloop(["- SMB", "- RDP", "- DHCP", "- BOOTP"]) + "\n[+] Answer> ",
        "RPC involves using all of the following ports execpt which one?" + randomloop(["- 123", "- 135", "- 139", "- 445"]) + "\n[+] Answer> ",
        
    ]

    port_questions = [
        Question(port_question_prompts[0], "FTP Data Transfer"),
        Question(port_question_prompts[1], "FTP Control"),
        Question(port_question_prompts[2], "RDP"),
        Question(port_question_prompts[3], "NetBIOS Name"),
        Question(port_question_prompts[4], "SUNRPC"),
        Question(port_question_prompts[5], "SMB"),
        Question(port_question_prompts[6], "POP3"),
        Question(port_question_prompts[7], "SYSLOG"),
        Question(port_question_prompts[8], "NetBIOS Datagram"),
        Question(port_question_prompts[9], "DHCP"),
        Question(port_question_prompts[10], "NetBIOS Session"),
        Question(port_question_prompts[11], "IMAP"),
        Question(port_question_prompts[12], "SNMP"),
        Question(port_question_prompts[13], "LDAPS"),
        Question(port_question_prompts[14], "BOOTP"),
        Question(port_question_prompts[15], "123"),
        
    ]

    osi_question_prompts = [
        "What is layer 3 of the OSI model?" + randomloop(["- Application", "- Network", "- Transport", "- Session"]) + "\n[+] Answer> ",
        "What is layer 7 of the OSI model?" + randomloop(["- Presentation", "- Network", "- Physical", "- Application"]) + "\n[+] Answer> ",
        "What is layer 1 of the OSI model?" + randomloop(["- Application", "- Physical", "- Network", "- Transport"]) + "\n[+] Answer> ",
        "What is layer 5 of the OSI model?" + randomloop(["- Session", "- Data Link", "- Physical", "- Transport"]) + "\n[+] Answer> ",
        "What is layer 6 of the OSI model?" + randomloop(["- Transport", "- Session", "- Presentation", "- Data Link"]) + "\n[+] Answer> ",
        "What is layer 2 of the OSI model?" + randomloop(["- Physical", "- Application", "- Data Link", "- Transport"]) + "\n[+] Answer> ",
        "What is layer 4 of the OSI model?" + randomloop(["- Transport", "- Network", "- Data Link", "- Session"]) + "\n[+] Answer> ",
        "What form is information in at Layer 7 of the OSI model?" + randomloop(["- Data", "- Packets", "- Segments", "- Bits", "- Frames"]) + "\n[+] Answer> ",
        "What form is information in at Layer 2 of the OSI model?" + randomloop(["- Data", "- Packets", "- Segments", "- Bits", "- Frames"]) + "\n[+] Answer> ",
        "What form is information in at Layer 5 of the OSI model?" + randomloop(["- Data", "- Packets", "- Segments", "- Bits", "- Frames"]) + "\n[+] Answer> ",
        "What form is information in at Layer 6 of the OSI model?" + randomloop(["- Data", "- Packets", "- Segments", "- Bits", "- Frames"]) + "\n[+] Answer> ",
        "What form is information in at Layer 1 of the OSI model?" + randomloop(["- Data", "- Packets", "- Segments", "- Bits", "- Frames"]) + "\n[+] Answer> ",
        "What form is information in at Layer 4 of the OSI model?" + randomloop(["- Data", "- Packets", "- Segments", "- Bits", "- Frames"]) + "\n[+] Answer> ",
        "What form is information in at Layer 3 of the OSI model?" + randomloop(["- Data", "- Packets", "- Segments", "- Bits", "- Frames"]) + "\n[+] Answer> ",
        "Router communications, packet forwarding, and ARP happen at which layer of the OSI model?" + randomloop(["- Application", "- Presentation", "- Session", "- Transport", "- Network", "- Data Link", "- Physical"]) + "\n[+] Answer> ",
        "Encryption and Decryption is done at which layer of the OSI model?" + randomloop(["- Application", "- Presentation", "- Session", "- Transport", "- Network", "- Data Link", "- Physical"]) + "\n[+] Answer> ",
        "TCP and UDP is utilized at which layer of the OSI model?" + randomloop(["- Application", "- Presentation", "- Session", "- Transport", "- Network", "- Data Link", "- Physical"]) + "\n[+] Answer>",
        "Switches are commonly associated with which layer of the OSI model?" + randomloop(["- Application", "- Presentation", "- Session", "- Transport", "- Network", "- Data Link", "- Physical"]) + "\n[+] Answer> ",
        "The GUI is utilized at which layer of the OSI model?" + randomloop(["- Application", "- Presentation", "- Session", "- Transport", "- Network", "- Data Link", "- Physical"]) + "\n[+] Answer> ",
        "Communication between two devices is done at which layer of the OSI model?" + randomloop(["- Application", "- Presentation", "- Session", "- Transport", "- Network", "- Data Link", "- Physical"]) + "\n[+] Answer> ",
        "Cables, media, signals, and binary transmissions are all associated with which layer of the OSI model?" + randomloop(["- Application", "- Presentation", "- Session", "- Transport", "- Network", "- Data Link", "- Physical"]) + "\n[+] Answer> ",
    ]

    #Question(question_prompts[##], "x"),
    osi_questions = [
        Question(osi_question_prompts[0], "Network"),
        Question(osi_question_prompts[1], "Application"),
        Question(osi_question_prompts[2], "Physical"),
        Question(osi_question_prompts[3], "Session"),
        Question(osi_question_prompts[4], "Presentation"),
        Question(osi_question_prompts[5], "Data Link"),
        Question(osi_question_prompts[6], "Transport"),
        Question(osi_question_prompts[7], "Data"),
        Question(osi_question_prompts[8], "Frames"),
        Question(osi_question_prompts[9], "Data"),
        Question(osi_question_prompts[10], "Data"),
        Question(osi_question_prompts[11], "Bits"),
        Question(osi_question_prompts[12], "Segments"),
        Question(osi_question_prompts[13], "Packets"),
        Question(osi_question_prompts[14], "Network"),
        Question(osi_question_prompts[15], "Presentation"),
        Question(osi_question_prompts[16], "Transport"),
        Question(osi_question_prompts[17], "Data Link"),
        Question(osi_question_prompts[18], "Application"),
        Question(osi_question_prompts[19], "Session"),
        Question(osi_question_prompts[20], "Physical"),
    ]

    ct1_question_prompts = [
        "Where are Windows event logs stored?(X:\\XXXX\\xxxx\\xxx)\n[+] Answer> ",
        "Where is Windows DNS info stored?(X:\\XXXX\\xxxx\\XXX)\n[+] Answer> ",
        "What is the base file where all UNIX logs are stored?\n[+] Answer> ",
        "Where is UNIX DNS info stored?\n[+] Answer> ",
        "What provides information and statistics about protocols in use and current TCP/IP network connections.?" + randomloop(["- ipconfig", "- netstat", "- /etc/hosts", "- iptables"]) + "\n[+] Answer> ",
        "What allows a diskless client machine to discover its own IP address, the address of a server host, and the name of a file to loaded into memory and executed?" + randomloop(["- DHCP", "- DNS", "- BOOTP"]) + "\n[+] Answer> ",
        "What is based on BOOTP, adding the capability of automatic allocation of reusable network addresses and addition configuration option?" + randomloop(["- BOOTP", "- DHCP", "- SMB", "- RISC"]) + "\n[+] Answer> ",
        "What are the 4 steps of the DHCP process. (Answer should look like 'Xxxx, Xxxx, Xxxx, Xxxx')?\n[+] Answer> ",
        "This is a single-clock, with reduced instruction only; register to register: 'LOAD' and 'STORE' are independent instructions; low cycles per second, large code sizes; spends more transistors on memory registers?" + randomloop(["- RISC", "- CISC", "- SPARC"]) + "\n[+] Answer> ",
        "This includes multi-clock complex instructions, memory to memory 'LOAD' and 'STORE' incorporated in instructions; small code sizes, high cycles per second; transistors used for storing complex instructions?" + randomloop(["- RISC", "- CISC", "- SPARC"]) + "\n[+] Answer> ",
        "This is a 32bit and 64bit open microprocessor architecture from Sun Microsystems. Based on RISC?" + randomloop(["- RISC", "- CISC", "- SPARC"]) + "\n[+] Answer> ",
        "What service is used to provide communication over LAN?" + randomloop(["- SMB", "- HTTP", "- NetBIOS", "- DNS"]) + "\n[+] Answer> ",
        "NetBios operates in which layer of the OSI model?" + randomloop(["- Transport", "- Session", "- Data Link", "- Presentation"]) + "\n[+] Answer> ",
        "NetBios names can be up to how many characters long?" + randomloop(["- 6", "- 15", "- 32", "- 128"]) + "\n[+] Answer>",
        "Which NetBIOS port provides name registration and resolution?" + randomloop(["- 136", "- 137", "- 138", "- 139"]) + "\n[+] Answer> ",
        "Which NetBIOS port provides Reliable, connection-oriented communication?" + randomloop(["- 136", "- 137", "- 138", "- 139"]) + "\n[+] Answer> ",
        "Which NetBIOS port provides distribution service for connection-oriented communication?" + randomloop(["- 136", "- 137", "- 138", "- 139"]) + "\n[+] Answer> ",
        "Which service allows systems to share files, printers, and serial ports within the same network?" + randomloop(["- SMTP", "- UDP", "- SSH", "- SMB"]) + "\n[+] Answer> ",
        "SMB is utilized on which port?\n[+] Answer> ",
        "SMB operates on the presentation and which other layer of the OSI model?" + randomloop(["- Transport", "- Session", "- Application" , "- Network"]) + "\n[+] Answer> ",
        "What protocol does telnet use over the internet?"+ randomloop(["- TCP", "- UDP", "- Ethernet" , "- DNS"]) + "\n[+] Answer> ",
    ]
    #Question(question_prompts[##], "x"),
    ct1_questions = [
        Question(ct1_question_prompts[0], "C:\WINDOWS\system32\config"),
        Question(ct1_question_prompts[1], "C:\WINDOWS\system32\DNS"),
        Question(ct1_question_prompts[2], "/var/log"),
        Question(ct1_question_prompts[3], "/etc/resolv.conf"),
        Question(ct1_question_prompts[4], "netstat"),
        Question(ct1_question_prompts[5], "BOOTP"),
        Question(ct1_question_prompts[6], "DHCP"),
        Question(ct1_question_prompts[7], "Discover, Offer, Request, Acknowledge"),
        Question(ct1_question_prompts[8], "RISC"),
        Question(ct1_question_prompts[9], "CISC"),
        Question(ct1_question_prompts[10], "SPARC"),
        Question(ct1_question_prompts[11], "NetBIOS"),
        Question(ct1_question_prompts[12], "Session"),
        Question(ct1_question_prompts[13], "15"),
        Question(ct1_question_prompts[14], "137"),
        Question(ct1_question_prompts[15], "139"),
        Question(ct1_question_prompts[16], "138"),
        Question(ct1_question_prompts[17], "SMB"),
        Question(ct1_question_prompts[18], "445"),
        Question(ct1_question_prompts[19], "Application"),
        Question(ct1_question_prompts[20], "TCP"),
    ]
    ct2_question_prompts = [
        "SEQ numbers are how many bits?" + randomloop(["- 32", "- 64", "- 16", "- 8"]) + "\n[+] Answer> ",
        "What are used by transmitters on each transmitted packet?" + randomloop(["- SEQ numbers", "- ACK numbers", "- PSH numbers", "- URG numbers"]) + "\n[+] Answer> ",
        "SEQ numbers are ________ when host initiates a TCP session." + "\n[+] Answer> ",
        "What are used to inform a sender that the transmitted data was sent successfully?" + randomloop(["- SEQ numbers", "- ACK numbers", "- PSH numbers", "- URG numbers"]) + "\n[+] Answer> ",
        "ACK numbers are based on _______ numbers and amount of data sent over transmission." + "\n[+] Answer> ",
        "What is the min size of a TCP header?" + randomloop(["- 20 bytes", "- 8 bytes", "- 64 bytes", "- 128 bytes"]) + "\n[+] Answer> ",
        "Source Port, Destination Port, SEQ number, ACK number, Flags, Window Size, Checksum, Urgent Pointer and Data are all part of what kind of header?" + randomloop(["- TCP", "- UDP", "- Ethernet", "- Browser"]) + "\n[+] Answer> ",
        "What is the max payload size for a TCP Header in bytes?" + randomloop(["- 1460", "- 1472", "- 1500", "- 1527"]) + "\n[+] Answer> ",
        "What is the min size of a UDP header?" + randomloop(["- 20 bytes", "- 8 bytes", "- 64 bytes", "- 128 bytes"]) + "\n[+] Answer> ",
        "Source Port, Destination Port, Length, Checksum, and Data are the ONLY parts of which header?" + randomloop(["- TCP", "- UDP", "- Ethernet", "- Browser"]) + "\n[+] Answer> ",
        "What is the max payload size for a UDP Header in bytes?" + randomloop(["- 1460", "- 1472", "- 1500", "- 1527"]) + "\n[+] Answer> ",
        "What is the min size of an Ethernet header?" + randomloop(["- 20 bytes", "- 8 bytes", "- 64 bytes", "- 128 bytes"]) + "\n[+] Answer> ",
        "Destination MAC, Source MAC, EtherType (0800 for IPv4), Payload, Checksum are the ONLY parts of which header?" + randomloop(["- TCP", "- UDP", "- Ethernet", "- Browser"]) + "\n[+] Answer> ",
        "What is the max payload size for an Ethernet Header in bytes?" + randomloop(["- 1460", "- 1472", "- 1500", "- 1527"]) + "\n[+] Answer> ",
        "What type of encryption does HTTPS use?" + randomloop(["- Symmetric", "- Asymmetric"]) + "\n[+] Answer> ",

    ]
    ct2_questions = [
        Question(ct2_question_prompts[0], "32"),
        Question(ct2_question_prompts[1], "SEQ numbers"),
        Question(ct2_question_prompts[2], "random"),
        Question(ct2_question_prompts[3], "ACK numbers"),
        Question(ct2_question_prompts[4], "SEQ"),
        Question(ct2_question_prompts[5], "20 bytes"),
        Question(ct2_question_prompts[6], "TCP"),
        Question(ct2_question_prompts[7], "1460"),
        Question(ct2_question_prompts[8], "8 bytes"),
        Question(ct2_question_prompts[9], "UDP"),
        Question(ct2_question_prompts[10], "1472"),
        Question(ct2_question_prompts[11], "64 bytes"),
        Question(ct2_question_prompts[12], "Ethernet"),
        Question(ct2_question_prompts[13], "1500"),
        Question(ct2_question_prompts[14], "Asymmetric"),
    ]
    unix_windows1_question_prompts = [
        "What does UNIX runlevel 0 mean?" + randomloop(["- Halt", "- Single User Mode", "- Unused", "- Reboot"]) + "\n[+] Answer> ",
        "What does UNIX runlevel 1 mean?" + randomloop(["- Single User Mode", "- Multiuser without NFS", "- Full multiuser mode", "- X11"]) + "\n[+] Answer> ",
        "What does UNIX runlevel 2 mean?" + randomloop(["- Multiuser without NFS", "- Full multiuser mode", "- Unused", "- HALT"]) + "\n[+] Answer> ",
        "What does UNIX runlevel 3 mean?" + randomloop(["- Full multiuser mode", "- Unused", "- Reboot", "- Single User Mode"]) + "\n[+] Answer> ",
        "What does UNIX runlevel 4 mean?" + randomloop(["- Unused", "- X11", "- HALT", "- Multiuser, without NFS"]) + "\n[+] Answer> ",
        "What does UNIX runlevel 5 mean?" + randomloop(["- X11", "- Reboot", "- Full multiuser mode", "- Multiuser, without NFS"]) + "\n[+] Answer> ",
        "What does UNIX runlevel 6 mean?" + randomloop(["- Reboot", "- Single User Mode", "- HALT", "- Unused"]) + "\n[+] Answer> ",
        "In Windows 10: Power-On-Self Test (POST) loads firmware settings, checks for valid disk system, checks for valid MBR; happens at which step in the boot process?" + randomloop(["- Pre-Boot", "- Windows Boot Manager", "- Windows OS Loader", "- Windows NT OS Kernel"]) + "\n[+] Answer> ",
        "In Windows 10: which step of the boot process checks if multiple OS's are on disk, starts winload.exe?" + randomloop(["- Pre-Boot", "- Windows Boot Manager", "- Windows OS Loader", "- Windows NT OS Kernel"]) + "\n[+] Answer> ",
        "In Windows 10: which step of the boot process does Winload.exe start important processes to kickstart the Windows Kernel?" + randomloop(["- Pre-Boot", "- Windows Boot Manager", "- Windows OS Loader", "- Windows NT OS Kernel"]) + "\n[+] Answer> ",
        "In Windows 10: Which step of the boot process picks up registry settings, additional drivers, etc., control is taken by system manager process, GUI is loaded?" + randomloop(["- Pre-Boot", "- Windows Boot Manager", "- Windows OS Loader", "- Windows NT OS Kernel"]) + "\n[+] Answer> ",
        "What are the steps of the UNIX boot process in order?(Answer should look like XXXXXX)\nA. Init\nB. GRUB\nC. BIOS\nD. Runlevel\nE. MBR\nF. Kernel " + "\n[+] Answer> ",
        "What does the BIOS step in the UNIX boot process do?" + randomloop(["- Executes MBR", "- Executes GRUB", "- Executes /sbin/init", "- Executes Kernel"]) + "\n[+] Answer> ",
        "What is the linux equivalent to a DLL on a Windows machine?" + "\n[+] Answer> ",
        "On Windows, if a path begins with \\\\ that would indicate that it is/is using what?" + "\n[+] Answer> ",
        "In Windows, what uses physical disk space to store memory data that is not actively being used in RAM to make room for something that is active, and acts as VIRTUAL MEMORY?" + randomloop(["- Page File", "- Page Table", "- Virtual Address", "- Page Directory"]) + "\n[+] Answer> ",
        #"What ?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ", 
    ]
    unix_windows1_questions = [
        Question(unix_windows1_question_prompts[0], "Halt"),
        Question(unix_windows1_question_prompts[1], "Single User Mode"),
        Question(unix_windows1_question_prompts[2], "Multiuser without NFS"),
        Question(unix_windows1_question_prompts[3], "Full multiuser mode"),
        Question(unix_windows1_question_prompts[4], "Unused"),
        Question(unix_windows1_question_prompts[5], "X11"),
        Question(unix_windows1_question_prompts[6], "Reboot"),
        Question(unix_windows1_question_prompts[7], "Pre-Boot"),
        Question(unix_windows1_question_prompts[8], "Windows Boot Manager"),
        Question(unix_windows1_question_prompts[9], "Windows OS Loader"),
        Question(unix_windows1_question_prompts[10], "Windows NT OS Kernel"),
        Question(unix_windows1_question_prompts[11], "CEBFAD"),
        Question(unix_windows1_question_prompts[12], "Executes MBR"),
        Question(unix_windows1_question_prompts[13], "Shared Object"),
        Question(unix_windows1_question_prompts[14], "Universal Naming Convention"),
        Question(unix_windows1_question_prompts[15], "Page File"),
    ]
    ct3_question_prompts = [
        "What is the standard TTL (Time to Live) for a Cisco or Solaris/AIX device?" + randomloop(["- 254", "- 128", "- 64", "- 512"]) + "\n[+] Answer> ",
        "What is the standard TTL (Time to Live) for a Windows device?" + randomloop(["- 254", "- 128", "- 64", "- 512"]) + "\n[+] Answer> ",
        "What is the standard TTL (Time to Live) for a Linux/Unix device?" + randomloop(["- 254", "- 128", "- 64", "- 512"]) + "\n[+] Answer> ",
        "What is the programs and other operation information used by a computer?" + randomloop(["- Software", "- Hardware", "- Firmware"]) + "\n[+] Answer> ", 
        "What is the collection of physical parts of a computer system?" + randomloop(["- Software", "- Hardware", "- Firmware"]) + "\n[+] Answer> ",
        "What is the semi-permanent software programmed into a read-only memory?" + randomloop(["- Software", "- Hardware", "- Firmware"]) + "\n[+] Answer> ",
        "How many groups of hexidecimal digits make up an IPv6 address?" + randomloop(["- 8", "- 10", "- 6", "- 4"]) + "\n[+] Answer> ",
        "How many bits long is an IPv6 address?" + randomloop(["- 128", "- 64", "- 256", "- 32"]) + "\n[+] Answer> ", 
        "What can you put in place of back to back 0s in an IPv6 address?" + "\n[+] Answer> ",
        "What command will print network connections, routing tables, interface stats with  the flags for: ALL, NUMERIC, TIMERS?" + randomloop(["- netstat -ano", "- ifconfig -ant", "- netstat -a", "- iptables -anT"]) + "\n[+] Answer> ",
        "What command displays and modifies entries in the Address Resolution Protocol (ARP) cache?" + randomloop(["- arp -a", "- routes", "- nestat -a", "- ifconfig"]) + "\n[+] Answer> ",
        "TTL determines the number of _____ a device can take?" + "\n[+] Answer> ", 
        #"What ?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ",
        #"What ?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ",
        #"What ?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ",
        #"What ?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ", 
    ]
    ct3_questions = [
        Question(ct3_question_prompts[0], "254"),
        Question(ct3_question_prompts[1], "128"),
        Question(ct3_question_prompts[2], "64"),
        Question(ct3_question_prompts[3], "Software"),
        Question(ct3_question_prompts[4], "Hardware"),
        Question(ct3_question_prompts[5], "Firmware"),
        Question(ct3_question_prompts[6], "8"),
        Question(ct3_question_prompts[7], "128"),
        Question(ct3_question_prompts[8], "::"),
        Question(ct3_question_prompts[9], "netstat -ano"),
        Question(ct3_question_prompts[10], "arp -a"),
        Question(ct3_question_prompts[11], "hops"),
        #Question(ct3_question_prompts[12], ""),
        #Question(ct3_question_prompts[13], ""),
        #Question(ct3_question_prompts[14], ""),
    ]
    storage_memory_question_prompts = [
        "In regards to HDDs/SSDs, what are sections of the drive that are separated from other segments of the drive?" + randomloop(["- Partitions", "- Sectors", "- Platters", "- Inodes"]) + "\n[+] Answer> ", 
        "In regards to HDDs/SSDs, what are subdivision of a track on a magnetic disk or optical disc?" + randomloop(["- Partitions", "- Sectors", "- Platters", "- Inodes"]) + "\n[+] Answer> ",
        "In regards to HDDs/SSDs, what is one of the disks in a hard disk drive?" + randomloop(["- Partition", "- Sector", "- Platter", "- Inode"]) + "\n[+] Answer> ",
        "In regards to HDDs/SSDs, what provides important information on files such as user and group ownership, access mode (read, write, execute permissions) and type?" + randomloop(["- Partitions", "- Sectors", "- Platters", "- Inodes"]) + "\n[+] Answer> ",
        "Each sector of a HDD stores a ______ amount of user-accessible data ?" + randomloop(["- Fixed", "- Random"]) + "\n[+] Answer> ",
        "What is the minimum storage unit of a hard drive?" + randomloop(["- Partition", "- Sector", "- Platter", "- Inode"]) + "\n[+] Answer> ", 
        "Each _______ provides a top and bottom recording surface." + randomloop(["- Partition", "- Sector", "- Platter", "- Inode"]) + "\n[+] Answer> ",
        "What refers to the virtual space that is allocated within the disk itself?" + randomloop(["- Logical", "- Physical"]) + "\n[+] Answer> ",
        "What refers to the physical hardware within the system?" + randomloop(["- Logical", "- Physical"]) + "\n[+] Answer> ",
        "What is the Order of Volatility from  most to least?(Answer should look like XXXXXXX, replacing each X with the appropriate letter \nA. Registers and Caches\nB. Temporary File Systems\nC. Archival Media\nD. Physical Configuration, Network Topology\nE. Routing Table, ARP Cache, Process Table, Kernel Statistics, Memory\nF. Remote Logging and Monitoring Data that is relevant to the System in Question\nG. Disk" + "\n[+] Answer> ", 
        "In x86 you can have no more than how many GB or RAM?" + randomloop(["- 4", "- 8", "- 16", "- 32"]) + "\n[+] Answer> ", 
        "Which of these can have more than 4GB of RAM installed?" + randomloop(["- x86", "- x64"]) + "\n[+] Answer> ",
        "What is a system level memory protection that prevents the execution of data?" + "\n[+] Answer> ",
        "How would you logically make data that is smaller than a platter?" + randomloop(["- Partition", "- Refactor", "- Defragment"]) + "\n[+] Answer> ",
        "A hard link points to a(n) ______, or the direct file in memory ?" + "\n[+] Answer> ", 
        "A symbolic link points to the ______ ______, using its full path name?" + "\n[+] Answer> ", 
        #"What ?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ",
        #"What ?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ",
        #"What ?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ",
        #"What ?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ",  
    ]
    storage_memory_questions = [
        Question(storage_memory_question_prompts[0], "Partitions"),
        Question(storage_memory_question_prompts[1], "Sectors"),
        Question(storage_memory_question_prompts[2], "Platter"),
        Question(storage_memory_question_prompts[3], "Inodes"),
        Question(storage_memory_question_prompts[4], "Fixed"),
        Question(storage_memory_question_prompts[5], "Sector"),
        Question(storage_memory_question_prompts[6], "Platter"),
        Question(storage_memory_question_prompts[7], "Logical"),
        Question(storage_memory_question_prompts[8], "Physical"),
        Question(storage_memory_question_prompts[9], "AEBGFDC"),
        Question(storage_memory_question_prompts[10], "4"),
        Question(storage_memory_question_prompts[11], "x64"),
        Question(storage_memory_question_prompts[12], "Data Execution Prevention"),
        Question(storage_memory_question_prompts[13], "Partition"),
        Question(storage_memory_question_prompts[14], "inode"),
        Question(storage_memory_question_prompts[15], "original file"),
    ]
    domains_logs_question_prompts = [
        "What was the first Windows OS to use Kerberos?" + randomloop(["- 2000", "- XP", "- 98", "- Vista"]) + "\n[+] Answer> ",
        "What is a server that responds to authentication requests and verifies users on computer networks?" + randomloop(["- Domain Controller", "- Active Directory", "- Mail", "- Media"]) + "\n[+] Answer> ",
        "The Domain Controller holds the key to the _______?" + randomloop(["- Active Directory", "- Kingdom", "- Registry", "- Shadow File"]) + "\n[+] Answer> ", 
        "The active directory for Windows is called Microsoft Active Directory or Microsoft _______?" + "\n[+] Answer> ", 
        "Every _______ has a Domain Controller, but not every domain has an Active Directory?" + "\n[+] Answer> ",
        "The active directory for Linux is commonly named?" + "\n[+] Answer> ",
        "Where does Windows store Event Logs? C:\Windows\system32\___" + randomloop(["- config", "- logs", "- events", "- error"]) + "\n[+] Answer> ",
        "Which answer does not explain on what circumstances does Windows create logs for?" + randomloop(["- Event", "- Error", "- Warning", "- Information", "- Danger"]) + "\n[+] Answer> ",
        "What does Windows store in each log about the specific log message?" + "\n[+] Answer> ",
        "In which log does Unix store general message and system related items? /var/log/_____" + "\n[+] Answer> ",
        "In which log does Unix store authentication logs?/var/log/_____" + "\n[+] Answer> ", 
        "In which log does Unix store Kernel logs? /var/log/_____" + "\n[+] Answer> ", 
        "In which log does Unix store Crond logs (cron job) /var/log/_____?" + "\n[+] Answer> ",
        "In which log does Unix store mail server logs? /var/log/_____" + "\n[+] Answer> ",
        "In Powershell what command do you use to get something?" + randomloop(["- Get", "- Start", "- Out", "- Stop", "- Set", "- New"]) + "\n[+] Answer> ",
        "In Powershell what command do you use to run something?" + randomloop(["- Get", "- Start", "- Out", "- Stop", "- Set", "- New"]) + "\n[+] Answer> ",
        "In Powershell what command do you use to output something?" + randomloop(["- Get", "- Start", "- Out", "- Stop", "- Set", "- New"]) + "\n[+] Answer> ",
        "In Powershell what command do you use to stop something that is running?" + randomloop(["- Get", "- Start", "- Out", "- Stop", "- Set", "- New"]) + "\n[+] Answer> ",
        "In Powershell what command do you use to define something ?" + randomloop(["- Get", "- Start", "- Out", "- Stop", "- Set", "- New"]) + "\n[+] Answer> ",
        "In Powershell what command do you use to create something new?" + randomloop(["- Get", "- Start", "- Out", "- Stop", "- Set", "- New"]) + "\n[+] Answer> ",
        "What is the network protocol that uses secret-key cryptography to\nauthenticate client-server applications?" + randomloop(["- Kerberos", "- AzureAD", "- Samba", "- Active Directory"]) + "\n[+] Answer> ",
        "What port does Kerberos typically operate on?" + randomloop(["- 88", "- 123", "- 445", "- 6689"]) + "\n[+] Answer> ",
    ]
    domains_logs_questions = [
        Question(domains_logs_question_prompts[0], "2000"),
        Question(domains_logs_question_prompts[1], "Domain Controller"),
        Question(domains_logs_question_prompts[2], "Active Directory"),
        Question(domains_logs_question_prompts[3], "AzureAD"),
        Question(domains_logs_question_prompts[4], "domain"),
        Question(domains_logs_question_prompts[5], "Samba"),
        Question(domains_logs_question_prompts[6], "config"),
        Question(domains_logs_question_prompts[7], "Danger"),
        Question(domains_logs_question_prompts[8], "Information"),
        Question(domains_logs_question_prompts[9], "messages"),
        Question(domains_logs_question_prompts[10], "auth.log"),
        Question(domains_logs_question_prompts[11], "kern.log"),
        Question(domains_logs_question_prompts[12], "cron.log"),
        Question(domains_logs_question_prompts[13], "maillog"),
        Question(domains_logs_question_prompts[14], "Get"),
        Question(domains_logs_question_prompts[15], "Start"),
        Question(domains_logs_question_prompts[16], "Out"),
        Question(domains_logs_question_prompts[17], "Stop"),
        Question(domains_logs_question_prompts[18], "Set"),
        Question(domains_logs_question_prompts[19], "New"),
        Question(domains_logs_question_prompts[20], "Kerberos"),
        Question(domains_logs_question_prompts[21], "88"),
    ]
    networking_question_prompts = [
        "Which network topology has as a series of devices, 'daisy chained', with successive coaxial cable and appropriate connectors and terminators?" + randomloop(["- Bus", "- Mesh", "- Ring", "- Star"]) + "\n[+] Answer> ",
        "Which network topology has a concentrator/hub device that acts as a central point for all cabling, allowing all connected users to communicate with each other?" + randomloop(["- Bus", "- Mesh", "- Ring", "- Star"]) + "\n[+] Answer> ",
        "Which network topology connects devices in a complete ring?" + randomloop(["- Bus", "- Mesh", "- Ring", "- Star"]) + "\n[+] Answer> ", 
        "Which network topology has every device connected to every other device via more than one route?" + randomloop(["- Bus", "- Mesh", "- Ring", "- Star"]) + "\n[+] Answer> ", 
        "Which network topology consists of at least two machines with redundant connections? A physical connection between devices to every other device is not required?" + randomloop(["- Mesh", "- Ring", "- Star", "- Partial Mesh"]) + "\n[+] Answer> ",
        "Which network topology is an organized grouping of devices where every device connects to one another?" + randomloop(["- Mesh", "- Bus", "- Star", "- Full Mesh"]) + "\n[+] Answer> ",
        "What is the function of connecting multiple computers to the Internet (or any other IP network) using one or multiple routable IP addresses?" + randomloop(["- NAT", "- PAT"]) + "\n[+] Answer> ",
        "What uses a network device that translates multiple local addresses to a single global address by keeping track of port assignments?" + randomloop(["- NAT", "- PAT"]) + "\n[+] Answer> ",
        "Is 10.0.0.0/8 a public or private IP address range?" + "\n[+] Answer> ",
        "Is 172.16.0.0/12 a public or private IP address range??" + "\n[+] Answer> ",
        "Is 192.168.0.0/16 a public or private IP address range?" + "\n[+] Answer> ",
        "Is 169.254.0.0/16 a public or private IP address range?" + "\n[+] Answer> ",
        "The IP address 169.254.0.0/16 is also known by what special name?" + "\n[+] Answer> ",
        "What class would IP addresses starting with 0-126 with a cidr of /1-8 be?" + randomloop(["- A", "- B", "- C", "- D", "- E"]) + "\n[+] Answer> ",
        "What class would IP addresses starting with 127-191 with a cidr of /9-16 be?" + randomloop(["- A", "- B", "- C", "- D", "- E"]) + "\n[+] Answer> ",
        "What class would IP addresses starting with 192-223 with a cidr of /17-24 be?" + randomloop(["- A", "- B", "- C", "- D", "- E"]) + "\n[+] Answer> ",
        "What class would IP addresses starting with 224-239 be?" + randomloop(["- A", "- B", "- C", "- D", "- E"]) + "\n[+] Answer> ",
        "What class would IP addresses starting with 240-255 be?" + randomloop(["- A", "- B", "- C", "- D", "- E"]) + "\n[+] Answer> ",
        "Which command utility uses the ICMP messages Echo (Request) and Echo Reply to request a response from a remote host to verify if it is available for communication?" + "\n[+] Answer> ", 
        #"What ?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ",
        #"What ?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ",
        #"What ?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ",
    ]
    networking_questions = [
        Question(networking_question_prompts[0], "Bus"),
        Question(networking_question_prompts[1], "Star"),
        Question(networking_question_prompts[2], "Ring"),
        Question(networking_question_prompts[3], "Mesh"),
        Question(networking_question_prompts[4], "Partial Mesh"),
        Question(networking_question_prompts[5], "Full Mesh"),
        Question(networking_question_prompts[6], "NAT"),
        Question(networking_question_prompts[7], "PAT"),
        Question(networking_question_prompts[8], "Private"),
        Question(networking_question_prompts[9], "Private"),
        Question(networking_question_prompts[10], "Private"),
        Question(networking_question_prompts[11], "Private"),
        Question(networking_question_prompts[12], "APIPA"),
        Question(networking_question_prompts[13], "A"),
        Question(networking_question_prompts[14], "B"),
        Question(networking_question_prompts[15], "C"),
        Question(networking_question_prompts[16], "D"),
        Question(networking_question_prompts[17], "E"),
        Question(networking_question_prompts[18], "ping"),
        #Question(networking_question_prompts[19], ""),
        #Question(networking_question_prompts[20], ""),
        #Question(networking_question_prompts[21], ""),
    ]
    routing_question_prompts = [
        "Which routing protocol is a Path Vector Protocol (PVP), which maintains paths to different hosts, networks, and gateway routers and determines the routing decision based on that?" + randomloop(["- BGP", "- EIGRP", "- IGRP", "- RIP"]) + "\n[+] Answer> ", 
        "Which routing protocol has an AD of 20?" + randomloop(["- External BGP", "- EIGRP", "- IGRP", "- RIP", "- OSPF"]) + "\n[+] Answer> ",
        "Which routing protocol has an AD of 90?" + randomloop(["- BGP", "- EIGRP", "- IGRP", "- RIP", "- OSPF"]) + "\n[+] Answer> ",
        "Which routing protocol has an AD of 120?" + randomloop(["- BGP", "- EIGRP", "- IGRP", "- RIP", "- OSPF"]) + "\n[+] Answer> ",
        "Which routing protocol has an AD of 110?" + randomloop(["- BGP", "- EIGRP", "- IGRP", "- RIP", "- OSPF"]) + "\n[+] Answer> ", 
        "Which routing protocol is an advanced distance-vector routing protocol that is used on a computer network for automating routing decisions and configuration? The protocol was designed by Cisco Systems as a proprietary protocol, available only on Cisco routers." + randomloop(["- BGP", "- EIGRP", "- IGRP", "- RIP"]) + "\n[+] Answer> ",
        "Which routing protocol is a proprietary distance vector routing protocol used to communicate routing information within a host network? It was invented by Cisco." + randomloop(["- BGP", "- EIGRP", "- IGRP", "- RIP"]) + "\n[+] Answer> ",
        "Which routing protocol is dynamic routing protocol which uses hop count as a routing metric to find the best path between the source and the destination network? It is a distance vector routing protocol that works on the application layer of the OSI model and uses port number 520." + randomloop(["- BGP", "- EIGRP", "- IGRP", "- RIP"]) + "\n[+] Answer> ",
        "Which routing protocol is routing protocol for Internet Protocol (IP) networks. It uses a link state routing (LSR) algorithm and falls into the group of interior gateway protocols (IGPs), operating within a single autonomous system (AS)?" + randomloop(["- OSPF", "- EIGRP", "- IGRP", "- RIP"]) + "\n[+] Answer> ", 
        "What do we use to map IP network addresses to the hardware addresses?" + "\n[+] Answer> ",
        "Which layer of the OSI model does ARP operate on?" + randomloop(["- Session", "- Network", "- Presentation", "- Application"]) + "\n[+] Answer> ",
        "______ is the process by which a packet is forwarded from one network to another?" + "\n[+] Answer> ",
        "What type of routing is the method by which the system administrator manually enters routes in the routing table?" + randomloop(["- Static", "- Dynamic", "- Random", "- Closed"]) + "\n[+] Answer> ", 
        "The main benefit of static routing is that no routing protocol traffic is generated by the _____." + randomloop(["- User", "- Router", "- NIC", "- Server"]) + "\n[+] Answer> ",
        "Static routing is recommended for networks with _______ bandwidth?" + randomloop(["- Low", "- High"]) + "\n[+] Answer> ",
        "What is used to give the router a path to send traffic that is destined for destinations that are not in the routing table?" + randomloop(["- Default Route", "- Masked Route", "- Dynamic Route", "- MAC"]) + "\n[+] Answer> ",
        "Which routing protocols build routing tables from information received from other routers in the Internetwork?" + randomloop(["- Static", "- Dynamic", "- Random", "- Closed"]) + "\n[+] Answer> ", 
        "Which routing protocols were developed to address some limitations of distance vector protocols?" + randomloop(["- Link-State", "- Routing Information", "- Border Gateway"]) + "\n[+] Answer> ",
        "Routes of unknown origin have an AD of what?" + randomloop(["- 0", "- 100", "- 210", "- 255"]) + "\n[+] Answer> ",
        "Connected Interfaces have an AD of what?" + randomloop(["- 0", "- 100", "- 210", "- 255"]) + "\n[+] Answer> ",
        "Static routes have an AD of what?" + randomloop(["- 0", "- 1", "- 5", "- 200"]) + "\n[+] Answer> ",
        "External BGP routes have an AD of what?" + randomloop(["- 20", "- 90", "- 115", "- 255"]) + "\n[+] Answer> ",
        "Internal EIGRP routes have an AD of what?" + randomloop(["- 20", "- 90", "- 115", "- 255"]) + "\n[+] Answer> ",
        "Which EGP (exterior gateway protocol) uses Path-Vector?" + randomloop(["- BGP", "- EIGRP", "- IGRP", "- RIP", "- OSPF"]) + "\n[+] Answer> ",
        "Which routing protocol has an AD of 200?" + randomloop(["- Interal BGP", "- EIGRP", "- IGRP", "- RIP", "- OSPF"]) + "\n[+] Answer> ",    
    ]

    routing_questions = [
        Question(routing_question_prompts[0], "BGP"),
        Question(routing_question_prompts[1], "BGP"),
        Question(routing_question_prompts[2], "EIGRP"),
        Question(routing_question_prompts[3], "RIP"),
        Question(routing_question_prompts[4], "OSPF"),
        Question(routing_question_prompts[5], "EIGRP"),
        Question(routing_question_prompts[6], "IGRP"),
        Question(routing_question_prompts[7], "RIP"),
        Question(routing_question_prompts[8], "OSPF"),
        Question(routing_question_prompts[9], "ARP"),
        Question(routing_question_prompts[10], "Network"),
        Question(routing_question_prompts[11], "Routing"),
        Question(routing_question_prompts[12], "Static"),
        Question(routing_question_prompts[13], "Router"),
        Question(routing_question_prompts[14], "Low"),
        Question(routing_question_prompts[15], "Default Route"),
        Question(routing_question_prompts[16], "Dynamic"),
        Question(routing_question_prompts[17], "Link-State"),
        Question(routing_question_prompts[18], "255"),
        Question(routing_question_prompts[19], "0"),
        Question(routing_question_prompts[20], "1"),
        Question(routing_question_prompts[21], "20"),
        Question(routing_question_prompts[22], "90"),
        Question(routing_question_prompts[23], "BGP"),
        Question(routing_question_prompts[24], "Internal BGP"),
    ]
    linux_file_question_prompts = [
        "In linux this is the actual owner of the file or directory, also known as the user?" + randomloop(["- Owner", "- Group", "- Other"]) + "\n[+] Answer> ", 
        "For linux files what does the permission 'r' mean?" + randomloop(["- Read", "- Write", "- Execute"]) + "\n[+] Answer> ",
        "For linux files what does the permission 'w' mean?" + randomloop(["- Read", "- Write", "- Execute"]) + "\n[+] Answer> ",
        "For linux files what does the permission 'x' mean?" + randomloop(["- Read", "- Write", "- Execute"]) + "\n[+] Answer> ",
        "For linux directories what permission do you have if you can view the contents of the directory?" + randomloop(["- r", "- w", "- x"]) + "\n[+] Answer> ", 
        "For linux directories what permission do you have if you can create or delete files or remove sub-directories within that parent directory?" + randomloop(["- r", "- w", "- x"]) + "\n[+] Answer> ",
        "For linux directories what permission do you have if you change into a directory using cd?" + randomloop(["- r", "- w", "- x"]) + "\n[+] Answer> ",
        "Who has read and write permission for a file with these permissions? (rw-------)" + randomloop(["- Owner", "- Group", "- Other"]) + "\n[+] Answer> ",
        "What permissions do other users have on a file with these permissions? (rwxrw-r--)" + "\n[+] Answer> ", 
        "What command do you use to set permissions for files and directories?" + "\n[+] Answer> ",
        "A file with 777 set as its permissions allows which users to read, write, and execute?" + randomloop(["- All", "- User and Group", "- User only", "- Group and Other"]) + "\n[+] Answer> ",
        #"What ?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ",
        #"What ?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ", 
        #"What ?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ",
        
    ]
    linux_file_questions = [
        Question(linux_file_question_prompts[0], "Owner"),
        Question(linux_file_question_prompts[1], "Read"),
        Question(linux_file_question_prompts[2], "Write"),
        Question(linux_file_question_prompts[3], "Execute"),
        Question(linux_file_question_prompts[4], "r"),
        Question(linux_file_question_prompts[5], "w"),
        Question(linux_file_question_prompts[6], "x"),
        Question(linux_file_question_prompts[7], "owner"),
        Question(linux_file_question_prompts[8], "read"),
        Question(linux_file_question_prompts[9], "chmod"),
        Question(linux_file_question_prompts[10], "All"),
        #Question(linux_file_question_prompts[11], ""),
        #Question(linux_file_question_prompts[12], ""),
        #Question(linux_file_question_prompts[13], ""),
      
    ]
    number_conv_question_prompts = [
        "What is binary " + rlist[0] + " in base 10?" + "\n[+] Answer> ",
        "What is hex " + rlist[1] + " in base 10" + "\n[+] Answer> ",
        "What is oct " + rlist[2] + " in base 10" + "\n[+] Answer> ",
        "What is dec " + str(rlist[3]) + " in base 2" + "\n[+] Answer> ",
        "What is dec " + str(rlist[4]) + " in base 8" + "\n[+] Answer> ",
        "What is dec " + str(rlist[5]) + " in base 16" + "\n[+] Answer> ",
    ]

    number_conv_questions = [
        Question(number_conv_question_prompts[0], (str(int(rlist[0], 2)))),
        Question(number_conv_question_prompts[1], (str(int(rlist[1], 16)))),
        Question(number_conv_question_prompts[2], (str(int(rlist[2], 8)))),
        Question(number_conv_question_prompts[3], (str(bin(rlist[3])[2:]))),
        Question(number_conv_question_prompts[4], (str(oct(rlist[4])[2:]))),
        Question(number_conv_question_prompts[5], (str(hex(rlist[5])[2:])))
        
    ]
    networking_commands_prompts = [
        "The ________ utility uses ICMP to send messages and then uses the returning ICMP \nTime Exceeded (Time to Live) error messages to identify routers from source to destination." + "\n[+] Answer> ",
        "Two commonly used options when using ping on a Microsoft Windows host are __ (ping\nspecified host until stopped)and __<####>(specify size of ping packet)." + randomloop(["-t -l", "-c -s", "-h -s"]) + "\n[+] Answer> ",
        "Two commonly used options when using ping on a *Nix host are __ (stop after sending\n'count' Echo packets)and __<####>(specify the number of data bytes to be sent)." + randomloop(["-t -l", "-c -s", "-h -s"]) + "\n[+] Answer> ",
        "What would you type on a *Nix machine to use the traceroute utility, followed by the\nIP address or hostname?" + "\n[+] Answer> ", 
        "What would you type on a Windows machine to use the traceroute utility, followed by \nthe IP address or hostname?" + "\n[+] Answer> ", 
        "When using traceroute to troubleshoot a network problem by IP address only, use the\n_____ option as it does not resolve IP addresses to hostnames." + randomloop(["- -d", "- -h", "- -e", "- -r"]) + "\n[+] Answer> ", 
        "UNIX uses ICMP for ping but ____ for traceroute" + randomloop(["- TCP", "- UDP", "- DNS", "- HTTP"]) + "\n[+] Answer> ",
        "On Windows systems, IP configurations are displayed using the ________ command?" + "\n[+] Answer> ", 
        "On UNIX-based systems, IP configurations are displayed using the ________ command?" + "\n[+] Answer> ",
        "Using ________, an administrator can set up, maintain, and view the tables of IPv4 \npacket filter rules in the Linux kernel?" + "\n[+] Answer> ", 
        "Which iptables flag will list rules added in verbose mode?" + randomloop(["- -L", "- -F", "- -D", "- -p"]) + "\n[+] Answer> ",
        "Which iptables flag will flush all existing rules?" + randomloop(["- -F", "- -P", "- -j", "- -D"]) + "\n[+] Answer> ",
        "Which iptables flag will set the default policy on the specified chain?" + randomloop(["- -P", "- -D", "- -A", "- -L"]) + "\n[+] Answer> ",
        "Which iptables flag will append or add a rule to a specific chain?" + randomloop(["- -A", "- -j", "- -i", "- -p"]) + "\n[+] Answer> ",
        "Which iptables flag will jump to the target of the rule?" + randomloop(["- -j", "- -i", "- -L", "- -F"]) + "\n[+] Answer> ",
        "Which iptables flag will call out a specific interface?" + randomloop(["- -i", "- -j", "- -c", "- -p"]) + "\n[+] Answer> ",
        "Which iptables flag will delete a rule?" + randomloop(["- -D", "- -L", "- -j", "- -p"]) + "\n[+] Answer> ",
        "Which iptables flag will call for a specific protocol?" + randomloop(["- -D", "- -L", "- -j", "- -p"]) + "\n[+] Answer> ",
        #"What ?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ", 
        #"What ?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ",
    ]
    networking_commands_questions = [
        Question(networking_commands_prompts[0], "traceroute"),
        Question(networking_commands_prompts[1], "-t -l"),
        Question(networking_commands_prompts[2], "-c -s"),
        Question(networking_commands_prompts[3], "traceroute"),
        Question(networking_commands_prompts[4], "tracert"),
        Question(networking_commands_prompts[5], "-d"),
        Question(networking_commands_prompts[6], "UDP"),
        Question(networking_commands_prompts[7], "ipconfig"),
        Question(networking_commands_prompts[8], "ifconfig"),
        Question(networking_commands_prompts[9], "IPtables"),
        Question(networking_commands_prompts[10], "-L"),
        Question(networking_commands_prompts[11], "-F"),
        Question(networking_commands_prompts[12], "-P"),
        Question(networking_commands_prompts[13], "-A"),
        Question(networking_commands_prompts[14], "-j"),
        Question(networking_commands_prompts[15], "-i"),
        Question(networking_commands_prompts[16], "-D"),
        Question(networking_commands_prompts[17], "-p"),
        #Question(networking_commands_prompts[18], ""),
    ]

    security_prompts = [
        "_______ is a Linux host-based IDS used to monitor and send alerts on identified \nfilesystem changes." + "\n[+] Answer> ", 
        "Tripwire scans the file system as instructed by the configuration file, \n/etc/tripwire/______?" + "\n[+] Answer> ",
        "Tripwire scans the file system with policies set forth in /etc/tripwire/_____?" + "\n[+] Answer> ", 
        "What is hardware and/or software that protects computers and networks from external \nattacks by regulating internet traffic?" + randomloop(["- Firewall", "- IDS", "- DoS", "- DDoS"]) + "\n[+] Answer> ",
        "Which type of firewall is a software application or suit of applications installed on \na single computer?" + randomloop(["- Host Based", "- Network Based"]) + "\n[+] Answer> ", 
        "Which type of firewall functions on the network level, filters data as it travels from \nthe internet to computers on the network, and operates with a set of data management rules \nthat apply to the entire network?" + randomloop(["- Host Based", "- Network Based"]) + "\n[+] Answer> ",
        "What is a security tool used to monitor, detect, and respond to unauthorized activity \nand anomalies to detect possible intrusions?" + randomloop(["- Firewall", "- IDS", "- DoS", "- DDoS"]) + "\n[+] Answer> ", 
        "Which type of IDS collects and analyzes data that originates on a computer that hosts \na service, such as a web server?" + randomloop(["- Host Based", "- Network Based"]) + "\n[+] Answer> ",
        "Which type of IDS analyzes data packets that travel over the actual network to verify \ntheir nature as malicious or benign, and is effective in detecting unauthorized \noutsider access and bandwidth theft/DOS?" + randomloop(["- Host Based", "- Network Based"]) + "\n[+] Answer> ", 
        "Network ________ is the protection of the network devices, data, and users." + "\n[+] Answer> ",
        "A network ______ is defined as something that has the potential to damage the network,\nto include data, hosts, or users." + "\n[+] Answer> ", 
        "Hardware failures, access, malware, social engineering, and denial of service, are some\nthe the most common network _______." + "\n[+] Answer> ",
        "To help mitigate hardware failures and continue to provide access, _______ must be \nmaintained?" + randomloop(["- Redundancy", "- Staffing", "- Available Stock", "- Training"]) + "\n[+] Answer> ", 
        "Entry into an area, device, or the ability to retrieve data is called ______." + "\n[+] Answer> ",
        "In the network security realm, access is divided into two main types: physical and ________?" + "\n[+] Answer> ", 
        "Which form of access should be protected through the use of locking cabinets, doors, \nand buildings; or using security guards, cameras and safes?" + randomloop(["- Physical", "- Logical", "- Remote"]) + "\n[+] Answer> ",
        "Which form of access protects data by means of passwords, permissions, access control \nlists, and traffic filtering with devices such as firewalls?" + randomloop(["- Physical", "- Logical", "- Remote"]) + "\n[+] Answer> ", 
        "Which form of access is non-local, logical access to network systems or resources from \na separate physical location?" + randomloop(["- Physical", "- Logical", "- Remote"]) + "\n[+] Answer> ",
        "What is any program or code designed to disrupt or deny operations, gain unauthorized \naccess to system resources, or otherwise exhibits abusive behavior?" + "\n[+] Answer> ",
        "Which form of malware is a program or piece of code that replicates itself and spreads \nnormally from user interaction, but not across networks?" + randomloop(["- Virus", "- Worm", "- Macro", "- Trojan", "- Rootkit", "- Adware/Spyware"]) + "\n[+] Answer> ",
        "Which form of malware is very similar in function to a virus but has the ability to \nreplicate itself across networks, and does not require another program or a user to spread?" + randomloop(["- Virus", "- Worm", "- Macro", "- Trojan", "- Rootkit", "- Adware/Spyware"]) + "\n[+] Answer> ",
        "Which form of malware exploits a program's built-in macro function, with malicious \nresults?" + randomloop(["- Virus", "- Worm", "- Macro", "- Trojan", "- Rootkit", "- Adware/Spyware"]) + "\n[+] Answer> ",
        "Which form of malware looks legitimate to a user but performs malicious functions in \nthe background such as keystroke logging or opening ports?" + randomloop(["- Virus", "- Worm", "- Macro", "- Trojan", "- Rootkit", "- Adware/Spyware"]) + "\n[+] Answer> ",
        "Which form of malware is a Trojan that uses low level computing functions to hide \nthemselves from anti-malware tools?" + randomloop(["- Virus", "- Worm", "- Macro", "- Trojan", "- Rootkit", "- Adware/Spyware"]) + "\n[+] Answer> ",
        "This is different from traditional malware in that it does not execute destructive \nfunctions on the systems?" + randomloop(["- Virus", "- Worm", "- Macro", "- Trojan", "- Rootkit", "- Adware/Spyware"]) + "\n[+] Answer> ",
        "What is the process of exploiting human behavior to gain unauthorized access to \ninformation?" + "\n[+] Answer> ",
        "What popular form of social engineering is an information gathering technique to obtain\nsensitive personal information through a fraudulent solicitation in an email or on a web\nsite, in which the perpetrator masquerades as a legitimate business \nor reputable person?" + "\n[+] Answer> ",
        "A ______ ________ _______ attack involves an adversary flooding a targeted network with\ntraffic until the network is unable to respond \nor possibly even crashes?" + "\n[+] Answer> ",
        "This other form of DoS, a _________ _________ __________ __________, overwhelms a \nsystem like a DoS but through multiple source computers?" + "\n[+] Answer> ",

    ]
    security_questions = [
        Question(security_prompts[0], "tripwire"),
        Question(security_prompts[1], "tw.cfg"),
        Question(security_prompts[2], "tw.pol"),
        Question(security_prompts[3], "Firewall"),
        Question(security_prompts[4], "Host Based"),
        Question(security_prompts[5], "Network Based"),
        Question(security_prompts[6], "IDS"),
        Question(security_prompts[7], "Host Based"),
        Question(security_prompts[8], "Network Based"),
        Question(security_prompts[9], "security"),
        Question(security_prompts[10], "threat"),
        Question(security_prompts[11], "threats"),
        Question(security_prompts[12], "Redundancy"),
        Question(security_prompts[13], "access"),
        Question(security_prompts[14], "logical"),
        Question(security_prompts[15], "Physical"),
        Question(security_prompts[16], "Logical"),
        Question(security_prompts[17], "Remote"),
        Question(security_prompts[18], "malware"),
        Question(security_prompts[19], "Virus"),
        Question(security_prompts[20], "Worm"),
        Question(security_prompts[21], "Macro"),
        Question(security_prompts[22], "Trojan"),
        Question(security_prompts[23], "Rootkit"),
        Question(security_prompts[24], "Adware/Spyware"),
        Question(security_prompts[25], "Social Engineering"),
        Question(security_prompts[26], "phishing"),
        Question(security_prompts[27], "denial of service"),
        Question(security_prompts[28], "distributed denial of service"),
    ]

    subnetting_prompts = [
        #"What is the first host on this subnet? 192.168.20.12 /26 (###.###.###.###)" + "\n[+] Answer> ", 
        #"What is the last host on this subnet? 210.15.0.32 /20 (###.###.###.###)" + "\n[+] Answer> ", 
        #"What is the subnet mask for a /20" + "\n[+] Answer> ", 
        #"What is the broadcast IP for this subnet? 142.176.99.219 /22 (###.###.###.###)" + "\n[+] Answer> ",
        "What is the first host of the subnet that this IP address belongs to: " + iplist[0] + "\n[+] Answer> ", 
        "What is the last host of the subnet that this IP address belongs to: " + iplist[1] + "\n[+] Answer> ",
        "What is the network address of this IP address: " + iplist[2] + "\n[+] Answer> ",
        "What is the broadcast address of the subnet that this IP address belongs to: " + iplist[3] + "\n[+] Answer> ",
        "What is the netmask of this IP address: " + iplist[4] + "\n[+] Answer> ",  

    ]
    subnetting_questions = [
        Question(subnetting_prompts[0], str(ipaddress.IPv4Network((ipaddress.IPv4Interface(iplist[0])).network)[1])),
        Question(subnetting_prompts[1], str(ipaddress.IPv4Network((ipaddress.IPv4Interface(iplist[1])).network)[-2])),
        Question(subnetting_prompts[2], str((ipaddress.IPv4Interface(iplist[2])).network)[:-3]),
        Question(subnetting_prompts[3], str((ipaddress.IPv4Network((ipaddress.IPv4Interface(iplist[3])).network)).broadcast_address)),
        Question(subnetting_prompts[4], str((ipaddress.IPv4Interface(iplist[4])).netmask)),
        #Question(subnetting_prompts[5], ""),
    ]

    tcp_ip_prompts = [ 
        #"?" + "\n[+] Answer> ", 
        #"What?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ",
        "What is 'layer 1' of the TCP/IP stack?" + randomloop(["- Network Interface", "- Internet", "- Transport", "- Application"]) + "\n[+] Answer> ",
        "What is 'layer 2' of the TCP/IP stack?" + randomloop(["- Network Interface", "- Internet", "- Transport", "- Application"]) + "\n[+] Answer> ",
        "What is 'layer 3' of the TCP/IP stack?" + randomloop(["- Network Interface", "- Internet", "- Transport", "- Application"]) + "\n[+] Answer> ",
        "What is 'layer 4' of the TCP/IP stack?" + randomloop(["- Network Interface", "- Internet", "- Transport", "- Application"]) + "\n[+] Answer> ",
        "On a TCP/IP network, each device (computer, router, or other device) with a\nconnection to the network is referred to as a _____?" + "\n[+] Answer> ",
        "TCP/IP services primarily operate in the _____/_____ model?" + randomloop(["- client/server", "- server/client", "- client/client", "- server/server"]) + "\n[+] Answer> ", 
        "TCP/IP is a routed network protocol, which means that it is easy to pass data\nbetween two or more _____ or across _____ links?" + randomloop(["- LANs WAN", "- PANs LAN", "- CANs WAN"]) + "\n[+] Answer> ",
        "All TCP/IP traffic gets encapsulated into a ________?" + "\n[+] Answer> ", 
        "Which layer of the TCP/IP stack do NICs/repeaters/hubs/switches work at?" + randomloop(["- Network Interface", "- Internet", "- Transport", "- Application"]) + "\n[+] Answer> ",
        "Which layer of the TCP/IP stack do routers/ARP/RARP/ICMP work at?" + randomloop(["- Network Interface", "- Internet", "- Transport", "- Application"]) + "\n[+] Answer> ",
        "______ is the reverse of ARP in that the host knows its physical address but does\nnot have an IP address?(XXXX)" + "\n[+] Answer> ",
        "TCP/IP uses _____ Version II as its frame format?" + "\n[+] Answer> ",
        "A ______ domain is another name for a TCP/IP networks?" + "\n[+] Answer> ", 
        "TCP/IP use what form of multiplexing to allow it and other services that are user\nand implementation dependent to arrive at the network interface on the same physical\nconnection?" + randomloop(["- ports", "- MAC addresses", "- IP Addresses"]) + "\n[+] Answer> ", 
        "What is a binary TCP/IP Application Layer protocol that allows a user to establish\na virtual connection with another host?" + "\n[+] Answer> ",
        "What is a UNIX software utility often used as an alternative to telnet which allows\na user on a UNIX host to log in to another UNIX host over a TCP/IP internetwork?" + "\n[+] Answer> ",
        "Which layer of the TCP/IP stack has it's data encapsulated like: |Frame Header|Frame Data|Frame Footer|" + randomloop(["- Network Interface", "- Internet", "- Transport", "- Application"]) + "\n[+] Answer> ",
        "Which layer of the TCP/IP stack has it's data encapsulated like: |IP Header|IP Data|" + randomloop(["- Network Interface", "- Internet", "- Transport", "- Application"]) + "\n[+] Answer> ",
        "Which layer of the TCP/IP stack has it's data encapsulated like: |UDP Header|UDP Data|" + randomloop(["- Network Interface", "- Internet", "- Transport", "- Application"]) + "\n[+] Answer> ",
        "Which layer of the TCP/IP stack has it's data encapsulated like: |Data|" + randomloop(["- Network Interface", "- Internet", "- Transport", "- Application"]) + "\n[+] Answer> ",
    ]
    
    tcp_ip_questions = [
        #Question(tcp_ip_prompts[], ""),
        Question(tcp_ip_prompts[0], "Network Interface"),
        Question(tcp_ip_prompts[1], "Internet"),
        Question(tcp_ip_prompts[2], "Transport"),
        Question(tcp_ip_prompts[3], "Application"),
        Question(tcp_ip_prompts[4], "host"),
        Question(tcp_ip_prompts[5], "client/server"),
        Question(tcp_ip_prompts[6], "LANs WAN"),
        Question(tcp_ip_prompts[7], "Frame"),
        Question(tcp_ip_prompts[8], "Network Interface"),
        Question(tcp_ip_prompts[9], "Internet"),
        Question(tcp_ip_prompts[10], "RARP"),
        Question(tcp_ip_prompts[11], "DIX"),
        Question(tcp_ip_prompts[12], "Broadcast"),
        Question(tcp_ip_prompts[13], "Ports"),
        Question(tcp_ip_prompts[14], "Telnet"),
        Question(tcp_ip_prompts[15], "Rlogin"),
        Question(tcp_ip_prompts[16], "Network Interface"),
        Question(tcp_ip_prompts[17], "Internet"),
        Question(tcp_ip_prompts[18], "Transport"),
        Question(tcp_ip_prompts[19], "Application"),
    ]
    more_ports_prompts = [
        #"What service runs on TCP port ?" + randomloop(["- ", "-  ", "-   ", "- "]) + "\n[+] Answer> ",
        "What is the range of well known ports?" + randomloop(["- 0-1023", "- 1024-49151", "- 49152-65535"]) + "\n[+] Answer> ",
        "What is the range of registered ports?" + randomloop(["- 0-1023", "- 1024-49151", "- 49152-65535"]) + "\n[+] Answer> ",
        "What is the range of private ports?" + randomloop(["- 0-1023", "- 1024-49151", "- 49152-65535"]) + "\n[+] Answer> ",
        "What service runs on TCP port 443?" + randomloop(["- HTTPS", "- RDP", "- SMB", "- HTTP"]) + "\n[+] Answer> ",
        "What service runs on TCP port 23?" + randomloop(["- Telnet", "- FTP Control", "- FTP Data Transfer", "- SSH"]) + "\n[+] Answer> ",
        "What service runs on UDP port 69?" + randomloop(["- TFTP", "- DHCP", "- SMB", "- SSH"]) + "\n[+] Answer> ",
        "What service runs on TCP port 513?" + randomloop(["- Rlogin", "- SMB", "- SSH", "- SUNRPC"]) + "\n[+] Answer> ",
        "What service runs on TCP port 22?" + randomloop(["- SSH", "- Telnet", "- FTP Control", "- BOOTP"]) + "\n[+] Answer> ",
        """What exchange is missing in both rows below for this SSH Diffie Helman exchange? \n
        CLIENT                       SERVER
         RHP                         TCP22 
        ----------------SYN--------------->
        <-------------SYN/ACK--------------
        ----------------ACK--------------->
        <-----SSH Version Supported--------
        ------SSH Version Supported------->
        ----                           --->
        <---                           ----
        ------Asymmetric Key Exchange----->
        <-----Asymmetric Key Exchange------\n""" + "\n[+] Answer> ",
        "What service runs on UDP ports 1812 and 1813?" + randomloop(["- RADIUS", "- TACACS+", "- HTTPS", "- SMB"]) + "\n[+] Answer> ",
        "What service runs on UDP ports 1645 and 1646?" + randomloop(["- RADIUS", "- TACACS+", "- HTTPS", "- SMB"]) + "\n[+] Answer> ",
        "What service runs on TCP port 49?" + randomloop(["- TACACS+", "- RDP", "- IMAP", "- SSH"]) + "\n[+] Answer> ",
        "What service runs on TCP port 53?" + randomloop(["- DNS", "- TFTP", "- HTTP", "- POP3"]) + "\n[+] Answer> ",
        
    ]
    more_ports_questions = [
        #Question(more_ports_prompts[], ""),
        Question(more_ports_prompts[0], "0-1023"),
        Question(more_ports_prompts[1], "1024-49151"),
        Question(more_ports_prompts[2], "49152-65535"),
        Question(more_ports_prompts[3], "HTTPS"),
        Question(more_ports_prompts[4], "Telnet"),
        Question(more_ports_prompts[5], "TFTP"),
        Question(more_ports_prompts[6], "Rlogin"),
        Question(more_ports_prompts[7], "SSH"),
        Question(more_ports_prompts[8], "Diffie Hellman Key Exchange"),
        Question(more_ports_prompts[9], "RADIUS"),
        Question(more_ports_prompts[10], "RADIUS"),
        Question(more_ports_prompts[11], "TACACS+"),
        Question(more_ports_prompts[12], "DNS"),
        #Question(more_ports_prompts[13], ""),
        #Question(more_ports_prompts[14], ""),

    ]
    practical_prompts = [
 #======================================================================================
        """Given the below netstat output what address has established a Telnet connection with your local computer? (###.###.###.###)

    C:\\>netstat -an
    Proto       Local Address      Foreign Address         State
    TCP         0.0.0.0:135        0.0.0.0:0               LISTENING
    TCP         0.0.0.0:445        0.0.0.0:0               LISTENING
    TCP         200.51.61.4:23     109.54.23.88:3477       ESTABLISHED
    TCP         200.51.61.4:25     0.0.0.0:0               LISTENING
    TCP         200.51.61.4:4015   178.53.200.64:80        ESTABLISHED
    UDP         200.51.61.4:69     *.*                                 \n""" + "\n[+] Answer> ",
 #======================================================================================
        """Given the below netstat output which IP address is the client? (###.###.###.###)

    C:\\>netstat -an
    Proto       Local Address      Foreign Address         State
    TCP         200.51.61.4:23     109.54.23.88:3477       ESTABLISHED\n""" + "\n[+] Answer> ",
#======================================================================================
        """Given the below ping, what opperating system is being used?
- *Nix 
- Windows 
- Solaris

    C:\\>ping 178.54.16.85

    Pinging 178.54.16.85 with 32 bytes of data:
    Reply from 178.54.16.85: bytes=32 time=2ms TTL=128
    Reply from 178.54.16.85: bytes=32 time=2ms TTL=128
    Reply from 178.54.16.85: bytes=32 time=2ms TTL=128
    Reply from 178.54.16.85: bytes=32 time=2ms TTL=128

    Ping statistics for 178.54.16.85:
        Packets: Sent = 1, Recieved = 1, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 2ms, Maximum = 2ms, Average = 2ms\n""" + "\n[+] Answer> ",
#======================================================================================
        """Given the below ping, what opperating system is being used?
- *Nix 
- Windows 
- Solaris

    C:\\>ping 10.212.16.102

    Pinging 10.212.16.102 with 32 bytes of data:
    Reply from 10.212.16.102: bytes=32 time=2ms TTL=64
    Reply from 10.212.16.102: bytes=32 time=2ms TTL=64
    Reply from 10.212.16.102: bytes=32 time=2ms TTL=64
    Reply from 10.212.16.102: bytes=32 time=2ms TTL=64

    Ping statistics for 178.54.16.85:
        Packets: Sent = 1, Recieved = 1, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 2ms, Maximum = 2ms, Average = 2ms\n""" + "\n[+] Answer> ",
#======================================================================================
        """Given the below ping, what opperating system is being used?
- *Nix 
- Windows 
- Solaris

    C:\\>ping 10.212.16.102

    Pinging 10.212.16.102 with 32 bytes of data:
    Reply from 10.212.16.102: bytes=32 time=2ms TTL=254
    Reply from 10.212.16.102: bytes=32 time=2ms TTL=254
    Reply from 10.212.16.102: bytes=32 time=2ms TTL=254
    Reply from 10.212.16.102: bytes=32 time=2ms TTL=254

    Ping statistics for 178.54.16.85:
        Packets: Sent = 1, Recieved = 1, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 2ms, Maximum = 2ms, Average = 2ms\n""" + "\n[+] Answer> ",
#========================================================================================
        """In order, what is missing from the below IPv4 Header: (XXXXX, XXXXX)
╔═════════╦════════╦════════════╦════════╦════╦═══════╦══════════╦═════╦══════════╦══════════╦════════╦══════╗
║   IP    ║ Header ║  Priority  ║        ║    ║       ║ Fragment ║     ║          ║          ║ Source ║ Dest ║              
║         ║        ║  and type  ║        ║ ID ║ Flags ║          ║ TTL ║ Protocol ║          ║        ║      ║
║ Version ║ Length ║ of service ║        ║    ║       ║  Offset  ║     ║          ║          ║   IP   ║  IP  ║                        
╚═════════╩════════╩════════════╩════════╩════╩═══════╩══════════╩═════╩══════════╩══════════╩════════╩══════╝\n""" + "\n[+] Answer> ",
    #========================================================================================
        """The host computer is sending out a multicast packet. This multicast packet has the
following addresses:

    FF02::1 All Nodes Address
    FF01::2 All Routers Address
    
Which of the following devices will process this packet?(XXXX #, XXXX #)

                            ╔══════╗
                            ║ PC:1 ║
                           ╔╚══════╝╗
              Router 1     ╚════════╝      Router 2   
            ╔═════════╗        |         ╔═════════╗                      
            ║    ↑    ║        |         ║    ↑    ║
            ║   ← →   ║\       |        /║   ← →   ║
            ║    ↓    ║ \      |       / ║    ↓    ║
            ╚═════════╝  \   Switch   /  ╚═════════╝
                          \ ╔══════╗ /
                           \║   -→ ║/
                           /║  ←-  ║\\
                          / ╚══════╝ \\
             ╔══════╗    /     |      \   ╔══════╗
             ║ PC:2 ║   /      |       \  ║ PC:3 ║
            ╔╚══════╝╗ /       |        \╔╚══════╝╗
            ╚════════╝         |         ╚════════╝ 
                        ┌──────↑───┐ 
                        │TO:FF02::2│
                        └──────────┘
                            ╔══↑═══╗ 
                            ║ Host ║
                           ╔╚══════╝╗
                           ╚════════╝\n""" + "\n[+] Answer> ",
#========================================================================================
        """From left to right how many bits can be in each section of an IPv4 Header?(#, #, # etc.)

    4          4         8         ___     16    ___       13       8       8         ___       32       __
╔═════════╦════════╦════════════╦════════╦════╦═══════╦══════════╦═════╦══════════╦══════════╦════════╦══════╗
║   IP    ║ Header ║  Priority  ║ Total  ║    ║       ║ Fragment ║     ║          ║  Header  ║ Source ║ Dest ║              
║         ║        ║  and type  ║        ║ ID ║ Flags ║          ║ TTL ║ Protocol ║          ║        ║      ║
║ Version ║ Length ║ of service ║ Length ║    ║       ║  Offset  ║     ║          ║ Checksum ║   IP   ║  IP  ║                        
╚═════════╩════════╩════════════╩════════╩════╩═══════╩══════════╩═════╩══════════╩══════════╩════════╩══════╝\n""" + "\n[+] Answer> ",
#========================================================================================
        """From left to right how many bytes can be in each section of an Ethernet Header?(#, #, # etc.)

    ___        6          2
╔═════════╦═════════╦═══════════╗
║  Dest   ║  Source ║  Protocol ║              
║   MAC   ║   MAC   ║    Type   ║                        
╚═════════╩═════════╩═══════════╝\n""" + "\n[+] Answer> ",
#========================================================================================
        """From left to right how many bits can be in each section of a TCP Header?(#, #, # etc.)

    ___       16        32          ___       4         6        6     ___    16         16        16
╔═════════╦════════╦════════════╦═════════╦════════╦══════════╦══════╦═════╦════════╦══════════╦════════╗
║ Source  ║ Target ║   Source   ║ ACK Seq ║ Header ║          ║ Code ║     ║ Sender ║   TCP    ║ Urgent ║              
║         ║        ║            ║         ║        ║ Reserved ║      ║ TTL ║ Window ║          ║  Data  ║
║   Port  ║  Port  ║ Sequence # ║    #    ║ Length ║          ║ Bits ║     ║  Size  ║ Checksum ║  Size  ║                       
╚═════════╩════════╩════════════╩═════════╩════════╩══════════╩══════╩═════╩════════╩══════════╩════════╝\n""" + "\n[+] Answer> ",
#========================================================================================
        """From left to right how many bits can be in each section of an UPD Header?(#, #, # etc.)

     16       ___       ___       16
╔═════════╦═════════╦════════╦══════════╗
║  Source ║  Dest   ║ Length ║ Checksum ║            
║  Port   ║  Port   ║        ║          ║             
╚═════════╩═════════╩════════╩══════════╝\n""" + "\n[+] Answer> ",                
    ]
    practical_questions = [
        Question(practical_prompts[0], "109.54.23.88"),
        Question(practical_prompts[1], "109.54.23.88"),
        Question(practical_prompts[2], "Windows"),
        Question(practical_prompts[3], "*Nix"),
        Question(practical_prompts[4], "Solaris"),
        Question(practical_prompts[5], "Total Length, Header Checksum"),
        Question(practical_prompts[6], "Router 1, Router 2"),
        Question(practical_prompts[7], "16, 3, 16, 32"),
        Question(practical_prompts[8], "6"),
        Question(practical_prompts[9], "16, 32, 16"),
        Question(practical_prompts[10], "16, 16"),
        #Question(practical_prompts[11], ""),
        #Question(practical_prompts[12], ""),
        #Question(practical_prompts[13], ""),
        #Question(practical_prompts[14], ""),
        #Question(practical_prompts[15], ""),
        #Question(practical_prompts[16], ""),
    ]

    more_networking_prompts = [
        #"?" + "\n[+] Answer> ", 
        #"What?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ",
        "What is it called when communications occur in only one direction?" + randomloop(["- Simplex", "- Half-Duplex", "- Full-duplex"]) + "\n[+] Answer> ",
        "What is it called when communications occur in two directions but not at the same time?" + randomloop(["- Simplex", "- Half-Duplex", "- Full-duplex"]) + "\n[+] Answer> ",
        "What is it called when communications occur in two directions simultaneously?" + randomloop(["- Simplex", "- Half-Duplex", "- Full-duplex"]) + "\n[+] Answer> ",
        "Within the Data Link Layer which sub layer is an upper sub layer and handles error\nchecking and flow control between the sender and receiver across a network?" + randomloop(["- LLC", "- MAC"]) + "\n[+] Answer> ",
        "Within the Data Link Layer which sub layer is responsible for communicating with\n the Network Layer?" + randomloop(["- LLC", "- MAC"]) + "\n[+] Answer> ",
        "Within the Data Link Layer which sub layer is a lower sub layer that is responsible\nfor mapping between logical and physical addressing and access to the network media?" + randomloop(["- LLC", "- MAC"]) + "\n[+] Answer> ",
        "Which 802 standard deals with internetworking?" + randomloop(["- 802.1", "- 802.8", "- 802.11", "- 802.15.1"]) + "\n[+] Answer> ",
        "Which 802 standard deals with MANs?" + randomloop(["- 802.6", "- 802.8", "- 802.11", "- 802.12"]) + "\n[+] Answer> ",
        "Which 802 standard deals with Fiber Optic?" + randomloop(["- 802.8", "- 802.15", "- 802.11", "- 802.12"]) + "\n[+] Answer> ",
        "Which 802 standard deals with Wireless LAN?" + randomloop(["- 802.8", "- 802.15", "- 802.11", "- 802.12"]) + "\n[+] Answer> ",
        "Which 802 standard deals with Bluetooth?" + randomloop(["- 802.1", "- 802.8", "- 802.11", "- 802.15.1"]) + "\n[+] Answer> ",
        "Which 802 standard deals with Ethernet?" + randomloop(["- 802.3", "- 802.8", "- 802.11", "- 802.15.1"]) + "\n[+] Answer> ",
        "What is the world's most popular type of LAN defined by IEEE?" + "\n[+] Answer> ",
        """From left to right how many bytes max can be in each section of an Ethernet Frame?(#, #, # etc.)

    ╔══════════╦════════════╦══════════╦═════════╦═════════════╗
    ║ Dest MAC ║ Source MAC ║ Protocol ║  Data   ║ Frame Check ║  
    ║ Address  ║  Address   ║   Type   ║ Payload ║   Sequence  ║   
    ╚══════════╩════════════╩══════════╩═════════╩═════════════╝\n""" + "\n[+] Answer> ", 
        "C_________, I_________, Av_________, N_________, and Au_________ are the five pilars\nof Information Assurance(IA)?(Xxxxx, Xxxxx, etc.)" + "\n[+] Answer> ",
        "What is the principle of keeping information private and protected from unauthorized\naccess?" + randomloop(["- Confidentiality", "- Integrity", "- Availability"]) + "\n[+] Answer> ",
        "What is the principle of ensuring data is accurate and free of error or unauthorized\nmodification?" + randomloop(["- Confidentiality", "- Integrity", "- Availability"]) + "\n[+] Answer> ",
        "What is the principle of ensuring that systems operate continuously and that\nauthorized personnel access the data they need?" + randomloop(["- Confidentiality", "- Integrity", "- Availability"]) + "\n[+] Answer> ",
        "What is the analysis and practice of concealing information and securing sensitive data?" + "\n[+] Answer> ",
        "What is a form of one-way encryption where data of variable length is input to an\nalgorithm and a value of fixed length results are output?" + "\n[+] Answer> ",
        "What is a technique of providing confidentiality by converting plaintext into ciphertext?" + "\n[+] Answer> ",
        "Which type of encryption uses a single key to encrypt and decrypt the data, where\nboth the sender and receiver must have a copy of the same key?" + randomloop(["- Symmetric", "- Asymmetric"]) + "\n[+] Answer> ",
        "Which type of encryption uses a different key for encryption than decryption, this\nkey pair consists of both a private key and public key?" + randomloop(["- Symmetric", "- Asymmetric"]) + "\n[+] Answer> ",
        "What is the process of combining and transmitting multiple analog or digital signals\nvia a single transmission medium?" + "\n[+] Answer> ",
        "What is the process of combining analog or digital signals with each signal\nhaving its own timeslot to transmit or receive data via a single carrier?" + "\n[+] Answer> ",
        "What is the technology based on transmitting packets (blocks of data in frame format) via multiple paths at the same time?" + "\n[+] Answer> ",
        "What is the Parent Domain in the following url: www.mynet.work." + "\n[+] Answer> ",
        "What is the Top Level Domain in the following url: www.mynet.work." + "\n[+] Answer> ",
        "What is the Host in the following url: www.mynet.work." + "\n[+] Answer> ",

    ]
    more_networking_questions = [
        #Question(more_networking[], ""),
        Question(more_networking_prompts[0], "Simplex"),
        Question(more_networking_prompts[1], "Half-Duplex"),
        Question(more_networking_prompts[2], "Full-Duplex"),
        Question(more_networking_prompts[3], "LLC"),
        Question(more_networking_prompts[4], "LLC"),
        Question(more_networking_prompts[5], "MAC"),
        Question(more_networking_prompts[6], "802.1"),
        Question(more_networking_prompts[7], "802.6"),
        Question(more_networking_prompts[8], "802.8"),
        Question(more_networking_prompts[9], "802.11"),
        Question(more_networking_prompts[10], "802.15.1"),
        Question(more_networking_prompts[11], "802.3"),
        Question(more_networking_prompts[12], "Ethernet"),
        Question(more_networking_prompts[13], "6, 6, 2, 1500, 4"),
        Question(more_networking_prompts[14], "Confidentiality, Integrity, Availability, Nonrepudiation, Authentication"),
        Question(more_networking_prompts[15], "Confidentiality"),
        Question(more_networking_prompts[16], "Integrity"),
        Question(more_networking_prompts[17], "Availability"),
        Question(more_networking_prompts[18], "Cryptography"),
        Question(more_networking_prompts[19], "hashing"),
        Question(more_networking_prompts[20], "Encryption"),
        Question(more_networking_prompts[21], "Symmetric"),
        Question(more_networking_prompts[22], "Asymmetric"),
        Question(more_networking_prompts[23], "Multiplexing"),
        Question(more_networking_prompts[24], "Time Division Multiplexing"),
        Question(more_networking_prompts[25], "packet switching"),
        Question(more_networking_prompts[26], "mynet"),
        Question(more_networking_prompts[27], "work"),
        Question(more_networking_prompts[28], "www"),
        #Question(tcp_ip_prompts[29], ""),

    ]

    windows_filesys_prompts = [
        #"?" + "\n[+] Answer> ", 
        #"What?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ",
        "Which layer of the Windows file system contains the actual storage media itself\n(tape, metallic hard disk, solid stat transistors, etc)?" + randomloop(["- Physical", "- File System", "- Filename", "- Metadata", "- Data"]) + "\n[+] Answer> ",
        "Which layer of the Windows file system includes filesystem structure details such as\ncluster size (allocation size)?\n└►Boot Sector\n" + randomloop(["- Physical", "- File System", "- Filename", "- Metadata", "- Data"]) + "\n[+] Answer> ",
        "Which layer of the Windows file system includes file names map to metadata and user\ninterface with the file system?\n├►Root Directory\n└► MFT\n" + randomloop(["- Physical", "- File System", "- Filename", "- Metadata", "- Data"]) + "\n[+] Answer> ",
        "Which layer of the Windows file system includes file metadata containing pointers\nand other descriptors such as timestamps?\n├► FAT \n├► Root Directory\n└► MFT\n" + randomloop(["- Physical", "- File System", "- Filename", "- Metadata", "- Data"]) + "\n[+] Answer> ",
        "Which layer of the Windows file system is where file data can be stored and located?\n└► Data Area\n" + randomloop(["- Physical", "- File System", "- Filename", "- Metadata", "- Data"]) + "\n[+] Answer> ",
        "The _____ file system is the original file system used since the early days of DOS?" + "\n[+] Answer> ",
        """ Fill in the two blanks below for a FAT16 file system.(XXXXX, XXXXXX)
    ╔══╦═════════╦═════╦═════╦═══════════╦═══════════╦════════╗
    ║1.:Reserved ║ FAT ║ Fat ║ 2._____   ║ Data Area ║ Unused ║
    ║__:  Area   ║  #1 ║  #2 ║           ║           ║  Area  ║  
    ╚══╩═════════╩═════╩═════╩═══════════╩═══════════╩════════╝
        """ + "\n[+] Answer> ",
        """ Fill in the two blanks below for a FAT32 file system.(XXXXX, XXXXXX)
    ╔══╦═════════╦═════╦═════╦══════╦═══════╦═════════╦════════╗
    ║1.:Reserved ║ FAT ║ Fat ║ Data : 2.___ :  Data   ║ Unused ║
    ║__:  Area   ║  #1 ║  #2 ║ Area :       :  Area   ║  Area  ║  
    ╚══╩═════════╩═════╩═════╩══════╩═══════╩═════════╩════════╝
        """ + "\n[+] Answer> ",
        "What is part of the Reserved Area of the FAT file system, and identifies the\nstructural details for the FAT file systems?" + randomloop(["- Boot Record", "- FAT", "- Data Area", "- Root Directory"]) + "\n[+] Answer> ",
        "What is the allocation table that id's' cluster allocations for FAT file systems?" + randomloop(["- Boot Record", "- FAT", "- Data Area", "- Root Directory"]) + "\n[+] Answer> ",
        "What contains directory entries for all files and folders in the FAT file system?" + randomloop(["- Boot Record", "- FAT", "- Data Area", "- Root Directory"]) + "\n[+] Answer> ",
        "What stores the root directory and file data in the FAT file system?" + randomloop(["- Boot Record", "- FAT", "- Data Area", "- Root Directory"]) + "\n[+] Answer> ",
        "In the FAT16 files system, the root directory is located directly after ______." + randomloop(["- Boot Record", "- FAT #1", "- FAT #2", "- Data Area"]) + "\n[+] Answer> ",
        "In the FAT32 files system, the root directory is located in the ______, but not in a\ndefined location." + randomloop(["- Boot Record", "- FAT #1", "- FAT #2", "- Data Area"]) + "\n[+] Answer> ",
        "Which  FAT file system can allocate up to " +'2\u00b9'+'\u2076' + " clusters?" + randomloop(["- FAT16", "- FAT32"]) + "\n[+] Answer> ",
        "Which  FAT file system can allocate up to " +'2\u00b2'+'\u2078' + " clusters?" + randomloop(["- FAT16", "- FAT32"]) + "\n[+] Answer> ",
        "How does FAT16 mark bad clusters? 0x_______" + "\n[+] Answer> ",
        "How does FAT32 mark bad clusters? 0x_______" + "\n[+] Answer> ",
        "Every file on a FAT volume has a ___-byte directory entry containing info such as\nfilename, starting cluster address, size, file attributes." + "\n[+] Answer> ",
        "Filenames in FAT are stored in the directory entry using what naming convention?" + randomloop(["- 8.3", "- 6.3", "- 16.8", "- 2.2"]) + "\n[+] Answer> ",
        "In FAT, filenames that are longer than eight characters are ______." + "\n[+] Answer> ",
        "File attribute status is stored in the ____th byte of the directory entry in FAT?" + randomloop(["- 12", "- 8", "- 16", "- 10"]) + "\n[+] Answer> ",
        "The three main timestamps stored in the directory entry are created, ___, & written?" + "\n[+] Answer> ",
        "What are the master keys for Windows Registry?\n(Pick two seperated by a (,), in reverse alphabetical order)" + randomloop(["- HKEY_USERS", "- HKEY_LOCAL_MACHINE", "- HKEY_CLASSES_ROOT", "- HKEY_CURRENT_USER", "- HKEY_CURRENT_CONFIG"]) + "\n[+] Answer> ",
        "Which registry key contains a SID sub-key for all loaded user profiles?" + randomloop(["- HKEY_USERS", "- HKEY_LOCAL_MACHINE", "- HKEY_CLASSES_ROOT", "- HKEY_CURRENT_USER", "- HKEY_CURRENT_CONFIG"]) + "\n[+] Answer> ",
        "Which registry key contains specific information about the hardware, software, and preferences for all users who log into the system?" + randomloop(["- HKEY_USERS", "- HKEY_LOCAL_MACHINE", "- HKEY_CLASSES_ROOT", "- HKEY_CURRENT_USER", "- HKEY_CURRENT_CONFIG"]) + "\n[+] Answer> ",
        "Which registry key is derived from two keys, HKLM\\Software\\Classes and\nHKU\\<userSID>\\Software\\Classes and is used to associate file types with programs\nthat are used to open them?" + randomloop(["- HKEY_USERS", "- HKEY_LOCAL_MACHINE", "- HKEY_CLASSES_ROOT", "- HKEY_CURRENT_USER", "- HKEY_CURRENT_CONFIG"]) + "\n[+] Answer> ",
        "Which registry key is derived from HKU\\<userSID> and contains user profiles\nenvironment settings of interactively logged on user?" + randomloop(["- HKEY_USERS", "- HKEY_LOCAL_MACHINE", "- HKEY_CLASSES_ROOT", "- HKEY_CURRENT_USER", "- HKEY_CURRENT_CONFIG"]) + "\n[+] Answer> ",
        "Which registry key is derived from a link to\nHKLM\\SYSTEM\\CurrentControlSet\\Hardware Profiles\\Current\nand is used to establish the current hardware configuration profile?" + randomloop(["- HKEY_USERS", "- HKEY_LOCAL_MACHINE", "- HKEY_CLASSES_ROOT", "- HKEY_CURRENT_USER", "- HKEY_CURRENT_CONFIG"]) + "\n[+] Answer> ",

    ]
    windows_filesys_questions = [
        Question(windows_filesys_prompts[0], "Physical"),
        Question(windows_filesys_prompts[1], "File System"),
        Question(windows_filesys_prompts[2], "Filename"),
        Question(windows_filesys_prompts[3], "Metadata"),
        Question(windows_filesys_prompts[4], "Data"),
        Question(windows_filesys_prompts[5], "FAT"),
        Question(windows_filesys_prompts[6], "Boot Record, Root Directory"),
        Question(windows_filesys_prompts[7], "Boot Record, Root Directory"),
        Question(windows_filesys_prompts[8], "Boot Record"),
        Question(windows_filesys_prompts[9], "FAT"),
        Question(windows_filesys_prompts[10], "Root Directory"),
        Question(windows_filesys_prompts[11], "Data Area"),
        Question(windows_filesys_prompts[12], "FAT #2"),
        Question(windows_filesys_prompts[13], "Data Area"),
        Question(windows_filesys_prompts[14], "FAT16"),
        Question(windows_filesys_prompts[15], "FAT32"),
        Question(windows_filesys_prompts[16], "FFF7"),
        Question(windows_filesys_prompts[17], "FFFFFFF7"),
        Question(windows_filesys_prompts[18], "32"),
        Question(windows_filesys_prompts[19], "8.3"),
        Question(windows_filesys_prompts[20], "Truncated"),
        Question(windows_filesys_prompts[21], "12"),
        Question(windows_filesys_prompts[22], "accessed"),
        Question(windows_filesys_prompts[23], "HKEY_USERS, HKEY_LOCAL_MACHINE"),
        Question(windows_filesys_prompts[24], "HKEY_USERS"),
        Question(windows_filesys_prompts[25], "HKEY_LOCAL_MACHINE"),
        Question(windows_filesys_prompts[26], "HKEY_CLASSES_ROOT"),
        Question(windows_filesys_prompts[27], "HKEY_CURRENT_USER"),
        Question(windows_filesys_prompts[28], "HKEY_CURRENT_CONFIG"),
        
    ]

    thingsigottoldlastminute_prompts = [
        #"?" + "\n[+] Answer> ",
        #"What?" + randomloop(["- ", "- ", "- ", "- "]) + "\n[+] Answer> ",
        "Which space is strictly reserved for running a privileged operation system kernel,\nkernel extensions, and most device drivers?" + randomloop(["- Kernel", "- User"]) + "\n[+] Answer> ", 
        "Which space is the memory area where application software and some drivers execute?" + randomloop(["- Kernel", "- User"]) + "\n[+] Answer> ",
        "What port term means, a TCP or UDP port number that is configured to accept packets?" + randomloop(["- Open", "- Closed"]) + "\n[+] Answer> ",
        "What port term means, a TCP or UDP port number that rejects connections or ignores\nall packets directed at it?" + randomloop(["- Open", "- Closed"]) + "\n[+] Answer> ",
        "In order for communication to be established on a given open port, there needs to be\nan ______ (service) _______  on that port to accept the incoming packets and process them?(XXXXX XXXXXXX)" + "\n[+] Answer> ",
        "Which TCP Flag is used to request for graceful connection termination?" + randomloop(["- SYN", "- ACK", "- FIN", "- RST", "- PSH", "- URG"]) + "\n[+] Answer> ",
        "Which TCP Flag is used to abruptly terminate the connection if the sender feels\nsomething is wrong with the TCP connection?" + randomloop(["- SYN", "- ACK", "- FIN", "- RST", "- PSH", "- URG"]) + "\n[+] Answer> ",
        "Which TCP Flag is used to immediately send segments to the network layer as soon as it\nreceives signal from the application layer?" + randomloop(["- SYN", "- ACK", "- FIN", "- RST", "- PSH", "- URG"]) + "\n[+] Answer> ",
        "Data inside a segment with a ____ = 1 flag is forwarded to the applicaiton layer\nimmediately even if there is more data to be given?" + randomloop(["- SYN", "- ACK", "- FIN", "- RST", "- PSH", "- URG"]) + "\n[+] Answer> ",
        "What is a distributed file system protocol originally developed by Sun Microsystems,\nallowing a user on a client computer to access files over a computer network much\nlike local storage is accessed typically using port 2049?" + "\n[+] Answer> ",
        "What is a command-line firewall utility that uses policy chains to allow or block traffic?" + "\n[+] Answer> ",
        "Input, forward, and ouput are the three chains that what utility uses?" + "\n[+] Answer> ",
        "Which iptables chain is used to control the behavior for incoming connections?" + randomloop(["- Input", "- Forward", "- Output"]) + "\n[+] Answer> ",
        "Which iptables chain is used for incoming connections that aren't actually being delievered locally?" + randomloop(["- Input", "- Forward", "- Output"]) + "\n[+] Answer> ",
        "Which iptables chain is used for outgoing connections?" + randomloop(["- Input", "- Forward", "- Output"]) + "\n[+] Answer> ",
        """Given the below iptables output, which chain has not been used?

:~$ sudo iptables -L -v

Chain INPUT (policy ACCEPT 9380K packets, 11G bytes)
 pkts bytes target     prot opt in     out     source
    destination
  
Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source
    destination

Chain OUTPUT (policy ACCEPT 5821K packets, 17G bytes)
 pkts bytes target     prot opt in     out     source
    destination\n""" + randomloop(["- Input", "- Forward", "- Output"]) + "\n[+] Answer> ",

        """Given the below ping what iptables rule is set?

C:\\Users\\Me>ping 192.168.5.28

Pinging 192.168.5.28 with 32 bytes of data:
Reply from 192.168.5.28: Destination port unreachable.
Reply from 192.168.5.28: Destination port unreachable.
Reply from 192.168.5.28: Destination port unreachable.
Reply from 192.168.5.28: Destination port unreachable.

Ping statistics for 192.168.5.28:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),\n"""  + randomloop(["- Accept", "- Drop", "- Reject"]) + "\n[+] Answer> ",
        """Given the below ping what iptables rule is set?

C:\\Users\\Me>ping 192.168.5.28

Pinging 192.168.5.28 with 32 bytes of data:
Reply from 192.168.5.28: bytes=32 time<1ms TTL=64
Reply from 192.168.5.28: bytes=32 time<1ms TTL=64
Reply from 192.168.5.28: bytes=32 time<1ms TTL=64
Reply from 192.168.5.28: bytes=32 time<1ms TTL=64

Ping statistics for 192.168.5.28:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms\n"""  + randomloop(["- Accept", "- Drop", "- Reject"]) + "\n[+] Answer> ",
        """Given the below ping what iptables rule is set?

C:\\Users\\Me>ping 192.168.5.28

Pinging 192.168.5.28 with 32 bytes of data:
Request timed out.
Request timed out.
Request timed out.
Request timed out.

Ping statistics for 192.168.5.28:
    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),\n"""  + randomloop(["- Accept", "- Drop", "- Reject"]) + "\n[+] Answer> ",
        "Which iptables rule acts like a connection never happened, and is best if you don't\nwant the source to realize your system exists?" + randomloop(["- Accept", "- Drop", "- Reject"]) + "\n[+] Answer> ",
        "Which iptables rule won't allow the connection but send back an error?" + randomloop(["- Accept", "- Drop", "- Reject"]) + "\n[+] Answer> ",
        """What will the below iptables command do to 10.10.10.10?

iptables -A INPUT -p tcp --dport ssh -s 10.10.10.10 - j DROP""" + randomloop(["- Block all SSH connections", "- Allow all SSH connections"]) + "\n\n[+] Answer> ",
        "What would you type in command line if you wanted to add an object or value to Registry?" + randomloop(["- reg add", "- reg query", "- reg delete", "- reg copy", "- reg load"]) + "\n[+] Answer> ",
        "What would you type in command line if you wanted to displays a registry object value?" + randomloop(["- reg add", "- reg query", "- reg delete", "- reg copy", "- reg load"]) + "\n[+] Answer> ",
        "What would you type in command line if you wanted to remove an object from Registry?\nIt can also delete a value from a remote machine." + randomloop(["- reg add", "- reg query", "- reg delete", "- reg copy", "- reg load"]) + "\n[+] Answer> ",
        "What would you type in command line if you wanted to change the path or move a\nRegistry to another machine?" + randomloop(["- reg add", "- reg query", "- reg delete", "- reg copy", "- reg load"]) + "\n[+] Answer> ",
        "What would you type in command line if you wanted to load a hive file into a subkey\nin the registry?" + randomloop(["- reg add", "- reg query", "- reg delete", "- reg copy", "- reg load"]) + "\n[+] Answer> ",
        "What translates I/O related function calls into specific hardware device requests?" + randomloop(["- Device Driver", "- File System Driver", "- Network Driver"]) + "\n[+] Answer> ",
        "What accepts file oriented I/O requests and translates them into I/O operations\ndestined for the disk?" + randomloop(["- Device Driver", "- File System Driver", "- Network Driver"]) + "\n[+] Answer> ",
        "What accepts network I/O request and translates them into I/O communications destined\nfor other network devices?" + randomloop(["- Device Driver", "- File System Driver", "- Network Driver"]) + "\n[+] Answer> ",
    ]

    thingsigottoldlastminute_questions = [
        Question(thingsigottoldlastminute_prompts[0], "Kernel"),
        Question(thingsigottoldlastminute_prompts[1], "User"),
        Question(thingsigottoldlastminute_prompts[2], "Open"),
        Question(thingsigottoldlastminute_prompts[3], "Closed"),
        Question(thingsigottoldlastminute_prompts[4], "application listening"),
        Question(thingsigottoldlastminute_prompts[5], "FIN"),
        Question(thingsigottoldlastminute_prompts[6], "RST"),
        Question(thingsigottoldlastminute_prompts[7], "PSH"),
        Question(thingsigottoldlastminute_prompts[8], "URG"),
        Question(thingsigottoldlastminute_prompts[9], "NFS"),
        Question(thingsigottoldlastminute_prompts[10], "iptables"),
        Question(thingsigottoldlastminute_prompts[11], "iptables"),
        Question(thingsigottoldlastminute_prompts[12], "input"),
        Question(thingsigottoldlastminute_prompts[13], "forward"),
        Question(thingsigottoldlastminute_prompts[14], "output"),
        Question(thingsigottoldlastminute_prompts[15], "Forward"),
        Question(thingsigottoldlastminute_prompts[16], "Reject"),
        Question(thingsigottoldlastminute_prompts[17], "Accept"),
        Question(thingsigottoldlastminute_prompts[18], "Drop"),
        Question(thingsigottoldlastminute_prompts[19], "Drop"),
        Question(thingsigottoldlastminute_prompts[20], "Reject"),
        Question(thingsigottoldlastminute_prompts[21], "Block all SSH connections"),
        Question(thingsigottoldlastminute_prompts[22], "reg add"),
        Question(thingsigottoldlastminute_prompts[23], "reg query"),
        Question(thingsigottoldlastminute_prompts[24], "reg delete"),
        Question(thingsigottoldlastminute_prompts[25], "reg copy"),
        Question(thingsigottoldlastminute_prompts[26], "reg load"),
        Question(thingsigottoldlastminute_prompts[27], "Device Driver"),
        Question(thingsigottoldlastminute_prompts[28], "File System Driver"),
        Question(thingsigottoldlastminute_prompts[29], "Network Driver"),
        #Question(thingsigottoldlastminute_prompts[30], ""),
        #Question(thingsigottoldlastminute_prompts[31], ""),
        #Question(thingsigottoldlastminute_prompts[32], ""),
        #Question(thingsigottoldlastminute_prompts[33], ""),
        #Question(thingsigottoldlastminute_prompts[34], ""),
        #Question(thingsigottoldlastminute_prompts[35], ""),
        #Question(thingsigottoldlastminute_prompts[36], ""),
        #Question(thingsigottoldlastminute_prompts[37], ""),
        
    ]

def AllTheQs():
    output = ""
    i = 0
    for i in range(0, len(QuestionBank.quiz_choices)):
        output += "\n\n"
        output += str("=" * 80) + "\n║ "
        output += QuestionBank.quiz_choices[i][0]
        output += "\n" + str("=" * 80)

        j = 0
        for quest in getattr(QuestionBank, (QuestionBank.quiz_choices[i][1] + "_questions")):
            j += 1
            output +=  "\n\n" + str(j) + ". " + quest.prompt
            output += "  " + quest.answer

    return output

#print(AllTheQs())