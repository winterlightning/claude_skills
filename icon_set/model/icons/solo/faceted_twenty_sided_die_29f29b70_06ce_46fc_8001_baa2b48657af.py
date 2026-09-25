'A many sided gaming die has an irregular polygonal perimeter filled with triangular facets. Diagonal edges converge at several internal corners, giving the unnumbered object a three dimensional form.\nPlan: Hexagonal die perimeter and central triangular facet with shared corner spokes.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '29f29b70-06ce-46fc-8001-baa2b48657af'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/board game geometry_29f29b70-06ce-46fc-8001-baa2b48657af.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'faceted-twenty-sided-die'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('faceted', 'twenty', 'sided', 'die')

    # Repair: Reduce to four broad triangular facets sharing outer vertices, avoiding narrow perimeter pockets.
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

        poly('outer',(24,6),(42,16),(42,32),(24,42),(6,32),(6,16),(24,6))
        poly('facets',(24,6),(42,32),(6,32),(24,6));join('facets','outer')
