"""A long rounded handle angles upward-right into a broad hammer head. One side has a curved claw opening, while the opposite side ends in a short angular striking face.
Symbol plan: One coherent claw-hammer silhouette with a circular grip end and parallel diagonal handle sides. Preserve the claw opening and angular striking face; omit grip decoration.
Keyshape: CIRCLE; centerline extremes radius 20 about (24,24).
Construction reference: hammer; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '20af476c-a57f-4ace-b516-465f1fa2eefd'
SOURCE_PATH = 'pictographic-primitives/construction/hammer_20af476c-a57f-4ace-b516-465f1fa2eefd.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'claw-hammer-on-diagonal'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    aliases = ()
    keywords = ('claw', 'hammer', 'on', 'diagonal')

    def build(self):

        def segments(name,*points):
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{j}',a,b)

        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def rect(name,l,t,r,b,q=0):
            if not q:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
                return
            points=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
            ids=[]
            for j,(a,z) in enumerate(zip(points,points[1:])):
                if a==z:continue
                n=f'{name}-{j}'
                if j%2:self.add_arc(n,a,z,radius_x=q)
                else:self.add_line(n,a,z)
                ids.append(n)
            self.add_contour(name,*ids,closed=True)

        self.add_line('handle-left',(9,29),(21,20))
        self.add_arc('claw',(21,20),(16,8),radius_x=5,radius_y=12,sweep=False)
        segments('head',(16,8),(26,8),(34,14),(42,22),(36,30),(31,25))
        self.add_line('handle-right',(31,25),(15,37))
        self.add_arc('grip',(15,37),(9,29),radius_x=5)
        self.add_contour('hammer','handle-left','claw','head-1','head-2','head-3','head-4','head-5','handle-right','grip',closed=True)
