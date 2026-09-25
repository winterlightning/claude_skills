"""Folded Shawl with Fringe.

Plan: Crossed shawl panels with open neckline and three fringe strands. Bounds8,4,40,44. Broad diagonal folds.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4683deb3-c716-41ba-a197-fa79c507de7c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/shaw_4683deb3-c716-41ba-a197-fa79c507de7c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crossed-fringed-shawl'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('crossed', 'fringed', 'shawl')

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

        poly('shawl',(16,4),(32,4),(40,20),(32,32),(24,40),(16,32),(8,20),closed=True)
        poly('cross',(16,4),(24,20),(32,32));join('cross','shawl')
        line('other-fold',(32,4),(24,20));join('other-fold','shawl');join('other-fold','cross')
        for j,(x,y) in enumerate([(16,32),(24,40),(32,32)]):line(f'fringe-{j}',(x,y),(x,44));join(f'fringe-{j}','shawl')
