# # # # # # x = 25
# # # # # #
# # # # # # if x % 5 == 0:
# # # # # #     print("5", end='')
# # # # # # if x % 10 == 0:
# # # # # #     print("10", end='')
# # # # # # if x % 25 == 0:
# # # # # #     print("25", end='')
# # # # # #####OUTPUT 525
# # # # #
# # # # # x = 25
# # # # #
# # # # # if x % 5 == 0:
# # # # #     print("5", end = '')
# # # # #     if x % 10 == 0:
# # # # #         print("10", end='')
# # # # #         if x % 25 == 0:
# # # # #             print("25",end='')
# # # # # ####OUTPUT 5
# # # #
# # # # #
# # # # # x = 25
# # # # # if x % 25 == 0:
# # # # #     print("25", end ='')
# # # # # elif x % 5 == 0:
# # # # #     print("5", end ='')
# # # # # else:
# # # # #     print("10", end ='')
# # # #
# # # # #####OUTPUT 25
# # # #
# # # # #
# # # # # X = "A"
# # # # # X = X*2
# # # # # print(X)
# # # # # #####OUTPUT AA
# # # # #
# # # # # y = 8
# # # # # z = 9
# # # # # print(str(y) + str(z))
# # # # #
# # # # # ####OUPUT 89
# # # # #
# # # # # x, y = 12, 26
# # # # #
# # # # # if 0 <= x <= y:
# # # # #     if x <= 20 and y < 50:
# # # # #         x = x // 10
# # # # #         if y > 50:
# # # # #             x += 1
# # # # #         y = y - 5
# # # # #     else:
# # # # #         y -= 1
# # # # # else:
# # # # #     y -= x
# # # # # print(x + y)
# # # #
# # # # #####OUTPUT 22
# # # #
# # # #
# # # # # x = 3
# # # # # y = 4
# # # # # if x == 2 and y == 3 or y == 4 or y == 5:
# # # # #     print("X")
# # # # # elif (x == 3 ) and (y == 3 or y == 4 or y == 5):
# # # # #     print('Y')
# # # # # else:
# # # # #     print('Z')
# # # #
# # # # ### and is first
# # # # #### if (x == 2 and y == 3) or (y == 4) or (y == 5)
# # # #
# # # # #
# # # # # x = 5
# # # # # y = 10
# # # # #
# # # # # a = 5 if (x+y) % 10 == 0 else 95
# # # # # print(a)
# # # # #
# # # # # ####OUTPUT 95
# # # # #
# # # # #
# # # # # sum = 0
# # # # # for i in range(1,4):
# # # # #     for j in range(1,i):
# # # # #         sum += i * j
# # # # # print(sum)
# # # # #
# # # # # #####OUTPUT 11 REVIEW !!!!!
# # # # #
# # # # #
# # # # # sum = 0
# # # # # for i in range(1,4):
# # # # #     for j in range(1,i):
# # # # #         sum += i * j
# # # # #         break
# # # # # print(sum)
# # # # # #####OUTPUT 5
# # # # #
# # # # # sum = 0
# # # # # for i in range(1,4):
# # # # #     for j in range(1, i):
# # # # #         sum += i * j
# # # # #     break
# # # # # print(sum)
# # # # #
# # # # # #####OUTPUT 0
# # # # #
# # # # #
# # # # #
# # # # # sum, product = 0, 0
# # # # # while True:
# # # # #     if sum == product:
# # # # #         product = product * sum
# # # # #         continue
# # # # #     if sum == (prouct * 2):
# # # # #         break
# # # # #     sum = sum + 1
# # # # # print(str(sum) + " " + str(product))
# # # # #
# # # # # ##### OUTPUT infinite loop
# # # # #
# # # # #
# # # # # a = 5
# # # # # for i in range(5):
# # # # #     x = x + a
# # # # # print(x)
# # # #
# # # # #### x is not defined OUTPUT ERROR
# # # #
# # # # x = 0
# # # # for i in range(5):
# # # #     x = x + i
# # # # print(x)
# # # #
# # # # #### OUTPUT 10
# # # #
# # # # def num_find(x):
# # # #     x = x+1
# # # #
# # # # x = 5
# # # # print(num_find(x))
# # # #
# # # # #### no return therefore it will print NONE
# # # #
# # # #
# # # # def pattern(n):
# # # #     for i in range(1, n+1):
# # # #         for j in range(1,n+1):
# # # #             if i + j >= n + 1:
# # # #                 print("*", end = "")
# # # #             else:
# # # #                 print(" ", end = "")
# # # #         print()
# # # # pattern(5)
# # #
# # #
# # # #List are mutable
# # # #Tuple is immutable
# # #
# # # # a = (12, 56, 90,23)
# # # # b = (2,3,4)
# # # # c = a + b
# # # # print(c)
# # # # a_list = list(a)
# # # # print(a_list)
# # #
# # # # a = 12,
# # # # b = (12,)
# # # # c = (12, 1, 6, 9)
# # # # d = a + b
# # # #
# # # # print(d)
# # # # print(c[1:3])
# # # # e = list(d)
# # # # e[0] = 3
# # # # print(e)
# # #
# # #
# # # # my_tup = (12, 56, 90, 23)
# # # # # a,b,c,d = my_tup
# # # # *a, b = my_tup
# # # # print(a,b)
# # # # # print(a,b,c,d)
# # #
# # # # print([12, 34] * 3)
# # # # print(4 in [1,2,4])
# # # # # in checks if True or False
# # # # print(len((2,4,6,7)))
# # # # print(sum((2,4,6,7)))
# # # # print(min((2,4,6,7)))
# # # # print((1,2,2,3,2). count(2))
# # #
# # #
# # # # Keys are immutable
# # # my_dict = {"name": "John", "age" : 21}
# # # print(my_dict["name"])
# # # my_dict["name"] = "Sally"
# # # print(my_dict)
# # # my_dict["address"] = "Gainesville"
# # # print(my_dict)
# # # del my_dict["name"]
# # # print(my_dict)
# # #
# # # for key, value in my_dict.items():
# # #     print(f"{key}, {value}")
# #
# # # x = (22,67,45,23)
# # # a,b = x
# # # print(b)
# # # #####ERROR
# #
# # # my_dict = {'name':'tim', 'age':21, }
# # # my_dict['height']=5.5
# # # del my_dict['name']
# # # my_dict['age'] =my_dict['age'] + my_dict['height']
# # # print(my_dict['age'])
# # # ##########26.5
# # #
# # #
# # # a = [2, (7, 'joe'), 'welcome',6]
# # # print(a[1][-1],a[-2][-3],a[0:-3],a[3:1:-2])
# # #
# # # #set is unordered collection of elements NO INDEXING MUTABLE
# # # a = {1,2,3}
# # # b = set([4,5,6])
# # # c = a.union(b)
# # # print(a,b,c)
# # #
# # # a = {2,3,4}
# # # b ={3,4,5}
# # # e = a.intersection(b)
# # # print(a,b,e)
# # #
# # # h = a.difference(b)
# # # print(a,b,h)
# # #
# # # a_list = [1,3,10,8,45]
# # # a,b,*c,d = a_list
# # # print(b,c)
# # #
# # # a = [1,5] + [3]
# # # a.append(1)
# # # a.extend([1,3])
# # # b = set(a)
# # # print(b)
# # # #Sets have only unique elements so no repeating numbers
# # #
# # # info = {'major':'computer science', 'age':21}
# # # info['name']='robert'
# # # print(info['age'],'name' in info, len(info), len(info['name']), 'robert' in info)
# #
# # #Membership Operators: in and not in
# # #Identity operators: is and is not
# # #
# # # a = [1,2,3] #Mutable
# # # b = [1,2,3]
# # # print(a is b)
# # #
# # # a = (1,2,3) # Immutable so it has the same ID
# # # b = (1,2,3)
# # # print(a is b)
# # #
# # # a = [2,(7,'Joe'), 'welcome', [6, 3], 5]
# # # print(a[3])
# #
# # def consecutive_four(my_list):
# #     count = 1
# #     for i in range(len(my_list)-1):
# #         if my_list[i] == my_list[+1]:
# #             count += 1
# #             if count == 4:
# #                 return True
# #         else:
# #             count = 1
# #     return False
# #
# # print(consecutive_four([3,3,3,5,5,5]))
# # print(consecutive_four([5,5,3,3,3,5,5,5]))
# #
# # def sum_by_parity(my_list):
# #     sum_even = 0
# #     sum_odd = 0
# #     for i in range(len(my_list)):
# #         if i % 2 == 0:
# #             sum_even += my_list[i]
# #         else:
# #             sum_odd += my_list[i]
# #
# #     return [sum_even, sum_odd]
# #
# # print(sum_by_parity([3,4,5,6,3,2]))
# #
# # def expan_by_index(my_list):
# #     new_list = []
# #     for i in range(len(my_list)):
# #         for j in range(my_list[i]):
# #             new_list.append(i)
# #     return new_list
# #
# # print(expan_by_index([2,1,3]))
# #
# # tuple_example = [1, (2,3), 'Hello']
# # tuple_example[1][0] = 4
# # print(tuple_example[1])
# # ##########ERROR TUPLES ARE IMMUTABLE
# #
#
#
# class Student:
#
#
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade = grade
# s = Student("Shannon", 98)
# print(Student.s)
# print(s.name)

class Monster:
    def __init__(self,level=1,name="Monster"):

        from cow import Cow
        from dragon import Dragon
        from ice_dragon import IceDragon

        class HeiferGenerator:
            cow_names = ['heifer', 'kitteh']

            quote_lines = '    \\\n'
            quote_lines += '     \\\n'
            quote_lines += '      \\\n'

            cowImages = ["        ^__^\n" +
                         "        (oo)\\_______\n" +
                         "        (__)\\       )\\/\\\n" +
                         "            ||----w |\n" +
                         "            ||     ||\n",

                         "       (\"`-'  '-/\") .___..--' ' \"`-._\n" +
                         "         ` *_ *  )    `-.   (      ) .`-.__. `)\n" +
                         "         (_Y_.) ' ._   )   `._` ;  `` -. .-'\n" +
                         "      _.. `--'_..-_/   /--' _ .' ,4\n" +
                         "   ( i l ),-''  ( l i),'  ( ( ! .-'\n"
                         ]

            dragon_names = ['dragon', 'ice-dragon']
            dragon_types = [Dragon, IceDragon]

            dragon_image = "           |\\___/|       /\\  //|\\\\\n" + \
                           "           /0  0  \\__   /  \\// | \\ \\\n" + \
                           "          /     /  \\/_ /   //  |  \\  \\\n" + \
                           "          \\_^_\\'/   \\/_   //   |   \\   \\\n" + \
                           "          //_^_/     \\/_ //    |    \\    \\\n" + \
                           "       ( //) |        \\ //     |     \\     \\\n" + \
                           "     ( / /) _|_ /   )   //     |      \\     _\\\n" + \
                           "   ( // /) '/,_ _ _/  ( ; -.   |    _ _\\.-~       .-~~~^-.\n" + \
                           " (( / / )) ,-{        _      `.|.-~-.          .~         `.\n" + \
                           "(( // / ))  '/\\      /                ~-. _.-~      .-~^-.  \\\n" + \
                           "(( /// ))      `.   {            }                 /      \\  \\\n" + \
                           " (( / ))     .----~-.\\        \\-'               .~         \\  `.   __\n" + \
                           "            ///.----..>        \\            _ -~            `.  ^-`  \\\n" + \
                           "              ///-._ _ _ _ _ _ _}^ - - - - ~                   `-----'\n"

            cows = None

            @staticmethod
            def get_cows():
                if HeiferGenerator.cows is None:
                    HeiferGenerator.cows = [None] * (len(HeiferGenerator.cow_names) + len(HeiferGenerator.dragon_names))
                    # add the 'regular' cows
                    num_regular = len(HeiferGenerator.cow_names)
                    for index in range(num_regular):
                        HeiferGenerator.cows[index] = Cow(HeiferGenerator.cow_names[index])
                        HeiferGenerator.cows[index].image = HeiferGenerator.quote_lines + HeiferGenerator.cowImages[
                            index]

                    # add the dragons
                    for index in range(len(HeiferGenerator.dragon_names)):
                        HeiferGenerator.cows[num_regular + index] = HeiferGenerator.dragon_types[index](
                            HeiferGenerator.dragon_names[index],
                            HeiferGenerator.quote_lines + HeiferGenerator.dragon_image
                        )

                return HeiferGenerator.cows