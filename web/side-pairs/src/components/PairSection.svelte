<script>
  // A combination primitive's card on Progression (Review icons): where its side pair stands, and the form to make or
  // change it.
  import '../styles/picker.css';
  import PairPicker from './PairPicker.svelte';
  import {POSITIONS, STATUS, TRACK, forms, notices, pairs, loadPair, openForm, partName, combinedURL} from '../lib/picker.svelte.js';
  let {row} = $props();
  $effect(() => { loadPair(row.uuid); });
  const saved = $derived(pairs.get(row.uuid));
  const form = $derived(forms.get(row.uuid));
</script>

<section class="component-brief side-pair">
  <div class="side-pair-head"><strong>Side pair</strong>
    {#if saved}{@const [label, tone] = STATUS[saved.status] || STATUS.waiting}<span class={'badge ' + tone}>{label}</span>{/if}
  </div>
  {#if saved}
    <p>Main: {partName(saved.row, 'main')} · Sub: {partName(saved.row, 'sub')} · {POSITIONS[saved.row.position] || 'position not set'}</p>
    {#if !form && saved.status === 'generated'}
      <img class="side-pair-result" src={combinedURL(row.uuid, saved.row.generated?.at)} alt={row.concept + ' — combined'} loading="lazy">
    {/if}
  {:else if !form}
    <p class="muted">Not on the Side combination page yet. Pick its main and sub icons to save it.</p>
  {/if}
  {#if form}
    <PairPicker {row} />
  {:else}
    <button type="button" class="brief-edit login-only" onclick={() => openForm(row)}>{saved ? 'Change side pair' : 'Make side pair'}</button>
  {/if}{#if !form && notices.has(row.uuid)}
    <p class="side-pair-message" role="status">{notices.get(row.uuid)}<a href={'primitives.html?view=side&q=' + encodeURIComponent(row.uuid)}>Open it →</a></p>
  {/if}{#if saved || form}<a href={TRACK}>All saved side pairs →</a>{/if}
</section>
