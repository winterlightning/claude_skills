"""Fresh manual-fix reconstruction: complete original reference and geometric UI forms."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cba37bed-3b52-500d-a313-087354344c54'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__folding-pocket-knife-cba37bed/20260925T090056Z-thuan-mac/reference/folding pocket knife_cba37bed-3b52-500d-a313-087354344c54.svg'
AUTHOR = "gpt-6"

def circle(self,name,x,y,r):
    self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
    self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
    self.add_contour(name,name+'-a',name+'-b',closed=True)

def leaf(self,name,a,b,r):
    self.add_arc(name+'-a',a,b,radius_x=r)
    self.add_arc(name+'-b',b,a,radius_x=r)
    self.add_contour(name,name+'-a',name+'-b',closed=True)

class Revision(Solo48):
    icon_id = 'folding-pocket-knife-cba37bed'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'tools'
    exception = {'reason': 'Preserve reference blade angle and natural blade/handle proportions instead of distorting the silhouette to an envelope.', 'approved_by': 'user (delegated visual exception judgment)', 'approved_on': '2026-09-25', 'svg_sha256': '38ab003011b408322924511c07a5c52275306ff0a8b53e0b6596149924bb3bc7'}
    aliases = ()
    keywords = ()

    def build(self):
        self.add_line('handle-top',(10,33),(27,33))
        self.add_arc('shoulder',(27,33),(35,29),radius_x=10,sweep=False)
        self.add_arc('handle-right',(35,29),(35,43),radius_x=7)
        self.add_line('handle-bottom',(35,43),(10,43))
        self.add_arc('handle-left',(10,43),(10,33),radius_x=5)
        self.add_contour('handle','handle-top','shoulder','handle-right','handle-bottom','handle-left',closed=True)
        self.add_arc('blade-edge',(8,4),(27,33),radius_x=38,sweep=False)
        self.add_line('blade-spine',(35,29),(8,4))
        self.add_contour('blade','blade-spine','blade-edge')
        self.relate('connect','handle','blade')
