"""Tape Measure and Pencil.

Plan: Tape case and ruled tape below a separate diagonal pencil; their asymmetry describes a tool pair.
Reduction / construction: Ruler: repeat short ticks; omit pivot and pencil ferrule.
Envelope: SQUARE, exact SOLO48 contract extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f548d50-0fc3-4907-97f1-f325dcee9b85'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/home improvement 11_8f548d50-0fc3-4907-97f1-f325dcee9b85.svg'
AUTHOR = 'gpt-6'


class Batch064Icon1(Solo48):
    icon_id = 'tape-measure-and-pencil-batch-064'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('tape', 'measure', 'and', 'pencil')

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

        path('case',(6,34),[('A',(22,34),8,8,True)])
        self.add_polyline('tape',(6,42),(6,34),(22,34),(42,34),(42,42))
        self.relate('connect','case','tape')
        for x in (18,30):
            self.add_line(f'tick-{x}',(x,34),(x,42))
            self.relate('connect',f'tick-{x}','tape')
        self.add_polyline('pencil',(28,24),(26,16),(32,6),(42,10),(36,22),(28,24),closed=True)
