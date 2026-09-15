"""texture: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dfd6c8ee-febb-5675-bdca-66f6927cbd01'
SOURCE_PATH = 'pictographic-primitives/nature/texture_dfd6c8ee-febb-5675-bdca-66f6927cbd01.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Texture(Solo48):
    icon_id = 'texture'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature'
    aliases = ()
    keywords = ('texture', 'nature')

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

        for i,y in enumerate((9, 19, 29, 39)):
            xs=(6, 24, 42);commands=[]
            for j,(a,b) in enumerate(zip(xs,xs[1:])):
                amplitude=3*(-1 if j%2==0 else 1)
                commands.append(('C',(a+(b-a)/3,y+amplitude*4/3),(b-(b-a)/3,y+amplitude*4/3),(b,y)))
            path(f'wave-{i}',(xs[0],y),commands)
