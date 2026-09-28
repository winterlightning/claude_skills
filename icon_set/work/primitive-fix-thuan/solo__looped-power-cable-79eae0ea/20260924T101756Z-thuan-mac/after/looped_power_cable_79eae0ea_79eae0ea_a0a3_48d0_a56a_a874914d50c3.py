"""Broad looped cable ends in a rounded plug with two evenly spaced prongs. SQUARE centerlines (6,6)-(42,42); tangent loop shoulders and larger plug opening."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='79eae0ea-a0a3-48d0-a56a-a874914d50c3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__looped-power-cable-79eae0ea/20260924T101756Z-thuan-mac/reference/circle cable_79eae0ea-a0a3-48d0-a56a-a874914d50c3.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='plug: rounded body and paired prongs'
DESIGN_PLAN='Broad looped cable ends in a rounded plug with two evenly spaced prongs. SQUARE centerlines (6,6)-(42,42); tangent loop shoulders and larger plug opening.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='looped-power-cable-79eae0ea'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('looped', 'power', 'cable', '79eae0ea')
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
        self.path('plug',(26,6),[('L',(34,6)),('L',(34,18)),('L',(26,18)),('A',(20,12),6,6,True),('A',(26,6),6,6,True)],True)
        self.path('cable',(20,12),[('C',(6,28),(10,12),(6,19)),('A',(24,42),18,14,False),('A',(42,28),18,14,False)]);self.relate('connect','cable','plug')
        for y in (6,18):
            self.add_line(f'prong-{y}',(34,y),(42,y));self.relate('connect','plug',f'prong-{y}')
