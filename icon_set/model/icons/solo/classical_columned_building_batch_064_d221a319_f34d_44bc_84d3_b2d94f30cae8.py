"""Classical Courthouse Building.

Plan: A courthouse pediment above four equally spaced classical columns.
Reduction / construction: Landmark: repeated columns and broad triangular roof; omit ornamental capitals.
Envelope: SQUARE, exact SOLO48 contract extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd221a319-f34d-44bc-84d3-b2d94f30cae8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jailhouse_d221a319-f34d-44bc-84d3-b2d94f30cae8.svg'
AUTHOR = 'gpt-6'


class Batch064Icon14(Solo48):
    icon_id = 'classical-columned-building-batch-064'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('classical', 'columned', 'building')

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

        self.add_polyline('roof',(6,18),(24,6),(42,18),(6,18),closed=True)
        for i,x in enumerate((9,19,29,39)):
            self.add_line(f'column-{i}',(x,26),(x,34))
        self.add_line('base',(6,42),(42,42))
