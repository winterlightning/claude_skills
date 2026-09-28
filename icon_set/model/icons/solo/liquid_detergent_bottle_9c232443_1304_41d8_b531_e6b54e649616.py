'Restored the angled rounded cap, nozzle and rounded flat-bottom drop label. VRECT_L gives the label room below the cap; all defining elements preserved, with the cap raised for clearance. Construction references: droplet (rounded label) and soap-dispenser-droplet (cap and nozzle).'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9c232443-1304-41d8-b531-e6b54e649616'
SOURCE_PATH='pictographic-primitives/wayfinding/liquid detergent_9c232443-1304-41d8-b531-e6b54e649616.svg'
AUTHOR='gpt-6'
PARENT_MODULE='icon_set/model/icons/solo/liquid_detergent_bottle_9c232443_1304_41d8_b531_e6b54e649616.py'
class Drawing(Solo48):
    icon_id='liquid-detergent-bottle'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases=()
    keywords=('liquid detergent',)

    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            k=f'{n}-{i}';end=c[1]
            if c[0]=='L':self.add_line(k,start,end)
            elif c[0]=='A':self.add_arc(k,start,end,radius_x=c[2],radius_y=c[3],sweep=c[4])
            elif c[0]=='C':self.add_bezier(k,start,(c[2],c[3],end))
            ids.append(k);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        self.path('bottle',(12,44),[('A',(8,40),4,4,True),('L',(8,30)),('C',(16,14),(8,26),(12,14)),('L',(30,18)),('C',(40,32),(36,20),(40,28)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44))],True)
        self.path('cap',(16,14),[('L',(19,7)),('C',(28,7),(21,3),(25,6)),('C',(33,11),(31,8),(34,8)),('L',(30,18))]);self.relate('connect','cap','bottle')
        self.add_line('nozzle',(28,7),(30,4));self.relate('connect','cap','nozzle')
        self.path('label',(24,25),[('C',(18,31),(21,25),(18,28)),('L',(18,32)),('A',(21,35),3,3,False),('L',(27,35)),('A',(30,32),3,3,False),('L',(30,31)),('C',(24,25),(30,28),(27,25))],True)

    icon_id = 'liquid-detergent-bottle'
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('liquid', 'detergent', 'bottle')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
