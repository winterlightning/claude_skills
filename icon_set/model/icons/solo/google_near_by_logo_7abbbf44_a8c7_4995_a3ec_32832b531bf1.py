"""google-near-by-logo: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7abbbf44-a8c7-4995-a3ec-32832b531bf1'
SOURCE_PATH = 'pictographic-primitives/logos/google near by logo_7abbbf44-a8c7-4995-a3ec-32832b531bf1.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class GoogleNearByLogo(Solo48):
    icon_id = 'google-near-by-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('google', 'near', 'by', 'logo', 'logos')

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
        self.add_arc('hole-a',(24,15),(24,25),radius_x=5)
        self.add_arc('hole-b',(24,25),(24,15),radius_x=5)
        self.add_contour('hole','hole-a','hole-b',closed=True)
