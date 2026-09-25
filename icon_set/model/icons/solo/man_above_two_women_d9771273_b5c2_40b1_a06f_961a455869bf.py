'Three people in triangular grouping with equal radius4 heads, upper man and two lower women. Bounds4,8 to44,40; all head-to-shoulder gaps exactly8 centerline.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd9771273-b5c2-40b1-a06f-961a455869bf'
SOURCE_PATH = 'pictographic-primitives/users/user multiple half male female_d9771273-b5c2-40b1-a06f-961a455869bf.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'human_ref/user.svg: equal circular heads with open shoulder arches.'
OMISSIONS = 'Fringes omitted to avoid filling small faces; top shoulders shortened between women.'

def path(s,n,p,cs,closed=False):
    ids=[]
    for j,c in enumerate(cs):
        eid=f'{n}-{j}';q=c[-1]
        if c[0]=='L':s.add_line(eid,p,q)
        elif c[0]=='A':s.add_arc(eid,p,q,radius_x=c[1],radius_y=c[2],sweep=c[3])
        elif c[0]=='C':s.add_bezier(eid,p,(c[1],c[2],q))
        ids.append(eid);p=q
    s.add_contour(n,*ids,closed=closed)
def circle(s,n,x,y,r):
    path(s,n,(x-r,y),[('A',r,r,True,(x+r,y)),('A',r,r,True,(x-r,y))],True)

class Drawing(Solo48):
    icon_id = 'man-above-two-women'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'users'
    categories = ('users', 'primitives')
    aliases = ()
    keywords = ('user', 'multiple', 'half', 'male', 'female')
    def build(self):
        circle(self,'man',24,12,4)
        path(self,'man-shoulders',(22,25),[('A',2,1,True,(24,24)),('A',2,1,True,(26,25))])
        for n,x in [('left',10),('right',38)]:
            circle(self,n+'-head',x,27,4)
            path(self,n+'-shoulder',(x-6,40),[('A',6,1,True,(x,39)),('A',6,1,True,(x+6,40))])
            path(self,n+'-hair',(x-4,27),[('L',(x-6,31))])
            path(self,n+'-hair-r',(x+4,27),[('L',(x+6,31))])
            self.relate('connect',n+'-head',n+'-hair')
            self.relate('connect',n+'-head',n+'-hair-r')
