"""A broad outlined arrow pointing diagonally down and right.
Review before drawing: The current diagonal shaft has a shallow angle and unequal-looking arm recesses; the source has a balanced 45-degree direction.
Reviewer feedback: Manual fix request (no more specific instruction).
Plan: SQUARE ink extremes (4,4)-(44,44). Matched radius-4 arm caps, 45-degree parallel shaft walls, a smooth diagonal end cap and a rounded outside corner.
Construction reference: Lucide corner-down-right original and atoms: matching shaft and head direction; supplied reference owns the outlined silhouette.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4a1977b5-8625-54b6-bf28-f30aca7f45a1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arrow-down-right-with-rounded-ends/20260928T164600Z-thuan-mac/reference/arrow thick corner bottom right_4a1977b5-8625-54b6-bf28-f30aca7f45a1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arrow-down-right-with-rounded-ends'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('arrow', 'down', 'right', 'with', 'rounded', 'ends')

    def build(self):

        def path(n, start, steps, closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(steps):
                p=f'{n}-{i}'
                if kind=='L': self.add_line(p,here,end)
                elif kind=='A': self.add_arc(p,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(p,here,(args[0],args[1],end))
                here=end;members.append(p)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def poly(n,*pts): self.add_polyline(n,*pts,closed=pts[0]==pts[-1])
        def line(n,a,b): self.add_line(n,a,b)
        def join(a,b): self.relate('connect',a,b)
        path('arrow',(8,14),[('L',(28,34)),('L',(10,34)),('A',(10,42),4,4,False),('L',(38,42)),('A',(42,38),4,4,False),('L',(42,10)),('A',(34,10),4,4,False),('L',(34,28)),('L',(14,8)),('C',(8,14),(10,4),(4,10))],True)
