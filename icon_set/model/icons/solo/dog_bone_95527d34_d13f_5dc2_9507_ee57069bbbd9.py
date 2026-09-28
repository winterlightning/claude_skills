"""dog-bone: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95527d34-d13f-5dc2-9507-ee57069bbbd9'
SOURCE_PATH = 'pictographic-primitives/pets/dog bone_95527d34-d13f-5dc2-9507-ee57069bbbd9.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class DogBone(Solo48):
    icon_id = 'dog-bone'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    categories = ('pets', 'primitives')
    aliases = ()
    keywords = ('dog', 'bone', 'pets')

    def build(self):
        # Plan: HRECT_L; mirrored four lobes with matching waist transitions; removed stray one-unit tip.
        # Reference: Lucide bone: one coherent outline and paired end lobes.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        path('bone',(16,17),[
         ('C',(14,17),(17,8),(10,8)),('C',(6,8),(4,12),(4,17)),('C',(4,21),(7,22),(7,24)),
         ('C',(7,26),(4,27),(4,31)),('C',(4,36),(6,40),(10,40)),('C',(17,40),(14,31),(16,31)),
         ('L',(32,31)),('C',(34,31),(31,40),(38,40)),('C',(42,40),(44,36),(44,31)),
         ('C',(44,27),(41,26),(41,24)),('C',(41,22),(44,21),(44,17)),('C',(44,12),(42,8),(38,8)),
         ('C',(31,8),(34,17),(32,17)),('L',(16,17))],True)
