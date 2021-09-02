"""
0 0 0
0 0 1
0 0 2
0 0 3
0 1 0
0 1 1
0 1 2
0 1 3
0 2 0
0 2 1
0 2 2
0 2 3
0 3 0
0 3 1
0 3 2
0 3 3
1 0 0
"""



def nums1(size=3):
    l = [0]*size
    pv=-1 #place value (reverse index)
    while pv > -(size):
        yield l
        #print("pv:",pv)
        if l[pv] < 9:
            l[pv] += 1
        elif l[pv] == 9:
            #pv -= 1
            while l[pv] == 9:
                pv -= 1
                if pv < -size:
                    return
            l[pv] +=1
            for i  in range(pv+1,0): # pv to list[-1]
                l[i] = 0
            pv =-1


if __name__ == "__main__":
    for l in nums1(2):
        print(l, sep ='')
    la = [l for l in nums1(3)]
    print("la: ",*la)
