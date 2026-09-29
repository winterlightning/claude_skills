"""Restore horizontal T handle, straight spindle, stepped base and two opposing curved arrows with clear arrowheads.
Reference comparison: The rejected valve replaced the T handle with an oval and omitted its raised mount, while the rotation arrows were disconnected hooks.
Construction references: No useful Lucide valve match; supplied reference controls the T handle and opposing rotation directions.
Omissions: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c273354b-5432-4673-a3f2-ea097c59edd5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rotating-valve-handle/20260929T051531Z-thuan-mac/reference/valve_c273354b-5432-4673-a3f2-ea097c59edd5.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'rotating-valve-handle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def path(self, name, start, *steps, closed=False):
        ids=[]; p=start
        for n,step in enumerate(steps):
            key=f"{name}-{n}"; end=step[1]
            if step[0]=='L': self.add_line(key,p,end)
            elif step[0]=='C': self.add_bezier(key,p,(step[2],step[3],end))
            else: self.add_arc(key,p,end,radius_x=step[2],radius_y=step[3],sweep=step[4],large_arc=step[5] if len(step)>5 else False)
            ids.append(key);p=end
        if closed and p!=start:
            key=f"{name}-close";self.add_line(key,p,start);ids.append(key)
        self.add_contour(name,*ids,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def build(self):
        # Central T handle, straight spindle and broad valve base; arrows curl around both sides.
        self.path('handle',(20,12),('L',(30,12)),('A',(30,18),3,3,True),('L',(20,18)),('A',(20,12),3,3,True),closed=True)
        self.add_line('spindle',(25,18),(25,36))
        self.path('mount',(18,40),('L',(18,37)),('A',(21,34),3,3,True),('L',(29,34)),('A',(32,37),3,3,True),('L',(32,40)))
        self.path('base',(9,44),('L',(9,40)),('L',(41,40)),('L',(41,44)))
        self.path('left-turn',(12,5),('C',(9,31),(0,11),(2,24)))
        self.add_polyline('left-arrow',(4,31),(9,31),(8,26))
        self.path('right-turn',(38,32),('C',(39,6),(49,26),(48,13)))
        self.add_polyline('right-arrow',(44,6),(39,6),(40,11))
        self.relate('connect','handle','spindle');self.relate('connect','mount','spindle');self.relate('connect','base','mount');self.relate('connect','left-turn','left-arrow');self.relate('connect','right-turn','right-arrow')

Drawing.exception = {'reason': 'Compact arrowheads, handle opening and stepped mount need local spacing below MIC. User authorized the full mechanical symbol at48px with4px strokes.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'd20601205e8c7c2b6be678197c3195ae05d65791e80304fcac40ff9bfb12db2f'}
