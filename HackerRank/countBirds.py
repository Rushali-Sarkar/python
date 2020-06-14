def countEach(birds: [int]) -> ({int: int}, int) :
    birdsID = set(birds)
    counts = [birds.count(ID) for ID in birdsID]
    return dict(zip(birdsID, counts)), max(counts)


def migratoryBirds(birds: [int]) -> int:
    birdcount, maximum = countEach(birds)
    return(min([key  for (key, value) in birdcount.items() if value == maximum]))


