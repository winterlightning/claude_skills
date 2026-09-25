"""Three birds over a stepped telescope and tripod; angled optical barrel and shared tripod joint retain the scene."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '16ec9c7e-624d-4955-83bd-4f0d8fbcba1f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__birdwatching-telescope-beneath-three-birds/20260925T060624Z-thuan-mac/reference/bird watching 2_16ec9c7e-624d-4955-83bd-4f0d8fbcba1f.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'birdwatching-telescope-beneath-three-birds-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('bird watching 2',)

    def build(self):
        # Plan: Three birds over a stepped telescope and tripod; angled optical barrel and shared tripod joint retain the scene.
        # Construction reference: telescope: stepped barrel and shared tripod joint

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

        for n,x,y in [('left',8,8),('middle',22,6),('right',36,6)]:
         poly('bird-'+n,(x-2,y),(x,y+2),(x+2,y))
        poly('objective',(26,20),(38,16),(42,26),(30,30),(26,20))
        poly('barrel',(27,21),(16,23),(19,32),(30,28));join('objective','barrel')
        poly('eyepiece',(16,23),(6,27),(9,36),(19,32));join('eyepiece','barrel')
        line('mount',(30,30),(30,37));join('mount','objective')
        poly('tripod',(20,42),(30,37),(40,42));join('tripod','mount')
        line('center-leg',(30,37),(30,42));join('center-leg','tripod');join('center-leg','mount')
