"""A rounded magic cauldron with an outlined rim, floating bubble and sparkle.
Review before drawing: The current rim and bubble are solid strokes/dots, losing the hollow rim and bubble in the reference.
Reviewer feedback: Manual fix request (no more specific instruction).
Plan: SQUARE ink extremes (4,4)-(44,44). Restore an outlined capsule rim and hollow floating bubble; retain smooth symmetric bowl, paired feet and magic cross. Feet stay single strokes to avoid tiny closed loops.
Construction reference: No useful direct Lucide cauldron match; coherent tangent curves and mirrored bowl derive from the inspected source.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '72f64d5e-456e-45c1-80a8-12d9cbe19516'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bubbling-magic-cauldron/20260928T164600Z-thuan-mac/reference/witch cauldron_72f64d5e-456e-45c1-80a8-12d9cbe19516.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bubbling-magic-cauldron'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('bubbling', 'magic', 'cauldron')

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
        path('rim',(10,18),[('L',(38,18)),('A',(38,26),4,4,True),('L',(10,26)),('A',(10,18),4,4,True)],True)
        path('bowl',(10,26),[('C',(15,35),(10,30),(12,33)),('C',(24,39),(18,38),(20,39)),('C',(33,35),(28,39),(30,38)),('C',(38,26),(36,33),(38,30))]);join('rim','bowl')
        for s in (-1,1):
            line(f'foot-{s}',(24+s*9,35),(24+s*13,42));join(f'foot-{s}','bowl')
        circle('bubble',14,9,3)
        poly('spark-h',(30,9),(34,9),(38,9));poly('spark-v',(34,6),(34,9),(34,12));join('spark-h','spark-v')

# User explicitly delegated drawing-specific exceptions after UI/UX review.
Drawing.exception = {'reason': 'Preserve the hollow cauldron rim and floating hollow bubble while retaining a full bowl. Bubble and sparkle have 2px visible clearance above the rim. Reviewed at native 48px in both themes.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-28', 'svg_sha256': 'c7a9b408837901d692b1284b933d930e3c7a85d54a652f13eea343a387475c5f'}
