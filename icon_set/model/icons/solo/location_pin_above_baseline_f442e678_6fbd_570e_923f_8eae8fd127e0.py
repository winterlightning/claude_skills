'pin. Pin narrowed from VRECT_L to VRECT_M; bigger circular opening and a longer detached baseline restore the source proportions. Point remains symmetric and clear of the baseline. Construction reference: local Lucide map-pin.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f442e678-6fbd-570e-923f-8eae8fd127e0'
SOURCE_PATH = 'pictographic-primitives/interface-essential/pin_f442e678-6fbd-570e-923f-8eae8fd127e0.svg'
AUTHOR = 'gpt-6'
PARENT_MODULE = 'icon_set/model/icons/solo/location_pin_above_baseline_f442e678_6fbd_570e_923f_8eae8fd127e0.py'
class Drawing(Solo48):
    icon_id = 'location-pin-above-baseline'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('pin',)

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
        self.path('pin',(10,18),[('A',(38,18),14,14,True),('C',(24,36),(38,24),(30,31)),('C',(10,18),(18,31),(10,24))],True)
        self.circle('opening',24,18,5)
        self.add_line('baseline',(12,44),(36,44))

    icon_id = 'location-pin-above-baseline'
    category = 'interface-essential'
    aliases = ()
    keywords = ('pin', 'map', 'location', 'marker', 'place', 'navigation')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
