"""News page with headline, two short text lines and rising market arrow;9-unit row spacing.
Symbol plan: shared contour owners and attachment nodes; repeated marks share a spacing parameter.
Omissions: Header box reduced to headline; chart intermediate zigzag removed for clearance.
Construction: Lucide arrow-down-right: shared arrow endpoint; adapted to an upward market direction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='55261672-8aa2-44d9-b648-0fed630f399c'
SOURCE_PATH='pictographic-primitives/_uncategorized_38/trading news 1_55261672-8aa2-44d9-b648-0fed630f399c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='trading-news-1'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('trading', 'news', '1')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.box('page',6,6,42,42,4)
        self.add_line('headline',(15,15),(33,15))
        for i,y in enumerate((24,33)):
            self.add_line(f'text-{i}',(15,y),(17,y))
        self.add_line('trend',(25,33),(33,24))
        self.add_polyline('arrow',(25,24),(33,24),(33,32))
        self.relate('connect','trend','arrow')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
    def path(self,n,start,ops,closed=False):
        p=start;members=[]
        for i,op in enumerate(ops):
            name=f'{n}-{i}';end=op[1]
            if op[0]=='L':self.add_line(name,p,end)
            elif op[0]=='A':self.add_arc(name,p,end,radius_x=op[2],radius_y=op[3],sweep=op[4])
            elif op[0]=='B':self.add_bezier(name,p,(op[2],op[3],end))
            members.append(name);p=end
        if closed and p!=start:
            self.add_line(n+'-close',p,start);members.append(n+'-close')
        self.add_contour(n,*members,closed=closed)
