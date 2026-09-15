from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '380869ce-057f-4cbf-be51-92de0ec1f4e3'
SOURCE_PATH = 'pictographic-primitives/animals/spider_380869ce-057f-4cbf-be51-92de0ec1f4e3.svg'
AUTHOR = 'gpt-6'


class SpiderOnThread(Solo48):
    icon_id = 'spider-on-thread'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('spider', 'thread', 'web', 'arachnid', 'legs', 'hanging', 'halloween', 'bug')

    def build(self) -> None:
        self.add_arc('body0',(14,26),(24,16),radius_x=10)
        self.add_arc('body1',(24,16),(34,26),radius_x=10)
        self.add_arc('body2',(34,26),(24,36),radius_x=10)
        self.add_arc('body3',(24,36),(14,26),radius_x=10)
        self.add_contour('body','body0','body1','body2','body3',closed=True)
        self.add_line('thread',(24,6),(24,16))
        self.relate('connect','thread','body')
        for side in (-1,1):
         for j,(root,elbow,tip) in enumerate([((24,16),(11,15),(6,18)),((14,26),(8,25),(6,27)),((14,26),(10,34),(6,36)),((24,36),(14,40),(12,42))]):
          def p(v): return (v[0] if side==-1 else 48-v[0],v[1])
          self.add_polyline(f'leg-{side}-{j}',p(root),p(elbow),p(tip))
          self.relate('connect','body',f'leg-{side}-{j}')
         self.relate('connect',f'leg-{side}-1',f'leg-{side}-2')
        self.relate('connect','leg--1-0','leg-1-0')
        self.relate('connect','thread','leg--1-0')
        self.relate('connect','thread','leg-1-0')
        self.relate('connect','leg--1-3','leg-1-3')
