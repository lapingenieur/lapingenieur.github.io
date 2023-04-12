<script lang="ts">
  export let regions: Array<[string, string]>;

  let scrollY: number;

  let topBar = true;
  let menuVisible = false;

  let shrunk = false;
  let lastChange = 0;
  const offset = 60; // px
  let timeoutBuffer: any;

  function handleScroll(reccursive = false) {
    // display top bar when at the top of the page, otherwise only button
    // in each case the button will open the rod menu

    if (scrollY <= offset) {
      // at top
      topBar = true;
      lastChange = 0;
      shrunk = false;
    } else {
      // not at top
      topBar = false;

      if (lastChange - scrollY - offset > 0) {
        // scrolled up
        shrunk = false;
        lastChange = scrollY;
      } else if (scrollY - lastChange - offset > 0) {
        // scrolled down
        shrunk = true;
        lastChange = scrollY;
      }
    }
    
    // fixes bugs
    if (!reccursive) timeoutBuffer = setTimeout(() => handleScroll(true), 500);
  }

  function buttonPushed() {
    menuVisible = !menuVisible

    shrunk = false;
    lastChange = scrollY;
  }
</script>
<svelte:window
  on:scroll={() => handleScroll()}
  bind:scrollY={scrollY}
/>

<div class="menu-around" class:menuVisible class:topBar class:shrunk>
  <div class="bar-placeholder">
    <div class="the-title">
      <span>n°500 506</span>
    </div>
  </div>

  <div class="menu">
    <div class="menu-container">
      <nav class="rod">
        {#each regions as region}
          <a href="#{region[1]}" on:click={() => menuVisible = false}>{region[0]}</a>
        {/each}
      </nav>
    </div>
  </div>

  <div class="button-container">
    <button on:click={buttonPushed} class="menu-button">
      <svg viewBox="0 0 24 24" class="close">
        <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
      </svg>
      <svg viewBox="0 0 24 24" class="open">
        <path d="M3,6H21V8H3V6M3,11H21V13H3V11M3,16H21V18H3V16Z" />
      </svg>
    </button>
  </div>
</div>

<style>
  .menu-around {
    position: fixed;
    top: 0;
    left: 0;

    --menu-transition-time: 0.6s;
    --menu-transition: var(--menu-transition-time) cubic-bezier(.9,0,.1,1);
    --placeholder-transition-time: 0.47s;
    --placeholder-transition-function: cubic-bezier(.9,0,.1,1);
    --placeholder-transition: var(--placeholder-transition-time) var(--placeholder-transition-function);

    --placeholder-topoffset: -3.6em;
  }

  .bar-placeholder {
    z-index: 100;

    position: absolute;
    top: var(--placeholder-topoffset);
    left: 0;
    height: 3.4em;
    width: 100vw;

    overflow: hidden;
    transition: all var(--placeholder-transition);

    background: linear-gradient(45deg, #e66465, #9198e5 150%);
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
  }
  .menu-around.topBar .bar-placeholder {
    top: 0;
    left: 0;
  }
  
  .the-title {
    z-index: 100;
    position: fixed;
    top: 0;
    left: 0;
    height: 3.4em;
    width: 100%;

    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;

    transition: all var(--menu-transition);
  }
  .the-title span {
    font-size: 2.5em;
    font-style: italic;
  }
  .menu-around:not(.topBar) .the-title {
    top: var(--placeholder-topoffset);
  }

  .menu {
    z-index: 101;

    position: absolute;
    height: 4em;
    width: 4em;
    top: 0;
    left: 0;
    border-bottom-right-radius: 100%;

    overflow: hidden;
    transition:
      top var(--menu-transition),
      height var(--menu-transition),
      width var(--menu-transition);

    background: linear-gradient(135deg, #e66465 -20%, #9198e5 190%);
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
  }
  .menu-around.menuVisible .menu {
    /* get PI/4 position for the greatest viewport dimension and apply as 1/1 ratio-ed size */
    --size: calc(1.42 * 100vmax);
    width: var(--size);
    height: var(--size);
  }
  .menu-around.topBar:not(.menuVisible) .menu {
    height: 0;
    width: 0;
  }
  .menu-around:not(.menuVisible).shrunk .menu {
    top: -4.5em;
  }

  .button-container {
    z-index: 102;
    position: relative;
    top: 0;
    left: 0;
    height: 4em;
    width: 4em;

    transition: top var(--menu-transition);
  }
  .menu-around:not(.menuVisible).shrunk .button-container {
    top: -4.5em;
  }

  .menu-button {
    padding: 0;

    border: none;
    background: transparent;
    border-bottom-right-radius: 100%;
    transition: all 0.5s cubic-bezier(.22,.94,.54,1.07);

    height: 100%;
    width: 100%;
  }
  .menu-around.menuVisible .menu-button {
    border-bottom-right-radius: 0;
  }

  .menu-around.topBar .menu-button {
    border-bottom-right-radius: 0;
    height: 85%;
    width: 85%;
  }

  .menu-around svg {
    transition: all 0.5s cubic-bezier(.22,.94,.54,1.07);
    position: absolute;
    top: 43%;
    left: 43%;
    width: 60%;
    height: 60%;
  }
  .menu-around:not(.menuVisible) .open {
    transform: translate(-50%, -50%) scale(1);
  }
  .menu-around.menuVisible .open {
    transform: translate(-50%, -50%) scale(0);
  }
  .menu-around:not(.menuVisible) .close {
    transform: translate(-50%, -50%) scale(0);
  }
  .menu-around.menuVisible .close {
    transform: translate(-50%, -50%) scale(1);
  }

  .menu .menu-container {
    position: absolute;
    top: 0;
    left: 0;
    height: 100vh;
    width: 100vw;

    display: flex;
    flex-direction: column;
    /* justify-content: center; */
    align-items: center;
  }
  .menu .menu-container::before,
  .menu .menu-container::after {
    content: "";
    margin: auto;
  }

  nav.rod {
    padding: 4em 0;
    width: 100%;

    display: flex;
    flex-direction: column;
    /* using before/after margins here */
    /* justify-content: center; */
    align-items: center;

    overflow-y: auto;

    gap: 2.4em;
  }

  .rod a {
    position: relative;
    text-align: center;
    transition: color 0.2s;

    color: black;
    text-decoration: none;
    font-size: 3em;
  }
</style>
