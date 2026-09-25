"""Angel heart with halo and mirrored wings. Lucide heart informs matching circular lobes; the source supplies floating oval halo and hanging feathers. One broad feather per wing; fine feather divisions omitted.
Keyshape SQUARE: exact SOLO48 envelope; 4px stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5eceeb50-90bb-44d1-b139-73fdd09edb8b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/love it angel_5eceeb50-90bb-44d1-b139-73fdd09edb8b.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='angel-heart'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('angel', 'heart')

    def build(self):
        self.path('halo',(16,10),[('A',(32,10),8,4,True),('A',(16,10),8,4,True)],True)
        self.path('heart',(24,28),[('A',(14,28),5,5,False),('C',(24,42),(14,34),(20,39)),('C',(34,28),(28,39),(34,34)),('A',(24,28),5,5,False)],True)
        for n,s in [('left',1),('right',-1)]:
            def p(x,y):return (24+s*(x-24),y)
            self.path(n+'-wing',p(14,28),[('A',p(6,28),4,4,s<0),('L',p(6,38)),('A',p(14,38),4,4,s<0),('L',p(14,35))])
            self.relate('connect','heart',n+'-wing')

    def path(self,name,start,commands,closed=False):
        members=[];here=start
        for j,(kind,end,*args) in enumerate(commands):
            eid=f'{name}-{j}'
            if kind=='L':self.add_line(eid,here,end)
            elif kind=='A':self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C':self.add_bezier(eid,here,(args[0],args[1],end))
            members.append(eid);here=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
