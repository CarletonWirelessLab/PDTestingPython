# Three packet_starts with high energy level p1,p2,p3
# Beacon with the same energuy level as (p1,p2,p3) and it has a certain mac address(Bmac)
# Preamble with low energy level (packet without payload)
# We will send [p1,p2,p3,Beacon,Preamble]
# The test will pass if the Device under test (DUT) will be silent in the silent period
# N=Number of all detected packets
# N_Beacons= Number of all Beacons in the received signal
# Mac_packets= list of all MACs
# Bmac= Beacon MAC
# packet_start= starts of the packets 
# Rate = Rate of each packet
count_fail=0
count_pass=0
for n  in range(N-2):
      if  Mac_packets[n]== 'Bmac' and type_packet[n]=='Beacon':
          silent_period=(length[n+1]*8)/(Rate[n+1])
          if (packet_start[n+1]<= packet_start[n+2]) and  (packet_start[n+2] <= (packet_start[n+1]+silent_period)):
               count_fail=count_fail+1
          else:
              count_pass=count_pass+1
              
              
prob_success=(count_pass/(count_pass+count_fail))*100
              
             