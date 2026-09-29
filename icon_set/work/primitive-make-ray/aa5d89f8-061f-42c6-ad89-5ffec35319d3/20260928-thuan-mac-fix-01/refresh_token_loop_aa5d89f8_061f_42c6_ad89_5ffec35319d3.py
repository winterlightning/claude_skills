"""Two concentric circles centered at (21,21) with radii 15 and 8, open in the lower-right quadrant; token centered (35,35), radius 7. Ink extremes (4,4)-(44,44).
Lucide rotate-cw: continuous circular sweep; source keeps two loops without an arrow. Deliberate open lower-right sector accommodates the separate coin."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'aa5d89f8-061f-42c6-ad89-5ffec35319d3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__refresh-token-loop/20260928T175139Z-thuan-mac/reference/refresh token authentication coin loading_aa5d89f8-061f-42c6-ad89-5ffec35319d3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'refresh-token-loop'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('refresh', 'token', 'loop')

    exception = {'reason': 'User authorized visual exceptions for UI quality. Concentric loops retain a uniform 3px ink gap, and the detached token has approximately 3px clearance. This preserves the original two open loops and a separate round token without a misleading contact. Readable in both themes at 48px; all strokes 4px.', 'approved_by': 'user: delegated visual-exception decision to gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'd76344c482d2a50e6e93d4bff38df85d0a8f6280eb48b2af92e94bd330676cf7'}

    def build(self):

        def curve(name,start,c1,c2,end):
            self.add_bezier(name,start,(c1,c2,end))
        def path(name,start,steps,closed=False):
            point=start
            ids=[]
            for j,(kind,end,*args) in enumerate(steps):
                part=f'{name}-{j}'
                if kind=='L': self.add_line(part,point,end)
                elif kind=='A': self.add_arc(part,point,end,radius_x=args[0],sweep=args[1])
                elif kind=='C': curve(part,point,args[0],args[1],end)
                ids.append(part)
                point=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,True),('A',(x-r,y),r,True)],True)

        for name,r in [('outer',15),('inner',8)]:
            x=y=21
            path(name,(x+r,y),[('A',(x,y-r),r,False),('A',(x-r,y),r,False),('A',(x,y+r),r,False)])
        circle('token',35,35,7)
