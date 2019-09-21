### Aladdin has to travel from place to place on his magic carpet in a circular fashion. Given a list of destinations,
### calculate whether Aladdin has enough magic to make a round trip. You are given two lists - 
### 1. dist -  list of destinations, and the costs of magic that is required to travel from one point to another.
### 2. magic - the amount of magic you receive at a particular destination. The indices of both list correspond to a point.
### Problem: Find the first point(index of dist) that has enough magic to make a circular trip.

### Example: dist = [3,2,5,6] magic = [2,6,3,4]
### If we start with index = 0, we start with 2 magic.
### Next: magic = magic - dist[index] + magic[index + 1]
### And so on. Remember that these lists are circular. That means index = 3 means the next destination is index = 0
### If there are no starting points in the dist list that make the round trip, return -1

def can_make_trip(index, magic, dist):
    print("### Computing for index:", index)
    length = len(dist)
    current_magic = magic[index]
    print("Magic:", current_magic)
    for i in range(index, index + length):
        if current_magic < dist[i%length]:
            return False
        current_magic -= dist[i%length]
        if i != index -1:
            current_magic += magic[(i+1)%length]
        print("Magic at [{}] iteration:". format(i), current_magic)
        if current_magic <= 0:
            return False
    return True


def aladdin_carpet(magic, dist):
    for i in range(len(dist)):
        if can_make_trip(i, magic, dist):
            return i
    return -1


if __name__ == "__main__":
    print(aladdin_carpet([3,2,5,6],[2,6,3,4]))

