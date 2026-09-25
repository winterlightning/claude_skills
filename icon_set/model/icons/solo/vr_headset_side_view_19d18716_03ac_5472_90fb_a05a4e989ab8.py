"""Side VR headset with arched head strap and sweeping rear strap. Horizontal envelope; Lucide headset strap construction; deliberate right-facing asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '19d18716-03ac-5472-90fb-a05a4e989ab8'
SOURCE_PATH = 'pictographic-primitives/technology/meta quest_19d18716-03ac-5472-90fb-a05a4e989ab8.svg'
AUTHOR = 'gpt-6'

class VrHeadsetSideView(Solo48):
    icon_id = 'vr-headset-side-view'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('vr', 'headset', 'quest', 'virtual-reality', 'goggles', 'device', 'side')

    def build(self):
        # Plan: Rebuild the visor with shared strap stations and consistent corner radii; widen the rear folded band and preserve the smooth overhead strap.

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
        path('visor',(28,20), [('L',(40,20)),('A',(44,24),4,4,True),('L',(44,36)),('A',(40,40),4,4,True),('L',(28,40)),('A',(24,36),4,4,True),('L',(24,26)),('L',(24,24)),('A',(28,20),4,4,True)],True)
        path('head-strap',(8,26), [('A',(24,26),8,18,True)]);join('head-strap','visor')
        poly('rear-strap',(24,26),(8,26),(4,32),(4,40),(12,36),(24,36));join('rear-strap','visor');join('rear-strap','head-strap')
