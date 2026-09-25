"""Tanjirou head: swept hair with a single forelock, circular jaw, forehead scar and paired eyes. Human reference supplies round jaw construction. No useful Lucide character match; source identity retained. Omit fine curls and brows; simplify the small scar zigzag to one broad angular bend.
Keyshape SQUARE: exact SOLO48 envelope; 4px stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ef48cbe-cc4f-4534-9267-a5b1a90c74e3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-02/demon slayer kamado tanjirou_9ef48cbe-cc4f-4534-9267-a5b1a90c74e3.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='tanjirou-head'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('tanjirou', 'head')

    def build(self):
        self.path('head',(6,24),[('C',(20,6),(6,14),(12,8)),('L',(20,10)),('C',(42,24),(31,6),(42,12)),('A',(24,42),18,18,True),('A',(6,24),18,18,True)],True)
        self.add_polyline('scar',(23,18),(27,21),(23,24))
        for n,x in [('left',17),('right',31)]:self.add_dot(n+'-eye',(x,31))

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
