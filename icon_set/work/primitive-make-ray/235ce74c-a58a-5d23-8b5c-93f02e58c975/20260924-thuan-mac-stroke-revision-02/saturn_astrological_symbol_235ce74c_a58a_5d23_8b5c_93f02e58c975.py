"""Saturn glyph with a cross at the top of a long stem and a smooth asymmetric sickle. VRECT_L centerlines (8,4)-(40,44). One coherent cubic hook replaces mismatched elliptic arcs."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='235ce74c-a58a-5d23-8b5c-93f02e58c975'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__saturn-astrological-symbol/20260924T101756Z-thuan-mac/reference/astrology saturn_235ce74c-a58a-5d23-8b5c-93f02e58c975.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='No useful direct Lucide match'
DESIGN_PLAN='Saturn glyph with a cross at the top of a long stem and a smooth asymmetric sickle. VRECT_L centerlines (8,4)-(40,44). One coherent cubic hook replaces mismatched elliptic arcs.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='saturn-astrological-symbol'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('saturn', 'astrological', 'symbol')
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
        self.path('stem-and-sickle',(16,4),[('L',(16,12)),('L',(16,24)),('C',(28,20),(20,18),(24,20)),('C',(40,28),(35,20),(40,22)),('C',(18,44),(40,37),(30,44))])
        self.add_polyline('crossbar',(8,12),(16,12),(28,12));self.relate('connect','crossbar','stem-and-sickle')
