"""Diagonal rounded handle joins a broad flowing bristle head. SQUARE centerlines (6,6)-(42,42). Tangents flow around the cap and working tip; slanted shared seam separates materials."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d94b82bd-4c5f-4d8d-833a-9a520a8bed54'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__long-paintbrush-with-curved-bristle-tip/20260924T101756Z-thuan-mac/reference/brush_d94b82bd-4c5f-4d8d-833a-9a520a8bed54.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='paintbrush: coherent handle/head seam'
DESIGN_PLAN='Diagonal rounded handle joins a broad flowing bristle head. SQUARE centerlines (6,6)-(42,42). Tangents flow around the cap and working tip; slanted shared seam separates materials.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='long-paintbrush-with-curved-bristle-tip'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('long', 'paintbrush', 'with', 'curved', 'bristle', 'tip')
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
        self.path('handle',(20,24),[('L',(34,8)),('C',(38,6),(35,7),(36,6)),('C',(42,10),(40,6),(42,8)),('C',(40,14),(42,12),(41,13)),('L',(26,32)),('L',(20,24))],True)
        self.path('bristles',(20,24),[('C',(12,28),(16,22),(12,24)),('C',(10,36),(11,32),(11,33)),('C',(6,42),(9,39),(8,41)),('C',(26,32),(18,42),(26,38))]);self.relate('connect','bristles','handle')
