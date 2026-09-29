"""Three equal circle nodes; bond endpoints use exact 3-4-5 circle points.
Reference comparison: Current bottom nodes are flattened and unequal; diagonal bonds meet circles unevenly. Use three equal circular nodes and exact shared bond endpoints.
Construction reference: Lucide circle: equal circular nodes.
SOLO48 keyshape SQUARE; uniform 4-unit strokes; explicit coherent symbol ownership.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='14a03156-aefb-4868-8884-03d2980af425'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__molecule/20260928T172849Z-thuan-mac/reference/molecule_14a03156-aefb-4868-8884-03d2980af425.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='molecule'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('molecule',)

    def build(self):

        # Typed path helpers own continuous contours, repeated radii and real junctions.
        def path(name,start,commands,closed=False):
            here=start;members=[]
            for i,c in enumerate(commands):
                kind,end,*args=c; ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A':
                    rx,ry,sweep=args
                    self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif kind=='C':
                    c1,c2=args
                    self.add_bezier(ident,here,(c1,c2,end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        for n,x,y in [('top',24,11),('left',11,37),('right',37,37)]:
            path(n,(x-3,y+4),[('A',(x-5,y),5,5,True),('A',(x,y-5),5,5,True),('A',(x+5,y),5,5,True),('A',(x+3,y+4),5,5,True),('A',(x-3,y+4),5,5,True)],True)
        line('left-bond',(21,15),(14,33));line('right-bond',(27,15),(34,33));line('base-bond',(16,37),(32,37))
        join('top','left-bond');join('top','right-bond');join('left','left-bond');join('right','right-bond');join('left','base-bond');join('right','base-bond')
