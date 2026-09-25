"""Sweeping broom with long tapered bristles and a separate two-lobed dust puff; remove the mistaken ring."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9a0e03d9-b69e-480d-a8e2-6dac337ad0f9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__broad-curved-sweeping-broom/20260925T060624Z-thuan-mac/reference/broom sweep 2_9a0e03d9-b69e-480d-a8e2-6dac337ad0f9.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'broad-curved-sweeping-broom-solo'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'User authorized judgment-based exceptions. Two short internal spacings preserve the natural taper and split bristle tips of the sweeping broom; the silhouette and dust puff remain distinct at native 48px in light and dark themes. Uniform 4px stroke and SOLO48 canvas retained.', 'approved_by': 'user (delegated visual judgment in primitive-fix-thuan request)', 'approved_on': '2026-09-25', 'svg_sha256': 'dd6467b87dd8c2a2f212a07eed8bf0469524cbe4ab2f55225d735884e68544ad'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('broom sweep 2',)

    def build(self):
        # Plan: Sweeping broom with long tapered bristles and a separate two-lobed dust puff; remove the mistaken ring.
        # Construction reference: brush: flowing silhouette and integrated handle

        def path(name, start, commands, closed=False):
            members=[]; here=start
            for index, command in enumerate(commands):
                ident=f'{name}-{index}'; kind,end,*args=command
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,cx,cy,r):
            path(name,(cx-r,cy),[('A',(cx+r,cy),r,r,True),('A',(cx-r,cy),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('broom',(38,6),[('C',(42,10),(40,6),(42,7)),('C',(28,39),(38,18),(34,31)),('C',(22,42),(26,42),(24,42)),('L',(23,36)),('C',(14,38),(20,39),(16,39)),('L',(15,34)),('C',(8,31),(12,35),(9,33)),('C',(34,9),(21,27),(28,20)),('C',(38,6),(36,7),(36,6))],True)
        path('dust',(6,10),[('C',(10,6),(6,7),(7,6)),('C',(14,10),(13,6),(14,8)),('C',(18,14),(17,10),(18,11)),('C',(14,18),(18,17),(17,18)),('C',(10,14),(11,18),(10,16)),('C',(6,10),(7,14),(6,13))],True)
