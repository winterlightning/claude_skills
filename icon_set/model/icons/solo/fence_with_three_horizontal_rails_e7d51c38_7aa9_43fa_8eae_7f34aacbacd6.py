'Two tall rounded posts support three evenly spaced horizontal rails between them. The straight rails meet the inner post edges, forming a broad open fence panel viewed directly from the front.\nPlan: Two broad posts and three regularly spaced rails with genuine endpoint contacts.\nConstruction reference: Lucide fence original and atomic-debug: vertical posts and attached cross rails.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7d51c38-7aa9-43fa-8eae-7f34aacbacd6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/corral_e7d51c38-7aa9-43fa-8eae-7f34aacbacd6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'fence-with-three-horizontal-rails'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('fence', 'with', 'three', 'horizontal', 'rails')

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

        for side,x in [('left',4),('right',36)]:
         poly(side,(x,8),(x+8,8),(x+8,16),(x+8,24),(x+8,32),(x+8,40),(x,40),(x,32),(x,24),(x,16),(x,8))
        for y in (16,24,32):
         line(f'rail-{y}',(12,y),(36,y));join(f'rail-{y}','left');join(f'rail-{y}','right')
