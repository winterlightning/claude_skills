from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '593cce8b-28e5-4f6d-bd33-3d5365e5cf90'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__spider/20260927T101636Z-thuan-mac-1/reference/spider_593cce8b-28e5-4f6d-bd33-3d5365e5cf90.svg'
AUTHOR = 'gpt-6'


class Spider(Solo48):
    icon_id = 'spider'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('spider', 'arachnid', 'eight legs', 'bug', 'web', 'halloween', 'tarantula', 'insect')

    def build(self):
        # One tapered body outline gives the spider a small head and broad abdomen.
        right=[
            ((24,6),(28,6),(30,10),(30,14)),
            ((30,14),(30,18),(28,20),(28,22)),
            ((28,22),(32,23),(34,28),(34,32)),
            ((34,32),(34,35),(33,37),(32,38)),
            ((32,38),(30,42),(27,42),(24,42)),
        ]
        segments=[]
        for index,(start,c1,c2,end) in enumerate(right):
            name=f'body-r-{index}'
            self.add_bezier(name,start,(c1,c2,end));segments.append(name)
        for index,(start,c1,c2,end) in enumerate(reversed(right)):
            mirror=lambda p:(48-p[0],p[1])
            name=f'body-l-{index}'
            self.add_bezier(name,mirror(end),(mirror(c2),mirror(c1),mirror(start)))
            segments.append(name)
        self.add_contour('body',*segments,closed=True)
        roots=((30,14),(28,22),(34,32),(32,38))
        tips=((42,6),(42,20),(42,28),(42,42))
        for side in (-1,1):
            orient=lambda p:p if side==1 else (48-p[0],p[1])
            for index,(root,tip) in enumerate(zip(roots,tips)):
                name=f'leg-{side}-{index}'
                self.add_line(name,orient(root),orient(tip))
                self.relate('connect',name,'body')
