"""Fresh primitive-make-ray runs for the six claimed meaning repairs."""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from icon_set.scripts.primitive_fix import load_icon, render_previews
from icon_set.scripts.build_gate import gate

AUTHOR = 'gpt-6'
SOURCE_ICON_ID = 'per-icon in claim.json and generated module'
SOURCE_PATH = 'per-icon staged reference in claim.json'
BATCH = Path(__file__).resolve().parent

COMMON = '''
    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)
'''

DESIGNS = {
'safety-fire-right': dict(keyshape='SQUARE', problem='The rejected arrow sits over two short generic squiggles; it loses the original flowing fire and outlined lower flame.', change='Restore a pointed enclosed lower flame and a rising open flame trail beneath a crisp right arrow; omit the third trail to give the flame opening room.', plan='Directional arrow at top; open and enclosed flame tongues flow upward to the right. Square centerline extremes (6,6)-(42,42). Intentional directional asymmetry. No useful local Lucide flame-trail match.', code='''
        self.add_polyline('arrow', (32,6), (42,16), (32,26))
        self.add_line('shaft', (6,16), (42,16))
        self.relate('connect','arrow','shaft')
        self.add_bezier('upper-flame', (6,26), ((14,26),(17,26),(22,24)))
        self.add_bezier('lower-flame-top', (6,42), ((9,31),(18,37),(25,32)))
        self.add_bezier('lower-flame-bottom', (25,32), ((22,42),(15,42),(6,42)))
        self.add_contour('lower-flame','lower-flame-top','lower-flame-bottom',closed=True)
'''),
'scuba-diver': dict(keyshape='HRECT_L', problem='The rejected diver has a box-shaped tank dominating an angular body, a floating head, and no clear flipper silhouette.', change='Draw a horizontal swimmer with a compact solid back tank, bent leg and flat flipper stroke, forward reaching arm, circular head and a water surface.', plan='Head (39,23), radius 5; neck (27,28) is exactly 13 away, so head/body ink gap is 4. Torso tangent follows (12,-5); first arm direction (5,12) is perpendicular, keeping the neck nearest. Tank is a compact solid rounded cylinder above the back. HRECT_L extremes (4,8)-(44,40).', code='''
        self.add_bezier('surface',(4,8),((10,10),(15,10),(20,8)),((26,10),(32,10),(38,8)),((40,9),(42,10),(44,10)))
        self.circle('head',39,23,5)
        self.add_line('torso',(27,28),(15,33))
        self.add_polyline('leg',(15,33),(8,26),(4,26))
        self.add_polyline('arm',(27,28),(32,40),(44,40))
        self.add_line('tank',(15,21),(23,21))
        self.relate('connect','torso','leg')
        self.relate('connect','torso','arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
'''),
'seated-jet-ski-rider': dict(keyshape='SQUARE', problem='The rejected rider has a tiny head and the bent body merges with the hull into a mound; the seated leg is no longer clear.', change='Enlarge the head, separate the upright rider and reaching arm, show a hanging bent leg, and open the craft silhouette around that leg.', plan='Head (24,10), r4; neck (24,22) gives exact 4 ink gap. Upright upper torso bends into a seated hip; bow faces left. Hull is interrupted behind the hanging leg. Square intended extremes (6,6)-(42,42).', code='''
        self.circle('head',24,10,4)
        self.add_line('torso',(24,22),(24,25))
        self.add_bezier('back',(24,25),((24,27),(30,28),(30,30)))
        self.add_polyline('leg',(30,30),(24,30),(27,37))
        self.add_polyline('arm',(24,22),(19,28),(13,28))
        self.add_bezier('bow',(13,28),((10,28),(6,32),(6,34)),((6,36),(8,37),(10,37)))
        self.add_line('front-hull',(10,37),(18,37))
        self.add_line('seat',(30,30),(36,30))
        self.add_bezier('stern',(36,30),((40,30),(42,33),(42,35)),((40,36),(37,36),(34,36)))
        self.add_bezier('water',(6,44),((12,42),(18,42),(24,44)),((30,42),(36,42),(42,44)))
        for a,b in [('torso','back'),('back','leg'),('torso','arm'),('arm','bow'),('bow','front-hull'),('leg','seat'),('seat','stern')]:
            self.relate('connect',a,b)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
'''),
'seated-meditation-broad-cross': dict(keyshape='SQUARE', problem='The rejected figure has arched wing-like arms and two floating crossed sticks instead of folded seated legs.', change='Replace the crossed sticks with rounded folded knees and overlapping shins, and angle relaxed arms down to the knees.', plan='Head centered (24,11), r5; neck (24,24), exact 4 ink gap. Mirrored arms rest beside the folded lap. Crossed shin owns its diagonal; rear shin stops behind it. Square extremes (6,6)-(42,42).', code='''
        self.circle('head',24,11,5)
        self.add_line('torso',(24,24),(24,32))
        self.add_polyline('left-arm',(24,24),(17,24),(12,32),(6,32))
        self.add_polyline('right-arm',(24,24),(31,24),(36,32),(42,32))
        self.add_bezier('folded-legs',(15,32),((14,32),(13,32),(12,32)),((6,32),(6,35),(6,37)),((6,40),(10,42),(14,42)),((20,42),(28,42),(34,42)),((38,42),(42,40),(42,37)),((42,35),(42,32),(36,32)),((35,32),(34,32),(33,32)))
        self.add_line('front-shin',(15,32),(30,42))
        self.add_line('rear-shin',(33,32),(26,36))
        for a,b in [('torso','left-arm'),('torso','right-arm'),('left-arm','right-arm'),('folded-legs','front-shin'),('folded-legs','rear-shin'),('left-arm','folded-legs'),('right-arm','folded-legs')]:
            self.relate('connect',a,b)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
'''),
'seated-overhead-stretch': dict(keyshape='SQUARE', problem='The rejected raised-arm figure sits above a disconnected X, so the lower half does not clearly read as a seated yoga pose.', change='Restore a rounded folded lap with overlapping shins and rebalance the overhead arms around a larger head and short upright torso.', plan='Head (24,14), r5, neck (24,27), exact 4 ink gap. Arms mirror about x24 and rise above the head. Folded lap uses the same vocabulary as meditation. Square extremes (6,6)-(42,42).', code='''
        self.circle('head',24,14,5)
        self.add_line('torso',(24,27),(24,32))
        self.add_bezier('left-arm',(24,27),((13,27),(6,19),(6,6)))
        self.add_bezier('right-arm',(24,27),((35,27),(42,19),(42,6)))
        self.add_bezier('folded-legs',(15,32),((9,32),(6,35),(6,37)),((6,40),(10,42),(14,42)),((20,42),(28,42),(34,42)),((38,42),(42,40),(42,37)),((42,35),(39,32),(33,32)))
        self.add_line('front-shin',(15,32),(30,42))
        self.add_line('rear-shin',(33,32),(26,36))
        for a,b in [('torso','left-arm'),('torso','right-arm'),('left-arm','right-arm'),('folded-legs','front-shin'),('folded-legs','rear-shin')]:
            self.relate('connect',a,b)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
'''),
'seated-person-with-cane': dict(keyshape='VRECT_L', problem='The rejected figure leans awkwardly, its arm visually merges into the cane hook, and the detached seat is hard to identify as a chair.', change='Make the seated back upright with a horizontal reaching arm, a clear chair seat and leg, bent knee, and a separate upright hooked cane.', plan='Head (14,9), r5; neck (14,22), exact 4 ink gap. Torso, thigh and lower leg form one seated stroke. Cane remains a separate prop. VRECT_L extremes (8,4)-(40,44).', code='''
        self.circle('head',14,9,5)
        self.add_line('torso',(14,22),(14,27))
        self.add_arc('hip',(14,27),(18,31),radius_x=4,sweep=False)
        self.add_line('thigh',(18,31),(24,31))
        self.add_arc('knee',(24,31),(28,35),radius_x=4)
        self.add_line('shin',(28,35),(28,44))
        self.add_contour('body','torso','hip','thigh','knee','shin')
        self.add_line('arm',(14,22),(24,22))
        self.add_polyline('chair',(8,44),(8,40),(18,40))
        self.add_arc('cane-hook',(32,25),(40,25),radius_x=4)
        self.add_line('cane-shaft',(40,25),(40,44))
        self.add_contour('cane','cane-hook','cane-shaft')
        self.relate('connect','body','arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''')
}

def main():
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    selected=set(sys.argv[1:])
    records=json.loads((BATCH/'drafts.json').read_text()) if selected else []
    for claimdir in sorted((ROOT/'icon_set/work/primitive-fix-thuan').glob('*/20260929T084652Z-thuan-mac')):
        claim=json.loads((claimdir/'claim.json').read_text()); item=claim['item']; name=item['icon_id']; design=DESIGNS[name]
        if selected and name not in selected:
            continue
        reference=next((claimdir/'reference').glob('*.svg')); uuid=reference.stem[-36:]; concept=reference.stem[:-37]
        run=ROOT/'icon_set/work/primitive-make-ray'/uuid/(stamp+'-meaning-fix')
        run.mkdir(parents=True)
        meta={'concept':concept,'source_uuid':uuid,'reference_path':str(reference.relative_to(ROOT))}
        (run/(name+'.metadata.json')).write_text(json.dumps(meta,indent=2)+'\n')
        comparison={'current_problem':design['problem'],'feedback':item['feedback'],'revision':design['change'],'original_render':str(claimdir/'original.png'),'rejected_render':str(claimdir/'rejected.png')}
        (run/'comparison.json').write_text(json.dumps(comparison,indent=2)+'\n')
        module=run/(name.replace('-','_')+'_'+uuid.replace('-','_')+'.py')
        source=f'''"""{design['change']}
Construction plan: {design['plan']}
Human construction: icon_set/references/human_ref/full_body_ref.png.
Lucide person-standing original and atomic-debug: articulated limbs and shared torso nodes.
Source comparison: {design['problem']}
Omissions: fine source outline doubling; preserve the complete action and its identifying prop.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uuid!r}
SOURCE_PATH = {meta['reference_path']!r}
AUTHOR = {AUTHOR!r}
class AuthoredIcon(Solo48):
    icon_id = {name!r}
    keyshape = Keyshape.{design['keyshape']}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/activity'
    aliases = ()
    keywords = {tuple(name.split('-'))!r}
{COMMON}
    def build(self):
{design['code']}
'''
        module.write_text(source)
        icon=load_icon(module); report=icon.validate_icon(); svg=icon.to_svg()
        (run/(name+'.svg')).write_text(svg)
        (run/'validation.txt').write_text(report.describe())
        render_previews(svg,name,48,run)
        info={**meta,**comparison,'icon_id':name,'key':item['key'],'author':AUTHOR,'module':str(module.relative_to(ROOT)),'run':str(run.relative_to(ROOT)),'svg':str((run/(name+'.svg')).relative_to(ROOT)),'validation_status':report.status}
        records=[r for r in records if r['icon_id']!=name]+[info]
        print(name,report.describe())
    (BATCH/'drafts.json').write_text(json.dumps(records,indent=2)+'\n')

if __name__=='__main__': main()
