#Lottery Ticket Selector
#https://station.terra.money/validator/terravaloper1jvcr78cgwpvcsucf628fa8qjrahmcskqnhq5g8
#pip install terra_sdk
from terra_sdk.client.lcd import LCDClient
import math
import random
import datetime
# Connect to Terra with SDK and get delegator info
terra = LCDClient(chain_id="columbus-4", url="https://lcd.terra.dev")
validator_info = terra.staking.delegations(validator="terravaloper1jvcr78cgwpvcsucf628fa8qjrahmcskqnhq5g8")

# Lottery Tickets
lottery_tickets=[]

#Print date and time for video recording
print("The lottery has started at:  ")
now = datetime.datetime.now()
print(str(now))

print("Processing Tickets")
for x in range(len(validator_info)):
	# Clear temporary list
	temp = []  
	# Get delegator address
	delegator_address=validator_info[x].delegator_address
	# Get amount of stake, rounded down
	delegator_amount=math.floor(validator_info[x].balance.amount/1000000)
	print(delegator_address+": amount of entries = "+str(delegator_amount))
    # Create a list of repeated addresses based on delegator amount
	temp=[delegator_address] * delegator_amount
	lottery_tickets.extend(temp)


# We save the list to file because the lottery is done based on snapshot taken during the week
with open('listfile.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % place for place in lottery_tickets)

#Print date and time for video recording

