candidate1=input("enter first candidate name :- ")
candidate2=input("enterv second candidate name :- ")
cand1_votes=0
cand2_votes=0
voters_id=[1,2,3,4,5,6,7,8,9,10]
no_of_voters=len(voters_id)
print("total numbers of voters = ",no_of_voters)
print()
voted=[]
while True:
    if voters_id==[]: 
        print("voting is over")
        if cand1_votes>cand2_votes:
            print(f"Congratulation {candidate1} won the election with {cand1_votes-cand2_votes} votes")
        elif cand2_votes>cand1_votes:
            print(f"Congratulation {candidate2} won the election with {cand2_votes-cand1_votes} votes")
        elif cand1_votes == cand2_votes:
            print("voting is tied")
        break
    
    else:
        print("Welcome To Online Voting System\n")
        voter=int(input("enter your id :- "))
        if voter in voted:
            print("Sorry  you already voted \n")
        else:
            if voter in voters_id:
                print(f"1.{candidate1}\n2.{candidate2}")
                choice=int(input("enter your choice:- "))
                if choice==1:
                    cand1_votes+=1
                    print(f"You voted {candidate1}")
                    print("Thanks for Voting\n")
                elif choice==2:
                    cand2_votes+=1 
                    print(f"You voted {candidate2}")
                    print("Thanks For Voting\n")
                else:
                    print("You are not vote anyone")
                    print("Thanks For Voting\n")
                voters_id.remove(voter)
                voted.append(voter)
            else:
                print("Sorry you are not allowed to vote because your i'd is wrong")
                print("Thanks For Visiting Online Voting System\n")