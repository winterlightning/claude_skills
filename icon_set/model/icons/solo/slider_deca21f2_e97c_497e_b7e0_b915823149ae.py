"""slider: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'deca21f2-e97c-497e-b7e0-b915823149ae'
SOURCE_PATH = 'pictographic-primitives/symbol/slider_deca21f2-e97c-497e-b7e0-b915823149ae.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Slider(Solo48):
    icon_id = 'slider'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('slider', 'symbol')

    def build(self):
        # Plan: HRECT_L; identical round knobs and rails ending exactly on their boundaries; removed one-unit intrusions.
        # Reference: Lucide sliders-horizontal: a common rail definition and exact knob placement.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L':self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C':self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A':self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry=None):
            ry=rx if ry is None else ry
            path(name,(cx-rx,cy),[('A',(cx,cy-ry),rx,ry,True),('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)

        # Every rail stops exactly at its own circular knob's extreme.
        for i,cx,y in [(0,16,13),(1,32,27)]:
         oval(f'knob-{i}',cx,y,5)
         self.add_line(f'left-{i}',(4,y),(cx-5,y));self.add_line(f'right-{i}',(cx+5,y),(44,y))
         self.relate('connect',f'left-{i}',f'knob-{i}');self.relate('connect',f'right-{i}',f'knob-{i}')
        self.add_line('base',(4,40),(44,40))
