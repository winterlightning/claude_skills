"""pin-three: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '99969027-edcc-4ca3-946a-a4e68acb97fe'
SOURCE_PATH = 'pictographic-primitives/other/pin three_99969027-edcc-4ca3-946a-a4e68acb97fe.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PinThree(Solo48):
    icon_id = 'pin-three'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('pin', 'three', 'other')

    def build(self):
        # Plan: VRECT_L; circular crown and mirrored tangent shoulders meet at one centered pin tip.
        # Reference: Lucide map-pin: symmetric location outline and centered marker.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        # Left and right halves share their apex, crown and tangent controls.
        path('pin',(24,44),[('C',(18,38),(8,30),(8,20)),('A',(24,4),16,16,True),
         ('A',(40,20),16,16,True),('C',(40,30),(30,38),(24,44))],True)
