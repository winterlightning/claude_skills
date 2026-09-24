"""smart house open. One wireless arc above a connected roof and walls; two opening chevrons retained. Omitted secondary wifi arc.
Symbol plan: shared circle/rounded-frame parameters; meaningful joints reuse endpoints.
Reference: supplied SVG; Lucide shopping-basket and square-user construction inspected.
Human construction uses human_ref/user.svg where applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cd72149b-476c-4b5b-a1fd-e19535644748'
SOURCE_PATH='pictographic-primitives/_uncategorized_34/smart house open_cd72149b-476c-4b5b-a1fd-e19535644748.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='smart-house-open'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('smart house open',)
    def build(self):
        self.add_arc('wifi',(17,7),(31,7),radius_x=7,radius_y=3)
        self.add_polyline('house',(8,26),(24,16),(40,26),(40,44),(8,44),closed=True)
        for i in (0,1):
            def p(x,y):return (48-x if i else x,y)
            self.add_polyline('open-'+str(i),p(20,28),p(16,32),p(20,36))

    def circle(self,n,x,y,r):
        pts=[(x-r,y),(x,y-r),(x+r,y),(x,y+r),(x-r,y)]
        for i in range(4): self.add_arc(f'{n}-{i}',pts[i],pts[i+1],radius_x=r)
        self.add_contour(n,*(f'{n}-{i}' for i in range(4)),closed=True)
    def box(self,n,l,t,r,b,q=4):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        for i in range(8):
            if i%2:self.add_arc(f'{n}-{i}',pts[i],pts[(i+1)%8],radius_x=q)
            else:self.add_line(f'{n}-{i}',pts[i],pts[(i+1)%8])
        self.add_contour(n,*(f'{n}-{i}' for i in range(8)),closed=True)
    def cross(self,n,x,y,r):
        for i,(dx,dy) in enumerate([(-r,0),(r,0),(0,-r),(0,r)]):self.add_line(f'{n}-{i}',(x,y),(x+dx,y+dy))
        for i in range(4):
            for j in range(i):self.relate('connect',f'{n}-{i}',f'{n}-{j}')

# Contract keyshape visible bounds: (6, 2, 42, 46).
