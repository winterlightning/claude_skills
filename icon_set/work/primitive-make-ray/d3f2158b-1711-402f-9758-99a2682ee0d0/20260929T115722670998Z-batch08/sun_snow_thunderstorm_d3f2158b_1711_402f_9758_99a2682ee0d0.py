"""The rejected sun looks like a small loop attached to the cloud; restore a larger visible solar arc while preserving lightning and snow. No written feedback.
Symbol plan: Lucide cloud-sun: sun partially hidden by the cloud. Fine rays omitted; two snow pellets retained.
Keyshape SQUARE, authored on the SOLO48 integer grid with 4-unit strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d3f2158b-1711-402f-9758-99a2682ee0d0'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__sun-snow-thunderstorm/20260929T115301Z-thuan-mac/reference/weather snow thunder_d3f2158b-1711-402f-9758-99a2682ee0d0.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='sun-snow-thunderstorm'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('sun', 'snow', 'thunderstorm')

    def path(self,n,start,ops,closed=False):
        here=start; members=[]
        for i,(kind,end,*args) in enumerate(ops):
            m=f'{n}-{i}'
            if kind=='L': self.add_line(m,here,end)
            elif kind=='A': self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
            members.append(m); here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)

    def build(self):

        self.path('cloud',(10,30),[('C',(6,24),(6,30),(6,28)),('A',(14,16),8,8,True),('C',(26,14),(16,10),(22,10)),('C',(36,22),(32,14),(35,18)),('C',(42,30),(42,22),(42,26))])
        self.path('sun',(14,16),[('C',(10,6),(5,14),(5,6)),('C',(26,14),(19,6),(24,8))]);self.relate('connect','sun','cloud')
        self.add_polyline('bolt',(26,24),(18,33),(30,33),(22,42))
        self.add_dot('snow-left',(7,41));self.add_dot('snow-right',(41,41))
