'A macaw faces right with a domed head and a large downward hooked bill. Its long folded wing tapers toward the lower left above a narrow tail extending beneath the body.\nPlan: Macaw curved profile with hook bill and single folded wing; preserve downward tail.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ff21c89d-bd7b-4a37-8d27-89d2bc3b02dd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/macaw_ff21c89d-bd7b-4a37-8d27-89d2bc3b02dd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'macaw-profile-with-large-hooked-bill'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('macaw', 'profile', 'with', 'large', 'hooked', 'bill')

    # Repair: Remove cramped internal folded-wing contour; retain hooked bill, curved back and long tail.
    # Repair: Unify the tail into one pointed terminal contour, removing the artificial narrow parallel tail strip.
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

        path('bird',(30,4),[('C',(40,12),(36,4),(40,8)),('L',(34,20)),('L',(32,14)),('C',(28,34),(34,24),(34,30)),('L',(8,44)),('L',(16,28)),('C',(20,12),(16,20),(16,8)),('C',(30,4),(24,4),(26,4))],True)
