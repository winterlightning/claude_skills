"""One round lower-left bow and a toothless diagonal shaft; SQUARE centerlines (6,6)-(42,42). Shaft edges are parallel with a broad opening. Preserve the round hole where present; omit the blank reference stray dot."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='7f99ed9d-aefc-4d4a-9237-167f01c21fea'
SOURCE_PATH='pictographic-primitives/symbol/state key_7f99ed9d-aefc-4d4a-9237-167f01c21fea.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'key-round'
DESIGN_PLAN = 'One round lower-left bow and a toothless diagonal shaft; SQUARE centerlines (6,6)-(42,42). Shaft edges are parallel with a broad opening. Preserve the round hole where present; omit the blank reference stray dot.'
class Drawing(Solo48):
    icon_id = 'key-round-bow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('key', 'round', 'bow')

    def path(self, name, start, commands, closed=False):
        members=[]
        for i,(kind,end,*args) in enumerate(commands):
            member=f'{name}-{i}'
            if kind=='L': self.add_line(member,start,end)
            elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
            members.append(member); start=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,cx,cy,r):
        self.path(name,(cx-r,cy),[('A',(cx,cy-r),r,r,True),('A',(cx+r,cy),r,r,True),('A',(cx,cy+r),r,r,True),('A',(cx-r,cy),r,r,True)],True)

    def build(self):
        self.path('outline',(32,29),[('A',(6,29),13,13,True),('A',(19,16),13,13,True),('C',(25,17),(21,16),(23,16)),('L',(36,6)),('L',(42,6)),('L',(42,12)),('L',(31,23)),('C',(32,29),(32,25),(32,27))],True)
        self.circle('hole',19,29,4)
