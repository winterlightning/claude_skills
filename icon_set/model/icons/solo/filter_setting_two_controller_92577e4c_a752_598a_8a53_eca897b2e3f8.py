"""filter-setting-two-controller: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92577e4c-a752-598a-8a53-eca897b2e3f8'
SOURCE_PATH = 'pictographic-primitives/interface-essential/filter setting two controller_92577e4c-a752-598a-8a53-eca897b2e3f8.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class FilterSettingTwoController(Solo48):
    icon_id = 'filter-setting-two-controller'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('filter', 'setting', 'two', 'controller', 'interface-essential')

    def build(self):
        # Plan: Shared circular knobs with exact rail endpoints; no intrusions or misaligned one-unit caps.
        # Reference: Lucide sliders-horizontal: one owning definition for each rail and knob.
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

        for i,(cx,cy) in enumerate([(17, 13), (32, 35)]):
         oval(f'knob-{i}',cx,cy,5)
         self.add_line(f'left-{i}',(4,cy),(cx-5,cy));self.add_line(f'right-{i}',(cx+5,cy),(44,cy))
         self.relate('connect',f'left-{i}',f'knob-{i}');self.relate('connect',f'right-{i}',f'knob-{i}')
