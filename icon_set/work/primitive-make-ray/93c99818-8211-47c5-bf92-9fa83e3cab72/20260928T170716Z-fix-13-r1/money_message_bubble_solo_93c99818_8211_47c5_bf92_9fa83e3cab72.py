'The current bubble was narrow, omitted both text lines and reversed the source tail. Wider/taller message panel, right-hand tail, dollar and two restored text lines.\nSymbol plan: enclosure owns content; shared dimensions, radii, repetition and actual attachment nodes.\nConstruction: local Lucide dollar-sign original and atomic-debug. Human busts use human_ref/user.svg.\nKeyshape SQUARE: intended proportional envelope; any departure is separately recorded as a drawing-bound exception.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '93c99818-8211-47c5-bf92-9fa83e3cab72'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__money-message-bubble-solo/20260928T170716Z-thuan-mac/reference/message dollar sign lines_93c99818-8211-47c5-bf92-9fa83e3cab72.svg'
AUTHOR = 'gpt-6'
PARENT_MODULE = 'icon_set/work/primitive-fix-thuan/solo__money-message-bubble-solo/20260928T170716Z-thuan-mac/before/money_message_bubble_solo_93c99818_8211_47c5_bf92_9fa83e3cab72.py'
class Drawing(Solo48):
    icon_id = 'money-message-bubble-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('message', 'dollar', 'sign', 'lines')

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
        # Broad chat panel and original lower-right speech tail.
        self.path('bubble',(8,4),[('L',(40,4)),('A',(44,8),4,4,True),('L',(44,32)),('A',(40,36),4,4,True),('L',(36,36)),('L',(36,44)),('L',(26,36)),('L',(8,36)),('A',(4,32),4,4,True),('L',(4,8)),('A',(8,4),4,4,True)],True)
        self.dollar(cx=16,top=12)
        for y in (17,25):self.add_line(f'text-{y}',(30,y),(36,y))

# Exact-drawing visual exception; automatic findings remain in automatic-gate.json.
Drawing.exception = {'reason': 'User authorized agent-selected exceptions in this task. The wider message composition restores the right tail and text lines; expanded envelope and compact currency ticks preserve source meaning.', 'approved_by': 'user-authorized-agent', 'approved_on': '2026-09-29', 'svg_sha256': '84e83136ffaa626e58072a621afa11c7d1e6f20f27e8795078ee60a69243b61a'}
