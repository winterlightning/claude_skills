"""Geometric Hexagon Cube.

Plan: Angular folded ribbon emblem in hexagonal silhouette; integrated faces rather than hosted content. Bounds8,4,40,44.
Construction reference: No useful local Lucide match.
Final review: Retained integrated hexagonal folded-face emblem; no literal typeface text.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d6a8cf5-2635-415b-98c2-e3cae60e130f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/reason studios logo_2d6a8cf5-2635-415b-98c2-e3cae60e130f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'reason-studios-angular-emblem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('reason', 'studios', 'angular', 'emblem')

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

        poly('emblem',(24,4),(40,14),(40,34),(24,44),(8,34),(8,14),closed=True)
        poly('fold',(24,4),(24,24),(40,34));join('fold','emblem')
        poly('left-face',(8,14),(24,24),(8,34));join('left-face','emblem');join('left-face','fold')
