#build a basic smart home climate monitoring script that reads an atmospheric status string and prints out hardware recommendation(e.g., "turn on AC","activate heater","idle").

print("========== Order-Tracking System ==========")

status=input("Enter order status(hot,cold,normal) = ").lower().strip()

if status=="Hot".lower():
    recommendation="Turn on AC."
    
elif  status=="Cold".lower():
    recommendation="Activate Heater."

elif status=="Normal".lower():
    recommendation="Idle"
    
else:
    recommendation="Invalid status. Please enter Hot,Cold,Normal."
    
print("\n----- HARDWARE RECOMMENDATION -----")
print(recommendation)
