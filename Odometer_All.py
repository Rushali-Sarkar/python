numbers = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]

def is_feasible( distance : int ) -> bool:
    distance = [ int ( each ) for each in str ( distance ) ]
    
    for i in range( len ( distance ) - 1 ):
        
        if distance[i] >= distance[i+1] :
            return False
        
    return True


def limits(length:int) -> (int,int):
    
    lowest = int("".join( str(each) for each in numbers [0:length] ))
    highest = int("".join( str(each) for each in numbers [-length:] ))
    
    return lowest , highest


def generate(length:int) -> [int]:
    
    if length == 1 :
        return numbers
    
    else:
        return [ element * 10 + each for element in generate( length - 1 ) for each in numbers[ element % 10 : ] ]
    
    
length_keys = [ each for each in numbers ]
odometer_values = [ generate ( each ) for each in numbers ]

odometer_dict = dict( zip ( length_keys, odometer_values ) )


def nth_shift_length ( reading : int , position : int) -> int:
    odometer = odometer_dict [ len( str ( reading ) ) ]
    l = len(odometer)
    
    if reading not in odometer:
        return -1
    
    i = odometer.index ( reading )
    final_index = ( position + i ) % l
    
    if position < 0:
        final_index = ( l + position + i ) % l
        
    return odometer [ final_index ]


def distance_length ( reading_one : int , reading_two :  int) -> int:
    odometer = odometer_dict[ len( str ( reading_one ) ) ]
    
    if reading_one not in odometer or reading_two not in odometer:
        return -1
    
    return abs ( odometer.index ( reading_one ) - odometer.index ( reading_two ) )
 




all_odometer = [ each for i in range ( 1,10 ) for each in generate ( i ) ]




def distance ( reading_one : int , reading_two : int ) -> int:
    
    
    if reading_one not in all_odometer or reading_two not in all_odometer:
        return -1
    
    return abs (all_odometer.index( reading_one )- all_odometer.index( reading_two ) )




def nth_shift(reading:int, position:int) -> int:
    
    
    if reading not in all_odometer:
        return -1
    
    i = all_odometer.index( reading )
    
    final_index = ( position + i ) % 511
    
    if position < 0:
        final_index = ( 511 + position + i ) % 511
        
    return all_odometer[ final_index ]


    
        
        
    


























