"""Long diagonal kitchen knife has a broad rounded cutting tip and an aligned rounded handle. Extrema 6,6,42,42.
Construction: pocket-knife: rounded grip; supplied blade controls long curved tip
Reduction: No essential features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='228264ac-5026-43da-8759-cb87af800439'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__long-rounded-tip-kitchen-knife/20260924T115443Z-thuan-mac/reference/blade_228264ac-5026-43da-8759-cb87af800439.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='long-rounded-tip-kitchen-knife'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('long', 'rounded', 'tip', 'kitchen', 'knife')
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

        path('blade',(20,26),[('L',(42,6)),('L',(42,10)),('A',(30,34),12,24,True),('L',(26,36)),('L',(20,26))],True)
        path('handle',(20,26),[('L',(10,34)),('A',(6,38),4,4,False),('A',(10,42),4,4,False),('L',(26,36))]);join('handle','blade')
