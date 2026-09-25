'Three narrow upright bars stand separately at different heights, with the center tallest and the left shortest. Their upper edges are flat while each lower edge tilts slightly in perspective.\nPlan: Three bars at differing heights; center tallest, left shortest. Retain tilted bottoms and open outlined interiors.\nConstruction reference: No useful exact Lucide match; source-specific construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '60d1b4c1-0681-41c0-a6ad-205e239e1d4c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/logo 1_60d1b4c1-0681-41c0-a6ad-205e239e1d4c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-tall-slanted-base-bars'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ()
    keywords = ('three', 'tall', 'slanted', 'base', 'bars')

    # Repair: Three 8-unit wide bars with exact 8-unit separations; original relative heights and slanted bases retained.
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L':self.add_line(member,here,end)
                elif kind=='A':self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(member,here,(args[0],args[1],end))
                here=end;members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)

        for j,(x,y,b) in enumerate([(4,20,38),(20,8,38),(36,16,36)]):poly(f'bar-{j}',(x,y),(x+8,y),(x+8,b+2),(x,b),(x,y))
