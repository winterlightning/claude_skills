"""alluvium: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3e4a9c7-dc3d-4a9b-81c9-23a3db70e396'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/alluvium_b3e4a9c7-dc3d-4a9b-81c9-23a3db70e396.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Alluvium(Solo48):
    icon_id = 'alluvium'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('alluvium', '_uncategorized_02')

    def build(self):
        # Plan: HRECT_L; three identical translated waves with smooth continuous tangents.
        # Reference: No exact wave reference; repeated curve definition.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        for i,y in enumerate((12,24,36)):
         path(f'wave-{i}',(4,y),[('C',(4+20/3,y-16/3),(24-20/3,y-16/3),(24,y)),
         ('C',(24+20/3,y+16/3),(44-20/3,y+16/3),(44,y))])
