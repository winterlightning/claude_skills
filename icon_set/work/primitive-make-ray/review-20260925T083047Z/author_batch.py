"""Fresh standalone SOLO48 revisions for the explicitly claimed batch."""
import json,re,sys,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
import cairosvg
HERE=Path(__file__).parent
AUTHOR='gpt-6'
SOURCE_ICON_ID=None  # Per-input identities are retained in each generated module.
SOURCE_PATH=str(HERE/'batch.json')
HELPERS=runpy.run_path(str(HERE.parent/'review-20260925T070522Z/author_batch.py'))['HELPERS']
HELPERS=HELPERS.replace('sweep=a[2])','sweep=a[2], large_arc=a[3] if len(a)>3 else False)')

DESIGNS=[
('VRECT_L','An upright twisted ribbon shaped like a figure eight. Restore the narrow vertical sweep and smooth upper/lower lobes instead of a broad diagonal slash.','Source-specific ribbon; no useful exact Lucide match.',[],'''
        path('ribbon',(28,4),[('C',(38,13),(35,4),(38,8)),('C',(31,26),(38,17),(34,22)),('L',(18,44)),('C',(10,30),(8,44),(7,36)),('L',(14,24)),('L',(28,4))],True)
        path('upper-lobe',(28,4),[('C',(8,14),(17,1),(8,6)),('C',(14,24),(8,18),(10,22))]);join('upper-lobe','ribbon')
        path('lower-lobe',(31,26),[('C',(33,37),(36,29),(36,34)),('C',(18,44),(30,43),(24,45))]);join('lower-lobe','ribbon')
'''),
('HRECT_L','A graphics card with a round fan, right-hand detail and four connector pins. Replace chamfers with consistent corner arcs and enlarge the fan opening.','Lucide cpu original and atomic-debug: rounded board and regularly spaced pins.',[],'''
        rect('board',4,8,44,34,4)
        circle('fan',16,21,5)
        line('detail',(29,25),(36,25))
        for i,x in enumerate(range(12,37,8)):
            line(f'pin-{i}',(x,34),(x,40));join(f'pin-{i}','board')
'''),
('VRECT_L','An ear of corn rises behind two overlapping husks. Restore the tall rounded cob and smooth asymmetric overlap while sharing leaf attachment nodes.','Source-specific corn silhouette; no useful exact Lucide match.',[],'''
        path('cob',(16,27),[('L',(16,12)),('A',(24,4),8,8,True),('A',(32,12),8,8,True),('L',(32,27))])
        path('husks',(24,44),[('C',(8,23),(12,44),(10,38)),('C',(16,27),(11,23),(14,25)),('C',(24,34),(20,29),(23,32)),('C',(32,27),(26,31),(29,29)),('C',(40,23),(35,25),(38,23)),('C',(24,44),(37,32),(40,44))],True);join('cob','husks')
        path('overlap',(24,34),[('C',(24,44),(23,37),(23,41))]);join('overlap','husks')
'''),
('SQUARE','A left-facing human head profile with forehead, nose, chin and short neck. Restore the source profile without the extra cough rays.','Shared human_ref/user.svg informs a round cranium; no detached head or torso, so head/body clearance is inapplicable. Source owns profile anatomy.', ['Two cough rays absent from the source were removed.'],'''
        # Continuous head and neck silhouette; no detached human components.
        path('head',(36,42),[('L',(36,35)),('C',(42,22),(36,31),(42,30)),('A',(26,6),16,16,False),('A',(10,22),16,16,False),('L',(6,28)),('L',(12,28)),('L',(12,32)),('A',(18,38),6,6,False),('L',(22,38)),('L',(22,42))])
'''),
('CIRCLE','A crescent moon with an upper tip and a lower-right tip. Restore the diagonal cutout and rounded lunar silhouette rather than a symmetric bracket.','Lucide moon original and atomic-debug: broad circular outer arc and displaced circular cutout.', ['Tiny reference extraction breaks at the tips are closed.'],'''
        path('moon',(24,4),[('A',(40,36),20,20,False,True),('A',(24,4),20,20,True)],True)
'''),
('CIRCLE','A crescent moon with an upper tip and a lower-right tip. Restore the diagonal cutout and rounded lunar silhouette rather than a symmetric bracket.','Lucide moon original and atomic-debug: broad circular outer arc and displaced circular cutout.', ['Tiny reference extraction breaks at the tips are closed.'],'''
        path('moon',(24,4),[('A',(40,36),20,20,False,True),('A',(24,4),20,20,True)],True)
'''),
('VRECT_L','Open scissors with two round finger loops and crossed blade faces. Restore the blade outlines, smooth tips and visible front-over-back overlap.','Lucide scissors original and atomic-debug: circular finger loops and deliberately interrupted back blade.', ['Tiny pivot omitted. Back lower shank reduced to a stroke.'],'''
        for name,x in [('left',14),('right',34)]:circle(name+'-loop',x,38,6)
        path('front-blade',(14,32),[('L',(19,25)),('L',(24,18)),('L',(34,4)),('C',(36,14),(39,8),(39,10)),('L',(28,26)),('L',(20,38))])
        path('back-blade',(24,18),[('L',(14,4)),('C',(12,16),(8,8),(9,12)),('L',(19,25))])
        line('back-shank',(28,26),(34,32))
        join('front-blade','left-loop');join('back-shank','right-loop');join('back-shank','front-blade');join('front-blade','back-blade')
'''),
('VRECT_L','A crowned chess piece with circular finial, collar, tapered stem and rounded base. Restore the missing stem so the crown reads as a chess piece.','Source-specific chess piece; no useful exact Lucide match.',[],'''
        circle('finial',24,7,3)
        path('crown',(16,24),[('L',(10,14)),('C',(14,13),(9,10),(12,11)),('L',(18,16)),('L',(24,10)),('L',(30,16)),('L',(34,13)),('C',(38,14),(36,11),(39,10)),('L',(32,24))]);join('finial','crown')
        rect('collar',14,24,34,30,2);join('crown','collar')
        path('stem-left',(18,30),[('C',(14,38),(18,33),(16,36))]);path('stem-right',(30,30),[('C',(34,38),(30,33),(32,36))]);join('stem-left','collar');join('stem-right','collar')
        path('base',(12,38),[('L',(14,38)),('L',(34,38)),('L',(36,38)),('A',(40,42),4,4,True),('L',(40,44)),('L',(8,44)),('L',(8,42)),('A',(12,38),4,4,True)],True);join('base','stem-left');join('base','stem-right')
'''),
('CIRCLE','A coin bearing a serif capital D. Restore the letter’s projecting serifs and a balanced rounded bowl inside the circular coin.','Source-specific letter and coin; rounded contour construction.',[],'''
        circle('coin',24,24,20)
        poly('top-serif',(16,14),(19,14),(23,14))
        poly('bottom-serif',(16,34),(19,34),(23,34))
        line('stem',(19,14),(19,34));join('stem','top-serif');join('stem','bottom-serif')
        path('bowl',(23,14),[('A',(33,24),10,10,True),('A',(23,34),10,10,True)]);join('bowl','top-serif');join('bowl','bottom-serif')
'''),
('VRECT_L','A crystal ball seated on a two-tier rounded stand. Restore the softly rounded pedestal and hide the ball’s lower arc behind its support.','Source-specific crystal ball; circular orb and repeated pedestal radii.',[],'''
        path('orb',(15,31),[('A',(33,31),15,15,True,True)])
        path('upper-stand',(12,38),[('L',(12,34)),('A',(15,31),3,3,True),('L',(33,31)),('A',(36,34),3,3,True),('L',(36,38))]);join('orb','upper-stand')
        path('base',(11,38),[('L',(12,38)),('L',(36,38)),('L',(37,38)),('A',(37,44),3,3,True),('L',(11,44)),('A',(11,38),3,3,True)],True);join('upper-stand','base')
'''),
('SQUARE','A three-dimensional cube selection marker made from disconnected corner strokes. Restore the three-way upper corners and bottom-center depth edge.','Lucide cuboid original and atomic-debug: shared three-way face junctions.',[],'''
        poly('top',(18,9),(24,6),(30,9))
        for side in (-1,1):
            p=lambda x,y:(24+side*x,y)
            poly(f'upper-{side}',p(18,22),p(18,16),p(12,12))
            line(f'depth-{side}',p(18,16),p(12,20));join(f'upper-{side}',f'depth-{side}')
            poly(f'lower-{side}',p(18,30),p(18,36),p(12,40))
        poly('center',(17,20),(24,24),(31,20));line('center-v',(24,24),(24,30));join('center','center-v')
        poly('bottom',(18,39),(24,42),(30,39));line('bottom-v',(24,36),(24,42));join('bottom','bottom-v')
'''),
('SQUARE','An isometric cube connects to three outlined circular nodes. Restore the hollow nodes and keep the three visible cube faces balanced.','Lucide cuboid original and atomic-debug: shared face junction and coherent cube boundary.',[],'''
        poly('cube',(24,18),(34,24),(34,30),(24,36),(14,30),(14,24),closed=True)
        poly('faces',(14,24),(24,28),(34,24));line('vertical',(24,28),(24,36));join('cube','faces');join('cube','vertical');join('faces','vertical')
        circle('top-node',24,10,4);line('top-link',(24,14),(24,18));join('top-link','top-node');join('top-link','cube')
        for name,x,a in [('left',10,(14,30)),('right',38,(34,30))]:
            circle(name+'-node',x,38,4);line(name+'-link',a,(x,34));join(name+'-node',name+'-link');join(name+'-link','cube')
'''),
('SQUARE','A cupcake with a domed top and uneven dripping icing above a tapered wrapper. Restore multiple rounded drips and retain intentional asymmetry.','Source-specific frosting; no useful exact local Lucide match.',[],'''
        path('frosting',(10,30),[('C',(6,24),(6,30),(6,27)),('C',(14,14),(6,19),(9,15)),('C',(24,6),(16,8),(20,6)),('C',(34,14),(28,6),(32,8)),('C',(42,24),(39,15),(42,19)),('C',(38,32),(42,28),(40,32)),('C',(32,29),(34,34),(32,32)),('C',(26,29),(32,24),(26,24)),('L',(26,32)),('C',(20,32),(26,37),(20,37)),('L',(20,28)),('C',(14,28),(20,24),(14,24)),('C',(10,30),(14,30),(12,30))],True)
        path('wrapper',(10,30),[('L',(13,39)),('C',(17,42),(13,41),(15,42)),('L',(31,42)),('C',(35,39),(33,42),(35,41)),('L',(38,32))]);join('wrapper','frosting')
'''),
('VRECT_L','Euro currency sign with two unequal-length crossbars and smooth open terminals. Restore the short flat ends and the shorter lower crossbar.','Lucide euro original and atomic-debug: coherent curved bowl with unequal parallel bars.',[],'''
        path('curve',(40,4),[('L',(34,4)),('C',(18,20),(24,4),(18,12)),('C',(18,28),(18,23),(18,25)),('C',(34,44),(18,36),(24,44)),('L',(40,44))])
        poly('upper-bar',(8,20),(18,20),(31,20));poly('lower-bar',(8,28),(18,28),(28,28));join('curve','upper-bar');join('curve','lower-bar')
'''),
('HRECT_L','A plough with a bent handle, rounded beam and pointed curved share. Restore the upright handle angle and sweeping blade instead of a flat trapezoid.','Source-specific agricultural implement; no useful exact Lucide match.',[],'''
        path('handle',(4,8),[('L',(10,8)),('C',(16,14),(12,8),(14,11)),('L',(22,22))])
        path('beam',(18,32),[('L',(18,28)),('A',(24,22),6,6,True),('L',(38,22)),('A',(44,28),6,6,True),('L',(28,28)),('A',(24,32),4,4,False)])
        path('share',(10,32),[('L',(18,32)),('L',(24,32)),('C',(32,40),(27,32),(29,37)),('L',(22,40)),('C',(10,32),(17,40),(12,36))],True);join('beam','share')
'''),
('HRECT_L','A left-pointing chili pepper with a full curved belly and thin curling stem. Restore a coherent fruit contour and remove the heavy stem knot.','Source-specific naturally asymmetric pepper; no useful exact Lucide match.',[],'''
        path('pepper',(4,28),[('C',(30,20),(18,31),(24,25)),('C',(40,18),(33,17),(36,16)),('C',(44,24),(43,19),(44,21)),('C',(22,40),(44,32),(32,40)),('C',(4,28),(12,40),(5,34))],True)
        path('stem',(40,18),[('C',(39,8),(45,14),(44,10))]);join('stem','pepper')
'''),
('SQUARE','A curved soybean with a diagonally oriented oval hilum. Restore the softly rounded lower-left contour and slanted open interior oval.','Source-specific kidney silhouette; no useful exact Lucide match.',[],'''
        path('bean',(14,42),[('C',(6,32),(8,42),(6,36)),('C',(15,18),(6,26),(11,23)),('C',(23,7),(18,14),(17,10)),('C',(30,6),(25,6),(28,6)),('C',(42,20),(38,6),(42,13)),('C',(14,42),(42,32),(29,42))],True)
        path('hilum',(18,26),[('C',(25,19),(18,23),(22,19)),('C',(28,25),(28,19),(30,22)),('C',(19,29),(26,29),(21,32)),('C',(18,26),(18,28),(18,27))],True)
'''),
('SQUARE','A rising vector path connects two hollow endpoint nodes and branches rightward. Restore one continuous sweep and a shallow tangent branch.','Source-specific vector editing diagram; Lucide cuboid informs explicit shared branch nodes.',[],'''
        circle('lower',10,38,4);circle('upper',38,10,4)
        path('curve',(10,34),[('C',(18,23),(12,30),(15,26)),('C',(34,10),(24,15),(28,12))]);join('curve','lower');join('curve','upper')
        path('branch',(18,23),[('C',(42,20),(26,20),(34,20))]);join('curve','branch')
'''),
('SQUARE','A rounded coconut drink with a wavy cut band and bent straw. Restore the round shell and repeated small waves instead of one broad S-curve.','Source-specific coconut; Lucide drum supports coherent curved shell construction.',[],'''
        path('shell',(9,19),[('L',(30,19)),('L',(39,19)),('C',(42,28),(41,22),(42,25)),('C',(24,42),(42,36),(34,42)),('C',(6,28),(14,42),(6,36)),('C',(9,19),(6,25),(7,22))],True)
        path('wave',(6,28),[('C',(13,27),(9,28),(10,27)),('C',(20,31),(16,27),(16,31)),('C',(28,27),(24,31),(24,27)),('C',(36,31),(32,27),(32,31)),('C',(42,28),(39,31),(39,28))]);join('wave','shell')
        path('straw',(30,19),[('L',(33,10)),('C',(40,6),(34,7),(37,6)),('L',(42,6))]);join('straw','shell')
'''),
('SQUARE','A cylindrical drum with an elliptical head and downward-pointing triangular lacing. Correct the reversed triangle and restore the curved lower body.','Lucide drum original and atomic-debug: elliptical head, vertical walls and curved bottom.', ['The narrow lower rim band is omitted to keep the bottom opening clear.'],'''
        path('head',(6,12),[('A',(42,12),18,6,True),('A',(6,12),18,6,True)],True)
        path('body',(6,12),[('L',(6,20)),('L',(6,36)),('A',(42,36),18,6,False),('L',(42,20)),('L',(42,12))]);join('head','body')
        path('band',(6,20),[('C',(14,23),(8,22),(11,23)),('C',(24,24),(18,24),(21,24)),('C',(34,23),(27,24),(30,24)),('C',(42,20),(37,23),(40,22))]);join('band','body')
        poly('lacing',(14,23),(24,36),(34,23));join('lacing','band')
'''),
]

def main():
    rows=json.loads((HERE/'batch.json').read_text())
    assert len(rows)==len(DESIGNS)==20
    for i,(row,d) in enumerate(zip(rows,DESIGNS)):
        keyshape,plan,ref,omissions,body=d
        source=Path(row['ref']);uuid=re.search(r'[a-f0-9-]{36}$',source.stem).group();concept=source.stem[:-37]
        out=ROOT/'icon_set/work/primitive-make-ray'/uuid/f'20260925T083047Z-thuan-revision-{i:02}'
        out.mkdir(parents=True,exist_ok=False);ident=row['key'].split('/')[1]
        meta={'concept':concept,'source_uuid':uuid,'reference_path':row['ref'],'icon_id':ident,'author':AUTHOR,'feedback':'Manual fix request'}
        (out/f'{ident}.metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
        module=out/(ident.replace('-','_')+'_'+uuid.replace('-','_')+'.py')
        module.write_text(f'"""{plan}\nConstruction: {ref}\nFresh SOLO48 revision; original preserved.\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID = {uuid!r}\nSOURCE_PATH = {row["ref"]!r}\nAUTHOR = {AUTHOR!r}\n\nclass Drawing(Solo48):\n    icon_id = {ident!r}\n    keyshape = Keyshape.{keyshape}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects"\n    aliases = ()\n    keywords = {tuple(ident.split("-"))!r}\n\n    def build(self):\n'+HELPERS+body)
        row.update(run=str(out.relative_to(ROOT)),module=str(module.relative_to(ROOT)),plan=plan,construction_reference=ref,omissions=omissions,keyshape=keyshape)
        icon=load_icon(module);svg=icon.to_svg();report=icon.validate_icon()
        (out/f'{ident}.svg').write_text(svg);(out/'validation.txt').write_text(report.describe());render_previews(svg,ident,48,out)
        cairosvg.svg2png(url=str(source),write_to=str(out/'reference.png'),output_width=192,output_height=192)
        cairosvg.svg2png(url=str(next((Path(row['fix'])/'before').glob('*.svg'))),write_to=str(out/'before.png'),output_width=192,output_height=192,background_color='#fff')
        print(i,ident,report.status,len(report.errors),len(report.warnings),flush=True)
        (HERE/'batch.json').write_text(json.dumps(rows,indent=2)+'\n')

if __name__=='__main__':main()
