"""Closed hardcover book with clean rounded spine and broad bottom page band. Lucide book informs radius6 spine and straight page rule. Secondary thin spine seam omitted for clearance.
Keyshape VRECT_L: exact SOLO48 envelope; 4px stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '50c84aaa-af44-4a3d-9303-9dbfdf04c956'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hardcover_50c84aaa-af44-4a3d-9303-9dbfdf04c956.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='closed-hardcover-book-source-50c84aaa'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('closed', 'hardcover', 'book', 'source', '50c84aaa')

    def build(self):
        self.path('book',(8,38),[('L',(8,10)),('A',(14,4),6,6,True),('L',(40,4)),('L',(40,32)),('L',(40,44)),('L',(14,44)),('A',(8,38),6,6,True)],True)
        self.path('pages',(8,38),[('A',(14,32),6,6,True),('L',(40,32))]);self.relate('connect','pages','book')

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
