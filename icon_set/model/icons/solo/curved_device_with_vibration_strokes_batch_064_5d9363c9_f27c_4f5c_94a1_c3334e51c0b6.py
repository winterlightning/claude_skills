"""Vibrating Haptic Sensor.

Plan: A broad haptic device with a lower central notch and mirrored vibration marks.
Reduction / construction: Vibrate: paired angular motion strokes; omit crowded interior device stripe.
Envelope: HRECT_L, exact SOLO48 contract extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5d9363c9-f27c-4f5c-94a1-c3334e51c0b6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/haptic sensor vibration 1_5d9363c9-f27c-4f5c-94a1-c3334e51c0b6.svg'
AUTHOR = 'gpt-6'


class Batch064Icon7(Solo48):
    icon_id = 'curved-device-with-vibration-strokes-batch-064'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('curved', 'device', 'with', 'vibration', 'strokes')

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

        path('device',(12,24),[('L',(36,24)),('A',(44,32),8,8,True),('A',(36,40),8,8,True),('L',(30,40)),('L',(24,34)),('L',(18,40)),('L',(12,40)),('A',(4,32),8,8,True),('A',(12,24),8,8,True)],True)
        for side in (-1,1):
            self.add_polyline(f'vibration-{side}',(24+side*6,8),(24+side*9,14),(24+side*14,10),(24+side*18,16))
