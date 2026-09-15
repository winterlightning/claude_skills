"""microsoft-visual-studio-logo-1: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2d7127b-4a91-4f1f-9461-fcc33608bdcb'
SOURCE_PATH = 'pictographic-primitives/logos/microsoft visual studio logo 1_c2d7127b-4a91-4f1f-9461-fcc33608bdcb.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class MicrosoftVisualStudioLogo1(Solo48):
    icon_id = 'microsoft-visual-studio-logo-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('microsoft', 'visual', 'studio', 'logo', 'logos')

    def build(self):
        # Plan: HRECT_L; mirrored infinity loops with continuous crossover tangents and matching bowls.
        # Reference: Lucide infinity: continuous crossing and balanced loops.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        # Mirrored loop definition with diagonal tangency at the crossover.
        path('infinity',(24,24),[
         ('C',(18,14),(17,8),(12,8)),('C',(7,8),(4,15),(4,24)),
         ('C',(4,33),(7,40),(12,40)),('C',(17,40),(18,34),(24,24)),
         ('C',(30,14),(31,8),(36,8)),('C',(41,8),(44,15),(44,24)),
         ('C',(44,33),(41,40),(36,40)),('C',(31,40),(30,34),(24,24))],True)
