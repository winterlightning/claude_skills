"""A bellied square sail on a mast above an open hull and a wave. SQUARE centerlines (6,6)-(42,42). Shared sail extrema and smooth wave quarters replace the uneven earlier wave."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'db3bca6b-db6e-54f4-a4d9-700a3c6b0783'
SOURCE_PATH = 'pictographic-primitives/transportation/bark_db3bca6b-db6e-54f4-a4d9-700a3c6b0783.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='sailboat: shared mast attachment and broad hull'
DESIGN_PLAN='A bellied square sail on a mast above an open hull and a wave. SQUARE centerlines (6,6)-(42,42). Shared sail extrema and smooth wave quarters replace the uneven earlier wave.'
OMISSIONS='Lower hull edge omitted as in the open source; small sail area rebalanced for clearance.'
class Drawing(Solo48):
    icon_id='sailing-bark-on-waves'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'transportation'
    aliases=()
    keywords=('sailing', 'bark', 'on', 'waves')
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
        self.path('sail',(16,6),[('C',(16,18),(20,10),(20,14)),('L',(24,18)),('L',(30,18)),('A',(37,12),7,6,False),('A',(30,6),7,6,False),('L',(16,6))],True)
        self.add_line('mast',(24,18),(24,28));self.relate('connect','sail','mast')
        self.path('hull',(12,32),[('C',(6,28),(9,32),(6,30)),('L',(24,28)),('L',(42,28)),('C',(36,32),(42,30),(39,32))]);self.relate('connect','mast','hull')
        self.path('water',(6,42),[('C',(15,40),(10,42),(11,40)),('C',(24,42),(19,40),(20,42)),('C',(33,40),(28,42),(29,40)),('C',(42,42),(37,40),(38,42))])
