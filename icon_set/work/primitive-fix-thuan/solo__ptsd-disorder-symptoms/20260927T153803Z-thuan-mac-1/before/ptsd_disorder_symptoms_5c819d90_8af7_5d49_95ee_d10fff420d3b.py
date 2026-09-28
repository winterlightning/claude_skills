"""ptsd-disorder-symptoms: Smooth human profile; earlier revisions preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5c819d90-8af7-5d49-95ee-d10fff420d3b'
SOURCE_PATH = 'pictographic-primitives/health/ptsd disorder symptoms_5c819d90-8af7-5d49-95ee-d10fff420d3b.svg'
AUTHOR = 'gpt-6'

class PtsdDisorderSymptoms(Solo48):
    icon_id = 'ptsd-disorder-symptoms'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('solo-ai-full-set', 'ptsd-disorder-symptoms')

    def build(self):
        # Plan: Human reference: icon_set/references/human_ref/user.svg and full_body_ref.png. Preserve the continuous neck and profile, with a circular skull and the identifying inner mark.
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
        path('profile',(15,44),[('L',(15,35)),('C',(8,20),(10,29),(8,26)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,26)),('L',(35,26)),('L',(35,30)),('C',(29,37),(35,35),(33,37)),('L',(29,44))])
        path('crack',(24,4),[('L',(18,14)),('L',(24,21))]);join('crack','profile')
