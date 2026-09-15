"""warp-wave: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '014729fe-2ae7-5177-be6f-8ec606990bf7'
SOURCE_PATH = 'pictographic-primitives/design/warp wave_014729fe-2ae7-5177-be6f-8ec606990bf7.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class WarpWave(Solo48):
    icon_id = 'warp-wave'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'wave', 'design')

    def build(self):
        # Plan: Equal translated waves with matched tangent directions; tiny flat fragments removed.
        # Reference: No exact Lucide wave match; repeated smooth curve definition.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        for i,y in enumerate((12, 24, 36)):
            xs=(4, 24, 44);commands=[]
            for j,(a,b) in enumerate(zip(xs,xs[1:])):
                amplitude=4*(-1 if j%2==0 else 1)
                commands.append(('C',(a+(b-a)/3,y+amplitude*4/3),(b-(b-a)/3,y+amplitude*4/3),(b,y)))
            path(f'wave-{i}',(xs[0],y),commands)
