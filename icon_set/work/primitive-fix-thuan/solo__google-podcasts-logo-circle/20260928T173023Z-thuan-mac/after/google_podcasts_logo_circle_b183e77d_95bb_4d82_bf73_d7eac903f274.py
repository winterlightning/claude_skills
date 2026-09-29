'The seven-stroke podcast mark was reduced to three thick bars. Restored all seven evenly spaced waveform strokes inside the circular badge.\nSymbol plan: typed contours, shared radii and exact attachment nodes; paired features use common dimensions.\nConstruction: Repeated waveform construction; supplied source pattern. Keyshape CIRCLE; any proportional departure is recorded as an exact-drawing exception.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b183e77d-95bb-4d82-bf73-d7eac903f274'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__google-podcasts-logo-circle/20260928T173023Z-thuan-mac/reference/google podcast logo 1_b183e77d-95bb-4d82-bf73-d7eac903f274.svg'
AUTHOR="gpt-6"
PARENT_MODULE='icon_set/work/primitive-fix-thuan/solo__google-podcasts-logo-circle/20260928T173023Z-thuan-mac/before/google_podcasts_logo_circle_b183e77d_95bb_4d82_bf73_d7eac903f274.py'
class Drawing(Solo48):
    icon_id='google-podcasts-logo-circle'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('google', 'podcast', 'logo', '1')

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

    def node(self,n,x,y,r,extra=()):
        import math
        offsets=set([(-r,0),(0,-r),(r,0),(0,r),*extra])
        offsets=sorted(offsets,key=lambda p:math.atan2(p[1],p[0]))
        pts=[(x+dx,y+dy) for dx,dy in offsets]
        self.path(n,pts[0],[('A',q,r,r,True) for q in pts[1:]+pts[:1]],True)

    def bubble(self):
        self.path('bubble',(22,38),[('L',(22,44)),('C',(40,22),(33,39),(40,31)),('C',(24,4),(40,12),(33,4)),('C',(8,21),(15,4),(8,11)),('C',(22,38),(8,31),(14,37))],True)
    def file(self):
        self.path('page',(12,4),[('L',(28,4)),('L',(40,16)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
        self.path('fold',(28,4),[('L',(28,12)),('A',(32,16),4,4,False),('L',(40,16))]);self.relate('connect','page','fold')

    def build(self):
        # Restore seven waveform strokes; one shared 5u pitch keeps the narrow gaps even.
        self.circle('badge',24,24,20)
        for i,(x,top,bottom) in enumerate([(9,23,25),(14,16,32),(19,22,30),(24,10,38),(29,20,28),(34,16,32),(39,23,25)]):
            self.add_line(f'wave-{i}',(x,top),(x,bottom))

# Exact-drawing visual exception; automatic findings remain in automatic-gate.json.
Drawing.exception = {'reason': 'User authorized agent-selected exceptions in this task. All seven source waveform bars are restored inside the circular badge. Their 5-unit pitch leaves 1px ink gaps at 48px, visibly separating the bars while retaining the original rhythm.', 'approved_by': 'user-authorized-agent', 'approved_on': '2026-09-29', 'svg_sha256': 'd7d3e7632ad261d149dae455fb2d53667a51dc2f02e92b6b1eb06facee538a39'}
