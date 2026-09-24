"""Bare foot and ankle profile has a broad instep, rounded toes, subtle sole arch and rounded heel. Extrema 6,6,42,42.
Construction: footprints: continuous anatomical outline; shared human reference reviewed, no detached head applies
Reduction: Toe separations omitted for side profile.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='701d2de1-4e8d-4d6a-a231-6a023e70c571'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__foot-and-ankle-profile/20260924T115443Z-thuan-mac/reference/heel_701d2de1-4e8d-4d6a-a231-6a023e70c571.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='foot-and-ankle-profile'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('foot', 'and', 'ankle', 'profile')
    def build(self):

        def path(name,start,steps,closed=False):
            here=start;members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
                else:self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m);here=end
            self.add_contour(name,*members,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def poly(n,*pts,closed=False):self.add_polyline(n,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('foot',(30,6),[('L',(30,16)),('C',(22,28),(30,22),(28,25)),('C',(10,33),(16,31),(14,33)),('A',(6,37),4,4,False),('A',(11,42),5,5,False),('C',(24,40),(16,42),(18,40)),('C',(34,42),(29,40),(30,42)),('A',(42,34),8,8,False),('C',(38,20),(42,29),(38,25)),('L',(38,6))])
