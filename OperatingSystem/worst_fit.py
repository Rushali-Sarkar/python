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


def worst_fit(blocks: list[int], processes: list[int]):

    allocation = [-1] * len(blocks)

    for process_number, process_size in enumerate(processes):
        worst_fit_block = -1
        for block_number, block_size in enumerate(blocks):
            if block_size >= process_size and allocation[block_number] == -1:
                if worst_fit_block == -1:
                    worst_fit_block = block_number
                elif blocks[block_number] > blocks[worst_fit_block]:
                    worst_fit_block = block_number
        if worst_fit_block != -1:
            printFragment(processes, blocks, allocation)
            allocation[worst_fit_block] = process_number
        if -1 not in allocation:
            break
    
    return

if __name__ == "__main__":

    max_blocks = int(input("Enter the maximum number of blocks \n"))
    max_block_size = int(input("Enter the maximum size of each block \n"))
    blocks = createRandomList(max_blocks, max_block_size)

    max_processes = int(input("Enter the maximum number of processes \n"))
    max_process_size = int(input("Enter the maximum size of each process \n"))
    processes = createRandomList(max_processes, max_process_size)

    print("-------------------------------------------------------------")
    print("Blocks: ", *blocks)
    print("Process: ", *processes)
    print("-------------------------------------------------------------")
    worst_fit(blocks, processes)