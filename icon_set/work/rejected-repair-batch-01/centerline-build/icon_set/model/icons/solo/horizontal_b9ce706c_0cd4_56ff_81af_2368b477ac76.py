"""horizontal: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9ce706c-0cd4-56ff-81af-2368b477ac76'
SOURCE_PATH = 'pictographic-primitives/photography/horizontal_b9ce706c-0cd4-56ff-81af-2368b477ac76.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Horizontal(Solo48):
    icon_id = 'horizontal'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('horizontal', 'photography')

    def build(self):
        # Plan: HRECT_L; opposed bowed rails are exact reflections.
        # Reference: Shared parabola construction, as in Panoramic.
        # Plan: HRECT_L (4,8)-(44,40); exact horizontal and vertical symmetry, identical parabolic rails, shared panel nodes.
        # Reference: No close panorama match; shared-axis geometric construction.
        # A shared parabola owns both bowed rails and the panel attachments.
        axis = 24
        panel_x = (14, 34)
        knots = (4, *panel_x, 44)
        for name, reflection in [('top', False), ('bottom', True)]:
            def point(x, y): return (x, 48-y if reflection else y)
            for i, (a, b) in enumerate(zip(knots, knots[1:])):
                ya = 12-(a-axis)**2/100
                yb = 12-(b-axis)**2/100
                step = (b-a)/3
                self.add_bezier(f'{name}-{i}', point(a,round(ya)),
                    (point(a+step,ya-step*(a-axis)/50),
                     point(b-step,yb+step*(b-axis)/50),point(b,round(yb))))
        self.add_line('left',(4,8),(4,40))
        self.add_line('right',(44,8),(44,40))
        # Reverse lower rail and left wall for one coherent perimeter.
        from dataclasses import replace
        from ...primitives import Bezier
        for i,p in enumerate(self.primitives):
            if p.element_id.startswith('bottom'):
                c1,c2,end=p.segments[0]
                self.primitives[i]=Bezier(p.element_id,p.end,p.start,((c2,c1,p.start.as_tuple()),))
            elif p.element_id=='left':self.primitives[i]=replace(p,start=p.end,end=p.start)
        self.add_contour('outline','top-0','top-1','top-2','right','bottom-2','bottom-1','bottom-0','left',closed=True)
