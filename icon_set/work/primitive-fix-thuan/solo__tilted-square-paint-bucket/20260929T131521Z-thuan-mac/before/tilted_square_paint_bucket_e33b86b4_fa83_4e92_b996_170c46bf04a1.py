'A square-sided paint bucket tilts diagonally with a long looped handle rising above it. A separate teardrop-shaped paint drop hangs to the lower right of the bucket.\nPlan: Tilted square paint bucket with tall loop handle and separate drop. Shared exact handle attachment.\nConstruction reference: paint-bucket: outlined tilted vessel and detached drop, source tall handle retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e33b86b4-fa83-4e92-b996-170c46bf04a1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/color bucket 1_e33b86b4-fa83-4e92-b996-170c46bf04a1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tilted-square-paint-bucket'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('tilted', 'square', 'paint', 'bucket')

    # Repair: Separate drop from bucket; preserve handle overlap as unresolved until a proper occluded construction is possible.
    # Repair: Split both bucket attachment points and stop the handle at the right wall, preserving the real physical connection.
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

        poly('bucket',(6,26),(10,22),(18,14),(22,18),(30,26),(18,38),(6,26))
        path('handle',(10,22),[('L',(10,12)),('A',(22,12),6,6,True),('L',(22,18))]);join('bucket','handle')
        path('drop',(38,30),[('C',(42,38),(39,32),(42,35)),('A',(34,38),4,4,True),('C',(38,30),(34,35),(37,32))],True)
