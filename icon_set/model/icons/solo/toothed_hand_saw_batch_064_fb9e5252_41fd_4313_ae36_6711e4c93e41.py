"""Wood Cutting Hand Saw.

Plan: A toothed hand saw with a broad grip and blade pointing to the right.
Reduction / construction: No useful exact Lucide match; use an open U-shaped grip and two broad blade teeth; omit the enclosed grip hole.
Envelope: HRECT_L, exact SOLO48 contract extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb9e5252-41fd-4313-ae36-6711e4c93e41'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/handsaw_fb9e5252-41fd-4313-ae36-6711e4c93e41.svg'
AUTHOR = 'gpt-6'


class Batch064Icon9(Solo48):
    icon_id = 'toothed-hand-saw-batch-064'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('toothed', 'hand', 'saw')

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

        self.add_polyline('handle',(4,22),(4,40),(16,40),(16,36),(16,18))
        self.add_polyline('blade',(16,18),(44,8),(44,20),(36,20),(32,28),(28,28),(24,36),(16,36))
        self.relate('connect','handle','blade')
