"""A broad bowl-shaped vessel under wireless signal arcs above water. SQUARE centerlines (6,6)-(42,42). Shared signal axis and symmetric hull, one smooth wave. Omit crowded rear rim and third signal tier."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='c301559e-579c-4654-91bd-95b3bbcf39dd'
SOURCE_PATH='pictographic-primitives/programing/lake formation_c301559e-579c-4654-91bd-95b3bbcf39dd.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'wifi'
DESIGN_PLAN = 'A broad bowl-shaped vessel under wireless signal arcs above water. SQUARE centerlines (6,6)-(42,42). Shared signal axis and symmetric hull, one smooth wave. Omit crowded rear rim and third signal tier.'
class Drawing(Solo48):
    icon_id = 'lake-vessel-signal'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    categories = ('programing', 'primitives')
    aliases = ()
    keywords = ('lake', 'vessel', 'signal')
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
        self.path('signal-outer',(13,10),[('C',(24,6),(16,7),(20,6)),('C',(35,10),(28,6),(32,7))])
        self.path('signal-inner',(21,18),[('C',(27,18),(23,16),(25,16))])
        self.path('vessel',(6,23),[('C',(24,30),(6,28),(14,30)),('C',(42,23),(34,30),(42,28))])
        self.path('water',(6,40),[('C',(15,42),(9,40),(11,42)),('C',(24,40),(19,42),(21,40)),('C',(33,38),(27,40),(29,38)),('C',(42,40),(37,38),(39,40))])
