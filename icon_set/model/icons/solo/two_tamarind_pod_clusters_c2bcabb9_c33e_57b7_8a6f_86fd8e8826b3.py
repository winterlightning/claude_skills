"""Two Tamarind Pods.

Two three-lobed tamarind pods spaced side by side. Shared swelling pattern and attached stems; centerline extremes (6,6)-(42,42). No useful local Lucide match; omit internal segment seams.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2bcabb9-c33e-57b7-8a6f-86fd8e8826b3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/tamarind_c2bcabb9-c33e-57b7-8a6f-86fd8e8826b3.svg'
AUTHOR = 'gpt-6'

class TwoTamarindPodClusters(Solo48):
    icon_id = 'two-tamarind-pod-clusters'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('two', 'tamarind', 'pods')

    def build(self):
        # Symbol plan: Two three-lobed tamarind pods spaced side by side. Shared swelling pattern and attached stems; centerline extremes (6,6)-(42,42). No useful local Lucide match; omit internal segment seams.

        def path(name, start, commands, closed=False):
            members=[]
            for i, command in enumerate(commands):
                kind,end,*args=command
                member=f'{name}-{i}'
                if kind=='L': self.add_line(member,start,end)
                elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
                members.append(member)
                start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)

        for i,x in enumerate((12,36)):
            path(f'pod-{i}',(x,12),[('C',(x+6,18),(x+4,12),(x+6,14)),('C',(x+4,24),(x+6,21),(x+4,22)),('C',(x+6,30),(x+4,26),(x+6,27)),('C',(x+4,36),(x+6,33),(x+4,34)),('C',(x,42),(x+4,40),(x+3,42)),('C',(x-6,36),(x-4,42),(x-6,40)),('C',(x-4,30),(x-6,33),(x-4,32)),('C',(x-6,24),(x-4,28),(x-6,27)),('C',(x-4,18),(x-6,21),(x-4,20)),('C',(x,12),(x-4,14),(x-3,12))],True)
            path(f'stem-{i}',(x,12),[('C',(x+4,6),(x,8),(x+2,6))]);join(f'pod-{i}',f'stem-{i}')
