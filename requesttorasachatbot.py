import requests

url = 'http://localhost:5005/webhooks/rest/webhook'
while True:   
    message = input("You: ")  
    payload = {
        "sender": "user",
        "message": message
    }    
    response = requests.post(url, json=payload)    
    if response.status_code == 200:
        data = response.json()
        if data:
            
            for resp in data:                
                print("Bot:", resp['text'])
                              
                buttons = resp.get("buttons")
                if buttons:
                    
                    print("Buttons received:")
                    for i, button in enumerate(buttons):
                        print(f"{i + 1}. {button['title']} (Payload: {button['payload']})")
                    
                    choice = input("Enter the number of the button you want to choose: ")
                    try:
                        choice_index = int(choice) - 1
                        if 0 <= choice_index < len(buttons):
                            
                            payload['message'] = buttons[choice_index]['payload']
                            #print("in payload message ")
                            #print(payload['message'])
                            if payload['message']== '/_yes':
                                continue
                            else:

                                response = requests.post(url, json=payload)
                                resp = response.json()
                                print(resp[0]['text'])
                        else:
                            print("Invalid choice.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
       
    else:
        print("Error:", response.status_code)


