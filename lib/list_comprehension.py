#!/usr/bin/env python3

def return_evens(num_list):
    # if([(num_list/2) for num_list in num_list]):
    #     return []
    # elif([(num_list/2) for num_list in num_list]&(num_list>0)):
    #     return num_list
    return [n for n in num_list if n%2==0]

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]