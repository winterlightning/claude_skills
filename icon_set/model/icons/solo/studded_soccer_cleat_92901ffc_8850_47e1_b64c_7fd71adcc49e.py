"""Left-facing studded soccer cleat. Lucide geometric principles; no useful exact local shoe match. Smooth toe, scooped collar and three equal studs retain identity. Omit tiny lace marks.
Keyshape HRECT_L: exact SOLO48 envelope; 4px stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '92901ffc-8850-47e1-b64c-7fd71adcc49e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cleat_92901ffc-8850-47e1-b64c-7fd71adcc49e.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='studded-soccer-cleat'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('studded', 'soccer', 'cleat')

    def build(self):
        self.path('shoe',(4,30),[('C',(14,22),(4,28),(9,25)),('L',(24,16)),('C',(28,8),(26,15),(25,8)),('C',(32,18),(31,8),(29,18)),('C',(40,12),(36,18),(38,12)),('C',(44,26),(43,12),(44,20)),('L',(44,32)),('L',(38,32)),('L',(24,32)),('L',(10,32)),('L',(4,32)),('L',(4,30))],True)
        for x in (10,24,38):
            self.add_line(f'stud-{x}',(x,32),(x,40));self.relate('connect',f'stud-{x}','shoe')

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
