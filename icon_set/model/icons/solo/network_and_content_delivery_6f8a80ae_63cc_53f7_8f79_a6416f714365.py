"""network-and-content-delivery: Smooth network cloud; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6f8a80ae-63cc-53f7-8f79-a6416f714365'
SOURCE_PATH = 'icons-json/websites/network and content delivery_6f8a80ae-63cc-53f7-8f79-a6416f714365.json'
AUTHOR = 'gpt-6'

class NetworkAndContentDelivery(Solo48):
    icon_id = 'network-and-content-delivery'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'websites'
    aliases = ()
    keywords = ('solo-ai-full-set', 'network-and-content-delivery')

    def build(self):
        # Plan: Preserve the cloud and three spreading network terminals. The center stem joins the cloud at a real midpoint.
        # Reference: Lucide cloud: original and atomic-debug geometry.

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
        path('cloud',(20,28),[('C',(8,17),(13,28),(8,23)),('C',(20,4),(8,10),(13,4)),('C',(31,12),(26,4),(29,7)),('C',(40,20),(37,10),(40,15)),('C',(32,28),(40,25),(37,28)),('L',(24,28)),('L',(20,28))],True)
        path('stem',(24,28),[('L',(24,30)),('L',(24,35)),('L',(24,44))]);join('stem','cloud');poly('branches',(13,40),(24,30),(35,40));join('branches','stem')
