from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96fa123b-1a28-4a25-87c0-68e7e675cef7'
SOURCE_PATH = 'icon_set/work/todo-references/settings toggle horizontal_96fa123b-1a28-4a25-87c0-68e7e675cef7.svg'
AUTHOR = 'gpt-6'
# Plan: Rounded settings panel with two horizontal switches, knobs on opposite ends.
# Construction references: toggle-left: capsule and circular knob; shared dimensions for both switches.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'settings-toggle-horizontal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('settings', 'toggle', 'horizontal')

    def build(self):
        self.box('panel',6,6,42,42)
        for n,y,x in [('upper',14,18),('lower',28,30)]:
            self.box(n,14,y,34,y+8,4)
            self.circle(n+'-knob',x,y+4,4)
            self.relate('connect',n,n+'-knob')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)

    def shield(self):
        self.add_bezier('crown-left',(8,12),((15,12),(21,7),(24,4)))
        self.add_bezier('crown-right',(24,4),((27,7),(33,12),(40,12)))
        self.add_line('wall-right',(40,12),(40,23))
        self.add_bezier('base-right',(40,23),((40,33),(33,40),(24,44)))
        self.add_bezier('base-left',(24,44),((15,40),(8,33),(8,23)))
        self.add_line('wall-left',(8,23),(8,12))
        self.add_contour('shield','crown-left','crown-right','wall-right','base-right','base-left','wall-left',closed=True)
