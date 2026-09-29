'The short hooked thumb and broad finger did not read as the source hand. Longer pointing finger, diagonal thumb and coherent rounded palm.\nSymbol plan: enclosure owns content; shared dimensions, radii, repetition and actual attachment nodes.\nConstruction: local Lucide hand original and atomic-debug. Human busts use human_ref/user.svg.\nKeyshape VRECT_L: intended proportional envelope; any departure is separately recorded as a drawing-bound exception.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'effbc2d1-e5a5-4a1b-88be-7ca24a41a9c1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__monitor-heart-beat-touch/20260928T170716Z-thuan-mac/reference/monitor heart beat touch_effbc2d1-e5a5-4a1b-88be-7ca24a41a9c1.svg'
AUTHOR = 'gpt-6'
PARENT_MODULE = 'icon_set/work/primitive-fix-thuan/solo__monitor-heart-beat-touch/20260928T170716Z-thuan-mac/before/monitor_heart_beat_touch_effbc2d1_e5a5_4a1b_88be_7ca24a41a9c1.py'
class Drawing(Solo48):
    icon_id = 'monitor-heart-beat-touch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('monitor', 'heart', 'beat', 'touch')

    def path(self,n,p,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            k=f'{n}-{i}';q=c[1]
            if c[0]=='L':self.add_line(k,p,q)
            elif c[0]=='A':self.add_arc(k,p,q,radius_x=c[2],radius_y=c[3],sweep=c[4])
            elif c[0]=='C':self.add_bezier(k,p,(c[2],c[3],q))
            ids.append(k);p=q
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=4,split=None):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        commands=[]
        for i in range(8):
            q=pts[(i+1)%8]
            if i%2:commands.append(('A',q,rad,rad,True))
            else:
                for p in (split or {}).get(i,[]):commands.append(('L',p))
                commands.append(('L',q))
        self.path(n,pts[0],commands,True)
    def phone(self,l=10,r=38,t=4,b=44,footer=36):
        self.box('phone',l,t,r,b,4,{2:[(r,footer)],6:[(l,footer)]})
        self.add_line('bezel',(l,footer),(r,footer));self.relate('connect','phone','bezel')
    def monitor(self):
        self.box('screen',4,4,44,34,4,{4:[(24,34)]})
        self.add_line('stand',(24,34),(24,44))
        self.add_polyline('base',(16,44),(24,44),(32,44))
        self.relate('connect','screen','stand');self.relate('connect','stand','base')
    def dollar(self,cx=24,top=13):
        # Tangent semicircular bowls; centered currency ticks attach at split nodes.
        y=top
        self.path('dollar',(cx+4,y),[('L',(cx,y)),('L',(cx-1,y)),('A',(cx-1,y+8),4,4,False),('L',(cx+1,y+8)),('A',(cx+1,y+16),4,4,True),('L',(cx,y+16)),('L',(cx-4,y+16))])
        self.add_line('currency-top',(cx,y-3),(cx,y));self.add_line('currency-bottom',(cx,y+16),(cx,y+19))
        self.relate('connect','dollar','currency-top');self.relate('connect','dollar','currency-bottom')

    def build(self):
        # Upper sensor and a continuous anatomical pointing-hand perimeter.
        self.path('sensor',(18,28),[('L',(16,28)),('A',(10,22),6,6,True),('L',(10,14)),('A',(34,14),12,10,True),('L',(34,22)),('A',(28,28),6,6,True),('L',(24,28))])
        self.add_polyline('pulse',(10,14),(16,14),(19,10),(24,16),(27,14),(34,14))
        self.relate('connect','sensor','pulse')
        self.path('hand',(14,44),[('L',(7,37)),('A',(13,31),4,4,True),('L',(18,36)),('L',(18,27)),('L',(18,25)),('A',(24,25),3,3,True),('L',(24,28)),('L',(24,34)),('L',(32,34)),('A',(40,42),8,8,True),('L',(40,44))])
        self.relate('connect','sensor','hand')
