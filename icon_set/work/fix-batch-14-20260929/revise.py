from author import *
D['person-with-flower']['code']=D['person-with-flower']['code'].replace("(28,30),(35,34),(42,30)","(30,31),(35,35),(42,31)").replace("(35,34)","(35,35)")
D['person-with-circular-object']['code']=D['person-with-circular-object']['code'].replace("oval('object',28,38,4,4)","oval('object',28,39,3,3)")
D['person-with-monocle-and-necktie']['code']="""
oval('face',24,16,12,12)
path('shoulders',(8,44),[('L',(8,40)),('A',(16,32),8,8,True),('L',(24,32)),('L',(32,32)),('A',(40,40),8,8,True),('L',(40,44))]);join('face','shoulders')
oval('monocle',25,16,2,2);line('temple',(27,16),(36,16));join('temple','face');join('temple','monocle')
poly('tie',(24,32),(18,38),(24,44),(30,38),(24,32));join('tie','shoulders')
"""
D['oval-amulet-with-teardrop-inset']['shape']='VRECT_L'
D['oval-amulet-with-teardrop-inset']['code']="""
path('pendant',(18,14),[('L',(30,14)),('C',(40,28),(36,14),(40,21)),('C',(24,44),(40,37),(33,44)),('C',(8,28),(15,44),(8,37)),('C',(18,14),(8,21),(12,14))],True)
path('loop',(18,14),[('L',(18,10)),('A',(30,10),6,6,True),('L',(30,14))]);join('loop','pendant')
path('drop',(24,23),[('C',(30,31),(27,25),(30,29)),('C',(18,31),(30,37),(18,37)),('C',(24,23),(18,29),(21,25))],True)
"""
D['portrait-with-bob-hair-and-pendant-collar-batch-086']['shape']='SQUARE'
D['portrait-with-bob-hair-and-pendant-collar-batch-086']['code']="""
path('bob',(9,27),[('L',(6,27)),('L',(6,24)),('A',(42,24),18,18,True),('L',(42,27)),('L',(39,27))])
oval('face',24,22,7,7)
path('shoulders',(6,42),[('A',(24,33),18,9,True),('A',(42,42),18,9,True)]);join('face','shoulders')
line('pendant',(22,42),(26,42))
"""
D['portrait-with-bob-hair-and-pendant-collar-batch-086']['issue']='The rejected portrait has a narrow open hair arch and dot ornament. Broaden the bob, restore its flat ends and show a small horizontal pendant below the shoulder arch.'
D['portrait-with-bob-hair-and-pendant-collar-batch-086']['omissions']='Reduce three necklace ornaments to one pendant bar; omit the tiny facial mark.'
D['padded-infant-car-seat']['code']="""
path('shell',(24,6),[('C',(38,18),(38,6),(38,12)),('L',(38,22)),('C',(42,32),(38,28),(42,29)),('A',(32,42),10,10,True),('L',(24,42)),('L',(16,42)),('A',(6,32),10,10,True),('C',(10,22),(6,29),(10,28)),('L',(10,18)),('C',(24,6),(10,12),(10,6))],True)
poly('harness',(10,18),(24,30),(38,18));join('harness','shell')
line('seat-seam',(24,30),(24,42));join('seat-seam','harness');join('seat-seam','shell')
"""
if __name__=='__main__':generate(sys.argv[1:])
