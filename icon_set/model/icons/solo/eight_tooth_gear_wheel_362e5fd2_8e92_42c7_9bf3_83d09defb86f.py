"""Settings Gear Cog.

Plan: Retained an eight-part gear rim and central circular opening. Broad outlined teeth become eight short radial teeth around a smooth repeated rim.
Construction reference: Lucide cog inspected; source eight-tooth outline differs, rebuilt using repeated quarter geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '362e5fd2-8e92-42c7-9bf3-83d09defb86f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/clank_362e5fd2-8e92-42c7-9bf3-83d09defb86f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'eight-tooth-gear-wheel'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('eight', 'tooth', 'gear', 'wheel')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        nodes=[(24,7),(36,12),(41,24),(36,36),(24,41),(12,36),(7,24),(12,12)]
        controls=[((30,7),(33,9)),((39,15),(41,18)),((41,30),(39,33)),((33,39),(30,41)),((18,41),(15,39)),((9,33),(7,30)),((7,18),(9,15)),((15,9),(18,7))]
        path('rim',nodes[0],[('C',nodes[(i+1)%8],*controls[i]) for i in range(8)],True)
        circle('opening',24,24,7)
        for i,end in enumerate([(24,4),(38,10),(44,24),(38,38),(24,44),(10,38),(4,24),(10,10)]):line('tooth-'+str(i),nodes[i],end);join('tooth-'+str(i),'rim')
