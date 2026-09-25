'A roof panel widens toward its flat lower edge and has rounded outer corners. Overlapping rows of curved shingles fill the panel, with their vertical joins staggered between adjacent rows.\nPlan: Roof panel with two staggered scalloped rows; reduce dense original tiling while retaining shingle pattern and flared panel.\nConstruction reference: No useful exact Lucide match; source-specific construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2d18a06-d56a-4d01-b254-7d5e183c8f8f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/material tile roof 1_c2d18a06-d56a-4d01-b254-7d5e183c8f8f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'scalloped-roof-shingles'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('scalloped', 'roof', 'shingles')

    # Repair: Shallower lower scallops leave eight centerline units above the bottom rail.
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

        poly('outline',(10,6),(24,6),(38,6),(40,24),(42,42),(6,42),(8,24),(10,6))
        path('upper-tiles',(10,6),[('A',(24,6),7,12,False),('A',(38,6),7,12,False)])
        path('lower-tiles',(8,24),[('A',(24,24),8,10,False),('A',(40,24),8,10,False)])
        join('outline','upper-tiles');join('outline','lower-tiles')
