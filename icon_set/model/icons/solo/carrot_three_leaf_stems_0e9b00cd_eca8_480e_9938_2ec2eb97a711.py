"""Simple Garden Carrot.

Plan: Rounded carrot shoulder, pointed root and three radiating foliage strokes retained. Narrow leaf loops and tiny root scores omitted. Keyshape VRECT_L uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: Lucide carrot: pointed root and radiating foliage; fine root scores omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e9b00cd-eca8-480e-9938-2ec2eb97a711'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/parsnip_0e9b00cd-eca8-480e-9938-2ec2eb97a711.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'carrot-three-leaf-stems'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('carrot', 'three', 'leaf', 'stems')

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

        path('root',(24,16),[('C',(34,24),(31,16),(34,18)),('C',(24,44),(34,31),(27,40)),('C',(14,24),(21,40),(14,31)),('C',(24,16),(14,18),(17,16))],True)
        for name,end in [('left',(8,6)),('top',(24,4)),('right',(40,6))]:
         line(name,(24,16),end);join(name,'root')
        join('left','top');join('left','right');join('top','right')
