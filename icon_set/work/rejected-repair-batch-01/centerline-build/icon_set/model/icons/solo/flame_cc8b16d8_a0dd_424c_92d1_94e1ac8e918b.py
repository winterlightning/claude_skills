"""flame-fire: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc8b16d8-a0dd-424c-92d1-94e1ac8e918b'
SOURCE_PATH = 'pictographic-primitives/fire/flame_cc8b16d8-a0dd-424c-92d1-94e1ac8e918b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class FlameFire(Solo48):
    icon_id = 'flame-fire'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'fire'
    aliases = ()
    keywords = ('flame', 'fire')

    def build(self):
        # Plan: VRECT_L; flowing main flame and smooth lower bowl preserve the smaller side tongue.
        # Reference: No close Lucide flame silhouette; retain deliberate asymmetric tongues.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        path('flame',(22,4),[('C',(26,7),(31,14),(31,20)),('C',(31,22),(30,25),(29,27)),
         ('L',(37,21)),('C',(39,25),(40,28),(40,31)),('C',(40,39),(33,44),(24,44)),
         ('C',(15,44),(8,38),(8,30)),('C',(8,20),(20,15),(22,4))],True)
