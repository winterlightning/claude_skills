'Suspended succulent planter: independent spacing revision.\n\nOne broad succulent leaf replaces the crowded three-point crown; deeper hanging bowl.\nNative solo family, VRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: sprout: broad leaf silhouettes around a central stem. Local Lucide originals and atomic-debug renders were inspected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5cbfa835-9e2f-4167-8646-e8f8c56bf395'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/hanging plant 2_5cbfa835-9e2f-4167-8646-e8f8c56bf395.svg'
AUTHOR = 'gpt-6'

class SuspendedSucculentPlanter(Solo48):
    icon_id = 'suspended-succulent-planter'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('planter', 'hanging', 'succulent', 'leaves', 'cord', 'bowl', 'plant')

    def build(self):
        # Plan: Raise the suspension shoulders and rebuild the succulent leaf as two coherent curves; preserve the wide elliptical bowl.

        # Each path owns a coherent stroke; control points preserve smooth tangents.
        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L': self.add_line(name, here, end)
                elif k == 'A': self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C': self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)
        def circle(n, x, y, r):
            path(n, (x-r,y), [('A',(x+r,y),r,r,True), ('A',(x-r,y),r,r,True)], True)
        def box(n, l, t, r, b, rad=4):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        poly('suspension',(8,32),(8,16),(24,4),(40,16),(40,32))
        path('pot',(8,32), [('L',(16,32)),('L',(32,32)),('L',(40,32)),('A',(8,32),16,12,True)],True);join('suspension','pot')
        path('leaf',(16,32), [('C',(24,20),(16,26),(20,23)),('C',(32,32),(28,23),(32,26))]);join('leaf','pot')
