"""Diagonal open-jaw wrench: parallel handle, round cap, circular head and angular open jaw. Lucide wrench informs continuous perimeter; preserve original downward-right jaw opening.
Keyshape SQUARE: exact SOLO48 envelope. Reviewer: clean centerlines and joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c6d942f0-d85e-49d4-a8eb-fa312e540764'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__open-jaw-mechanic-wrench/20260924T162025Z-thuan-mac/reference/pipe wrench_c6d942f0-d85e-49d4-a8eb-fa312e540764.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-jaw-mechanic-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('open', 'jaw', 'mechanic', 'wrench')

    def build(self):
        # Smooth neck transition is a single cubic supported by the current model API.
        # Its start tangent matches the diagonal handle, and its end tangent matches the circular head.
        self.add_line('handle-left',(7,34),(17,24))
        self.add_bezier('neck',(17,24),((20,21),(18,21),(18,18)))
        self.add_arc('head-left',(18,18),(30,6),radius_x=12)
        self.add_arc('head-right',(30,6),(42,18),radius_x=12)
        self.add_line('jaw-upper',(42,18),(34,10))
        self.add_line('jaw-inner',(34,10),(26,18))
        self.add_line('jaw-lower',(26,18),(34,26))
        self.add_arc('head-bottom',(34,26),(27,28),radius_x=10)
        self.add_line('handle-right',(27,28),(14,41))
        self.add_arc('handle-cap',(14,41),(7,34),radius_x=5)
        self.add_contour('wrench','handle-left','neck','head-left','head-right','jaw-upper','jaw-inner','jaw-lower','head-bottom','handle-right','handle-cap',closed=True)

    def path(self, name, start, steps, closed=False):
        members=[]; here=start
        for j,step in enumerate(steps):
            eid=f'{name}-{j}'
            if len(step)==2:
                self.add_line(eid,here,step); end=step
            else:
                end,rx,ry,sweep=step
                self.add_arc(eid,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
            members.append(eid);here=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)

    def cups(self):
        # Identical supporting palms mirrored about x24; vertical to horizontal tangent quarters.
        for n,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            self.path(n+'-hand',p(6,30),[p(6,32),(p(16,42),10,10,s<0),p(20,42)])
