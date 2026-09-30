"""Upload only the explicitly selected and visually reviewed batch revisions."""
import json,os,sys,shutil
from pathlib import Path
from icon_set.scripts.primitive_fix import finish,load_icon
from icon_set.scripts import work_queue

AUTHOR='gpt-6'
ROOT=Path(__file__).parent
items=json.loads((ROOT/'items.json').read_text())
CHANGES={
1:'Restored the broad diagonal wing, crossing fuselage, rounded nose and single upright tail from the source.',
2:'Rounded the card corners, wrapping thumb and lower palm, preserving the left-handed grip and text mark.',
3:'Restored the message line and envelope fold; rounded the holding thumb and wrist with clear lower-envelope spacing.',
4:'Rounded the ballot corner and box base while retaining the tilted ballot and curved gripping thumb.',
5:'Curved the lowering hand and extended the horizontal slot across the ballot tip.',
6:'Restored the open lower-left cube edge, lengthened the pointing finger and rounded the wider palm.',
7:'Rounded the identity card and supporting thumb/palm; restored a circular portrait mark and spaced text rule.',
8:'Smoothed the sheltering palm and restored a child hair lock inside the circular head.',
9:'Replaced angular shoulders with a smooth shoulder arc and softened the patting hand around the circular jaw.',
10:'Replaced the bracket-like hand with two rounded descending fingers and preserved the wave above the tub.',
11:'Restored a wider, flatter moustache with flowing mirrored lobes and upturned outer tips.',
12:'Enlarged and rounded the water droplet; separated the two cupped hands and curved their inner palms.',
13:'Restored rounded fingertips and curved wrists around the baby, plus its asymmetric hair curl.',
14:'Enlarged the circular face and deepened the angled book; retained the rounded headphone band and short ends.',
15:'Smoothed the helmet hairline and shoulders and replaced the facial dot with an outlined goatee.',
16:'Restored the missing upward migration arrow between the connected circular network nodes.',
17:'Enlarged and aligned the head, restored the lowered arm, rounded the pole grip and completed the triangular tent.',
}
OMISSIONS={
1:['Wing and tail proportions broadened to keep the required stroke clearance.'],
2:['Two source text rules reduced to one compact mark for interior clearance.'],
3:['Lower envelope edge ends before the hand to preserve clear negative space.'],
4:['Fine finger creases and the separate box rim are omitted at 48px.'],
5:['Fine thumb creases omitted.'],
6:['Small finger creases omitted.'],
7:['Portrait circle is reduced to a compact circular mark; small card text is one rule.'],
8:['Facial details beyond the source hair lock are omitted.'],
9:['Neck and clothing seams are simplified to shared bust construction.'],
10:['Three source fingers reduced to two rounded fingers.'],
11:['Lobe contours broadened to maintain the required openings.'],
12:['Cuffs and fine finger divisions omitted.'],
13:['Secondary thumb outlines omitted to keep room around the baby head.'],
14:['Earcups reduced to rounded band ends; page text omitted.'],
15:['Small eye marks omitted to preserve the identifying goatee and helmet.'],
16:['Three small internal chevrons omitted; the primary upward arrow is preserved.'],
17:['Outlined garment reduced to shared stick-figure anatomy; tent interior omitted.'],
}

for n in map(int,sys.argv[1:]):
    it=items[n-1];p=Path(it.get('latest',it['run']))
    claim=Path(it['claim']).parent
    if (claim/'result.json').exists():
        print(n,'already finished',flush=True);continue
    g=json.loads((p/'gate.json').read_text())
    assert g['status']=='pass' and not g['warnings'] and not g['errors'],(n,g)
    q=next(p.glob('*.py'));icon=load_icon(q);r=icon.validate_icon()
    assert r.status=='valid' and not r.warnings and not r.errors
    for nm in ['original','rejected']:
        src=claim/(nm+'.png')
        if src.exists():shutil.copy(src,p/src.name)
    meta=json.loads((p/(icon.icon_id+'.metadata.json')).read_text())
    meta.update(icon_id=icon.icon_id,author=AUTHOR,validation_status='valid',validation_warnings=[],build_gate_status='pass',
                before_problem=it['review'],feedback='No written feedback or reason supplied.',changes=CHANGES[n],
                visual_review='Inspected enlarged and at native 48px in both light and dark themes. Reference identity, curve flow and negative space reviewed.',
                omissions=OMISSIONS[n],artifacts=sorted(f.name for f in p.iterdir()))
    (p/'result.json').write_text(json.dumps(meta,indent=2)+'\n')
    note='No written feedback. '+CHANGES[n]+' AUTHOR gpt-6; validation and full build gate pass with zero warnings.'
    code=finish(work_queue.default_base_url(),os.environ.get('PICTOGRAPHIC_WORKER') or 'thuan-mac',it['key'],'done',note,ray_run=p)
    print(n,'finish exit',code,flush=True)
    if code:raise SystemExit(code)
