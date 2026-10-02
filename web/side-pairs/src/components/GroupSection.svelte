<script>
  // Pairs that reuse the same main or the same sub icon, folded; their rows are drawn once the group is opened.
  import '../styles/row.css';
  import PairRow from './PairRow.svelte';
  import {dataURL, round, ink} from '../lib/rules.js';
  let {store, group, by, editor, openGroups} = $props();
  let open = $state(openGroups.has(group.key));
  const size = $derived(by === 'main' ? store.sizes().main : store.sizes().sub);
  const item = $derived(group.item);
  const detail = $derived(!item ? `${by === 'main' ? 'Main' : 'Sub'} needed` : item.pending ? `Drawn ${by} · waiting`
    : item.document ? `Shared ${by} · ${round(ink(item, by === 'sub')[0])}×${round(ink(item, by === 'sub')[1])} / ${size}` : `Shared ${by}`);
  function toggle(e) { open = e.currentTarget.open;if (open) openGroups.add(group.key); else openGroups.delete(group.key); }
</script>

<details class="container-group side-group" {open} ontoggle={toggle}>
  <summary class="container-group-heading">
    {#if item}<img src={item.document ? dataURL(item.document) : item.preview_url} alt="" loading="lazy">{/if}
    <span class="container-group-label"><strong>{group.title}</strong><span class="muted">{detail}</span></span>
    <span class="chip">{group.rows.length.toLocaleString()} pair{group.rows.length === 1 ? '' : 's'}</span>
  </summary>
  <div class="side-list container-group-items">
    {#if open}{#each group.rows as row (row.id)}<PairRow {store} {row} {editor} />{/each}{/if}
  </div>
</details>
