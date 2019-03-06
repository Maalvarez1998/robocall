from googlevoice import Voice
import credentials

#create instance of voice class
Voice = Voice()

#pass google username and password from credentails
#log in to google Voice
Voice.login(credentials.username, credentials.password)
#prompt user to enter telephone to call
number_to_call = "+" + input("outgoing tel (Include Country Code")

#make the call
Voice.call(number_to_call, credentials.forwarding_number)

#ask user if they want to cancel call
if input("calling now... cancel?  [y/N]") == "y":
    Voice.cancel(number_to_call, credentials.forwarding_number)