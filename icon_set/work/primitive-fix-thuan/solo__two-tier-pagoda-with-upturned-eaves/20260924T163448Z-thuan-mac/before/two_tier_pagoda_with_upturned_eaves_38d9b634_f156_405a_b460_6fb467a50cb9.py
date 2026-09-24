'A compact pagoda has two broad roofs with upward-curving corners and a pointed upper crown. A small doorway opens in the lower story above a wide rectangular plinth.\nPlan: Two wide upturned eaves, central crown and open lower story. Exact 6,6–42,42.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '38d9b634-f156-405a-b460-6fb467a50cb9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/asian monastery_38d9b634-f156-405a-b460-6fb467a50cb9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-tier-pagoda-with-upturned-eaves'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('two', 'tier', 'pagoda', 'with', 'upturned', 'eaves')

    # Repair: Attach lower story directly to split eave; preserve pagoda roofs without crowded doorway.
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

        path('upper',(10,16),[('C',(24,6),(16,18),(20,10)),('C',(38,16),(28,10),(32,18))])
        path('lower',(6,28),[('C',(14,30),(8,30),(10,30)),('L',(34,30)),('C',(42,28),(38,30),(40,30))])
        poly('walls',(14,30),(14,42),(34,42),(34,30));join('walls','lower')
