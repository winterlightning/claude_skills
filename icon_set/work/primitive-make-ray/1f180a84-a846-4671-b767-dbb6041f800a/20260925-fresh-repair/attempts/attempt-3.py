from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='1f180a84-a846-4671-b767-dbb6041f800a'
SOURCE_PATH='pictographic-primitives/travel/passport_1f180a84-a846-4671-b767-dbb6041f800a.svg'
AUTHOR='gpt-6'
PLAN='Rounded passport cover with a large centered globe. One straight longitude and equator retain geographic graticule with four larger openings.'
CONSTRUCTION_REFERENCES='globe: circle plus cardinal graticule; rounded cover follows panel construction.'
OMISSIONS=['Back-cover reveal omitted to enlarge globe.', 'Paired curved meridians replaced with one straight longitude.']
class Drawing(Solo48):
    icon_id='travel-passport-with-globe'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('passport',)

    def path(self,n,start,commands,closed=False):
        here=start;members=[]
        for i,(kind,end,*a) in enumerate(commands):
            k=f'{n}-{i}';members.append(k)
            if kind=='L':self.add_line(k,here,end)
            elif kind=='A':self.add_arc(k,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C':self.add_bezier(k,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)

    def build(self):
        # Separate actual corner nodes permit exact support bounds for each cover wall.
        nodes=[(6,6),(42,6),(42,42),(6,42)]
        for i in range(4):self.add_line(f'cover-{i}',nodes[i],nodes[(i+1)%4])
        for i in range(4):self.relate('connect',f'cover-{i}',f'cover-{(i+1)%4}')
        self.circle('globe',24,24,10)
        self.add_polyline('equator',(14,24),(24,24),(34,24))
        self.add_polyline('longitude',(24,14),(24,24),(24,34))
        self.relate('connect','globe','equator');self.relate('connect','globe','longitude');self.relate('connect','equator','longitude')
