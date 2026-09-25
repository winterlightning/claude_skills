'Three empty horizontal rectangular bars form a vertical stack with generous gaps. Their left edges align, while the top bar is shorter than the two matching bars below.\nPlan: Three separated outlined bars, top shorter, bottom two equal. Each 8-unit high band needs two 8-unit gaps.\nConstruction reference: No useful exact Lucide match; source-specific construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35486d65-b399-4bde-a2f0-b94b9390a2cc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/betalist logo_35486d65-b399-4bde-a2f0-b94b9390a2cc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'stacked-outlined-bars'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('stacked', 'outlined', 'bars')

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

        for j,(y,w) in enumerate(((4,24),(20,32),(36,32))):poly(f'bar-{j}',(8,y),(8+w,y),(8+w,y+8),(8,y+8),(8,y))
