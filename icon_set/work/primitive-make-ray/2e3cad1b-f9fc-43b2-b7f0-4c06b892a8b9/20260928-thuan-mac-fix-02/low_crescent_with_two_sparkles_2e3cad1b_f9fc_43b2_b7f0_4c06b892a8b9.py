"""One smooth crescent and two diamond sparkle instances, each symmetric about its own axes. Ink extremes (4,4)-(44,44).
Lucide moon and sparkles: coherent crescent contour and four-point sparkle construction. Intentional upper-right sparkle arrangement follows the original."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2e3cad1b-f9fc-43b2-b7f0-4c06b892a8b9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__low-crescent-with-two-sparkles/20260928T175139Z-thuan-mac/reference/astrology stars_2e3cad1b-f9fc-43b2-b7f0-4c06b892a8b9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'low-crescent-with-two-sparkles'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('low', 'crescent', 'with', 'two', 'sparkles')

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

        curve('outer-a',(17,8),(10,10),(6,19),(6,28))
        curve('outer-b',(6,28),(6,37),(14,42),(23,42))
        curve('outer-c',(23,42),(31,42),(37,37),(39,31))
        curve('inner-a',(39,31),(31,37),(21,33),(16,27))
        curve('inner-b',(16,27),(11,21),(12,14),(17,8))
        self.add_contour('crescent','outer-a','outer-b','outer-c','inner-a','inner-b',closed=True)
        for name,x,y,r in [('large',36,12,6),('small',25,21,4)]:
            self.add_polyline(name,(x,y-r),(x+r,y),(x,y+r),(x-r,y),closed=True)
