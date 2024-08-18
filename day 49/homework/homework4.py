#Going Once, Going Twice, Sold!
max_bid = int(input()) 

while True:
    bid = int(input()) 
    
   
    if bid >= max_bid:
        
        print("Sold: " + str(bid))
        break