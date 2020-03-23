def nested_list_sum2(nested_list):
    '''
    Calculate sum of a nested list
    
    Input: Nested List (Lists)
    Output: Sum (Integer)
    
    '''
    
    return sum([int(item.strip('[ [] ]')) 
                for item in str(nested_list).split(',') 
                if item.strip() != '[]'])

def main():
    sample_list = [[7000,[415,[],321],5],6,21,9,[20,32,4],[],[12, [345,[900,12040]],12],11,[0,[],2400,5],19]
    list_sum = nested_list_sum2(sample_list)
    print("sample list = {}; \nsum of items in list = {}".format(sample_list, list_sum))
    
if __name__ == "__main__":
    main()