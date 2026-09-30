from revise import *
SPECS[3]['code']=SPECS[3]['code'].replace("(29,29)","(31,30)").replace("(34,20)","(36,20)").replace("(35,18),(37,18)","(37,18),(38,18)")
SPECS[6]['code']=SPECS[6]['code'].replace("(4,16)","(4,18)").replace("(44,16)","(44,18)").replace("(4,27)","(4,28)").replace("(24,27)","(24,28)").replace("(44,27)","(44,28)").replace("(11,24),(17,30)","(11,27),(17,29)").replace("(31,24),(37,30)","(31,27),(37,29)")
SPECS[7]['code']=SPECS[7]['code'].replace("(10,21)","(9,21)").replace("(16,6),(10,12)","(15,6),(9,12)").replace("(10,28)","(9,28)").replace("(10,33)","(9,33)").replace("(10,35),(11,36)","(9,35),(11,36)")
SPECS[10]['code']=SPECS[10]['code'].replace("x,22,3)","x,22,2)")
SPECS[13]['code']=SPECS[13]['code'].replace("(34,23),(36,30)","(38,23),(36,30)").replace("((30,20),(25,29),(13,33))","((28,18),(29,26),(24,28))")
SPECS[17]['code']=SPECS[17]['code'].replace("poly('arms',(27,28),(28,24),(32,24),(38,24),(42,28))","poly('arms',(24,24),(32,24),(42,28))")
# Rear facial details require a broader lower mask; use a wider envelope and staggered masks.
SPECS[9]['key']='HRECT_L'
SPECS[9]['code']='''
path('front',(4,8),[('L',(28,8)),('L',(28,20)),('C',(16,30),(28,26),(22,30)),('C',(4,20),(10,30),(4,26)),('L',(4,8))],True)
bez('frown',(13,21),((14,17),(18,17),(19,21)))
path('back',(28,16),[('L',(44,16)),('L',(44,28)),('C',(32,40),(44,36),(40,40)),('C',(20,30),(25,40),(20,36))]);join('front','back')
bez('smile',(31,29),((32,32),(34,32),(35,29)))
'''
SPECS[9]['note']='The current masks are rigid and their expression marks are tiny. No written feedback. Rebalanced the overlap and widened both opposing mouth curves so tragedy and comedy remain distinct; eyes are omitted to preserve clear expression spacing.'
if __name__=='__main__':
 for i in map(int,sys.argv[1:]):make(i)
