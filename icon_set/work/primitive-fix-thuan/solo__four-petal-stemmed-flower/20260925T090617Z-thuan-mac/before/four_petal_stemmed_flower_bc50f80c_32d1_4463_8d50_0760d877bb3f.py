"""Flower with Stem and Leaves.

Plan: Rounded flower lobes above stem and pointed leaves, bounds8,4,40,44. Omit tiny disk to preserve open blossom.
Construction reference: flower-2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc50f80c-32d1-4463-8d50-0760d877bb3f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bloom_bc50f80c-32d1-4463-8d50-0760d877bb3f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-petal-stemmed-flower'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('four', 'petal', 'stemmed', 'flower')

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

        path('bloom',(24,4),[('C',(30,12),(30,4),(32,8)),('C',(40,16),(36,8),(40,10)),('C',(30,20),(40,22),(36,24)),('C',(24,26),(32,24),(30,26)),('C',(18,20),(18,26),(16,24)),('C',(8,16),(12,24),(8,22)),('C',(18,12),(8,10),(12,8)),('C',(24,4),(16,8),(18,4))],True)
        line('stem',(24,26),(24,44));join('stem','bloom')
        path('leaf-left',(24,44),[('C',(8,35),(12,44),(8,40)),('C',(24,44),(16,35),(22,38))],True);join('leaf-left','stem')
        path('leaf-right',(24,44),[('C',(40,35),(26,38),(32,35)),('C',(24,44),(40,40),(36,44))],True);join('leaf-right','stem');join('leaf-right','leaf-left')
