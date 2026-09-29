from author_last import *
# Further native-size repairs. Each is authored into a fresh result folder.
SPECS[2]['body']='''
# Two shallow water waves; propeller crossbars and shafts remain visible.
for j,x in enumerate((4,24)):
    curve(self,f'wave-{j}',(x,5),((x+6,11),(x+14,11),(x+20,5)))
for x in (10,38):
    self.add_line(f'propeller-{x}',(x-5,16),(x+5,16))
    self.add_line(f'shaft-{x}',(x,16),(x,24))
    self.relate('connect',f'propeller-{x}',f'shaft-{x}')
curve(self,'body',(4,25),((6,25),(8,24),(10,24)),((15,24),(17,21),(24,21)),((31,21),(33,24),(38,24)),((40,24),(42,25),(44,25)),((46,25),(46,31),(44,31)),((38,31),(32,35),(24,35)),((16,35),(10,31),(4,31)),((2,31),(2,25),(4,25)),closed=True)
for x in (10,38):self.relate('connect','body',f'shaft-{x}')
curve(self,'pod',(4,31),((11,31),(14,36),(14,39)),((14,44),(34,44),(34,39)),((34,36),(37,31),(44,31)))
self.relate('connect','body','pod')
'''
SPECS[3]['body']='''
# Two rows of four crowns; facing bite edges are 8 units apart.
for jaw in ('upper','lower'):
    def p(x,y):return (x,y if jaw=='upper' else 48-y)
    curve(self,jaw+'-gum',p(4,20),(p(4,16),p(4,10),p(4,7)),(p(15,3),p(33,3),p(44,7)),(p(44,10),p(44,16),p(44,20)))
    self.add_line(jaw+'-bite',p(4,20),p(44,20))
    self.relate('connect',jaw+'-gum',jaw+'-bite')
    for j,x in enumerate((4,14,24,34)):
        curve(self,f'{jaw}-crown-{j}',p(x,14),(p(x+2,9),p(x+8,9),p(x+10,14)))
        if j:
            self.add_line(f'{jaw}-division-{j}',p(x,14),p(x,20))
            for part in (f'{jaw}-crown-{j}',f'{jaw}-crown-{j-1}',jaw+'-bite'):
                self.relate('connect',f'{jaw}-division-{j}',part)
            self.relate('connect',f'{jaw}-crown-{j}',f'{jaw}-crown-{j-1}')
        if j in (0,3):self.relate('connect',jaw+'-gum',f'{jaw}-crown-{j}')
'''
SPECS[8]['body']='''
# Diagonal pair of enclosed A/B buttons and separate outlined D-pad.
circle(self,'button-a',12,25,10)
circle(self,'button-b',35,13,11)
self.add_polyline('a',(9,29),(12,21),(15,29))
self.add_line('a-bar',(10,27),(14,27));self.relate('connect','a','a-bar')
self.add_line('b-stem',(32,7),(32,19))
curve(self,'b',(32,7),((40,7),(40,13),(32,13)),((40,13),(40,19),(32,19)))
self.relate('connect','b-stem','b')
self.add_polyline('dpad',(30,28),(38,28),(38,33),(44,33),(44,41),(38,41),(38,46),(30,46),(30,41),(24,41),(24,33),(30,33),closed=True)
'''
SPECS[8]['omissions']=['Omitted the D-pad center circle so its opening stays clear at 48px.']
for i in (10,11):
 SPECS[i]['body']=SPECS[i]['body'].replace('(14,28),(14,36)','(14,31),(14,37)').replace('(10,32),(18,32)','(11,34),(17,34)')
 SPECS[i]['body']=SPECS[i]['body'].replace('(14,37),(17,37)','(14,40),(17,40)').replace('(21,37),(27,37),(31,37)','(21,40),(27,40),(31,40)').replace('(34,37),(37,43)','(34,40),(37,43)')
# Team bust shoulders exactly tangent in ink (head r4 bottom11; shoulder top15).
SPECS[10]['body']=SPECS[10]['body'].replace("curve(self,f'shoulders-{j}',(cx-6,20),((cx-6,13),(cx+6,13),(cx+6,20)))", "self.add_arc(f'shoulders-{j}',(cx-6,21),(cx+6,21),radius_x=6)\n    self.relate('connect',f'head-{j}',f'shoulders-{j}')")
# Shoulder arcs at y15 tangent to circular head ink; mark as bust construction.
SPECS[10]['human_construction']='bust'
SPECS[9]['body']='''
rounded(self,'monitor',4,4,34,25,3)
self.add_line('stand',(15,25),(15,32));self.add_line('foot',(8,32),(21,32));self.relate('connect','monitor','stand');self.relate('connect','stand','foot')
# The reference game character is kept; at this scale the pad retains one action button.
self.add_arc('pac-arc',(22,10),(22,20),radius_x=6,large_arc=True,sweep=False)
self.add_line('pac-mouth-1',(22,20),(17,15));self.add_line('pac-mouth-2',(17,15),(22,10));self.add_contour('pacman','pac-arc','pac-mouth-1','pac-mouth-2',closed=True)
curve(self,'cable',(34,16),((44,16),(44,24),(37,30)));self.relate('connect','monitor','cable')
curve(self,'controller',(21,34),((25,31),(32,30),(37,30)),((44,30),(47,38),(42,42)),((38,46),(34,40),(31,41)),((26,42),(24,46),(20,44)),((14,41),(16,36),(21,34)),closed=True)
self.relate('connect','cable','controller')
self.add_dot('button',(36,35))
'''
SPECS[9]['change']='Restored the on-screen game character, monitor stand, connecting cable and a clear angled gamepad silhouette with one action button.'
SPECS[9]['omissions']=['Used one gamepad action button; omitted a tiny D-pad that crowded the foreground grip.']
SPECS[14]['body']=SPECS[14]['body'].replace("self.relate('connect','torso','raised-arm','rear-leg','front-leg')", "for part in ('raised-arm','rear-leg','front-leg'):self.relate('connect','torso',part)\nself.relate('connect','rear-leg','front-leg')")
# Restore a true sun arc behind the cloud; rays have short but visible air gaps.
SPECS[15]['body']='''
self.add_arc('sun',(9,23),(25,16),radius_x=8,large_arc=True)
self.add_line('ray-top',(15,2),(15,3))
self.add_line('ray-left',(2,15),(3,15))
self.add_line('ray-diagonal',(4,5),(5,6))
curve(self,'cloud',(22,37),((16,37),(8,38),(6,32)),((2,26),(8,20),(14,21)),((16,11),(29,10),(33,20)),((38,20),(41,22),(42,25)))
curve(self,'pin',(35,44),((31,39),(26,34),(26,30)),((26,18),(44,18),(44,30)),((44,34),(39,39),(35,44)),closed=True)
circle(self,'pin-hole',35,29,3)
'''
SPECS[16]['body']=SPECS[16]['body'].replace("self.relate('connect','torso','leg','arm')", "self.relate('connect','torso','leg');self.relate('connect','torso','arm')").replace('((17,47),(27,42),(27,35))','((17,47),(25,42),(25,37))')
SPECS[17]['body']='''
curve(self,'body',(14,16),((14,2),(34,2),(34,16)),((34,18),(35,21),(35,23)),((36,31),(39,36),(43,40)),((44,44),(35,43),(31,39)),((26,44),(18,44),(13,39)),((9,44),(3,44),(5,40)),((6,38),(8,36),(9,34)),((12,29),(13,25),(13,23)),((13,21),(14,18),(14,16)),closed=True)
curve(self,'left-flipper',(13,39),((17,36),(18,33),(18,31)))
curve(self,'right-flipper',(31,39),((27,36),(26,33),(26,31)))
self.relate('connect','body','left-flipper');self.relate('connect','body','right-flipper')
self.add_polyline('tail',(9,34),(4,26),(9,27),(11,22),(13,27))
self.relate('connect','tail','body')
for name,a,b in [('left-top',(14,16),(7,14)),('left-low',(13,23),(6,25)),('right-top',(34,16),(41,14)),('right-low',(35,23),(42,25))]:
    self.add_line(name,a,b)
    self.relate('connect','body',name)
'''
SPECS[19]['body']=SPECS[19]['body'].replace("(25,29),(19,36),(24,36),(23,41),(30,33),(25,33)","(26,29),(20,35),(24,35),(22,39),(28,33),(24,33)")

def refine(i):
 r=BATCH[i];prior=sorted((REPO/'icon_set/work/primitive-make-ray'/r['uuid']).glob('20260929T090411Z-meaning-*'))[-1]
 attempt=f'{int(prior.name[-2:])+1:02d}';dest=write(i,attempt)
 if SPECS[i].get('human_construction'):
  p=next(dest.glob('*.py'));p.write_text(p.read_text().replace('    aliases = ()','    human_construction = "bust"\n    aliases = ()'))
if __name__=='__main__':
 for i in map(int,sys.argv[1:]):refine(i)
