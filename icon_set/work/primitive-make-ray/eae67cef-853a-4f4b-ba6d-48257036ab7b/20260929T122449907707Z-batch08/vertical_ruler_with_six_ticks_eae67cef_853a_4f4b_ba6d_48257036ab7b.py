"""The rejected ruler is broad and its ticks dominate the interior; shorten the ticks and make the ruled edge read clearly. No written reviewer feedback.
Symbol plan: Lucide ruler: attached alternating ticks. Four ticks replace six to maintain spacing; fixed SOLO48 envelope limits slenderness.
Keyshape VRECT_M, authored on the SOLO48 integer grid with 4-unit strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='eae67cef-853a-4f4b-ba6d-48257036ab7b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__vertical-ruler-with-six-ticks/20260929T121814Z-thuan-mac/reference/ruler vertical_eae67cef-853a-4f4b-ba6d-48257036ab7b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='vertical-ruler-with-six-ticks'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('vertical', 'ruler', 'with', 'six', 'ticks')

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

        self.add_polyline('body',(10,4),(38,4),(38,44),(10,44),(10,36),(10,28),(10,20),(10,12),closed=True)
        for i,y in enumerate((12,20,28,36)):
            self.add_line(f'tick-{i}',(10,y),(20 if i%2==0 else 16,y));self.relate('connect',f'tick-{i}','body')
