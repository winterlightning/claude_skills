'A fan-shaped wireless symbol expands upward from a small circular base. Two curved interior divisions follow the broad outer arc, with straight diagonal sides enclosing the stacked open signal bands.\nPlan: Wireless fan enclosed by diagonal sides with two curved divisions and circle base. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: No useful direct Lucide match; coherent contours reconstructed from the inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '26da1028-851a-4a4d-abd8-95474fe8fe8a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/nest wifi logo_26da1028-851a-4a4d-abd8-95474fe8fe8a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'segmented-wireless-fan'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('segmented', 'wireless', 'fan')

    # Repair: Separate the circular base from the signal fan and retain one curved division; review whether the reduced segmentation preserves the source logo.
    # Repair: Reconnect the fan sides at the round base exact side extrema. Retain one broad inner signal band after the earlier pinched opening.
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

        path('fan',(20,38),[('L',(12,26)),('L',(6,18)),('C',(24,6),(10,10),(16,6)),('C',(42,18),(32,6),(38,10)),('L',(36,26)),('L',(28,38))])
        path('band',(12,26),[('C',(36,26),(18,18),(30,18))]);join('band','fan');circle('base',24,38,4);join('base','fan')
