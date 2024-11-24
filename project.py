import requests
class IRCTC:

    def __init__(self):

        user_input=input("""how would you like to proceed?
                         1. Enter 1 to check live train status.
                         2. Enter 2 to check PNR.
                         3. Enter 3 to check teain schedule""")
        
        if user_input == "1":
            print("live train status:")
        elif user_input == "2":
            print("PNR")

        else:
            self.train_schedule()

    def train_schedule(self):
        train_no = input("Enter the train number:")
        self.fetch_data(train_no)

    def fetch_data(self,train_no):
        data = requests.get(f"http://indianrailapi.com/api/v2/TrainSchedule/apikey/41758ae2c7c3e4ae790c76cf1ac2dffd/TrainNumber/{train_no}")

        data = data.json()
        for i in data['Route']:
            print(i['StationName'])
            


obj = IRCTC()