<script>
  // Side pairs are built from X main icons and Y sub icons; count the icons, the same way the Main icons and Sub
  // icons pages do, with their Icon review states and the combined icons'. Every cell links to where they are.
  import '../styles/summary.css';
  let {store, pairCount} = $props();
  const view = $derived.by(() => {
    store.version;
    const s = store, at72 = s.size === 72, sizes = s.sizes();
    const isText = i => [i.id, ...i.source_ids].some(id => s.statuses[id]?.reason === 'text_number');
    const mains = s.components.mains, subs = s.components.subs, textSubs = subs.filter(isText), iconSubs = subs.filter(i => !isText(i));
    const count = (list, status) => list.filter(i => i.status === status).length;
    // One source icon can have several drawings (alternative redraws or revised versions) and one drawing can serve
    // several sources; a pair uses one. Icon review lists distinct drawings, so these counts match its families.
    const drawings = list => [...new Map(list.flatMap(i => i.drawings).filter(d => d.status !== 'fail' && d.svg_sha256).map(d => [d.key, d])).values()];
    // Review decisions per drawing, the same states as Icon review.
    const reviewState = d => { const r = s.reviews[d.key] || 'ready';return r === 're-generated' ? 'ready' : r === 'disapprove' || r === 'claimed' ? 'pending' : r; };
    const tally = list => { const t = {approve: 0, ready: 0, pending: 0, rejected: 0};for (const d of list) t[reviewState(d)] = (t[reviewState(d)] || 0) + 1;return t; };
    const reviewCells = (list, family) => { const t = tally(list), page = 'index.html?family=' + family;
      return {count: list.length, page, cells: [['Approved', t.approve, 'approve', 'ok'], ['To review', t.ready, 'ready', 'todo'], ['Needs fix', t.pending, 'pending', 'fix'], ['Rejected', t.rejected, 'rejected', 'rej']]}; };
    const mainDrawings = drawings(mains), subDrawings = drawings(subs);
    const groups = [
      {title: at72 ? 'Main icons · 54' : 'Main icons', total: mains.length, page: at72 ? 'index.html?family=main-54' : 'side-mains.html',
       cells: [['Generated', count(mains, 'done'), 'done', 'ok'], ['Needs fix', count(mains, 'failing'), 'failing', 'fix'], ['Not generated', count(mains, 'missing'), 'missing', 'todo']],
       review: reviewCells(mainDrawings, at72 ? 'main-54' : 'side_main')},
      {title: at72 ? 'Sub icons · 36' : 'Sub icons', total: subs.length, page: at72 ? 'index.html?family=sub-36' : 'side-subs.html',
       cells: [['Generated', count(iconSubs, 'done'), 'done', 'ok'], ['Text', textSubs.length, 'text', 'text'], ['Needs fix', count(iconSubs, 'failing'), 'failing', 'fix'], ['Not generated', count(iconSubs, 'missing'), 'missing', 'todo']],
       review: reviewCells(subDrawings, at72 ? 'sub-36' : 'side_sub')}];
    let combined = null;
    if (s.run) {
      // Combined icons: the count links to Experiment (64) or Icon review (72), the review cells to Icon review.
      const state = icon => ({approve: 'approve', 're-generated': 'ready', disapprove: 'pending', claimed: 'pending'})[s.reviews[icon.key]] || s.reviews[icon.key] || 'ready';
      const reviewed = st => s.run.icons.filter(i => state(i) === st).length, review = 'index.html?family=' + sizes.combined;
      combined = {title: 'Combined · ' + sizes.canvas, count: s.run.count, page: at72 ? review : 'experiment.html?type=combination', review,
                  cells: [['Approved', reviewed('approve'), 'approve', 'ok'], ['To review', reviewed('ready'), 'ready', 'todo'], ['Needs fix', reviewed('pending'), 'pending', 'fix']]};
    }
    return {mains, subs, mainDrawings, subDrawings, groups, combined};
  });
  const href = (page, status) => page + (page.includes('?') ? '&' : '?') + 'status=' + status;
</script>

<section class="side-icon-summary">
  <p class="side-icon-total">{pairCount.toLocaleString()} side pairs, made from {view.mains.length.toLocaleString()} main icons ({view.mainDrawings.length.toLocaleString()} drawings) and {view.subs.length.toLocaleString()} sub icons ({view.subDrawings.length.toLocaleString()} drawings). A source with several drawings has alternative redraws or versions; each pair uses one.</p>
  {#each view.groups as group (group.title)}
    <div class="side-icon-group">
      <a class="side-icon-head" href={group.page}><strong>{group.title}</strong><span>{group.total.toLocaleString()} icons →</span></a>
      <div class="side-icon-cells">
        {#each group.cells as [label, value, status, tone] (status)}
          <a class={'side-icon-cell ' + tone} href={href(group.page, status)}><strong>{value.toLocaleString()}</strong><span>{label}</span></a>
        {/each}
      </div>
      <a class="side-icon-subhead" href={group.review.page}><strong>Icon review</strong><span>{group.review.count.toLocaleString()} drawings →</span></a>
      <div class="side-icon-cells">
        {#each group.review.cells as [label, value, status, tone] (status)}
          <a class={'side-icon-cell ' + tone} href={href(group.review.page, status)}><strong>{value.toLocaleString()}</strong><span>{label}</span></a>
        {/each}
      </div>
    </div>
  {/each}
  {#if view.combined}
    <div class="side-icon-group">
      <a class="side-icon-head" href={view.combined.page}><strong>{view.combined.title}</strong><span>{view.combined.count.toLocaleString()} combined icons →</span></a>
      <div class="side-icon-cells">
        {#each view.combined.cells as [label, value, status, tone] (status)}
          <a class={'side-icon-cell ' + tone} href={view.combined.review + '&status=' + status}><strong>{value.toLocaleString()}</strong><span>{label}</span></a>
        {/each}
      </div>
    </div>
  {/if}
</section>
