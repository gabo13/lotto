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
from sys import getsizeof as sof

def nums1(size=2):
    l = [0]*size
    pv=-1 #place value (reverse index)
    while pv > -(size):
<<<<<<< HEAD
        print(l)
        yield l
=======
        
        yield l.copy()
>>>>>>> 212fe33a4a5125628980a1d50c0b8a306a7cefbb
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


def nums2(size =2, tokens=None):
    l = [0]*size
    tsize=9
    if tokens:
    	t=list([tokens[0]]*size)
    	tsize=len(tokens)-1
    
    pv=-1 #place value (reverse index)
    while True:
        if not tokens:
        	yield l.copy()
        else:
        	#print('size t',len(t))
        	#print('size l',len(l))
        	for i in range(len(t)):
        		#print(l)
        		t[i]=tokens[l[i]]
        		#print('t[i]', t[i])
        	yield t.copy()
        if l[pv] < tsize:
            l[pv] += 1
        elif l[pv] == tsize:
            while l[pv] == tsize:
                pv -= 1
                if pv < -size:
                    return
            l[pv] +=1
            for i  in range(pv+1,0): # pv to list[-1]
                l[i] = 0
            pv =-1


if __name__ == "__main__":
    
    lista = list(range(3))
    print(lista)
<<<<<<< HEAD
    for i in nums2(3,list("cba")):
        print("".join(i))
=======
    la = [l for l in nums2(3,list('abcdefghijklmnopqrstuvwxyz0123456789'))]
    print("la: ",*la)
    print(sof(la)/1024, 'kb')
    '''
    for i in nums2(7,lista):
    	print(*i)
    '''
    
    
<<<<<<< HEAD
if __name__ == "__main__":
    #for l in nums1(2):
        #print(l, sep ='')
    la = [l for l in nums1(3)]
    print("la: ",*la)
=======
>>>>>>> 212fe33a4a5125628980a1d50c0b8a306a7cefbb
>>>>>>> 0750d11eccd707b04a3d9bb867efe705a2c53ed6
