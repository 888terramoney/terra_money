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
# Using previous snapshot because the lottery is done based on snapshot taken during the week
# open file and read the content in a list
with open('listfile.txt', 'r') as filehandle:
    lottery_tickets = [current_address.rstrip() for current_address in filehandle.readlines()]

#Print date and time for video recording

print("The lottery winner was selected at")
now = datetime.datetime.now()
print(str(now))


# Print lottery winner
print("the winner is")
print(random.choice(lottery_tickets))