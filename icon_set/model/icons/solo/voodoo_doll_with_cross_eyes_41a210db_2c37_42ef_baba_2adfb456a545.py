"""Voodoo Doll with Cross Eyes.

Plan: Large circular doll head, two cross eyes, outstretched rounded limbs and pin at left. Bounds (6,6)-(42,42).
Construction: Source doll; human_ref rounded limb vocabulary for a sewn toy.
Reduction: Upright, wide-headed sewn doll with two visible cross eyes and rounded limbs; pin omitted to preserve the defining face.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '41a210db-2c37-42ef-baba-2adfb456a545'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/voodoo doll_41a210db-2c37-42ef-baba-2adfb456a545.svg'
AUTHOR = 'gpt-6'


class IconVoodooDollWithCrossEyes(Solo48):
    icon_id = 'voodoo-doll-with-cross-eyes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    aliases = ()
    keywords = ('voodoo', 'doll', 'with', 'cross', 'eyes')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start
            members=[]
            for i, (kind,end,*args) in enumerate(commands):
                k=f"{name}-{i}"
                if kind == "L": self.add_line(k,here,end)
                elif kind == "A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind == "C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k)
                here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)],True)
        path('doll',(6,18),[('A',(24,6),18,12,True),('A',(42,18),18,12,True),('C',(34,28),(42,24),(37,27)),('L',(36,28)),('A',(40,32),4,4,True),('A',(36,36),4,4,True),('L',(36,38)),('A',(32,42),4,4,True),('L',(24,34)),('L',(16,42)),('A',(12,38),4,4,True),('L',(12,36)),('A',(8,32),4,4,True),('A',(12,28),4,4,True),('L',(14,28)),('C',(6,18),(11,27),(6,24))],True)
        for x in [18,30]:
         self.add_line('eye-a'+str(x),(x-2,16),(x+2,20));self.add_line('eye-b'+str(x),(x-2,20),(x+2,16));self.relate('connect','eye-a'+str(x),'eye-b'+str(x))
