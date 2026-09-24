"""Moon goddess with paired hair buns, circular jaw, flared robe and upward curling long sleeves. Head bottom20 and shoulder28 give exact4 ink gap.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction references: human_ref/user.svg and full_body_ref.png: round jaw and balanced head/body proportions.
Omissions: Robe folds reduced to open silhouette; complete sleeves retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6e05b984-8712-4797-804e-62b2166b344f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__chinese-moon-goddess/20260924T152540Z-thuan-mac/reference/chinese moon festival lady_6e05b984-8712-4797-804e-62b2166b344f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'chinese-moon-goddess'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference'
    aliases = ()
    keywords = ('chinese', 'moon', 'festival', 'lady')
    def build(self):

        def path(n, start, steps, closed=False):
            ids=[]; p=start
            for i,step in enumerate(steps):
                k=f'{n}-{i}';kind=step[0];q=step[1]
                if kind=='L': self.add_line(k,p,q)
                elif kind=='A': self.add_arc(k,p,q,radius_x=step[2],radius_y=step[3],sweep=step[4])
                elif kind=='B': self.add_bezier(k,p,(step[2],step[3],q))
                ids.append(k);p=q
            self.add_contour(n,*ids,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('head',(16,12),[('L',(16,10)),('A',(24,10),4,4,True),('A',(32,10),4,4,True),('L',(32,12)),('A',(16,12),8,8,True)],True)
        path('robe',(18,28),[('L',(24,28)),('L',(30,28)),('B',(42,42),(30,34),(36,38)),('L',(6,42)),('B',(18,28),(12,38),(18,34))],True)
        for side in (0,1):
         p=lambda x,y:(x,y) if not side else (48-x,y)
         path('sleeve-'+str(side),p(18,28),[('B',p(10,34),p(18,32),p(14,34)),('B',p(6,22),p(6,34),p(6,28))])
         join('robe','sleeve-'+str(side))
