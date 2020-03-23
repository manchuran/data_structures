def nested_list_sum(lst):
    '''
    Calculate sum of a nested list
    Input: Nested list (Lists)
    Output: Sum (Integer)
    '''
    
    if lst == []:
        return 0
    if type(lst[0]) is list:
        lst[0] = nested_list_sum(lst[0])
    return lst[0] + nested_list_sum(lst[1:])

def main():
    sample_list = [[7000,[415,[],321],5],6,21,9,[20,32,4],[],[12, [345,[900,12040]],12],11,[0,[],2400,5],19]
    list_sum = nested_list_sum(sample_list)
    print("sample list = {}; \nsum of items in list = {}".format(sample_list, list_sum))
    
if __name__ == "__main__":
    main()