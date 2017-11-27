import random


airports = ['LGA','SFO','SEA','DTW','SFO','EWR','ATL','ORD',
            'LAX','JFK','BOS','DCA']

sample_routes = {'LAX': ['SFO', 'ATL'],
                 'BOS': ['SFO', 'SEA'],
                 'SFO': ['JFK', 'BOS', 'BOS'],
                 'LGA': ['ATL', 'BOS'], 
                 'JFK': ['DCA', 'SFO'],
                 'ATL': ['SFO', 'SFO', 'DCA'],
                 'ORD': ['LAX', 'SFO'],
                 'DTW': ['BOS', 'LAX', 'JFK'], 
                 'DCA': ['SEA', 'SFO', 'LGA'], 
                 'SEA': ['DTW', 'SFO', 'LAX'], 
                 'EWR': ['SFO', 'ATL', 'SFO']}


def create_routes(airports):
    routes = {}
    for airport in airports:
        routes.setdefault(airport,[])
        num = 1 + random.randrange(1,len(airports)/2)
        while num > 0:
            choice = random.choice(airports)
            if choice != airport and choice not in routes[airport]:
                routes[airport].append(choice)
                num = num - 1
    return routes

def two_hops(routes,start,end):
    if end in routes[start]:
        return True
    for airport in routes[start]:
        if end in routes[airport]:
            return True
    return False

#########################################################################



def build_rangelist(length=10):
  l=[]
  lowval = 5
  
  for i in range(length):
    r = [lowval, lowval+random.randrange(1,20)]
    l.append(r)
    lowval = r[1] + random.randrange(1,20)
  return l
  
rangelist = build_rangelist()


def overlap(r1,r2):
    (x,y) = r1
    (a,b) = r2
    # return not (b < x or a > y)
    if  b < x or a > y:
        return False
    else:
        return True

    
def merge(r1,r2):
    a = min(r1[0],r2[0])
    b = max(r1[1],r2[1])
    return [a,b]

# add_range(rangelist,newrange)
def add_range(rangelist,newrange):
    # First find the spot
    i = 0
    while i < len(rangelist) and newrange[0] > rangelist[i][1]:
        i = i + 1
    while i < len(rangelist) and overlap(newrange,rangelist[i]):
        newrange = merge(newrange,rangelist[i])
        del rangelist[i]
    rangelist.insert(i,newrange)
        
    



########### Git answers
# pull
# edit
# commit
# push
######
# C, A, D, B, F, E
