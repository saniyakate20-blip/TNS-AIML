friends = {
    "aisha":["ben","carla"],
    "ben":["aisha","dev"],
    "carla":["aisha","dev"],
    "dev":["ben","carla","eli"],
    "eli":["dev"]
}

def add_person(g,name):
    g ={}
    if name not in g:
        g[name]=[]
    
    return g

def add_frindship(g,a,b):
    add_person(g,a)
    add_person(g,b)

    if b not in g[a]:
        g[a].append(b)
    if a not in g[b]:
        g[b].append(a)

add_person(friends,"aisha")
add_person(friends,"ben")
add_person(friends,"dev")
add_person(friends,"carla")
add_person(friends,"eli")

add_frindship(friends,"aisha","ben")
add_frindship(friends,"aisha","carla")
add_frindship(friends,"ben","dev")
add_frindship(friends,"carla","dev")
add_frindship(friends,"eli","dev")

for person,friend in friends.items():
    print(person, "->",friend)
    print(person,"has",len(friend),"friends")

