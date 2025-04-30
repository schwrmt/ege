print ("x y z w f")
for x in range (2):
    for y in range (2):
        for z in range(2):
            for w in range(2):
                f = ((y <= x) == ( w <= (not z) )) and ( w or x)
                print (x, y, z, w, int(f))