'A slender stem branches into three pointed oval leaves, with one upright at the top and two spreading sideways below. Each leaf has a short central vein connected to the branching stem.\nPlan: Three pointed leaves on a stem. Shared bilateral leaf arrangement; veins omitted to preserve their open interiors.\nConstruction reference: sprout and leaf: pointed leaf contours and a shared stem; three source leaves retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eda88d9c-f520-4ee1-8598-6c7e973f256b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/rhubarb_eda88d9c-f520-4ee1-8598-6c7e973f256b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-leaf-botanical-sprig'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('three', 'leaf', 'botanical', 'sprig')

    # Repair: Shorter top leaf and lower side leaves open the inter-leaf region, retaining all three leaves.
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

        path('top-leaf',(24,4),[('C',(24,20),(32,11),(32,15)),('C',(24,4),(16,15),(16,11))],True)
        path('left-leaf',(8,28),[('C',(24,36),(18,28),(24,30)),('C',(8,28),(14,40),(8,37))],True)
        path('right-leaf',(40,28),[('C',(24,36),(30,28),(24,30)),('C',(40,28),(34,40),(40,37))],True)
        poly('stem',(24,20),(24,36),(24,44));join('stem','top-leaf');join('stem','left-leaf');join('stem','right-leaf');join('left-leaf','right-leaf')
