"""Growing Seedling Plant.

Plan: VRECT_L, centerline extremes (8, 4, 40, 44); 48 x 48, stroke 4.
Terminal leaf and paired side leaves remain distinct above the low soil mound.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: sprout.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6e112b7-4042-4202-98d6-752ae1e27fa0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/millet_a6e112b7-4042-4202-98d6-752ae1e27fa0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-leaf-seedling-on-low-mound'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('three', 'leaf', 'seedling', 'on', 'low', 'mound')

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
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        poly('stem',(24,18),(24,33),(24,42))
        path('leaf-top',(24,18),[('C',(24,4),(14,12),(20,8)),('C',(24,18),(28,8),(34,12))],True);join('stem','leaf-top')
        path('leaf-left',(24,33),[('C',(8,24),(12,33),(8,30)),('C',(24,33),(16,24),(22,28))],True);join('stem','leaf-left')
        path('leaf-right',(24,33),[('C',(40,24),(26,28),(32,24)),('C',(24,33),(40,30),(36,33))],True);join('stem','leaf-right');join('leaf-left','leaf-right')
        path('soil',(8,44),[('C',(24,42),(12,42),(18,42)),('C',(40,44),(30,42),(36,42))]);join('soil','stem')
