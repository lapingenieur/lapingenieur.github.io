<script lang="ts">
  export let imgsrc: string|null = null;
  export let imgalt: string|null = null;
  export let title: string|null = null;
  export let minHeight = "6em";
  export let padding = "1em";
  export let rightRatio = "3"; // how much flex-grow to give to plate-right
</script>

<div class="plate" style="--min-height: {minHeight}; --padding: {padding}">
  {#if imgsrc}
    <div class="plate-left">
      <img src={imgsrc} alt={imgalt} />
    </div>
  {/if}

  <div class="plate-right" style="--rightRatio: {rightRatio}">
    <div class="plate-top">
      <img src={imgsrc} alt={imgalt} />
    </div>
    <slot />
  </div>
</div>

<style>
  .plate {
    /*** values below is defined in html part, according to Plate compenent attributes ***/
    /* --min-height: (value) */
    /* --padding: (value) */
    width: calc(100% - 2*var(--padding));
    height: auto;
    min-height: var(--min-height);
    padding: var(--padding);

    background-color: #fcfcfd;
    border-radius: 1.5em;

    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1em;
  }
  .plate-left {
    flex: 1;
    margin: 0.5em;

    display: none;
  }
  .plate-top {
    padding: 0.5em;
    max-width: 18em;
  }
  .plate-right {
    /*** value below is defined in html part, according to Plate compenent attributes ***/
    /* --rightRatio: (value) */
    flex: var(--rightRatio);
    height: 100%;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .plate img {
    width: 100%;
    aspect-ratio: 1 / 1;
  }
  .plate-right :global(h1.title) {
    margin: 0;
    font-weight: lighter;
  }
  .plate-right > :global(p) {
    margin: 0.5em 0 0 0;
    font-size: 1em;
    text-align: center;
    width: 100%;
  }
  
  .plate-right :global(:last-child) {
    margin-bottom: 0;
  }
  .plate-right :global(:first-child) {
    margin-top: 0;
  }

  @media screen and (min-width: 550px) {
    .plate {
      min-height: 8em;
      flex-direction: row;
    }
    .plate-left {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .plate-top {
      display: none;
    }
    .plate-right {
      align-items: flex-start;
    }
    .plate-right > :global(p) {
      text-align: justify;
    }
  }

  @media screen and (min-width: 960px) {
    .plate { min-height: 6em }
  }
</style>
