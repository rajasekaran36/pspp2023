def find_first_pair(dict,value):
    for key in dict:
        if dict[key] == value:
            return key,value
    else:
        return None

sample_dict = {'apple':80,'mango':70,'orange':30,'watermelon':70,'banana':50}
value_to_be_searched = int(input('Enter value to be searched:'))
pair = find_first_pair(sample_dict,value_to_be_searched)
if pair:
    print('The first match found:',pair)
else:
    print('Value not found')