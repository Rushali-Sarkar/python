def organizingContainers(container: [int]) -> str:
    
    containersums = []
    ballsums      = []

    for number, vessel in enumerate(container):
        containersums.append(sum(vessel))
        ballsums.append(sum(box[number] for box in container))

    if sorted(containersums) == sorted(ballsums):
        return "Possible"
    return"Impossible"
        






container1 = [997612619, 934920795, 998879231, 999926463] 
container2 = [960369681, 997828120, 999792735, 979622676] 
container3 = [999013654, 998634077, 997988323, 958769423] 
container4 = [997409523, 999301350, 940952923, 993020546]

print(organizingContainers([container1, container2, container3, container4]))
    




