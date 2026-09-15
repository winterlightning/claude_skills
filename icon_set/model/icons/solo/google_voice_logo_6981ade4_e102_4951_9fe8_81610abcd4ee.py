"""google-voice-logo: Smooth phone and voice wedge; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6981ade4-e102-4951-9fe8-81610abcd4ee'
SOURCE_PATH = 'icons-json/logos/google voice logo_6981ade4-e102-4951-9fe8-81610abcd4ee.json'
AUTHOR = 'gpt-6'

class GoogleVoiceLogo(Solo48):
    icon_id = 'google-voice-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('solo-ai-full-set', 'google-voice-logo')

    def build(self):
        # Plan: Preserve the telephone handset and upper-right quarter-disc. Use coherent handset curves and one true quarter circle.
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
        path('handset',(13,6),[('L',(19,14)),('L',(16,21)),('C',(27,32),(18,26),(22,30)),('L',(33,29)),('L',(42,36)),('C',(31,42),(39,40),(36,42)),('C',(6,17),(20,42),(6,28)),('C',(13,6),(6,11),(9,7))],True)
        path('voice',(28,6),[('A',(42,20),14,14,True),('L',(28,20)),('L',(28,6))],True)
