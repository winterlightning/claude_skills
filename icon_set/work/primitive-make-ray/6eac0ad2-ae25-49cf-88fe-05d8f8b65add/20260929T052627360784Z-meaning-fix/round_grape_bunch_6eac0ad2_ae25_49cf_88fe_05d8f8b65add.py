"""Seven individually readable fruit segments with a smooth central circular opening, occluded rear contours, a curved stem and a canvas-safe outer silhouette.
Reference comparison: The rejected drawing was a scalloped flower with one dot. The source contains seven overlapping round fruits and a curved stem.
Construction references: Lucide grape original and atomic-debug: individual rounded berries; source controls the seven-fruit cluster.
Omissions: Rear fruit outlines are interrupted at real occlusions to avoid a tangle of full circles.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6eac0ad2-ae25-49cf-88fe-05d8f8b65add'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-grape-bunch/20260929T051531Z-thuan-mac/reference/sugar apple_6eac0ad2-ae25-49cf-88fe-05d8f8b65add.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'round-grape-bunch'
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
        # Seven fruit segments. Four cardinal junctions on the central circle keep its inner opening smooth.
        self.circle('center-berry',24,22,6)
        self.path('upper-left',(18,22),('C',(14,10),(6,23),(5,10)),('C',(24,16),(19,10),(22,13)))
        self.path('upper-right',(24,16),('C',(40,14),(26,9),(36,7)),('C',(30,22),(44,21),(38,25)))
        self.path('left-middle',(18,22),('C',(16,37),(8,22),(7,36)),('C',(24,28),(20,38),(24,34)))
        self.path('right-middle',(30,22),('C',(32,37),(38,25),(38,34)),('C',(24,28),(27,39),(22,35)))
        self.path('far-right',(40,21),('C',(36,35),(47,22),(46,32)))
        self.path('bottom',(16,37),('C',(32,37),(14,46),(31,46)))
        self.path('stem',(24,16),('C',(28,4),(23,11),(25,6)))
        for name in ['upper-left','upper-right','left-middle','right-middle','stem']: self.relate('connect','center-berry',name)

Drawing.exception = {'reason': 'Adjacent fruit contours intentionally meet in the cluster. Compact openings and organic bounds retain all seven berries with4px strokes; user authorized native-size visual exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': '734cb2e71f57c076600af5a409b4a32fd5266b48fa517d996da65a30979b3f38'}
