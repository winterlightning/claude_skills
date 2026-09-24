"""Circular ring with three attached bent key shafts; SQUARE centerlines (6,6)-(42,42). Split ring at attachment quadrants; three distinct terminals. Small individual bow loops and extra teeth omitted to preserve space."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5b4ceba3-b822-46fa-bd5f-29ab137243d1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__key-ring-with-keys/20260924T100528Z-thuan-mac/reference/tools keys_5b4ceba3-b822-46fa-bd5f-29ab137243d1.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'key-round'
DESIGN_PLAN = 'Circular ring with three attached bent key shafts; SQUARE centerlines (6,6)-(42,42). Split ring at attachment quadrants; three distinct terminals. Small individual bow loops and extra teeth omitted to preserve space.'
class Drawing(Solo48):
    icon_id = 'key-ring-with-keys'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('key', 'ring', 'with', 'keys')

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
        self.circle('ring',22,18,12)
        self.add_polyline('left-key',(10,18),(6,30),(6,42),(14,42))
        self.add_polyline('middle-key',(22,30),(22,42),(30,42))
        self.add_polyline('right-key',(34,18),(42,18),(42,10))
        for n in ['left-key','middle-key','right-key']: self.relate('connect','ring',n)
