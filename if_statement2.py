code = (input("Enter code"))

if code == "*544#":
    print("0.Nyakua Bonus"
          "1.Data Deals"
          "2.Daily Bundles"
          "3.Weekly Bundles"
          "4.GO MONTHLY"
          "5.No Expiry"
          "6.Video Bundles"
          "7.Okoa Data"
          "8.Lipa Mdogo"
          "9.Data Plus NEW"
          "10.Hot Minutes"
          "98.MORE"
          )
else:
    print("Invalid MMI")


number = int(input("Enter prefered number"))
if number == 0:
    print("Nyakua Bonus")

elif number == 1:
    print("Data Deals")

elif number == 2:
    print("Daily Bundles")

elif number == 3:
    print("Weekly Bundles")

elif number == 4:
    print("GO MONTHLY")

elif number == 5:
    print("No Expiry")

elif number == 6:
    print("Video Bundles")

elif number == 7:
    print("Okoa Data")

elif number == 8:
    print("Lipa Mdogo")

elif number == 9:
    print("Data Plus NEW")

elif number == 10:
    print("Hot Minutes")

elif number == 98:
    print("MORE")

else:
    print("Invalid MMI")

