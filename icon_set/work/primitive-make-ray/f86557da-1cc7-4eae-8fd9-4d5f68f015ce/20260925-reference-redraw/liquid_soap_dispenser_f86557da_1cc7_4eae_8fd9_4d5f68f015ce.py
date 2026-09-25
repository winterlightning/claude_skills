'Corrected the concept from oxygen cylinder to liquid soap dispenser, following the visual reference. Restored a separate rectangular neck below the stem and T-shaped pump. VRECT_M keeps the bottle upright; body is broader and shorter than the source to preserve the three stacked structures. Construction references: soap-dispenser-droplet (separate pump, neck and body).'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f86557da-1cc7-4eae-8fd9-4d5f68f015ce'
SOURCE_PATH='pictographic-primitives/beauty/oxygen tank_f86557da-1cc7-4eae-8fd9-4d5f68f015ce.svg'
AUTHOR='gpt-6'
PARENT_MODULE='icon_set/model/icons/solo/oxygen_cylinder_with_t_valve_f86557da_1cc7_4eae_8fd9_4d5f68f015ce.py'
class Drawing(Solo48):
    icon_id='liquid-soap-dispenser'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('oxygen tank',)

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
        self.path('bottle',(18,20),[('L',(24,20)),('L',(30,20)),('A',(38,28),8,8,True),('L',(38,40)),('A',(34,44),4,4,True),('L',(14,44)),('A',(10,40),4,4,True),('L',(10,28)),('A',(18,20),8,8,True)],True)
        self.add_polyline('neck',(18,20),(18,12),(24,12),(30,12),(30,20));self.relate('connect','neck','bottle')
        self.add_line('stem',(24,4),(24,12));self.add_polyline('pump',(18,4),(24,4),(30,4));self.relate('connect','stem','neck');self.relate('connect','stem','pump')
