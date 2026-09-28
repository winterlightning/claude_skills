"""Fresh manual-fix reconstruction: complete original reference and geometric UI forms."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '187100cd-0bd8-46ed-983a-227a3588d8e9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__flaming-brazier/20260925T090056Z-thuan-mac/reference/greek fire_187100cd-0bd8-46ed-983a-227a3588d8e9.svg'
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
    icon_id = 'flaming-brazier'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'culture'
    exception = {'reason': 'Preserve actual bowl/leg contacts and the visible flame-to-rim gap; frame remains open and legible.', 'approved_by': 'user (delegated visual exception judgment)', 'approved_on': '2026-09-25', 'svg_sha256': '57801acef5d54ca68c6b60ef9264b954d008109cec3d8890d2fcc4b33c563a0b'}
    aliases = ()
    keywords = ()

    def build(self):
        self.add_line('rim',(8,25),(40,25))
        self.add_arc('bowl',(40,25),(8,25),radius_x=16,radius_y=11)
        self.add_contour('basin','rim','bowl',closed=True)
        for s in (-1,1):
            self.add_line(f'leg-{s}',(24+s*11,33),(24+s*14,44))
        self.add_line('brace',(10,44),(38,44))
        self.add_arc('flame-left',(16,19),(20,12),radius_x=10)
        self.add_arc('flame-notch',(20,12),(24,4),radius_x=7,sweep=False)
        self.add_arc('flame-right',(24,4),(32,19),radius_x=20)
        self.add_contour('flame','flame-left','flame-notch','flame-right')
