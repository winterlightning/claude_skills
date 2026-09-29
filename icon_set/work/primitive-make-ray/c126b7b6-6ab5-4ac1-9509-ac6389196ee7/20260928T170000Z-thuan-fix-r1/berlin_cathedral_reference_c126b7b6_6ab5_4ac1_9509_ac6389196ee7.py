"""A cathedral facade with two pointed towers, central window and arched doorway.
Review before drawing: The current facade has only three empty bays; its shortened central gable, absent round window and absent doorway remove defining architecture.
Reviewer feedback: Manual fix request (no more specific instruction).
Plan: SQUARE ink extremes (4,4)-(44,44). Restore the central rose window and arched door, raise the gable, add tower roof seams, and preserve the left cross. Shared axis x=24 controls paired towers.
Construction reference: Lucide church original and atoms: arched doorway and shared architectural attachment points. Original facade, rather than geographic assumptions, governs the two towers.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c126b7b6-6ab5-4ac1-9509-ac6389196ee7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__berlin-cathedral-reference/20260928T164600Z-thuan-mac/reference/landmark berlin cathedral_c126b7b6-6ab5-4ac1-9509-ac6389196ee7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'berlin-cathedral-reference'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('berlin', 'cathedral', 'reference')

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
        poly('outline',(6,42),(6,18),(12,12),(18,18),(18,24),(24,16),(30,24),(30,18),(36,12),(42,18),(42,42),(28,42),(20,42),(6,42))
        for x in (18,30):
            poly(f'wall-{x}',(x,18),(x,24),(x,42));join(f'wall-{x}','outline')
        for a,b in [(6,18),(30,42)]:
            line(f'roof-{a}',(a,18),(b,18));join(f'roof-{a}','outline')
        poly('cross-stem',(12,6),(12,8),(12,12));poly('crossbar',(8,8),(12,8),(16,8));join('cross-stem','crossbar');join('cross-stem','outline')
        circle('window',24,26,3)
        path('door',(20,42),[('L',(20,36)),('A',(28,36),4,4,True),('L',(28,42))]);join('door','outline')
