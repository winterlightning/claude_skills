from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='da3a18cb-9766-5ab1-b651-eb447e6f30a2'
SOURCE_PATH='pictographic-primitives/interface-essential/multiple tags 2_da3a18cb-9766-5ab1-b651-eb447e6f30a2.svg'
AUTHOR='gpt-6'
PLAN='Lucide tags: diagonal front tag with hole and offset partial rear outline. Shared overlap nodes; rear edge eight units from foreground edge.'
class Drawing(Solo48):
    icon_id='multiple-tags-2'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('multiple', 'tags', '2')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_polyline('front',(6,22),(22,6),(34,6),(34,14),(34,26),(26,34),(18,42),(6,30),closed=True)
        self.add_polyline('rear',(34,14),(42,22),(42,42),(26,42),(26,34))
        self.relate('connect','front','rear')
        self.circle('hole',24,20,2)

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,ops,closed=False):
        at=start;members=[]
        for i,op in enumerate(ops):
            eid=f'{n}-{i}';kind,end,*args=op
            if end==at:continue
            if kind=='L':self.add_line(eid,at,end)
            elif kind=='A':self.add_arc(eid,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='B':self.add_bezier(eid,at,(*args,end))
            at=end;members.append(eid)
        self.add_contour(n,*members,closed=closed)
    def rect(self,n,l,t,r,b,q=4):
        self.path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True)],True)
