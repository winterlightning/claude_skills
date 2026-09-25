"""Trimmed Garden Hedge.

Plan: Broad clipped hedge with four equal scallops and a straight soil edge.
Reduction / construction: No close Lucide hedge match; preserve lobed silhouette and reduce foliage texture.
Envelope: HRECT_L, exact SOLO48 contract extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2090da93-df4b-483a-b49e-a4314269dcfd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hedge_2090da93-df4b-483a-b49e-a4314269dcfd.svg'
AUTHOR = 'gpt-6'


class Batch064Icon3(Solo48):
    icon_id = 'clipped-garden-hedge-batch-064'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('clipped', 'garden', 'hedge')

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

        cmds=[]
        for x in range(4,44,10):cmds.append(('A',(x+10,16),5,8,True))
        cmds += [('L',(44,32)),('A',(36,40),8,8,True),('L',(12,40)),('A',(4,32),8,8,True),('L',(4,16))]
        path('hedge',(4,16),cmds,True)
        for x in (16,32):
            self.add_arc(f'foliage-{x}',(x-3,25),(x+3,29),radius_x=6,radius_y=6)
