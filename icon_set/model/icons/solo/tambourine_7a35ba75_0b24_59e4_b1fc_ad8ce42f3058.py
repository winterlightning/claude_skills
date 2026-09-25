"""Four equal jingle circles form cardinal attachments along an interrupted round frame. Shared radius and quarter-arc rim definition. Extremes (6,6)-(42,42); jingles are integral to the rim."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='7a35ba75-0b24-59e4-b1fc-ad8ce42f3058'
SOURCE_PATH='pictographic-primitives/music/tambourine_7a35ba75-0b24-59e4-b1fc-ad8ce42f3058.svg'
AUTHOR='gpt-6'

class Tambourine(Solo48):
    icon_id='tambourine'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "music"
    aliases=()
    keywords=('tambourine', 'percussion', 'jingles', 'instrument', 'rhythm', 'folk', 'music')

    def build(self):
        for name,cx,cy in (('top',24,10),('right',38,24),('bottom',24,38),('left',10,24)):
            r=4
            points=((cx-r,cy),(cx,cy-r),(cx+r,cy),(cx,cy+r))
            for n in range(4):self.add_arc(f'{name}-{n}',points[n],points[(n+1)%4],radius_x=r)
            self.add_contour(name,*[f'{name}-{n}' for n in range(4)],closed=True)
        for n,(start,end,a,b) in enumerate((((28,10),(38,20),'top','right'),((38,28),(28,38),'right','bottom'),((20,38),(10,28),'bottom','left'),((10,20),(20,10),'left','top'))):
            self.add_arc(f'rim-{n}',start,end,radius_x=10)
            self.relate('connect',f'rim-{n}',a)
            self.relate('connect',f'rim-{n}',b)
