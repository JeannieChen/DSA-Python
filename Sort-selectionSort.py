from http.client import MULTIPLE_CHOICES


def selection_sort(my_list):
    for i in range(len(my_list)-1): #0,1,2,3,4
        min_index = i
        for j in range(i+1,len(my_list),1): #1,2,3,4,5 / 2,3,4,5/ 3,4,5/ 4,5/ 5
            if my_list[j] < my_list[min_index]:
                min_index = j
        # swap min
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] =  temp
    
    return my_list


li1 = [1,4,2,6,5,1,3,7,9]
print(selection_sort(li1))
        
