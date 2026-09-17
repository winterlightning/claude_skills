"""Six Tooth Gear — independently authored for batch 49."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fe49e273-5964-4f58-94cd-8a4c93927aa8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_fe49e273-5964-4f58-94cd-8a4c93927aa8.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'six-tooth-gear-fe49e273-5964-4f58-94cd-8a4c93927aa8'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('six', 'tooth', 'gear')

    def build(self):
        # Plan: six flat tooth tips with concave roots, mirrored around x=24.
        # Extremes (6,6)-(42,42). Lucide settings informs the alternating root flow.
        self.add_line('top',(21,6),(27,6))
        segments=[((29,6),(28,14),(32,14)),((35,14),(38,10),(39,11)),
                  ((40,13),(41,15),(42,17)),((42,20),(36,21),(36,24)),
                  ((36,27),(42,28),(42,31)),((41,33),(40,35),(39,37)),
                  ((38,38),(35,34),(32,34)),((28,34),(29,42),(27,42))]
        self.add_bezier('right',(27,6),*segments)
        self.add_line('bottom',(27,42),(21,42))
        nodes=[(27,6)]+[s[2] for s in segments]
        mirror=lambda p:(48-p[0],p[1])
        reverse=[(mirror(s[1]),mirror(s[0]),mirror(nodes[i])) for i,s in reversed(list(enumerate(segments)))]
        self.add_bezier('left',(21,42),*reverse)
        self.add_contour('gear','top','right','bottom','left',closed=True)
        self.add_line('center-mark',(24,23),(24,25))


    def rectangle(self, name, x, y, w, h, attachments=()):
        # Split receiving edges at actual attachment nodes; one joined contour.
        corners=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
        nodes=[]
        for start,end in zip(corners,corners[1:]+corners[:1]):
            dx,dy=end[0]-start[0],end[1]-start[1]
            inside=[p for p in attachments if (p[0]-start[0])*dy == (p[1]-start[1])*dx
                    and 0 < (p[0]-start[0])*dx+(p[1]-start[1])*dy < dx*dx+dy*dy]
            inside.sort(key=lambda p:(p[0]-start[0])*dx+(p[1]-start[1])*dy)
            nodes.extend([start]+inside)
        self.add_polyline(name,*nodes,closed=True)

    def capsule(self, name, x, y, w, h):
        r = h // 2
        self.add_line(name+'-top', (x+r,y), (x+w-r,y))
        self.add_arc(name+'-right', (x+w-r,y), (x+w-r,y+h), radius_x=r)
        self.add_line(name+'-bottom', (x+w-r,y+h), (x+r,y+h))
        self.add_arc(name+'-left', (x+r,y+h), (x+r,y), radius_x=r)
        self.add_contour(name, *[name+s for s in ('-top','-right','-bottom','-left')], closed=True)

