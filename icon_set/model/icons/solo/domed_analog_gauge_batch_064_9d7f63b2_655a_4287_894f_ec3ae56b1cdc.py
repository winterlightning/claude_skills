"""Analog Dashboard Gauge Meter.

Plan: Domed analog gauge with a flat base and a diagonal needle.
Reduction / construction: Gauge: single arc and diagonal needle; omit extra bottom band and pivot ring.
Envelope: HRECT_L, exact SOLO48 contract extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d7f63b2-655a-4287-894f-ec3ae56b1cdc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/instrumentation_9d7f63b2-655a-4287-894f-ec3ae56b1cdc.svg'
AUTHOR = 'gpt-6'


class Batch064Icon11(Solo48):
    icon_id = 'domed-analog-gauge-batch-064'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('domed', 'analog', 'gauge')

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
        axis = 24

        path('housing',(4,40),[('L',(4,28)),('A',(44,28),20,20,True),('L',(44,40)),('L',(4,40))],True)
        self.add_line('needle',(22,29),(31,20))
