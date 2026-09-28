"""A diagonal arrow from an upper-left node overlaps a broad node-to-node U loop. All three ring nodes and the arrow remain. Lucide git-merge informs the smooth lower loop and attached nodes; the asymmetric arrow and source layout are preserved.
SOLO48 SQUARE, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='e601eded-1157-4544-9970-cc41755f1439'
SOURCE_PATH='pictographic-primitives/programing/internet of thing green grass_e601eded-1157-4544-9970-cc41755f1439.svg'
AUTHOR='gpt-6'

class MergeArrowNodes(Solo48):
    icon_id='merge-arrow-nodes'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/programming"
    aliases=()
    keywords=('merge', 'arrow', 'nodes', 'git', 'flow', 'graph', 'branch', 'connection')

    def build(self) -> None:
        def ring(name,x,y,r):
            points=((x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r))
            members=[]
            for i,(a,b) in enumerate(zip(points,points[1:])):
                member=f'{name}-{i}'
                self.add_arc(member,a,b,radius_x=r)
                members.append(member)
            self.add_contour(name,*members,closed=True)

        def join(*names):
            from itertools import combinations
            for a,b in combinations(names,2): self.relate('connect',a,b)

        ring('source',9,9,3)
        ring('upper-node',35,9,3)
        ring('left-node',9,27,3)
        self.add_line('arrow-shaft',(12,9),(28,28))
        self.add_polyline('arrow-head',(21,28),(28,28),(28,18))
        join('source','arrow-shaft')
        join('arrow-head','arrow-shaft')
        self.add_arc('loop-upper',(35,12),(42,23),radius_x=7,radius_y=11)
        self.add_line('loop-right',(42,23),(42,30))
        self.add_arc('loop-bottom',(42,30),(12,30),radius_x=15,radius_y=12)
        self.add_line('loop-left',(12,30),(12,27))
        self.add_contour('loop','loop-upper','loop-right','loop-bottom','loop-left')
        join('loop','upper-node')
        join('loop','left-node')
