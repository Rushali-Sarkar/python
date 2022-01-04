import random

def createRandomList(max_list_size: int, max_element_size: int) -> list[int]:
    length = random.randint(0, max_list_size)
    return [random.randint(0, max_element_size) for i in range(length)]

def getSpace(number: int) -> str:
    return " " * number

def printFragment(processes: list[int], blocks: list[int], allocation: list[int]) -> None:

    total_blocks = len(blocks)

    print("Block Number | Block Size | Process Allocated | Process Size")
    
    first_space = 11
    second_space = 8
    third_space = 15
    fourth_space = 12

    for i in range(total_blocks):
        
        first_element = str(i + 1)
        second_element = str(blocks[i])
        third_element = "Not Allocated" if allocation[i] == -1 else str(allocation[i] + 1)
        fourth_element = "None" if third_element == "Not Allocated" else str(processes[allocation[i]])

        print(first_element, getSpace(first_space - len(first_element)), "| ", second_element, getSpace(second_space - len(second_element)), "| ", third_element, getSpace(third_space - len(third_element)), "| ", fourth_element, getSpace(fourth_space - len(fourth_element)))
    
    print("-------------------------------------------------------------")
    return None

def first_fit(blocks: list[int], processes: list[int]) -> None:

    allocation = [-1] * len(blocks)

    for process_number, process_size in enumerate(processes):
        for block_number, block_size in enumerate(blocks):
            if block_size >= process_size and allocation[block_number] == -1:
                allocation[block_number] = process_number
                printFragment(processes, blocks, allocation)
                break
        if -1 not in allocation:
            break
    return None


if __name__ == "__main__":

    max_blocks = int(input("Enter the maximum number of blocks \n"))
    max_block_size = int(input("Enter the maximum size of each block \n"))
    blocks = createRandomList(max_blocks, max_block_size)

    max_processes = int(input("Enter the maximum number of processes \n"))
    max_process_size = int(input("Enter the maxium size of each process \n"))
    processes = createRandomList(max_processes, max_process_size)

    first_fit(blocks, processes)



