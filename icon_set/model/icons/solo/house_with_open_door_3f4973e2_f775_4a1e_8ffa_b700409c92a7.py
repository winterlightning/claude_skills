'Restored the separate doorway frame and angled open leaf, detached from the house baseline. VRECT_L permits sufficient vertical room; tiny handle omitted because it cannot remain separate at this stroke weight. Construction references: door-open (separate frame and angled door).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='3f4973e2-f775-4a1e-8ffa-b700409c92a7'
SOURCE_PATH='pictographic-primitives/other/house door open_3f4973e2-f775-4a1e-8ffa-b700409c92a7.svg'
AUTHOR='gpt-6'
PARENT_MODULE='icon_set/model/icons/solo/house_with_open_door_batch_025_05_3f4973e2_f775_4a1e_8ffa_b700409c92a7.py'
class Drawing(Solo48):
    icon_id='house-with-open-door'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('house door open',)

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
        self.add_polyline('house',(8,44),(8,16),(24,4),(40,16),(40,44),closed=True)
        self.add_polyline('frame',(16,20),(32,20),(32,36))
        self.add_polyline('door',(16,20),(24,24),(24,32),(16,36),closed=True)
        self.relate('connect','frame','door')
