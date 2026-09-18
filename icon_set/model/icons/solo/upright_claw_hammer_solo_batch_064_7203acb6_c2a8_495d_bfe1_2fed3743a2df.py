"""Claw Hammer Tool.

Plan: Upright claw hammer with left striking face and curved right claw.
Reduction / construction: Hammer: unified tool contour; omit grip seam and claw split at native size.
Envelope: VRECT_L, exact SOLO48 contract extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7203acb6-c2a8-495d-bfe1-2fed3743a2df'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/implement_7203acb6-c2a8-495d-bfe1-2fed3743a2df.svg'
AUTHOR = 'gpt-6'


class Batch064Icon15(Solo48):
    icon_id = 'upright-claw-hammer-solo-batch-064'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('upright', 'claw', 'hammer', 'solo')

    def build(self):

        def path(name, start, commands, closed=False):
            members=[]
            point=start
            for i,command in enumerate(commands):
                kind,end,*args=command
                member=f"{name}-{i}"
                if kind=='L':
                    self.add_line(member,point,end)
                else:
                    rx,ry,sweep=args
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep)
                members.append(member)
                point=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx,cy-ry),rx,ry,True),('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        axis = 24

        path('hammer',(axis-16,4),[('L',(26,4)),('A',(axis+16,18),14,14,True),('L',(axis+6,14)),('L',(axis+6,38)),('A',(axis-6,38),6,6,True),('L',(axis-6,16)),('L',(axis-16,16)),('L',(axis-16,4))],True)
