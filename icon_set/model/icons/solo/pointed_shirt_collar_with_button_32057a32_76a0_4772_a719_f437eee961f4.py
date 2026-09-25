"""Formal Dress Shirt Collar.

Plan: Paired pointed collars joined at center, short placket. Bounds4,8,44,40. Omit tiny button hole.
Construction reference: shirt.
Final review: Native light/dark review: recognizable reduced silhouette, balanced spacing and coherent joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '32057a32-76a0-4772-a719-f437eee961f4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/collar_32057a32-76a0-4772-a719-f437eee961f4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pointed-shirt-collar-with-button'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('pointed', 'shirt', 'collar', 'with', 'button')

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

        poly('collar-left',(4,8),(24,18),(14,32),(4,8),closed=True)
        poly('collar-right',(44,8),(24,18),(34,32),(44,8),closed=True);join('collar-left','collar-right')
        line('placket',(24,18),(24,40));join('placket','collar-left');join('placket','collar-right')
