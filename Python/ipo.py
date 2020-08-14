## Given a list of share purchase orders represented like so - 
## [[id, #of shares, price, timestamp] ....]
## and a total number of shares, return a list of ids who did not receive any shares.
## The shares are allocated using the following rules:
## The highest bidder gets all the shares he has bought.
## If they have the same price, assign them in the order of their timestamp.
## Final constraint -  if there are any shares left, keep assigning them

def IPO(bids, total_shares):
    bids.sort(key = lambda x: (-x[2], -x[1]))
    finished = set()
    while bids and total_shares != 0:
        bid = bids.pop(0)
        if total_shares >= bid[1]:
            total_shares -= bid[1]
        else:
            while totalShares != 0:
                for i in range(len(bids)):
                    if bids[i][3] == bid[3]:
                        bids[i][1] -= 1
                        totalShares -= 1

                        if bids[i][1] == 0:
                            finished.add(bids[i][0])
    


    ret = []
    for bid in sorted(bids, key = lambda x: x[0]):
        ret.append(bid[0])
    
    return ret


if __name__ == "__main__":
    bids = [
        [1,5,5,0],
        [2,7,8,1],
        [3,7,5,1],
        [4,10,3,3],
        [5,10,1,4]
    ]

    print(IPO(bids, 18))






