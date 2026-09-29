"""A descending angular zigzag arrow.
Review before drawing: The current shaft is compressed into a nearly horizontal slash, unlike the original tall stepped zigzag.
Reviewer feedback: Manual fix request (no more specific instruction).
Plan: Use a tall 32x44 ink envelope (8,2)-(40,46); preserve the two horizontal steps and downward head, with a steeper diagonal and longer upper stem.
Construction reference: Lucide corner-down-right original and atoms: unified directional shaft with a shared arrowhead tip. Intentional stepped asymmetry follows the source.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '302376a8-2f68-4599-bebe-1130fd7a00dc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arrow-down-with-angular-zigzag-shaft/20260928T164600Z-thuan-mac/reference/diagram zig zag fall large head_302376a8-2f68-4599-bebe-1130fd7a00dc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arrow-down-with-angular-zigzag-shaft'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('arrow', 'down', 'with', 'angular', 'zigzag', 'shaft')

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
        poly('shaft',(22,4),(22,12),(38,12),(10,24),(26,24),(26,44))
        poly('head',(14,32),(26,44),(38,32));join('head','shaft')
