"""adobe-cloud-logo: Interlocking cloud — clear spacing; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1a854686-429a-4caa-b2bb-aa9186cfd668'
SOURCE_PATH = 'icons-json/_uncategorized_01/adobe cloud logo_1a854686-429a-4caa-b2bb-aa9186cfd668.json'
AUTHOR = 'gpt-6'

class AdobeCloudLogoVariant2(Solo48):
    icon_id = 'adobe-cloud-logo-v2'
    variant_of = 'adobe-cloud-logo'
    variant_label = 'Interlocking cloud — clear spacing'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('solo-ai-full-set', 'adobe-cloud-logo')

    def build(self):
        # Plan: Opened the inner loop and lifted the outer cloud shoulder; removed a crowded short flourish.
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
        path('outer',(16,40),[('C',(4,26),(9,40),(4,34)),('C',(16,10),(4,16),(9,10)),('C',(24,16),(20,10),(22,13)),('C',(32,8),(25,11),(28,8)),('C',(44,24),(40,8),(44,16)),('C',(32,40),(44,33),(39,40)),('L',(22,40)),('L',(16,40))],True)
        path('inner',(22,40),[('L',(16,31)),('C',(24,22),(12,24),(19,18)),('L',(36,36)),('L',(32,40))]);join('inner','outer')
