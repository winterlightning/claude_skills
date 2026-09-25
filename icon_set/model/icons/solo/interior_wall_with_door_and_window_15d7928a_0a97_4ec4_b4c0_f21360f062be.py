"""Interior wall with doorway and four-pane window. Lucide door-closed: continuous frame and floor. Shared grid for equal window panes; omit sidewalls and knob to retain usable openings.
Keyshape SQUARE: exact SOLO48 envelope. Reviewer: clean centerlines and joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '15d7928a-0a97-4ec4-b4c0-f21360f062be'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/interior_15d7928a-0a97-4ec4-b4c0-f21360f062be.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'interior-wall-with-door-and-window'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('interior', 'wall', 'with', 'door', 'and', 'window')

    def build(self):
        self.add_line('ceiling',(6,6),(42,6))
        self.add_polyline('floor',(6,42),(16,42),(42,42))
        self.path('door',(6,42),[(6,18),((8,16),2,2,True),(14,16),((16,18),2,2,True),(16,42)])
        self.relate('connect','door','floor')
        self.add_polyline('window',(26,16),(34,16),(42,16),(42,24),(42,32),(34,32),(26,32),(26,24),closed=True)
        self.add_polyline('mullion',(34,16),(34,24),(34,32))
        self.add_polyline('transom',(26,24),(34,24),(42,24))
        for a,b in [('window','mullion'),('window','transom'),('mullion','transom')]:self.relate('connect',a,b)

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
