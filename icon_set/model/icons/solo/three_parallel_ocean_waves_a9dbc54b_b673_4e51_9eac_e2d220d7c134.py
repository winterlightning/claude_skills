'Three long wavy lines run horizontally in evenly spaced rows. Each alternates smoothly between rounded crests and troughs, with matching curves aligned vertically and no enclosing border around the water.\nPlan: Three smooth equal wave rows; repeated cubic crest/trough definition, shared 12-unit row spacing.\nConstruction reference: No useful exact Lucide match; source-specific construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a9dbc54b-b673-4e51-9eac-e2d220d7c134'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/ocean_a9dbc54b-b673-4e51-9eac-e2d220d7c134.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-parallel-ocean-waves'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('three', 'parallel', 'ocean', 'waves')

    # Repair: Shift outer wave rows inward; cubic extrema reach y=10 and y=38 exactly.
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

        for j,y in enumerate((13,24,35)):
         path(f'wave-{j}',(4,y),[('C',(14,y),(7,y+4),(11,y+4)),('C',(24,y),(17,y-4),(21,y-4)),('C',(34,y),(27,y+4),(31,y+4)),('C',(44,y),(37,y-4),(41,y-4))])
