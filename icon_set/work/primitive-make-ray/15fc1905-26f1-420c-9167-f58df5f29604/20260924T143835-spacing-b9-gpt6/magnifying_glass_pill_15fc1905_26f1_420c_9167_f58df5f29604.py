"""magnifying glass pill: fresh spacing repair.
Plan: Diagonal capsule inside the circular lens retains the reference direction; handle joins an exact lens node.
Keyshape SQUARE: SQUARE fits the lens and diagonal handle.
Omissions: Capsule shortened; internal divider omitted after internal-spacing failure.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='15fc1905-26f1-420c-9167-f58df5f29604'
SOURCE_PATH='pictographic-primitives/other/magnifying glass pill_15fc1905-26f1-420c-9167-f58df5f29604.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='magnifying-glass-pill'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('magnifying', 'glass', 'pill')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,segments,closed=False):
        at=start; members=[]
        for i,s in enumerate(segments):
            eid=f'{n}-{i}'; kind,end,*args=s
            if end==at: continue
            if kind=='L': self.add_line(eid,at,end)
            else: self.add_arc(eid,at,end,radius_x=args[0],sweep=args[1] if len(args)>1 else True)
            at=end; members.append(eid)
        self.add_contour(n,*members,closed=closed)
    def cross(self,n,x,y,r):
        for i,(dx,dy) in enumerate([(-r,0),(r,0),(0,-r),(0,r)]):
            self.add_line(f'{n}-{i}',(x,y),(x+dx,y+dy))
        for i in range(4):
            for j in range(i): self.relate('connect',f'{n}-{i}',f'{n}-{j}')

    def page(self):
        self.path('page',(12,4),[('L',(28,4)),('L',(40,16)),('L',(40,40)),('A',(36,44),4),('L',(12,44)),('A',(8,40),4),('L',(8,8)),('A',(12,4),4)],True)
    def phone(self,band=True):
        self.path('phone',(12,4),[('L',(36,4)),('A',(40,8),4),('L',(40,36)),('L',(40,40)),('A',(36,44),4),('L',(12,44)),('A',(8,40),4),('L',(8,36)),('L',(8,8)),('A',(12,4),4)],True)
        if band:
            self.add_line('separator',(8,36),(40,36));self.relate('connect','phone','separator')
    def house(self):
        self.path('house',(6,18),[('L',(24,6)),('L',(42,18)),('L',(42,38)),('A',(38,42),4),('L',(10,42)),('A',(6,38),4),('L',(6,18))],True)

    def build(self):
        self.add_arc('lens-a',(30,33),(12,9),radius_x=15)
        self.add_arc('lens-b',(12,9),(30,33),radius_x=15)
        self.add_contour('lens','lens-a','lens-b',closed=True)
        self.add_line('handle',(30,33),(42,42));self.relate('connect','handle','lens')
        self.add_line('pill-upper',(17,19),(19,17))
        self.add_bezier('pill-cap-right',(19,17),((22,14),(28,20),(25,23)))
        self.add_line('pill-lower',(25,23),(23,25))
        self.add_bezier('pill-cap-left',(23,25),((20,28),(14,22),(17,19)))
        self.add_contour('pill','pill-upper','pill-cap-right','pill-lower','pill-cap-left',closed=True)
