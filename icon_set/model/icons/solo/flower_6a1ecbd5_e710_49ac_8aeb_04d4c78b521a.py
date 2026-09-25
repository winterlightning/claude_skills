"""flower: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a1ecbd5-e710-49ac-8aeb-04d4c78b521a'
SOURCE_PATH = 'pictographic-primitives/nature/flower_6a1ecbd5-e710-49ac-8aeb-04d4c78b521a.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Flower(Solo48):
    icon_id = 'flower'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature'
    categories = ('nature', 'primitives')
    aliases = ()
    keywords = ('flower', 'nature')

    def build(self):
        # Plan: Five mirrored petals with smooth lobe curves; preserved the original center mark.
        # Reference: Lucide flower: coherent petal lobes and balanced center spacing.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        left,right,top,bottom=6,42,6,42
        path('flower',(24,top),[('C',(29,top),(32,top+3),(32,15)),
         ('C',(38,13),(right,17),(right,22)),('C',(right,27),(39,29),(35,30)),
         ('C',(39,36),(35,bottom),(30,bottom)),('C',(27,bottom),(25,39),(24,37)),
         ('C',(23,39),(21,bottom),(18,bottom)),('C',(13,bottom),(9,36),(13,30)),
         ('C',(9,29),(left,27),(left,22)),('C',(left,17),(10,13),(16,15)),
         ('C',(16,top+3),(19,top),(24,top))],True)
