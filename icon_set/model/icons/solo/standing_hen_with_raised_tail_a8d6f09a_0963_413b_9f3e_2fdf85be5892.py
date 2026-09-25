"""Standing hen with raised tail and right-facing beak. Lucide bird informs round breast and head. Preserve tail, beak and foot; omit tiny comb/wattle. Smooth arc sequence replaces uneven curves.
Keyshape HRECT_L: exact SOLO48 envelope. Reviewer: clean centerlines and joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8d6f09a-0963-413b-9f3e-2fdf85be5892'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/capon_a8d6f09a-0963-413b-9f3e-2fdf85be5892.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-hen-with-raised-tail'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('standing', 'hen', 'with', 'raised', 'tail')

    def build(self):
        self.path('hen',(4,12),[((18,22),15,15,False),(22,22),((28,16),6,6,False),(28,14),((34,8),6,6,True),((40,14),6,6,True),(44,18),(40,20),(40,22),((30,32),10,10,True),(18,32),((4,24),14,8,True),(4,12)],True)
        self.add_polyline('foot',(24,32),(24,40),(31,40));self.relate('connect','foot','hen')

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
