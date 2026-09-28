"""equipment-cement-cart: Clear cement wheelbarrow; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fbebeb22-f783-4b7a-80ca-ee1c22adc9bc'
SOURCE_PATH = 'pictographic-primitives/tools/equipment cement cart_fbebeb22-f783-4b7a-80ca-ee1c22adc9bc.svg'
AUTHOR = 'gpt-6'

class EquipmentCementCart(Solo48):
    icon_id = 'equipment-cement-cart'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    categories = ('primitives', 'tools')
    aliases = ()
    keywords = ('solo-ai-full-set', 'equipment-cement-cart')

    def build(self):
        # Plan: Preserve the loaded tray, single wheel and rear leg. A curved shoulder connects the tray to the full round wheel.
        # Reference: Original subject; preserve the distinctive silhouette and proportions.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
                if kind == "L" and tuple(end) == tuple(here):
                    continue
                if kind == "L":
                    self.add_line(ident, here, end)
                elif kind == "A":
                    rx, ry, sweep = args
                    self.add_arc(ident, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == "C":
                    c1, c2 = args
                    self.add_bezier(ident, here, (c1, c2, end))
                members.append(ident)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [("A",(cx+r,cy),r,r,True), ("A",(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name, (x0+r,y0), [
                ("L",(x1-r,y0)), ("A",(x1,y0+r),r,r,True),
                ("L",(x1,y1-r)), ("A",(x1-r,y1),r,r,True),
                ("L",(x0+r,y1)), ("A",(x0,y1-r),r,r,True),
                ("L",(x0,y0+r)), ("A",(x0+r,y0),r,r,True)], True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate("connect",a,b)
        path('tray',(4,18),[('L',(10,18)),('L',(34,18)),('L',(38,18)),('L',(28,28)),('L',(20,28)),('C',(17,35),(18,28),(17,31)),('A',(7,35),5,5,True),('C',(4,18),(7,28),(4,23))],True)
        path('wheel',(7,35),[('A',(17,35),5,5,True)]);join('wheel','tray')
        path('load',(10,18),[('C',(15,13),(9,14),(12,12)),('C',(23,8),(16,9),(19,8)),('C',(30,13),(27,8),(30,10)),('C',(34,18),(34,12),(36,15))]);join('load','tray')
        line('handle',(38,18),(44,10));join('handle','tray');poly('leg',(28,28),(38,38),(38,18));join('leg','tray')
