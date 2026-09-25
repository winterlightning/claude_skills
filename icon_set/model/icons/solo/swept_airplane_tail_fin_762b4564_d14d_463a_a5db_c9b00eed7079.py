"""Airplane Tail Fin.

Plan: Swept tail fin with open lower-left root; rounded rear base. Envelope 4,8–44,40.
Construction reference: plane (local original and atomic-debug inspected).
Simplification: Small lower-left root break retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '762b4564-d14d-463a-a5db-c9b00eed7079'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/plane tail_762b4564-d14d-463a-a5db-c9b00eed7079.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'swept-airplane-tail-fin'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('airplane', 'tail', 'fin')

    def build(self):
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

        def rect(name, left, top, right, bottom, r=2):
            pts=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for j,a in enumerate(pts):
                b=pts[(j+1)%8]; eid=f'{name}-{j}'; members.append(eid)
                if j%2: self.add_arc(eid,a,b,radius_x=r)
                else: self.add_line(eid,a,b)
            self.add_contour(name,*members,closed=True)

        self.add_line('leading',(10,34),(4,8))
        self.add_line('tip',(4,8),(12,8))
        self.add_arc('tip-round',(12,8),(18,12),radius_x=8,radius_y=6)
        self.add_line('sweep',(18,12),(32,30))
        self.add_arc('root-round',(32,30),(38,32),radius_x=8,radius_y=4,sweep=False)
        self.add_line('base-top',(38,32),(40,32))
        self.add_arc('rear',(40,32),(44,36),radius_x=4)
        self.add_line('rear-side',(44,36),(44,40))
        self.add_line('base',(44,40),(6,40))
        self.add_line('root',(10,34),(4,40))
        self.add_contour('fin','leading','tip','tip-round','sweep','root-round','base-top','rear','rear-side','base')
        self.relate('connect','fin','root')
