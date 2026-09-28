"""Standalone SOLO48 revisions; exact per-icon sources live in claimed.json."""
from pathlib import Path
import json,ast
SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/batch-20260924T093003Z-thuan-mac/claimed.json'
AUTHOR = 'gpt-6'
ROOT=Path(__file__).parent
previous=ROOT.parent/'batch-20260924T092136Z-thuan-mac/author.py'
HELPERS=next(ast.literal_eval(n.value) for n in ast.parse(previous.read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='HELPERS' for t in n.targets))
designs={
'diagonal-expand-square-icon-solo-b005-13':('SQUARE','Lucide maximize-2: clear diagonal shaft and open right-angle arrowhead.','Lower corner reduced to a compact rounded corner to preserve spacing.', '''
        # Outer rounded square; separated lower corner and upper-right arrow.
        path('frame',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
        poly('arrow',(25,15),(33,15),(33,23))
        line('shaft',(25,23),(33,15));join('arrow','shaft')
        path('corner',(15,29),[('L',(17,29)),('A',(19,31),2,2,True),('L',(19,33))])
'''),
'diagonal-eyedropper-beside-liquid-drop':('SQUARE','Lucide pipette: rounded bulb, crossbar and tapered nozzle.','Crossbar overhang shortened to keep separate teardrop readable.', '''
        # One angled pipette outline and a separate teardrop at lower right.
        path('pipette',(22,14),[('L',(28,8)),('C',(32,6),(30,6),(31,6)),('C',(38,12),(35,6),(38,9)),('C',(36,16),(38,14),(37,15)),('L',(30,22)),('L',(18,34)),('C',(10,38),(16,36),(12,34)),('L',(6,38)),('L',(6,34)),('C',(10,26),(10,30),(8,28)),('L',(22,14))],True)
        poly('flange',(21,13),(22,14),(30,22),(31,23));join('flange','pipette')
        path('drop',(36,30),[('C',(42,38),(38,33),(42,35)),('A',(36,42),6,4,True),('A',(30,38),6,4,True),('C',(36,30),(30,35),(34,33))],True)
'''),
'diagonal-eyedropper-with-three-graduations':('SQUARE','Lucide pipette: round bulb and coherent tube; evenly repeated graduation ticks.','No graduation removed; tiny nozzle transition simplified.', '''
        # Three repeated ticks use step(6,-6); a broad diagonal tube owns the series.
        path('pipette',(28,12),[('L',(32,8)),('C',(38,6),(34,6),(36,6)),('C',(42,12),(42,6),(42,10)),('C',(38,22),(42,16),(40,20)),('L',(20,40)),('C',(10,42),(18,42),(14,38)),('L',(6,42)),('L',(6,38)),('C',(10,30),(10,34),(8,32)),('L',(16,24)),('L',(22,18)),('L',(28,12))],True)
        poly('flange',(24,8),(28,12),(38,22),(42,26));join('flange','pipette')
        for i in range(3):
            x,y=10+6*i,30-6*i
            line(f'tick-{i}',(x,y),(x+3,y+3));join('pipette',f'tick-{i}')
'''),
'diagonal-lemongrass-stalk':('SQUARE','No useful exact Lucide match; coherent tapering curves and shared leaf junctions.','Fine root hairs and the crowded internal vein omitted; branching leaves retained.', '''
        # Bulb and tapering sheath flow into a fork of three long leaves.
        path('stalk',(10,42),[('C',(6,34),(6,42),(6,38)),('C',(16,24),(6,30),(12,27)),('C',(30,6),(23,17),(27,11)),('L',(27,20)),('L',(40,6)),('L',(32,22)),('L',(42,12)),('C',(20,36),(34,21),(26,29)),('C',(10,42),(17,41),(14,42))],True)
'''),
'diagonal-paperclip-batch-021-13':('SQUARE','Lucide paperclip: one continuous wire with smooth nested return bends.','No identity-bearing features omitted.', '''
        # A single wire, with diagonals separated by shared 12-unit sum offsets.
        path('wire',(42,30),[('L',(34,38)),('C',(24,42),(31,41),(28,42)),('C',(6,28),(14,42),(6,36)),('C',(10,20),(6,25),(8,22)),('L',(22,8)),('C',(30,6),(24,6),(27,6)),('C',(42,18),(37,6),(42,11)),('C',(38,26),(42,21),(40,24)),('L',(28,36)),('C',(20,28),(24,40),(16,32)),('L',(30,18))])
'''),
'diagonal-pen-with-curved-clip':('SQUARE','Lucide pen: rounded cap, long diagonal barrel and separate triangular nib.','Clip simplified to one smoothly attached curved stroke.', '''
        # Barrel edges share the 45-degree axis; clip grows from the cap seam.
        path('pen',(34,6),[('A',(42,14),8,8,True),('C',(38,20),(42,17),(40,18)),('L',(20,38)),('L',(6,42)),('L',(10,28)),('L',(28,10)),('C',(34,6),(30,8),(31,6))],True)
        line('cap-seam',(28,10),(38,20));join('pen','cap-seam')
        line('nib-seam',(10,28),(20,38));join('pen','nib-seam')
        path('clip',(38,20),[('C',(42,30),(42,22),(42,26)),('C',(32,40),(42,33),(36,36))])
        join('clip','pen');join('clip','cap-seam')
'''),
'diagonal-scalpel-with-curved-blade':('SQUARE','Lucide pen informed rounded handle cap and diagonal shoulder construction.','Redundant narrow collar line omitted; curved blade and handle seam retained.', '''
        # One continuous tool contour; curved lower blade meets a broad handle.
        path('tool',(14,26),[('L',(30,10)),('C',(34,6),(32,8),(32,6)),('A',(42,14),8,8,True),('C',(38,22),(42,18),(40,20)),('L',(24,36)),('C',(6,42),(20,40),(12,40)),('L',(14,26))],True)
        line('blade-seam',(14,26),(24,36));join('tool','blade-seam')
'''),
'dinosaur-skull':('SQUARE','Lucide skull: restrained eye socket detail; supplied side-view dinosaur reference owns silhouette.','Nostril and detached neck/shoulder marks omitted to preserve the skull opening.', '''
        # Long snout and a heavy lower jaw; rounded rear cranium, single eye socket.
        path('skull',(30,6),[('A',(42,18),12,12,True),('L',(42,30)),('A',(30,42),12,12,True),('L',(14,42)),('C',(6,34),(10,42),(8,38)),('L',(26,34)),('L',(30,26)),('L',(22,26)),('L',(6,24)),('L',(8,16)),('C',(16,9),(10,12),(13,10)),('L',(26,6)),('L',(30,6))],True)
        circle('eye',30,16,2)
'''),
'dizzy-head-profile':('SQUARE','Shared human_ref/user.svg and full_body_ref.png for simplified human curves; supplied profile retains its own anatomy.','Two minimal orbit marks replace the denser source star series.', '''
        # Left-facing head meets a shallow open orbit; a plus and a round spark sit above.
        path('orbit',(6,14),[('C',(14,20),(6,17),(10,19)),('C',(24,22),(17,21),(20,22)),('C',(34,20),(28,22),(31,21)),('C',(42,14),(38,19),(42,17))])
        path('face',(14,20),[('L',(8,30)),('L',(14,30)),('L',(14,34)),('A',(20,40),6,6,False),('L',(22,40)),('L',(22,42))])
        path('back',(34,20),[('C',(32,36),(38,26),(38,32)),('L',(32,42))])
        join('face','orbit');join('back','orbit')
        poly('spark-h',(14,8),(16,8),(18,8));poly('spark-v',(16,6),(16,8),(16,10));join('spark-h','spark-v')
        circle('spark-circle',32,8,2)
'''),
'dna-artificial-intelligence':('SQUARE','Lucide dna: two continuous S-shaped strands with deliberate crossings.','No rungs added: supplied source has only two strands.', '''
        # The second strand is the exact half-turn of the first; both crossings are shared nodes.
        for i in range(2):
            def p(x,y): return (x,y) if i==0 else (48-x,48-y)
            path('strand-'+str(i),p(32,6),[('C',p(30,16),p(28,8),p(30,12)),('C',p(18,32),p(30,28),p(30,32)),('C',p(6,34),p(14,32),p(10,30))])
        join('strand-0','strand-1')
''')
}
records=json.loads((ROOT/'claimed.json').read_text())
for r in records:
    key,ref,omit,body=designs[r['icon_id']]
    m=Path(r['run'])/(r['icon_id'].replace('-','_')+'_'+r['source_uuid'].replace('-','_')+'.py')
    m.write_text(f'''"""Bad-stroke revision. {ref}
Omissions: {omit}
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {r['source_uuid']!r}
SOURCE_PATH = {r['reference_path']!r}
AUTHOR = {AUTHOR!r}
class Revision(Solo48):
    icon_id = {r['icon_id']!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = {tuple(r['concept'].split())!r}
    def build(self):
'''+HELPERS+body)
    r.update(module=str(m),keyshape=key,construction_reference=ref,omissions=omit)
(ROOT/'claimed.json').write_text(json.dumps(records,indent=2)+'\n')
