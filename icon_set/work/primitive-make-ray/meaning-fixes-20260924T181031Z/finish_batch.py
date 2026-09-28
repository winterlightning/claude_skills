from pathlib import Path
import json, subprocess, sys
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
ROOT=Path(__file__).resolve().parents[4]
BATCH=Path(__file__).parent
STAMP='20260924T181031Z'
blocked={
 'bowling-pins-row': 'Cannot fit the required three continuous pin silhouettes in HRECT_L: 40 centerline units minus two 8-unit inter-pin gaps leaves 8 units per pin. A legal 8-unit neck leaves no room for a wider belly. The retained attempt fails MIC on the 4-unit necks and the hole/internal-spacing gate; touching head/body loops were not reused.',
 'diagonal-handshake': 'Cannot preserve the requested two thumbs and four separate rounded diagonal fingers within SOLO48 spacing. Even the reduced two-seam attempt has only 7.071 centerline units between finger-1/finger-2 and finger-2/outer palm, below 8; rounded lower fingers also exceed the keyshape. Adding the specified fingers would worsen this; further deletion loses the requested clasp anatomy.',
 'hands-gripping-wrists': 'Cannot preserve four recognizable gripping hands in the 36x36 centerline envelope: adjacent palm/wrist contours remain 2.828 units apart and parallel wrist edges only 6, below MIC 8. Reducing the hands to bars produces a mechanical pinwheel instead of a hand lock. No clearance exemptions were added.',
 'hand-holding-stopwatch': 'Cannot retain the named stopwatch and the specified thumb plus four rounded fingers at 48px. The rebuilt hand has four finger lobes, but crease-28 lies only 0.246 units from the stopwatch and the dial hand is only 3 units from its case, below MIC 8. Removing the watch yields a different concept; the failed full attempt is retained.'
}
visual={
 'afghan-hound-head': 'Long asymmetric flowing coat and elongated muzzle, one eye; no smile. Native light/dark reviewed.',
 'asymmetric-branched-snowflake': 'Six arms now have clear forks; balanced crystalline reading in both themes.',
 'branched-cold-snowflake': 'Six fully branched arms retain a conventional snowflake silhouette in both themes.',
 'batch-01-laptop-computers': 'Distinct screen hinge and flared base read as an open laptop at 48px.',
 'borobudur-stupas': 'One dominant spired stupa and two smaller domes on a joined platform; side spires omitted for spacing.',
 'boxer': 'Raised padded gloves and cuff shapes replace the headset-like portrait; circular head has exactly 4px ink gap to torso.',
 'boxer-avatar': 'Raised padded gloves and cuff shapes replace the headset-like portrait; circular head has exactly 4px ink gap to torso.',
 'bunny-holding-easter-egg': 'Long rounded ears, one profile eye, an egg and an attached supporting paw; simplified rabbit silhouette.',
 'cartoon-cat-face': 'Pointed ears, rounded cheeks, paired eyes and a small nose retain a cat reading.',
 'cloud-display-globe': 'Cloud remains distinct inside the globe and a separate pedestal restores the display-object reading.',
 'contactless-card-payment-dollar': 'Two radiating arcs and a horizontal payment card show contactless payment; dollar and hand deliberately omitted.',
 'crested-penguin': 'Side profile replaces the insect-like frontal candidate: upright body, bird beak, swept crest, flipper and foot.',
 'handcuffs-with-arched-connector': 'Large cuff openings, squared lock housings and arched connector distinguish handcuffs from headphones.',
 'owl-wearing-mortarboard': 'Large open circular eyes and pointed beak retain the owl face; body omitted to avoid the graduating-person reading.',
 'person-holding-smartphone': 'Upright phone and supporting bent arm remain distinct; head-to-torso ink gap is exactly 4px.',
 'stacked-hands': 'Rounded thumb and palm under a diagonally overlapping hand replace the abstract angular knot.'
}

def main():
    paths=sorted(BATCH.parent.glob('*/'+STAMP+'-meaning-*/candidate.json'),key=lambda p:json.loads(p.read_text())['icon_id'])
    assert len(paths)==20
    entries=[]
    for candidate in paths:
        r=json.loads(candidate.read_text());icon_id=r['icon_id'];run=candidate.parent
        claim_dir=ROOT/'icon_set/work/primitive-fix-thuan'/('solo__'+icon_id)/(STAMP+'-thuan-mac')
        claim=json.loads((claim_dir/'claim.json').read_text())
        r['reviewer_feedback']=claim['item'].get('feedback','')
        r['visual_review']=visual.get(icon_id,blocked.get(icon_id))
        r['visual_review_sizes']=[48,384];r['visual_review_themes']=['light','dark']
        r['outcome']='cannot-fix' if icon_id in blocked else 'done'
        r['note']=blocked.get(icon_id,visual.get(icon_id))
        r['artifacts'] += [icon_id+'.metadata.json','reference-48.png','reference-384.png','validation.txt']
        if r['outcome']=='done':
            assert r['validation_status']=='valid' and r['build_gate']['status']=='pass' and not r['build_gate']['warnings'],icon_id
        (run/'result.json').write_text(json.dumps(r,indent=2)+'\n')
        if not (claim_dir/'result.json').exists():
            args=[sys.executable,'icon_set/scripts/primitive_fix.py','--worker','thuan-mac','finish',
                  '--icon','solo/'+icon_id,'--run',str(run.relative_to(ROOT)),
                  '--outcome',r['outcome'],'--note',r['note']]
            result=subprocess.run(args,cwd=ROOT,text=True,capture_output=True)
            (run/'finish.log').write_text(result.stdout+result.stderr)
            print(icon_id,result.returncode,result.stdout.strip(),result.stderr.strip(),flush=True)
            if result.returncode:
                entries.append(dict(icon_id=icon_id,reported=False,error=result.stderr));continue
        receipt=json.loads((claim_dir/'result.json').read_text())
        assert receipt['outcome']==r['outcome'] and receipt['finished_at'],icon_id
        entries.append(dict(icon_id=icon_id,reported=True,outcome=receipt['outcome'],review_status=receipt.get('review_status'),run=str(run.relative_to(ROOT))))
    (BATCH/'outcomes.json').write_text(json.dumps(entries,indent=2)+'\n')
    print('CONFIRMED',len([e for e in entries if e['reported']]),'of',len(entries),flush=True)

if __name__=='__main__':main()
