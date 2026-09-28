"""A leaping dolphin with a curved back, small dorsal fin, projecting beak, broad flipper and forked tail. SQUARE centerlines (6,6)-(42,42). Smooth belly and back; intentional directional asymmetry. Omit tiny eye."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c0fe22a4-31db-554f-b6d7-6ce3be390288'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__leaping-dolphin/20260924T100528Z-thuan-mac/reference/dolphin_c0fe22a4-31db-554f-b6d7-6ce3be390288.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'fish'
DESIGN_PLAN = 'A leaping dolphin with a curved back, small dorsal fin, projecting beak, broad flipper and forked tail. SQUARE centerlines (6,6)-(42,42). Smooth belly and back; intentional directional asymmetry. Omit tiny eye.'
class Drawing(Solo48):
    icon_id = 'leaping-dolphin-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('leaping', 'dolphin')
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
        self.path('outline',(8,34),[('C',(20,10),(2,21),(13,10)),('L',(18,6)),('L',(26,8)),('L',(29,12)),('C',(42,24),(37,15),(42,18)),('C',(40,28),(42,26),(42,30)),('L',(32,23)),('C',(25,26),(30,25),(28,26)),('L',(27,20)),('C',(14,33),(17,19),(14,26)),('L',(23,39)),('C',(14,39),(20,38),(17,38)),('L',(6,42)),('L',(8,34))],True)
