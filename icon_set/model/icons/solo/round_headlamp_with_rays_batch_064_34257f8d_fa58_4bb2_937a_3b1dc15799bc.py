"""Vehicle Headlight Symbol.

Plan: A convex headlamp face sends three evenly spaced beams to the left.
Reduction / construction: No exact Lucide match; remove nested lens to preserve three clear rays.
Envelope: HRECT_L, exact SOLO48 contract extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34257f8d-fa58-4bb2-937a-3b1dc15799bc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/headlight_34257f8d-fa58-4bb2-937a-3b1dc15799bc.svg'
AUTHOR = 'gpt-6'


class Batch064Icon5(Solo48):
    icon_id = 'round-headlamp-with-rays-batch-064'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('round', 'headlamp', 'with', 'rays')

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

        path('lamp',(24,8),[('A',(24,40),20,16,True),('L',(24,8))],True)
        for i,y in enumerate((8,24,40)):
            self.add_line(f'ray-{i}',(4,y),(14,y))
