"""Decision Point with Check and Cross.

Symbol plan: Complete decision diagram: central diamond, upper stem, two mirrored descending output branches, check and cross as intrinsic outcome labels. Lucide network informs branching junctions. Maintain outcome labels and intentional check/cross asymmetry.
Keyshape SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'acb307dd-0410-4745-b448-73ba32d4513e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/diagrams/condition_acb307dd-0410-4745-b448-73ba32d4513e.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'decision-branch-with-check-and-cross'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('decision', 'point', 'with', 'check', 'and', 'cross')

    def build(self):
        self.add_polyline('decision',(24,20),(33,28),(24,36),(15,28),closed=True)
        self.add_line('stem',(24,6),(24,20));self.relate('connect','stem','decision')
        for i in range(2):
            def q(x,y):return (x if i==0 else 48-x,y)
            self.add_line(f'h-{i}',q(15,28),q(10,28));self.add_arc(f'bend-{i}',q(10,28),q(6,32),radius_x=4,sweep=i==1)
            self.add_line(f'v-{i}',q(6,32),q(6,42));self.add_contour(f'branch-{i}',f'h-{i}',f'bend-{i}',f'v-{i}');self.relate('connect',f'branch-{i}','decision')
        self.add_polyline('check',(6,14),(10,18),(14,10))
        self.graph([('x1',(34,10),(38,14)),('x2',(38,14),(42,18)),('x3',(34,18),(38,14)),('x4',(38,14),(42,10))])

    def graph(self,edges):
        for name,a,b in edges:self.add_line(name,a,b)
        for i,(name,a,b) in enumerate(edges):
            for other,c,d in edges[i+1:]:
                if {a,b}&{c,d}:self.relate('connect',name,other)
