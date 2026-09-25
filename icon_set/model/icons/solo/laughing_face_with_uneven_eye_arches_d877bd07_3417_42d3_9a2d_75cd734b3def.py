"""Laughing face with intentionally uneven eye arches and open mouth. Circle construction and one coherent asymmetric eye curve remove stray nodes. Source right eye is flatter; this deliberate asymmetry remains. No useful exact Lucide expression match.
Keyshape CIRCLE: exact SOLO48 envelope; 4px stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd877bd07-3417-42d3-9a2d-75cd734b3def'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face laugh wink_d877bd07-3417-42d3-9a2d-75cd734b3def.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='laughing-face-with-uneven-eye-arches'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('laughing', 'face', 'with', 'uneven', 'eye', 'arches')

    def build(self):
        self.circle('face',24,24,20)
        self.add_arc('left-eye',(15,17),(19,17),radius_x=2,sweep=True)
        self.add_bezier('right-eye',(28,17),((29,15),(31,15),(33,17)))
        self.path('mouth',(15,26),[('L',(33,26)),('A',(15,26),9,9,True)],True)

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
