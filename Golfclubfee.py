sClubmember = str(input("Are you a member or a non-member, type M for member or N for non-member?\n")).upper()
sDayorend = str(input("Do you practice golf on the weekend or weekday, type W for weekend or D for weekday?\n")).upper()
if sClubmember == "M":
    print("You are a member of our golf club, the fee for a member is only $35\n")
elif sDayorend == "W":
    print("You are a non-member of our golf club, the additional fee is $33, the entire fee for a non-member is $68\n")
elif sDayorend == "D":
    print("You are a non-member of our golf club, the additional fee is $25, the entire fee for a non-member is $60 \n")
else:
    print("You did not enter a correct statement")
