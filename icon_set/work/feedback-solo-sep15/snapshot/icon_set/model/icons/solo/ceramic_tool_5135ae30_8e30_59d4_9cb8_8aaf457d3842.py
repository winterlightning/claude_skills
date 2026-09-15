"""ceramic-tool: next hundred AI review; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5135ae30-8e30-59d4-9cb8-8aaf457d3842'
SOURCE_PATH = 'pictographic-primitives/hobbies/ceramic tool_5135ae30-8e30-59d4-9cb8-8aaf457d3842.svg'
AUTHOR = 'gpt-6'

class CeramicTool(Solo48):
    icon_id = 'ceramic-tool'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hobbies'
    aliases = ()
    keywords = ('ceramic', 'tool', 'hobbies', 'solo-ai-next100')

    def build(self):
        # Plan: A narrow-necked vase with a broad rounded belly and narrower foot. Mirrored tangents keep both shoulders smooth; foot width preserves the variant.
        # Reference: Lucide amphora original and atomic-debug construction.

        # Typed path helpers preserve each continuous stroke and its round joins.
        def path(name, start, commands, closed=False):
            members = []
            here = start
            for index, command in enumerate(commands):
                ident = f"{name}-{index}"
                kind, end, *args = command
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
        path('vase',(16,4),[('L',(32,4)),('C',(40,22),(30,10),(40,14)),('C',(35,44),(40,31),(35,35)),('L',(13,44)),('C',(8,22),(13,35),(8,31)),('C',(16,4),(8,14),(18,10))],True)
