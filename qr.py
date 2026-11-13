import qrcode

while True:
    print("\n ----QR CODE MAKER----")
    print("1. link or text")
    print("2. Contact card")
    print("3. Wifi")
    print("4. Exit")

    choice = input("Choose: ")


    if choice == "1":
        text = input("Enter text or link: ")
        file = input("File name")
        img = qrcode.make(text)
        img.save(file+".png")
        print("saved", file+ ".png")

    elif choice == "2":
        first = input("Enter firstname: ")
        last = input("Enter lastname: ")
        phone = input("Enter phone.no.: ")
        email = input("Enter Email: ")

        full = first +""+last
        card = ["Begin:Vcard","VERSION:3.0"]
        card.append("N:"+last+";"+first)
        card.append("FN"+full)
        card.append("TEL"+phone)
        card.append("EMAIL"+email)
        card.append("END:VCARD")
        vcard = "\n".join(card)

        img = qrcode.make(vcard)
        img.save("contact_qr.png")
        print("saved: contact_qr.png")



    elif choice == "3":
        ssid = input("wifi name: ")
        pas = input("wifi password: ")

        wifi = "WIFI:T:WPA;S:" + ssid
        wifi = wifi + ";P:" +pas+ ";;"

        img = qrcode.make(wifi)
        img.save("wifi_qr.png")
        print("saved: wifi_qr.png")

    elif choice == "4":
        print("Exit")
        break
    else:
        print("Wrong choice")