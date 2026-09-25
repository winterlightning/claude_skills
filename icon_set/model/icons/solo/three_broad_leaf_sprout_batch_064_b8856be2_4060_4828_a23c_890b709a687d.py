"""Three Leaf Plant Sprout.

Plan: Three leaf loops share a central stem; paired lateral leaves mirror about x=24.
Reduction / construction: Sprout: coherent leaf contours; omit small veins.
Envelope: SQUARE, exact SOLO48 contract extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8856be2-4060-4828-a23c-890b709a687d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/herbs_b8856be2-4060-4828-a23c-890b709a687d.svg'
AUTHOR = 'gpt-6'


class Batch064Icon2(Solo48):
    icon_id = 'three-broad-leaf-sprout-batch-064'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('three', 'broad', 'leaf', 'sprout')

    def build(self):

        def path(name, start, commands, closed=False):
            members=[]
            point=start
            for i,command in enumerate(commands):
                kind,end,*args=command
                member=f"{name}-{i}"
                if kind=='L':
                    self.add_line(member,point,end)
                else:
                    rx,ry,sweep=args
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep)
                members.append(member)
                point=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx,cy-ry),rx,ry,True),('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)

        path('top-leaf',(24,6),[('A',(24,22),9,9,True),('A',(24,6),9,9,True)],True)
        self.add_polyline('stem',(24,22),(24,40),(24,42))
        self.relate('connect','stem','top-leaf')
        for side in (-1,1):
            tip=(24+side*18,28); node=(24,40)
            path(f'leaf-{side}',tip,[('A',node,18,12,side<0),('A',tip,18,12,side<0)],True)
            self.relate('connect',f'leaf-{side}','stem')
