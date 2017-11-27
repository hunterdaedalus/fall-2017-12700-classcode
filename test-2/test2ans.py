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
    pass

def two_hops(routes,start,end):
    pass
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
    pass

def merge(r1,r2):
    pass

# add_range(rangelist,newrange)
def add_range(rangelist,newrange):
    pass



########### Git answers
# pull
# edit
# commit
# push
######
# C, A, D, B, F, E
