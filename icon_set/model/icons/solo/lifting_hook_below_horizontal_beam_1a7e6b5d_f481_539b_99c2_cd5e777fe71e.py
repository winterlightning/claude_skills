"""Central mounting block under a beam with a long J hook; one shared suspension node and a tangent lower bowl. Centerlines (4,8)-(44,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1a7e6b5d-f481-539b-99c2-cd5e777fe71e'
SOURCE_PATH = 'pictographic-primitives/construction/lift hook_1a7e6b5d-f481-539b-99c2-cd5e777fe71e.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='fishing-hook: broad uninterrupted hook bend'
DESIGN_PLAN='Central mounting block under a beam with a long J hook; one shared suspension node and a tangent lower bowl. Centerlines (4,8)-(44,40).'
OMISSIONS='Duplicate beam edge omitted.'
class Drawing(Solo48):
    icon_id='lifting-hook-below-horizontal-beam'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='construction'
    aliases=()
    keywords=('lifting', 'hook', 'below', 'horizontal', 'beam')
    def path(self, name, start, commands, closed=False):
        members=[]
        for i,(kind,end,*args) in enumerate(commands):
            member=f'{name}-{i}'
            if kind=='L': self.add_line(member,start,end)
            elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
            members.append(member); start=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,cx,cy,r):
        self.path(name,(cx-r,cy),[('A',(cx,cy-r),r,r,True),('A',(cx+r,cy),r,r,True),('A',(cx,cy+r),r,r,True),('A',(cx-r,cy),r,r,True)],True)


    def build(self):
        self.add_polyline('beam',(4,8),(16,8),(32,8),(44,8))
        self.add_polyline('mount',(16,8),(16,16),(24,16),(32,16),(32,8));self.relate('connect','beam','mount')
        self.path('hook',(24,16),[('L',(24,21)),('C',(34,30),(24,25),(34,24)),('A',(24,40),10,10,True),('A',(14,30),10,10,True),('L',(14,26))]);self.relate('connect','mount','hook')
