path = '''
            |     |          |     |      
            |     |          |     |
            |     |          |     |
            |     |          |     |
            |  1  |          |  2  |
            |     |          |     |
            |     |          |     |
            |     |          |     |
            |     |          |     |
            |     |          |     |
'''



path_2 = '''


                                      
            AAAA                        BBB
           AAAAAA                      BBBBB
          AAAAAAAA                    BBBBBBB
         AAAAAAAAAA                  BBBBBBBBB
        AAAAAAAAAAAA                BBBBBBBBBBB
       AAAAAAAAAAAAAA              BBBBBBBBBBBBBB
      AAAAAAAAAAAAAAAA            BBBBBBBBBBBBBBBB
     AAAAAAAAAAAAAAAAAA          BBBBBBBBBBBBBBBBBB
    AAAAAAAAAAAAAAAAAAAA        BBBBBBBBBBBBBBBBBBBB
   AAAAAAAAAAAAAAAAAAAAAA      BBBBBBBBBBBBBBBBBBBBBBB 




'''




path_3 = '''

            0000000000000     11111111111111     222222222222222
            0           0     1            1     2             2
            0           0     1            1     2             2
            0           0     1            1     2             2
            0         0 0     1          1 1     2          2  2
            0           0     1            1     2             2
            0           0     1            1     2             2
            0           0     1            1     2             2
            0           0     1            1     2             2
            0000000000000     11111111111111     222222222222222
            
            
'''
            
path_4 = '''

          =====================================================
          =                         11
          =
          =====================================================
          =                          10
          =
          =====================================================
          =                          9
          =
          =====================================================
          =                         8
          =
          =====================================================
          =                         7
          =
          =====================================================
          =                         6
          =
          =====================================================
          =                         5
          =
          =====================================================
          =                         4
          =
          =====================================================
          =                       3
          =
          =====================================================
          =                         2
          =
          =====================================================
          =                       1
          =
          =====================================================


'''



path_5 = '''


            00000000000000000010000000000000000000000000000000000
            00000000000000000000000000000000000000000000000000000
            00000000000000000000000000000000000000000000000100000
            00000000000000000000000000000000000000000000000000000
            00000000000000000000000000000000000000000000000000000
            00000000000000000000000000000000000000001000000000000
            00000000000000000000000000000000000000000000000000000
            00000000000000000000000000000000000000000000000000000
            00000000000000000000000000000000000000000000000000000
            00000000000001000000000000000000000000000000000000000
            00000000000000000000000000000000000000000000000000000
            00000000000000000000000000000000000000000000000000000
            00000000000000000000000000000000000000000000000000000
            00000000000000000000000000000000010000000000000000000
            00000000000000000000000000000000000000000000000000000
            00000000000000000000000000000000000000000000000000000
            00000000000000000000000000000000000000000000000000000
            00000000000000000000000000000000000000000000000000000
'''


escape = '''


            ????????????????????????????????????   ???                                          ???
            ???                         ???                            ?????????????????????????????????????????? 
            ???                         ???                                         ??????
            ???                         ???                                       ???    ???
            ????????????????????????????????????   ????????????????????????                        ???      ???
            ???                         ???                                     ???        ??? 
            ???                         ???                                    ???          ???
            ???                         ???                                   ???            ???
            ???                         ???                                  ???               ???
            ????????????????????????????????????   ???                          ??????????????????????????????????????????????????????
                                                                                    ???
            ?????????????????????????????????????????????                                          ???
                                        ???                                          ???
                                        ???                                          ???
                                        ???                                          ???
                                        ???                                          ???
                                        ???                        ?????????????????????????????????????????????????????????
            ?????????????????????????????????????????????                                                            ???
            ???                                                                                        ???
            ???                                                                                        ???
            ???                                                    ?????????????????????????????????????????????????????????
            ???                                                    ???
            ???                                                    ???
            ?????????????????????????????????????????????                        ?????????????????????????????????????????????????????????


'''








import random


print("????????? ????????? ???????????????.")
print("??????????????? ????????? 5?????? ?????? ??????????????? ?????????.")
print("3?????? ???????????? ???????????? ????????? ??? ??????????????? ????????????.")
print("???????????? ????????? ??? ?????? 5?????? ????????? ???????????????.")
print("####???????????? ????????? 4?????? ????????? ??? ??? ????????? ????????? ?????? ???????????????")
print(path)
right_path = random.randint(1,2)

choice = int(input("2?????? ?????? ????????????. ?????? ?????? ??????????????????? "))

if choice == right_path:
    print("???????????????!!")
    print("??? ?????? ????????? ???????????????.")

    print(path_2)
    right_path = random.randint(1,2)
    choice = int(input("A??? B??? ??? ?????? ??? ?????? ????????? ?????????????????????? [A?????? = 1??? B?????? = 2???] "))
    if choice == right_path:
        print("???????????????!!")
        print("??? ?????? ????????? ???????????????. ??????????????? ???????????? ????????? ??? ??????????????? ????????????.")

        print(path_3)
        right_path = random.randint(1,2)
        short_path = 0
        choice = int(input("0,1,2??? ??? ?????? 3?????? ??????. ??? ??? ??? ?????? ??????????????? ????????? 5?????? ????????? ??? ??? ??????. ?????? ?????? ?????? ???????????????? "))

        if choice == right_path:
            print("???????????????!! but ???????????? ???????????? ^^")
            print("4?????? ????????? ????????????!!")

            print(path_4)
            right_path = random.randint(1,11)
            choice = int(input("11????????? ??? ???????????? ????????????. ?????? ????????? ???????????? 5?????? ????????? ??? ??? ????????????? "))
            if choice == right_path:
                print("????????? ????????? ????????? ??????????????????!")
                print("????????? 5?????? ????????? ?????????????????????!")
                print("????????? ??????????????? ????????? 1??? ?????? ???????????? ?????? ????????????.")
                print("???????????? ????????? ????????? ????????? ????????????.")

                print(path_5)

                right_path = 5
                choice = int(input("????????? 1??? ????????? ????????????????  "))
                if choice == right_path:
                    print(escape)
                else:
                    print("????????? ???????????? ????????????...")
            else:
                print("????????? ????????????..")
                
               
                    
            
        elif choice == short_path:
            print("???????????? ??????????????????!!")
            print("5?????? ????????? ???????????????!")

            print("????????? ??????????????? ????????? 1??? ?????? ???????????? ?????? ????????????.")
            print("???????????? ????????? ????????? ????????? ????????????!")

            print(path_5)
            right_path = 5
            choice = int(input("????????? 1??? ????????? ???????????????? "))
            if choice == right_path:
                print(escape)
            else:
                print("????????? ???????????? ????????????..")
                        

            
            
        else:
            print("????????????..????????? ????????????..")
    else:
        print("3?????? ????????? ??? ???????????? ????????????")
        
        
else:
    print("?????? ??????????????????..")

































