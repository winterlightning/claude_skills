"""keyboard-command: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b75ae0ab-122c-4bf0-bbc7-faf135e366a4'
SOURCE_PATH = 'pictographic-primitives/interface-essential/keyboard command_b75ae0ab-122c-4bf0-bbc7-faf135e366a4.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class KeyboardCommand(Solo48):
    icon_id = 'keyboard-command'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('keyboard', 'command', 'interface-essential')

    def build(self):
        # Plan: SQUARE; four equal circular loops and a centered square replace 39 irregular segments.
        # Reference: Lucide command: one continuous run with four matching loops.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        # A single traversed stroke; four identical radius-six terminal loops.
        path('command',(18,18),[
         ('L',(12,18)),('A',(6,12),6,6,True),('A',(12,6),6,6,True),('A',(18,12),6,6,True),
         ('L',(18,36)),('A',(12,42),6,6,True),('A',(6,36),6,6,True),('A',(12,30),6,6,True),
         ('L',(36,30)),('A',(42,36),6,6,True),('A',(36,42),6,6,True),('A',(30,36),6,6,True),
         ('L',(30,12)),('A',(36,6),6,6,True),('A',(42,12),6,6,True),('A',(36,18),6,6,True),('L',(18,18))],True)
