from audioop import mul


def insertion_sort(my_list):
    for i in range(1,len(my_list)): #1,2,3,4,5
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1 # keep checking left items
    
    return my_list


li1 = [1,4,2,6,5,1,3,7,9]
print(insertion_sort(li1))
        
