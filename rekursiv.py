def sanash(son):
    if son == 0:
        return 
    print(son)
    sanash(son-1)

sanash(20)