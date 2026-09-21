"""Build the reviewed reuse map and files-only SOLO48 authoring handoff."""
import collections, hashlib, html, json, re, shutil
from pathlib import Path

P = Path(__file__).resolve().parent
ROOT = P.parents[2]
OLD = P.parent / 'container-classification-rest-20260921'
old = json.loads((OLD / 'review.json').read_text())['rows']
mapping = json.loads((P / 'mapping-decisions.json').read_text())
decision = json.loads((P / 'decisions.json').read_text())
drafts = {x['number']: x for x in json.loads((P / 'brief-drafts.json').read_text())}
shortlist = {x['number']: x for x in json.loads((P / 'shortlist.json').read_text())}
copies = {x['number']: x for x in json.loads((P / 'source-copies.json').read_text())}
catalog_path = ROOT / 'icon_set/.local/combined-dist/gallery/icons.json'
catalog = {x['icon_id']: x for x in json.loads(catalog_path.read_text())['icons']}
used = set(json.loads((P / 'registry-ids.json').read_text())) | set(catalog)
canonical = {int(k): v for k, v in mapping['canonical_source'].items()}
names = {45:'Stacked Wavy Paper Documents', 150:'Mountain Photo with Cloud',
         505:'Hand Presenting Identity Card', 506:'Hand Gripping Text Card',
         507:'Hand Gripping Portrait Card', 508:'Hand Gripping Blank Upright Document',
         537:'Blank Presentation Easel', 651:'Document with Extended Fold Seam',
         658:'Upright Frame with Small Inset', 624:'Softly Scalloped Circle',
         640:'Divided Field with Center Circle', 504:'Rounded Horizontal Panel'}
stop = set('a an the with and of in inside icon symbol simple empty blank shape geometric to from on at its has have is as each two three four five six one above below right left upper lower front rear short long large small rounded rectangular circular upright horizontal vertical separate broad narrow central containing contains beneath beside across into through behind within whose joins joined more than'.split())
stop.update('that this their them both each displays display showing shows carries carrying enters extends extending rising descending followed formed arranged sits stands surrounds supports fills connected attached visible divided paired consists appear appears takes near toward around over under along top bottom side edges edge'.split())
def tags_for(concept, description, category):
    words = re.findall(r'[a-z]+', concept.lower() + ' ' + description.lower())
    tags = list(dict.fromkeys(w for w in words if w not in stop and len(w)>2))[:8]
    for word in [category.replace('_',' '), 'outline', 'illustration', 'object', 'interface', 'line art']:
        if len(tags)>=6: break
        if word not in tags: tags.append(word)
    return tags

def previous_description(row):
    chunks=[]
    for component in row['components']:
        s=component['description']
        s=re.sub(r'Intrinsic details to retain with the subject:\s*', '', s)
        s=re.sub(r'(?i)\b(?:Exclude|Omit|Leave|Keep|Complete|Restore|Preserve|Do not)\b[^.]*\.?', '', s)
        chunks.append(' '.join(s.split()).strip())
    return ' '.join(chunks)

plans = {}
manifest = []
refdir = P/'authoring-references'
refdir.mkdir(exist_ok=True)
for row in old:
    n=row['number']; choice=mapping['choices'].get(str(n))
    if not choice or choice['action']=='R' or canonical.get(n,n)!=n: continue
    draft=drafts[n]
    assert draft['visually_checked_320_and_48'] and not draft.get('excluded_centered_container')
    concept=names.get(n,draft['concept'])
    target=choice.get('icon_id')
    repair=bool(target and any(c['icon_id']==target and c['source_linked'] for c in shortlist[n]['candidates']) and catalog[target]['family']=='solo')
    proposed=target if repair else re.sub(r'[^a-z0-9]+','-',concept.lower()).strip('-')
    if not repair and proposed in used:
        assert proposed in catalog and catalog[proposed]['family']!='solo', (n,proposed)
        proposed += '-solo'
    assert repair or proposed not in used, (n,proposed)
    used.add(proposed)
    subject={'concept':concept,'icon_id':proposed,'family':'solo','description':draft['description'],
             'tags':tags_for(concept,draft['description'],row['category'])}
    assert set(subject)=={'concept','icon_id','family','description','tags'}
    original=ROOT/'pictographic-primitives'/row['reference_path']
    dest=refdir/original.name
    if dest.exists(): assert dest.read_bytes()==original.read_bytes()
    else: shutil.copyfile(original,dest)
    assert hashlib.sha256(dest.read_bytes()).hexdigest()==copies[n]['sha256']
    manifest.append({'file':dest.name,**subject})
    plans[n]={'subject':subject,'action':choice['action'],'existing_target':target,
              'operation':'repair_existing' if repair else ('new_solo' if choice['action']=='N' else 'adapt_to_solo'),
              'reference_path':str(original),'source_uuid':row['uuid'],
              'source_copy':str(dest),'source_sha256':copies[n]['sha256'],
              'brief_path':str(P/'solo-briefs/briefs'/f'{original.stem}.md'),
              'source_numbers':[j for j in mapping['choices'] if canonical.get(int(j),int(j))==n]}
(refdir/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(P/'authoring-plans.json').write_text(json.dumps(plans,indent=2)+'\n')

art=P/'existing-artwork'; art.mkdir(exist_ok=True)
rows=[]
for original_row in old:
    row=dict(original_row); n=row['number']; c=mapping['choices'].get(str(n))
    row['rechecked_centering']=True
    if not c:
        assert row['route'] in ('container','side')
        row['centered_review_note']=decision.get('confirmed_container',{}).get(str(n),'Centered content confirmed in the second visual review.' if row['route']=='container' else 'Separate side modifier remains a side combination.')
        rows.append(row); continue
    target=c.get('icon_id'); row['route']='solo'; row['reuse_action']={'R':'reuse_existing_solo','A':'adapt_existing_artwork','C':'convert_existing_container','N':'new_solo_brief'}[c['action']]
    row['previous_name']=row['name']
    row['name']=names.get(n,drafts[n]['concept'] if n in drafts else row['name'])
    row['visual_reason']=decision['solo'].get(str(n),row['visual_reason'])
    row['source_was_solo']=original_row['route']=='solo'
    row['existing_target']=None
    if target:
        entry=catalog[target]; svg=(catalog_path.parent/entry['preview_url']).resolve()
        assert svg.is_file()
        if c['action']=='R': assert entry['family']=='solo' and entry.get('validation',{}).get('status')=='valid',target
        dest=art/(target+'.svg')
        if dest.exists(): assert dest.read_bytes()==svg.read_bytes()
        else: shutil.copyfile(svg,dest)
        row['existing_target']={'icon_id':target,'family':entry['family'],'preview':str(dest),
                                'svg_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
                                'validation':entry.get('validation',{}).get('status'),
                                'transform':c.get('transform') or ('flip-vertical' if n==629 else None)}
    base=canonical.get(n,n)
    row['canonical_source_number']=base
    plan=plans.get(base)
    row['authoring_plan']=plan
    row['brief_link']=plan['brief_path'] if plan else None
    row['new_generation_allowed']=False
    row['main_brief']=None;row['sub_brief']=None;row['sub_position']=None
    row['status']='todo' if c['action']=='N' and n==base else 'skip'
    row['reason']=None if row['status']=='todo' else 'other'
    desc=drafts[n]['description'] if n in drafts else previous_description(row)
    if n==219: desc='A right-facing dog profile sits inside a circular outline, with its neck joined to the lower circle edge.'
    row['components']=[{'name':names.get(n,row['name']),'family':'solo','description':desc}]
    row['notes']=mapping['notes'].get(str(n),'')
    if c['action']=='R':
        row['notes']='Existing solo artwork matches this subject; reuse the mapped target.'
        transform=row['existing_target'].get('transform')
        if transform: row['notes']+=' Display transform: '+transform+'.'
    if plan:
        name=plan['subject']['concept']; details=plan['subject']['description']
        instruction=f"SOLO48 authoring brief: {plan['brief_path']}\nProposed icon_id: {plan['subject']['icon_id']}\nOperation: {plan['operation']}"
        if n!=base: instruction+=f"\nShared target with source {base}; do not create another icon for this duplicate concept. Source-specific appearance remains visible in the review."
    else:
        assert c['action']=='R'
        name=row['name']; details=desc
        instruction=f"Reuse existing SOLO48 icon `{target}`. Do not generate a duplicate."
    row['reference_brief']=(f"# {name} — solo reuse review\n\nSource UUID: {row['uuid']}\n"
        f"Reference path: {ROOT/'pictographic-primitives'/row['reference_path']}\n"
        f"Family: solo (SOLO48)\n\nVisual description: {details}\n\n"
        f"Classification: {row['visual_reason']}\n\n{instruction}\n\n"
        f"Existing artwork: {target or 'No suitable existing whole icon found in the reviewed inventory.'}\n"
        f"Review note: {row['notes']}\n\nNo generation job was queued.\n")
    rows.append(row)

summary={'scope':750,'previous_solo':205,'additional_solo_corrections':len(decision['solo']),
         'classification':dict(collections.Counter(r['route'] for r in rows)),
         'solo_actions':dict(collections.Counter(r['reuse_action'] for r in rows if r['route']=='solo')),
         'original_205_actions':dict(collections.Counter(r['reuse_action'] for r in rows if r.get('source_was_solo'))),
         'distinct_authoring_briefs':len(plans),
         'authoring_operations':dict(collections.Counter(v['operation'] for v in plans.values())),
         'generation_queued':0,'first_100_rechecked_in_this_pass':False}
(P/'review.json').write_text(json.dumps({'summary':summary,'rows':rows},indent=2)+'\n')
(P/'triage.json').write_text(json.dumps([{'number':r['number'],'uuid':r['uuid'],'reference_path':r['reference_path'],'classification':r['route'],'reason':r['visual_reason'],'authoring_brief':r.get('brief_link')} for r in rows],indent=2)+'\n')
print(json.dumps(summary,indent=2))
