"""Vertical Spanner Wrench Tool.

Plan: Symmetric open end wrench with a U jaw and rounded handle.
Reduction / construction: Wrench: unified open jaw silhouette; preserve upright orientation and omit handle hole.
Envelope: VRECT_L, exact SOLO48 contract extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e832fdcc-c00d-4547-9cca-63111af74781'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hardware_e832fdcc-c00d-4547-9cca-63111af74781.svg'
AUTHOR = 'gpt-6'


class Batch064Icon6(Solo48):
    icon_id = 'upright-open-end-wrench-batch-064'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('upright', 'open', 'end', 'wrench')

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

        path('wrench',(axis-8,4),[('L',(axis-8,12)),('A',(axis+8,12),8,8,False),('L',(axis+8,4)),('A',(axis+16,16),8,12,True),('L',(axis+16,20)),('L',(axis+6,30)),('L',(axis+6,38)),('A',(axis-6,38),6,6,True),('L',(axis-6,30)),('L',(axis-16,20)),('L',(axis-16,16)),('A',(axis-8,4),8,12,True)],True)
