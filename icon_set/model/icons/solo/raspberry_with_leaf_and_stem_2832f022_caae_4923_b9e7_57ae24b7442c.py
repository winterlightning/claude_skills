"""Raspberry Fruit with Leaves.

Plan: Raspberry cluster simplified to five lobes and one leaf; bounds8,4,40,44.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2832f022-caae-4923-b9e7-57ae24b7442c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/raspberry_2832f022-caae-4923-b9e7-57ae24b7442c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'raspberry-with-leaf-and-stem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('raspberry', 'with', 'leaf', 'and', 'stem')

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

        path('berry',(24,16),[('C',(40,24),(34,12),(40,16)),('C',(34,34),(40,28),(38,32)),('C',(24,44),(34,42),(28,44)),('C',(14,34),(20,44),(14,42)),('C',(8,24),(10,32),(8,28)),('C',(24,16),(8,16),(14,12))],True)
        path('lobes',(8,24),[('C',(24,26),(12,32),(20,32)),('C',(40,24),(28,32),(36,32))]);join('lobes','berry')
        path('middle',(24,16),[('C',(24,26),(19,18),(19,23)),('L',(24,35))]);join('middle','berry');join('middle','lobes')
        path('leaf',(24,16),[('C',(10,4),(14,16),(10,9)),('C',(24,16),(18,4),(24,9))],True);join('leaf','berry')
