"""Independent icon-solo candidates; never reads prior icon geometry."""
from pathlib import Path
import json
import textwrap

AUTHOR = 'gpt-6'
SOURCE_ICON_ID = None  # Individual source identities are recorded in JOBS.
SOURCE_PATH = 'work/drawn-unpublished-2026-09-21/batch-04/README.md'
ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'work/drawn-unpublished-2026-09-21/batch-04/solo-results'
JOBS = [
('smiling-face-with-star-eyes', '3e7a0a74-079b-41a7-abfe-d06129db8361', '_uncategorized_17/face grin stars', 'CIRCLE', 'people/emotions', '''
    # Plan: concentric face; mirrored five-point eye definition; centered smile.
    # CIRCLE centerline radius 20. Lucide face-slightly-smiling + star.
    self.add_arc('face-top', (4,24), (44,24), radius_x=20)
    self.add_arc('face-bottom', (44,24), (4,24), radius_x=20)
    self.add_contour('face', 'face-top', 'face-bottom', closed=True)
    for i, cx in enumerate((15,33)):
        points = [(0,-6),(2,-2),(6,-2),(3,1),(4,5),(0,3),(-4,5),(-3,1),(-6,-2),(-2,-2)]
        self.add_polyline(f'eye-{i}', *((cx+x,19+y) for x,y in points), closed=True)
    self.add_bezier('smile', (16,31), ((20,36),(28,36),(32,31)))
'''),
('sun-and-cloud-with-rain', '33b4f573-ff3c-49d0-b558-91f25f42f57a', '_uncategorized_11/cloud sun rain', 'SQUARE', 'nature/weather', '''
    # Plan: cloud owns two lobes and an open lower edge; sun behind; rain series.
    # SQUARE extremes (6,6)-(42,42). Lucide cloud-sun-rain's reduced lobes.
    self.add_bezier('cloud-upper', (6,25), ((6,21),(9,19),(12,19)), ((12,11),(19,10),(22,16)))
    self.add_bezier('cloud-shoulder',(22,16),((24,20),(20,26),(28,26)),((30,26),(32,26),(34,28)))
    self.add_bezier('cloud-right', (34,28), ((34,30),(32,32),(30,32)))
    self.add_line('cloud-base', (18,32), (13,32))
    self.add_bezier('cloud-left', (13,32), ((9,32),(6,29),(6,25)))
    self.add_contour('cloud', 'cloud-base','cloud-left','cloud-upper','cloud-shoulder','cloud-right')
    self.add_arc('sun', (22,16), (34,28),radius_x=12)
    self.relate('connect','sun','cloud')
    for name,a,b in [('ray-top',(27,6),(27,7)),('ray-diagonal',(39,9),(41,7)),('ray-right',(42,22),(42,24))]:
        self.add_line(name,a,b)
    for i,x in enumerate((14,24,34)):
        self.add_line(f'rain-{i}',(x,40),(x-1,42))
'''),
('hooded-swaddle-with-crossed-blanket-folds','e0eaa90e-ee21-4ae5-bede-0c17096fa38f','_uncategorized_05/baby newborn','VRECT_L','people/babies','''
    # Plan: hood capsule, circular face opening, and two intersecting blanket seams.
    # VRECT_L extremes (8,4)-(40,44); shared human circular-head vocabulary.
    self.add_arc('hood', (8,20),(40,20),radius_x=16)
    self.add_line('right-upper',(40,20),(40,28))
    self.add_line('right-lower',(40,28),(40,36))
    self.add_arc('foot-right',(40,36),(32,44),radius_x=8)
    self.add_line('foot',(32,44),(16,44))
    self.add_arc('foot-left',(16,44),(8,36),radius_x=8)
    self.add_line('left-lower',(8,36),(8,32))
    self.add_line('left-upper',(8,32),(8,20))
    self.add_contour('blanket','hood','right-upper','right-lower','foot-right','foot','foot-left','left-lower','left-upper',closed=True)
    self.add_arc('face-top',(18,19),(30,19),radius_x=6)
    self.add_arc('face-bottom',(30,19),(18,19),radius_x=6)
    self.add_contour('face','face-top','face-bottom',closed=True)
    self.add_polyline('fold-main',(8,32),(24,34),(40,36))
    self.add_line('fold-upper',(40,28),(24,34))
    self.relate('connect','fold-main','blanket')
    self.relate('connect','fold-upper','blanket')
    self.relate('connect','fold-upper','fold-main')
'''),
('round-headed-baby-in-a-diagonal-wrap','ec8badad-3b98-4a32-bca0-d815508f5700','_uncategorized_05/baby hold hands','VRECT_M','people/babies','''
    # Plan: circular exposed head, shared side junctions, diagonal blanket edge.
    # VRECT_M extremes (10,4)-(38,44). The wrap contacts the head, not a detached bust.
    # Shared human_ref/user.svg circular anatomy; no eyes or fingers at this scale.
    self.add_arc('head-top',(10,18),(38,18),radius_x=14)
    self.add_arc('head-bottom-right',(38,18),(24,32),radius_x=14)
    self.add_arc('head-bottom-left',(24,32),(10,18),radius_x=14)
    self.add_contour('head','head-top','head-bottom-right','head-bottom-left',closed=True)
    self.add_line('wrap-right',(38,18),(38,30))
    self.add_bezier('wrap-bottom-right',(38,30),((38,38),(32,44),(24,44)),((18,44),(14,41),(12,38)))
    self.add_bezier('wrap-bottom-left',(12,38),((10,35),(10,33),(10,30)))
    self.add_line('wrap-left',(10,30),(10,18))
    self.add_contour('wrap','wrap-right','wrap-bottom-right','wrap-bottom-left','wrap-left')
    self.relate('connect','head','wrap')
    self.add_line('fold',(12,38),(24,32))
    self.relate('connect','fold','head')
    self.relate('connect','fold','wrap')
'''),
('three-star-rating-row','cf0d9970-8b38-5723-b109-a3be9696acdb','rating/rating star three','HRECT_M','symbols/ratings','''
    # Plan: three identical upright stars in one centered horizontal series.
    # HRECT_M requested extremes (4,10)-(44,38). A faithful shallow row cannot
    # reach the vertical extremes: retain that keyshape blocker, never stretch stars.
    # Lucide star informs the alternating tips and valleys of each coherent contour.
    for i,cx in enumerate((10,24,38)):
        points=[(0,-7),(2,-2),(6,-2),(3,2),(4,7),(0,4),(-4,7),(-3,2),(-6,-2),(-2,-2)]
        self.add_polyline(f'star-{i}',*((cx+x,24+y) for x,y in points),closed=True)
'''),
('user-centered-shape-diagram','0bed2a31-9297-4a65-99ad-c1ed293776b1','users/user experience design','SQUARE','people/interaction','''
    # Plan: central bust; square above, circle left, triangle right; three orbit arcs.
    # SQUARE extremes (6,6)-(42,42); user.svg anatomy and Lucide shapes.
    self.add_polyline('square',(20,6),(28,6),(28,14),(20,14),closed=True)
    self.add_arc('head-top',(21,24),(27,24),radius_x=3)
    self.add_arc('head-bottom',(27,24),(21,24),radius_x=3)
    self.add_contour('head','head-top','head-bottom',closed=True)
    # Exact 8 centerline / 4 ink head-to-shoulder gap, circular head.
    self.add_arc('shoulder-left',(18,41),(24,35),radius_x=6)
    self.add_arc('shoulder-right',(24,35),(30,41),radius_x=6)
    self.add_contour('shoulders','shoulder-left','shoulder-right')
    self.add_arc('circle-top',(6,30),(14,30),radius_x=4)
    self.add_arc('circle-bottom',(14,30),(6,30),radius_x=4)
    self.add_contour('circle','circle-top','circle-bottom',closed=True)
    self.add_polyline('triangle',(37,26),(42,35),(32,35),closed=True)
    self.add_bezier('orbit-left',(7,21),((7,17),(10,13),(13,12)))
    self.add_bezier('orbit-right',(35,12),((39,15),(41,19),(41,22)))
    self.add_bezier('orbit-bottom',(16,40),((18,41),(21,42),(24,42)),((27,42),(30,41),(32,40)))
'''),
('open-end-wrench-batch-04','8b71e7e7-15cf-4d31-8c76-295ef5576f53','other/flash wrench','SQUARE','objects/tools','''
    # Plan: single closed wrench silhouette on a rising diagonal; no modifier.
    # SQUARE centerline extremes (6,6)-(42,42). Lucide wrench: open jaw + round heel.
    self.add_bezier('head-left',(20,22),((17,12),(23,6),(30,6)))
    for i,(a,b) in enumerate(zip([(30,6),(24,14),(32,22)],[(24,14),(32,22),(42,12)]),1):
        self.add_line(f'jaw-{i}',a,b)
    self.add_bezier('head-right',(42,12),((42,21),(39,28),(28,28)))
    self.add_line('handle-right',(28,28),(14,41))
    self.add_arc('heel',(14,41),(8,33),radius_x=5)
    self.add_line('handle-left',(8,33),(20,22))
    self.add_contour('wrench','head-left',*[f'jaw-{i}' for i in range(1,4)],'head-right','handle-right','heel','handle-left',closed=True)
'''),
('magnifying-glass-batch-04','d2a83b3d-ee41-4915-81af-29e371bfd9b0','other/magnifying glass with plus','SQUARE','objects/tools','''
    # Plan: circle center (21,21), radius15; 3-4-5 node (30,33); radial handle.
    # SQUARE centerline extremes (6,6)-(42,42). Lucide search's single lens and stem.
    self.add_arc('lens-main',(30,33),(6,21),radius_x=15,large_arc=True,sweep=False)
    self.add_arc('lens-return',(6,21),(30,33),radius_x=15,sweep=False)
    self.add_contour('lens','lens-main','lens-return',closed=True)
    self.add_line('handle',(30,33),(42,42))
    self.relate('connect','handle','lens')
'''),
]

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    jobs=[]
    for index,(parent,uuid,source,keyshape,category,body) in enumerate(JOBS,1):
        variant=parent+('-v3' if index<=6 else '-v2')
        path=ROOT/'icon_set/model/icons/solo'/f'{variant.replace("-","_")}_{uuid.replace("-","_")}.py'
        content=f'''"""Independent full icon-solo drawing from the original batch-04 brief."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = {uuid!r}
SOURCE_PATH = {'pictographic-primitives/'+source+'_'+uuid+'.svg'!r}
AUTHOR = {AUTHOR!r}


class IndependentSolo(Solo48):
    icon_id = {variant!r}
    variant_of = {parent!r}
    variant_label = 'Independent icon-solo; original reference only'
    keyshape = Keyshape.{keyshape}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = {category!r}
    aliases = ()
    keywords = {tuple(parent.split('-'))!r}

    def build(self):
'''+textwrap.indent(textwrap.dedent(body).strip()+'\n','        ')
        path.write_text(content)
        jobs.append(dict(index=index,icon_id=variant,source_id=uuid,python=str(path.relative_to(ROOT)),keyshape=keyshape))
    (OUT/'jobs.json').write_text(json.dumps(jobs,indent=2)+'\n')

if __name__=='__main__':
    main()
