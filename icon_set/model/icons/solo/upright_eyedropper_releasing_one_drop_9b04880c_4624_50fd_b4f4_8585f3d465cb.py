"""Dropper with Liquid Drop.
Plan: Upright tool and separate falling drop; narrow axis leaves space for the collar. Centerline extremes (10,4)-(38,44).
Construction: Lucide pipette; shared crossbar and coherent tool outline.
Reduction: Interior reservoir omitted; bulb, collar, nozzle and teardrop retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b04880c-4624-50fd-b4f4-8585f3d465cb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/picker_9b04880c-4624-50fd-b4f4-8585f3d465cb.svg'
AUTHOR = 'gpt-6'
CATALOG_REFERENCE = 'pictographic-primitives/design/picker_9b04880c-4624-50fd-b4f4-8585f3d465cb.svg'

def _run(icon, name, *points):
    for i,(a,b) in enumerate(zip(points,points[1:]),1):
        icon.add_line(f'{name}-{i}',a,b)

def _circle(icon, name, cx, cy, radius):
    a,b=(cx-radius,cy),(cx+radius,cy)
    icon.add_arc(name+'-a',a,b,radius_x=radius)
    icon.add_arc(name+'-b',b,a,radius_x=radius)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)


class Drawing(Solo48):
    icon_id = 'upright-eyedropper-releasing-one-drop'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('dropper', 'with', 'liquid', 'drop')

    def build(self):
        axis=24
        self.add_arc('bulb',(18,10),(30,10),radius_x=6)
        _run(self,'body-right',(30,10),(30,18),(24,24),(18,18),(18,10))
        self.add_contour('body','bulb',*[f'body-right-{i}' for i in range(1,5)],closed=True)
        self.add_line('collar-left',(10,18),(18,18))
        self.add_line('collar-right',(30,18),(38,18))
        for name in ('collar-left','collar-right'):self.relate('connect',name,'body')
        _run(self,'drop-tip',(18,38),(24,32),(30,38))
        self.add_arc('drop-base',(30,38),(18,38),radius_x=6)
        self.add_contour('drop','drop-tip-1','drop-tip-2','drop-base',closed=True)
