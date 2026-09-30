from designs_people import *
SPECS[0]['code']='''
poly('kite',(33,6),(42,14),(34,25),(25,14),closed=True)
bez('tail',(34,25),((34,33),(42,35),(42,42)));join('kite','tail')
path('sweets',(6,33),[('C',(11,26),(6,27),(8,25)),('C',(20,26),(11,20),(20,20)),('C',(26,33),(23,25),(26,27))])
line('rim',(6,33),(26,33))
path('bowl',(26,33),[('C',(20,42),(25,39),(24,42)),('L',(12,42)),('C',(6,33),(8,42),(7,39))]);join('rim','bowl','sweets')
'''
SPECS[1]['code']=SPECS[0]['code']
SPECS[2]['code']='''
path('cloud',(17,18),[('L',(11,18)),('A',(11,8),5),('C',(16,6),(11,6),(13,6)),('C',(22,11),(20,6),(22,8))])
poly('kite',(33,18),(42,26),(31,36),(23,26),closed=True)
bez('tail',(31,36),((29,42),(37,42),(42,42)));join('tail','kite')
'''
SPECS[3]['code']='''
poly('block',(6,24),(42,32),(42,42),(6,42),closed=True)
path('left-handle',(10,25),[('L',(21,8)),('C',(26,6),(22,6),(24,6)),('C',(30,12),(30,6),(32,9)),('L',(20,27))]);join('block','left-handle')
path('right-handle',(29,29),[('L',(34,20)),('C',(38,18),(35,18),(37,18)),('C',(42,24),(42,18),(42,21)),('L',(38,31))]);join('block','right-handle')
'''
SPECS[5]['code']='''
for side in (-1,1):
 def p(x,y):return (24+side*(x-24),y)
 n=f'branch{side}'
 path(n,p(14,6),[('C',p(10,16),p(12,8),p(10,12)),('C',p(12,27),p(10,20),p(10,24)),('C',p(18,36),p(13,31),p(15,34)),('L',p(26,42))])
 for j,(a,b) in enumerate([((10,16),(6,8)),((10,16),(18,12)),((12,27),(6,22)),((12,27),(20,22)),((18,36),(8,34)),((18,36),(22,30))]):
  leaf=f'leaf{side}-{j}';line(leaf,p(*a),p(*b));join(leaf,n)
join('branch-1','branch1')
'''
SPECS[5]['note']='The rejected wreath has only two bulky leaf loops per branch. No written feedback. Restyled leaves as six clean strokes along each curved branch, restoring the repeated laurel rhythm and crossed stems without tiny enclosed openings.'
SPECS[6]['code']='''
path('top',(4,16),[('L',(8,10)),('C',(12,8),(9,8),(10,8)),('L',(36,8)),('C',(40,10),(38,8),(39,8)),('L',(44,16)),('L',(4,16))],True)
bez('filling',(4,27),((11,24),(17,30),(24,27)),((31,24),(37,30),(44,27)))
path('bottom',(4,38),[('C',(12,40),(4,40),(8,40)),('L',(36,40)),('C',(44,38),(40,40),(44,40))])
'''
SPECS[6]['note']='The current lasagna has a sharp top and an almost flat bottom dash. No written feedback. Rounded the top pasta corners, centered an even wavy filling, and restored a curved lower pasta edge; omitted the lower closed seam to keep layer gaps clear.'
SPECS[7]['code']=SPECS[7]['code'].replace("('C',(33,22),(32,13),(36,17)),('C',(28,28),(36,26),(32,30))","('C',(31,21),(30,14),(33,17)),('C',(27,27),(33,25),(30,28))").replace("('L',(28,26))","('L',(27,26))")
SPECS[8]['code']='''
path('wrench',(13,42),[('A',(6,35),7),('C',(9,30),(6,33),(7,31)),('L',(20,20)),('C',(30,6),(17,12),(22,6)),('L',(24,14)),('L',(32,22)),('L',(42,12)),('C',(35,27),(42,21),(40,26))])
poly('lightning',(35,27),(20,35),(38,35),(29,42));join('wrench','lightning')
'''
SPECS[9]['key']='SQUARE'
SPECS[9]['code']='''
path('front',(6,6),[('L',(32,6)),('L',(32,23)),('C',(19,37),(32,32),(25,37)),('C',(6,23),(13,37),(6,32)),('L',(6,6))],True)
self.add_dot('eye-left',(15,15));self.add_dot('eye-right',(23,15))
bez('frown',(16,27),((17,24),(21,24),(22,27)))
path('back',(32,15),[('L',(42,15)),('L',(42,30)),('C',(30,42),(42,39),(38,42)),('C',(21,37),(25,42),(22,40))]);join('back','front')
'''
SPECS[9]['note']='The current masks omit eyes and use tiny mouth marks. No written feedback. Enlarged the tragic foreground mask with eyes and a broad frown, keeping a curved second mask behind it. The rear facial details are occluded/simplified for legal spacing.'
SPECS[10]['code']=SPECS[10]['code'].replace('(16,32)','(17,31)').replace("poly('beak',(22,32),(24,35),(26,32))","poly('beak',(22,31),(24,33),(26,31))")
SPECS[12]['code']=SPECS[12]['code'].replace("(16,20)","(15,18)").replace("(33,20)","(33,18)")
SPECS[13]['code']='''
path('outline',(8,37),[('C',(19,18),(12,28),(19,24)),('C',(31,4),(19,7),(24,4)),('C',(40,14),(37,4),(40,8)),('L',(34,12)),('C',(29,34),(34,23),(36,30)),('C',(8,37),(23,39),(13,39))],True)
bez('wing',(19,18),((30,20),(25,29),(13,33)));join('wing','outline')
poly('leg',(27,36),(29,44),(37,44));join('leg','outline')
'''
SPECS[14]['code']=SPECS[14]['code'].replace("('C',(37,18),(42,15),(41,18)),('C',(32,10),(32,18),(31,14))","('C',(38,17),(42,15),(41,17)),('C',(32,10),(34,17),(32,14))")
SPECS[15]['code']=SPECS[15]['code'].replace("(6,30),(6,6)","(6,34),(6,6)").replace("(20,30)","(20,34)").replace("(42,30)","(42,34)")+"\njoin('building','rail');join('shoulders','rail')\n"
SPECS[17]['code']=SPECS[17]['code'].replace("(23,28),(26,24)","(27,28),(28,24)")
SPECS[18]['code']=SPECS[18]['code'].replace("circle('head',10,11,5)","circle('head',11,11,5)").replace("(10,24)","(11,24)").replace("(10,33)","(11,33)").replace("(39,29)","(41,29)").replace("(42,26),(39,27)","(42,26),(41,27)").replace("(33,31)","(33,33)")
SPECS[19]['code']=SPECS[19]['code'].replace("(32,19),(37,28),(40,24),(44,40)","(34,18),(44,40)")
SPECS[19]['note']='The rejected figure is stiff and undersized beside a plain peak. No written feedback. Smoothed the hanging arms around a coherent torso and balanced the mountain against it. The snow seam is omitted because a second line crowds the narrow peak.'
if __name__=='__main__':
 for i in map(int,sys.argv[1:]):make(i)
