'The monitor was narrow and short, and its source proportions were lost. Broader/taller screen with rounded corners and longer stand; retained plus and divide.\nSymbol plan: enclosure owns content; shared dimensions, radii, repetition and actual attachment nodes.\nConstruction: local Lucide monitor original and atomic-debug. Human busts use human_ref/user.svg.\nKeyshape SQUARE: intended proportional envelope; any departure is separately recorded as a drawing-bound exception.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6cbe1bf6-f7d0-4add-99b4-0d1a57f47f13'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__monitor-math/20260928T170716Z-thuan-mac/reference/monitor math_6cbe1bf6-f7d0-4add-99b4-0d1a57f47f13.svg'
AUTHOR = 'gpt-6'
PARENT_MODULE = 'icon_set/work/primitive-fix-thuan/solo__monitor-math/20260928T170716Z-thuan-mac/before/monitor_math_6cbe1bf6_f7d0_4add_99b4_0d1a57f47f13.py'
class Drawing(Solo48):
    icon_id = 'monitor-math'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('monitor', 'math')

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
        self.monitor()
        self.add_polyline('plus-h',(12,23),(17,23),(22,23))
        self.add_polyline('plus-v',(17,18),(17,23),(17,28));self.relate('connect','plus-h','plus-v')
        self.add_line('division-bar',(29,17),(36,17))
        self.add_dot('division-top',(32,10));self.add_dot('division-bottom',(32,24))

# Exact-drawing visual exception; automatic findings remain in automatic-gate.json.
Drawing.exception = {'reason': 'User authorized agent-selected exceptions in this task. The source-proportioned wider/taller screen and stand use an expanded envelope; compact plus/divide spacing remains clear at 48px.', 'approved_by': 'user-authorized-agent', 'approved_on': '2026-09-29', 'svg_sha256': '0d30150d0427901f3575f96d03cc0306d47e322ebef8825f3264928172ded5a0'}
