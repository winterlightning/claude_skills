'A pair of briefs faces forward beneath a broad rounded waistband. Curved leg openings rise from the narrow lower center, defining a full rounded front panel.\nPlan: Broad waistband with inward curved leg openings and full briefs panel.\nConstruction reference: No useful direct Lucide match; rebuilt from inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5deb3981-3d86-4b8b-b976-13d391c1b733'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bloomer_5deb3981-3d86-4b8b-b976-13d391c1b733.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'high-waist-underwear-briefs'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('high', 'waist', 'underwear', 'briefs')

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

        path('briefs',(4,8),[('L',(44,8)),('L',(44,16)),('C',(30,40),(40,28),(34,30)),('L',(18,40)),('C',(4,16),(14,30),(8,28)),('L',(4,8))],True)
        line('waist',(4,16),(44,16));join('waist','briefs')
