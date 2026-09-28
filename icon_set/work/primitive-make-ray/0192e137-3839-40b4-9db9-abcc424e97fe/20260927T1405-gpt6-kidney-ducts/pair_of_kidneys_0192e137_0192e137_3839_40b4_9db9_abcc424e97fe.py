"""Pair of Kidneys.
Plan: (4,8)-(44,40). Mirrored bean-shaped kidneys, inward notches and two short inward ducts. Long descending duct runs omitted for clearance. Shared side parameter preserves paired anatomy.
References: supplied original source; no useful direct Lucide organ match; supplied kidney contours and ducts.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0192e137-3839-40b4-9db9-abcc424e97fe'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pair-of-kidneys-0192e137/20260927T133654Z-thuan-mac-1/reference/kidney 1_0192e137-3839-40b4-9db9-abcc424e97fe.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pair-of-kidneys-0192e137'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('pair-of-kidneys',)
    keywords = ('pair', 'of', 'kidneys')

    def build(self):
        # Shorter paired bean bodies reserve lower space for two descending
        # ureters. Their mirrored dimensions are shared from one side plan.
        for side in (-1,1):
            def p(x,y): return (24+side*x,y)
            name=f'kidney-{side}'
            self.add_bezier(name+'-upper',p(10,8),
                            (p(16,8),p(20,12),p(20,20)))
            self.add_bezier(name+'-lower',p(20,20),
                            (p(20,28),p(16,32),p(10,32)))
            self.add_bezier(name+'-notch-lower',p(10,32),
                            (p(6,32),p(6,28),p(8,24)))
            self.add_bezier(name+'-notch-upper',p(8,24),
                            (p(5,20),p(8,9),p(10,8)))
            self.add_contour(name,name+'-upper',name+'-lower',
                             name+'-notch-lower',name+'-notch-upper',closed=True)
            self.add_line(f'ureter-{side}',p(10,32),p(4,40))
            self.relate('connect',name,f'ureter-{side}')
