"""Horizontal Blind with Right Pull.

Plan: HRECT centerlines (4,8)-(44,40); one structural headrail, two evenly spaced slats, a side support and the named pull cord. Left/right versions mirror the complete construction.
Construction references: Lucide blinds: sparse repeated slats and a separate weighted pull.
Reduction: Reduced the slat count to two and the small pull to a circular outline; retained cord orientation.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '8cae4a5a-3789-5381-a527-c8750fce7a6f'
SOURCE_PATH = 'pictographic-primitives/building/blinds horizontal closed_8cae4a5a-3789-5381-a527-c8750fce7a6f.svg'
SOURCE_ICON_IDS = ('8cae4a5a-3789-5381-a527-c8750fce7a6f',)
SOURCE_PATHS = ('pictographic-primitives/building/blinds horizontal closed_8cae4a5a-3789-5381-a527-c8750fce7a6f.svg',)
AUTHOR = 'gpt-6'


class HorizontalBlindWithRightPull(Solo48):
    icon_id = 'horizontal-blind-with-right-pull'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    aliases = ()
    keywords = ('horizontal', 'blind', 'with', 'right', 'pull')

    def build(self) -> None:
        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,command in enumerate(commands):
                k=f"{name}-{i}"
                kind,end,*args=command
                if kind=="L": self.add_line(k,here,end)
                elif kind=="A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=="C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[("A",(x,y+r),r,r,True),("A",(x,y-r),r,r,True)],True)

        mirror='horizontal-blind-with-right-pull'.endswith("left-pull")
        def pt(x,y):return (48-x,y) if mirror else (x,y)
        # The rail is split at support and cord attachment points.
        self.add_polyline("rail",pt(4,8),pt(44,8),pt(44,16),pt(40,16),pt(8,16),pt(4,16),closed=True)
        self.add_polyline("support",pt(8,16),pt(8,24),pt(8,32))
        self.relate("connect","rail","support")
        for i,y in enumerate((24,32)):
            self.add_polyline(f"slat-{i}",pt(4,y),pt(8,y),pt(30,y))
            self.relate("connect","support",f"slat-{i}")
        self.add_line("cord",pt(40,16),pt(40,34))
        self.relate("connect","rail","cord")
        x,y=pt(40,37)
        circle("pull",x,y,3)
        self.relate("connect","cord","pull")
