'A broad outlined chevron forms the front mountain, with a triangular opening rising from its base. A second peak begins behind its right slope and descends toward the far right.\nPlan: Front mountain chevron and separate rear peak with intentional slope contact.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3930ed08-5c2f-42dc-b402-bd089794a1c4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/alpine linux logo_3930ed08-5c2f-42dc-b402-bd089794a1c4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'twin-angular-mountain-peaks'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('twin', 'angular', 'mountain', 'peaks')

    # Repair: Widen the front chevron band without moving the outer peaks.
    # Repair: Narrow and lower the open notch to keep its surrounding chevron band broad enough.
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

        poly('front',(4,38),(18,10),(32,38),(22,38),(18,32),(14,38),(4,38))
        poly('back',(26,26),(34,10),(44,38));join('front','back')
