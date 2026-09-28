'A whole oval nut sits behind a cut half shown at an angle. The front half has a broad outer shell surrounding an irregular rounded kernel, with a small opening along its lower left edge.\nPlan: Whole oval behind a round cut half, with broad shell and kernel. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: No useful direct Lucide match; coherent contours reconstructed from the inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1e9a9c1-6924-4200-a493-a9575f93024e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/macadamia_b1e9a9c1-6924-4200-a493-a9575f93024e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'whole-macadamia-beside-cut-nut-half'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('whole', 'macadamia', 'beside', 'cut', 'nut', 'half')

    # Repair: End the occluded whole nut exactly at the front shell extrema; keep the cut rim and kernel clear.
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

        path('whole',(16,29),[('C',(6,22),(8,30),(6,28)),('C',(20,6),(6,14),(12,6)),('C',(29,16),(26,6),(29,10))]);circle('half',29,29,13);circle('kernel',29,29,4);join('whole','half')
