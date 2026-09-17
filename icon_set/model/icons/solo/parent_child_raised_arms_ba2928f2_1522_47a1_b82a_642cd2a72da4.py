"""Parent and Child.
Plan: Two vertically stacked mirrored raised-arm busts; head circles and open shoulders. Extrema (6,6)-(42,42).
Reference: human_ref/full_body_ref.png: separate circular heads and open simplified bodies.
Reduction: Compact stacked busts use child radius 2 and adult radius 3; no facial marks. Rounded raised arms and one-unit torso junctions preserve exact detached-head spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba2928f2-1522-47a1-b82a-642cd2a72da4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/family/parent with kids babies_ba2928f2-1522-47a1-b82a-642cd2a72da4.svg'
AUTHOR = 'gpt-6'

class Batch27Icon(Solo48):
    icon_id = 'parent-child-raised-arms'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/family"
    aliases = ()
    keywords = ('parent', 'and', 'child')

    def build(self):

        for name,y,r,spread in (('child',8,2,12),('adult',30,3,18)):
            self.add_arc(name+'-head-a',(24,y-r),(24,y+r),radius_x=r)
            self.add_arc(name+'-head-b',(24,y+r),(24,y-r),radius_x=r)
            self.add_contour(name+'-head',name+'-head-a',name+'-head-b',closed=True)
            neck=y+r+8
            self.add_line(name+'-torso',(24,neck),(24,neck+1))
            neck += 1
            x=24-spread
            radius=6 if name=='child' else 10
            self.add_line(name+'-left',(x,neck-radius-2),(x,neck-radius))
            self.add_arc(name+'-curve-left',(x,neck-radius),(x+radius,neck),radius_x=radius,sweep=False)
            self.add_line(name+'-base-1',(x+radius,neck),(24,neck))
            self.add_line(name+'-base-2',(24,neck),(26,neck))
            self.add_line(name+'-base-3',(26,neck),(48-x-radius,neck))
            self.add_arc(name+'-curve-right',(48-x-radius,neck),(48-x,neck-radius),radius_x=radius,sweep=False)
            self.add_line(name+'-right',(48-x,neck-radius),(48-x,neck-radius-2))
            self.add_contour(name+'-arms',name+'-left',name+'-curve-left',name+'-base-1',name+'-base-2',name+'-base-3',name+'-curve-right',name+'-right')
            self.relate('connect',name+'-torso',name+'-arms')
            self.mark_human_figure(name,head=name+'-head',torso=name+'-torso',torso_junction='start')
