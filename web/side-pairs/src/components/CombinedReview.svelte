<script>
  // The combined icon's review in Icon review (POST /api/reviews): its state, Approve (once its main and sub are
  // approved) and Disapprove with a note.
  import {REVIEW_LABELS} from '../lib/rules.js';
  let {store, pair, main, sub} = $props();
  const icon = $derived((store.version, store.item(pair.id)?.icon));
  // Reviews are plain data: read them again with the store's version.
  const status = $derived((store.version, icon ? store.reviews[icon.key] || icon.review || 'ready' : 'ready'));
  const waiting = $derived((store.version, [['main', main], ['sub', sub]].filter(([, item]) => item && store.reviews[item.model_key] !== 'approve').map(([role]) => role)));
  let message = $state(''), busy = $state(false);
  async function send(body) {
    busy = true;message = 'Saving…';
    try {
      const response = await fetch('/api/reviews', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({icon: icon.key, svg_sha256: icon.svg_sha256, ...body})});
      const data = await response.json().catch(() => ({}));if (!response.ok) throw Error(data.error || 'Could not save the review.');
      store.reviews[icon.key] = body.status;message = '';await store.refresh(pair.id);
    } catch (error) { message = error.message; }
    finally { busy = false; }
  }
  function disapprove() { const note = prompt('What needs fixing in the combined icon?');if (note) send({status: 'pending', reason: 'other', feedback: note}); }
</script>

{#if icon}
  <span class="side-review side-combined-review" data-status={status}>
    <span class="side-review-chip"><b>Combined</b> {REVIEW_LABELS[status] || status}</span>
    <button type="button" class="requires-login" data-action="approve" disabled={busy || status === 'approve' || waiting.length > 0}
            title={waiting.length ? 'Approve the ' + waiting.join(' and ') + ' first' : ''} onclick={() => send({status: 'approve'})}>Approve</button>
    <button type="button" class="requires-login" data-action="disapprove" disabled={busy || status === 'pending'} onclick={disapprove}>Disapprove</button>
    <span class="side-editor-message" role="status">{message}</span>
  </span>
{/if}
