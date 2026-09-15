"""speaker: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81d4c431-5d96-51d5-9f0d-22d192c29508'
SOURCE_PATH = 'pictographic-primitives/audio/speaker_81d4c431-5d96-51d5-9f0d-22d192c29508.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Speaker(Solo48):
    icon_id = 'speaker'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('speaker', 'audio')

    def build(self):
        # Plan: SQUARE; matching mounting ears around a centered circular cone.
        # Reference: No exact speaker-driver reference; repeated rotational geometry.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        # Four identical mounting ears, smoothly joined to the circular body.
        path('rim',(24,6),[
         ('C',(28,6),(31,7),(34,9)),('C',(40,3),(45,8),(39,14)),
         ('C',(43,20),(43,28),(39,34)),('C',(45,40),(40,45),(34,39)),
         ('C',(28,43),(20,43),(14,39)),('C',(8,45),(3,40),(9,34)),
         ('C',(5,28),(5,20),(9,14)),('C',(3,8),(8,3),(14,9)),('C',(17,7),(20,6),(24,6))],True)
        self.add_arc('cone-a',(24,17),(24,31),radius_x=7)
        self.add_arc('cone-b',(24,31),(24,17),radius_x=7)
        self.add_contour('cone','cone-a','cone-b',closed=True)
