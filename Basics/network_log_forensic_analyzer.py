#NETWORK_Logs
ip_logs = ( "192.168.1.1" , "10.0.0.5" , "192.168.1.1" , "172.16.0.1" , "192.168.1.1" , "10.0.0.5")
packet = ("TCP" , "FLAGS" , ( 80 , 443 , 8080 , 22) , "PAYLOAD_CLEAN")

while True:
    i=int(input("Press '1' to check Malicious log attempts , '2' to check log position , '3' to check Log Entry/Source_IP , '4' to check Suspicious Traffic , '5' to check Suspicious Target Ports and 6 to Exit: "))

    if (i==1):
        ip=input("Enter ip to check connection attempts :")
        print(f"Connection Attempts : {ip_logs.count(ip)}")

    elif(i==2):
        ip=input("Enter ip to locate suspicious port :")
        if(ip in ip_logs):
            print(f"Port : {ip_logs.index(ip)}")
        else:
            print("IP not found in logs!")

    elif(i==3):
        for log_entery ,source_ip in enumerate(ip_logs):
            print(f"Log Entry {log_entery} : Source_IP {source_ip}")

    elif(i==4):
        print(f"Target Investigation Window : {ip_logs[1:]}")
        print(f"Suspicious Traffic : {ip_logs[2:5]}")

    elif(i==5):
        print(f"Suspicious Target Ports {packet[2][2:]}")

    elif(i==6):
        print("Exiting system... ")
        break

    else:
        print("Invalid choice! Select form 1-6")    
    



