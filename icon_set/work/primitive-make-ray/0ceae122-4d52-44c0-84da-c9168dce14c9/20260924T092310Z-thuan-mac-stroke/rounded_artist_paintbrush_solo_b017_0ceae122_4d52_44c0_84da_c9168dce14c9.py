"""Diagonal artist brush with rounded handle, slanted ferrule and flowing bristle tip. Centerline extremes 6,6 to 42,42. Deliberately asymmetric sweep follows the source.
Construction reference: Lucide paintbrush: handle, collar and separate bristle contour.
Omissions: Thin double collar simplified to a single seam.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0ceae122-4d52-44c0-84da-c9168dce14c9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rounded-artist-paintbrush-solo-b017/20260924T092136Z-thuan-mac/reference/brush_0ceae122-4d52-44c0-84da-c9168dce14c9.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'rounded-artist-paintbrush-solo-b017'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/other'
    aliases = ()
    keywords = ('brush',)
    def build(self):
        self.path('handle',(19,24),[('L',(31,9)),('C',(36,6),(33,7),(34,6)),('A',(42,12),6,6,True),('C',(40,17),(42,14),(41,16)),('L',(27,30))])
        self.path('bristles',(19,24),[('C',(9,32),(13,23),(9,26)),('C',(6,42),(9,37),(8,40)),('C',(27,30),(22,42),(29,39))])
        self.add_polyline('ferrule',(17,22),(19,24),(27,30),(30,32))
        self.relate('connect','handle','bristles')
        self.relate('connect','handle','ferrule')
        self.relate('connect','bristles','ferrule')

    def path(self, name, start, commands, closed=False):
        members=[]
        for i,c in enumerate(commands):
            ident=f'{name}-{i}'
            if c[0]=='L': end=c[1];self.add_line(ident,start,end)
            elif c[0]=='A':
                _,end,rx,ry,sweep=c
                self.add_arc(ident,start,end,radius_x=rx,radius_y=ry,sweep=sweep)
            elif c[0]=='C':
                _,end,c1,c2=c
                self.add_bezier(ident,start,(c1,c2,end))
            members.append(ident);start=end
        self.add_contour(name,*members,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
