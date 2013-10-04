#! /usr/bin/env python


def show_index_list(name,the_list):
    print
    for index in range(len(the_list)):
        print "%s[%d] = %s" % (name,index,the_list[index])


fruits = ["apple","bannan","cherry","date"]
show_index_list("fruits",fruits)


fruits.append("elderberry")
show_index_list("fruits",fruits)

fruits.insert(0,"zuchinni")
show_index_list("fruits",fruits)
 
fruits.sort()
show_index_list("fruits",fruits)
