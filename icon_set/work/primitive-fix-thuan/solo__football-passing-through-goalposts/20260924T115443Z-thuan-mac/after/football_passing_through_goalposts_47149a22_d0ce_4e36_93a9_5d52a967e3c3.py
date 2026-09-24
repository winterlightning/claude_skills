"""A diagonal football travels between upright goalposts above a central post; two trail marks show motion. Extrema 6,6,42,42.
Construction: No useful Lucide goal-post match; original arrangement retained
Reduction: Ball laces omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='47149a22-d0ce-4e36-93a9-5d52a967e3c3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__football-passing-through-goalposts/20260924T115443Z-thuan-mac/reference/american football score_47149a22-d0ce-4e36-93a9-5d52a967e3c3.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='football-passing-through-goalposts'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('football', 'passing', 'through', 'goalposts')
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

        line('left-upright',(6,6),(6,18))
        poly('goal',(42,6),(42,28),(32,28),(22,28));line('post',(32,28),(32,42));poly('base',(22,42),(32,42),(42,42));join('post','goal');join('post','base')
        path('ball',(22,18),[('A',(32,8),8,8,True),('A',(22,18),8,8,True)],True)
        line('trail-low',(6,42),(8,37));line('trail-high',(11,29),(14,25))
