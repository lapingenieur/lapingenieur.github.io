<script lang="ts">
  export let regions: Array<[string, string]>;

  let scrollY: number;
  let innerWidth: number;
  let innerHeight: number;

  let topBar = true;
  let menuVisible = false;

  let shrunk = false;
  let hashChanged = false;
  let lastChange = 0;
  const offset = 60; // px
  const offsetPlus = 500; // px
  let timeoutBuffer: any;

  function handleScroll(reccursive = false) {
    // display top bar when at the top of the page, otherwise only button
    // in each case the button will open the rod menu

    if (hashChanged) {
      // hashchanged
      shrunk = false;
      hashChanged = false;
    } else if (scrollY <= offset) {
      // at top
      topBar = true;
      //lastChange = 0;
      shrunk = false;
    } else {
      topBar = false;
      // not at top

      if (innerWidth < 450 && scrollY <= offsetPlus) {
        // almost at top
        lastChange = 0;
        shrunk = false;
      } else if (lastChange - scrollY - offset > 0) {
        // scrolled up
        shrunk = false;
        lastChange = scrollY;
      } else if (scrollY - lastChange - offset > 0) {
        // scrolled down, hide on small devices and shrink wide devices
        shrunk = true;
        lastChange = scrollY;
      }
    }
    
    // fixes bugs
    if (innerWidth < 700 && !reccursive) timeoutBuffer = setTimeout(() => handleScroll(true), 500);
  }

  function buttonSommairePushed() {
    menuVisible = false

    if (innerWidth < 450) {
      shrunk = false;
      lastChange = scrollY;
    }
  }

  function buttonPushed() {
    menuVisible = !menuVisible

    if (innerWidth < 450) {
      shrunk = false;
      lastChange = scrollY;
    }
  }

  function handle_hashchange() {
    hashChanged = true;
  }
</script>
<svelte:window
  on:hashchange={handle_hashchange}
  on:scroll={() => handleScroll()}
  bind:scrollY={scrollY}
  bind:innerWidth={innerWidth}
  bind:innerHeight={innerHeight}
/>

<div class="menu-around" class:menuVisible class:topBar class:shrunk>
  <div class="menu">
    <div class="menu-container">
      <div class="the-title">
        <a href="#sommaire" on:click={buttonSommairePushed}>n°500 506</a>
      </div>
      <div class="rod-container">
        <nav class="rod">
          {#each regions as region}
            <a href="#{region[1]}" on:click={buttonPushed}>{region[0]}</a>
          {/each}
        </nav>
      </div>
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
  }

  .the-title {
    z-index: 100;
    height: 3.4em;
    width: 100%;
    margin-bottom: 1em;

    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;

    transition: all var(--menu-transition);
  }
  .the-title a {
    height: 1.36em;
    font-size: 2.5em;
    font-style: italic;
    vertical-align: middle;

    color: black;
    text-decoration: none;

    transition: all var(--menu-transition);
  }
  .menu-around.menuVisible .the-title {
    height: 5em;
    margin: 1.2em 0 0.8em;
  }
  .menu-around.menuVisible .the-title a {
    font-size: 3.5em;
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
    transition: all var(--menu-transition);

    background: linear-gradient(135deg, #e66465 -20%, #9198e5 190%);
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
  }

  .menu-around.menuVisible .menu {
    /* get PI/4 position for the greatest viewport dimension and apply as 1/1 ratio-ed size */
    --size: calc(1.42 * 100vmax);
    width: var(--size);
    height: var(--size);
  }
  @media screen and (max-width: 700px) {
    .menu-around:not(.menuVisible).shrunk .menu {
      top: -4.5em;
    }
    .menu-around:not(.menuVisible).topBar .menu {
      height: 3.4em;
      width: 100vw;
      border-bottom-right-radius: 0;
    }
  }
  @media screen and (min-width: 450px) and (max-width: 1000px) {
    .menu-around .menu {
      border-bottom-right-radius: 0;
    }
    .menu-around:not(.menuVisible) .menu {
      height: 3.4em;
      width: 100vw;
    }
  }
  @media screen and (min-width: 1000px){
    .menu {
      width: 0;
      height: 0;
    }
  }

  .button-container {
    z-index: 102;
    position: relative;
    top: 0;
    left: 0;
    height: 4em;
    width: 4em;

    transition:
      top var(--menu-transition),
      height 0.3s,
      width 0.3s;
  }
  @media screen and (max-width: 700px) {
    .menu-around:not(.menuVisible).shrunk .button-container {
      top: -4.5em;
    }
  }
  @media screen and (min-width: 1000px) {
    .button-container {
      height: 3.4em;
      width: 3.4em;
    }
  }
  @media screen and (min-width: 1200px) {
    .menu-around:not(.shrunk) .button-container,
    .menu-around.menuVisible .button-container {
      height: 5em;
      width: 5em;
    }
  }

  .menu-button {
    padding: 0;

    border: none;
    background: transparent;
    transition: all 0.5s cubic-bezier(.22,.94,.54,1.07);
    cursor: pointer;

    height: 100%;
    width: 100%;
  }
  .menu-around.menuVisible .menu-button {
    border-bottom-right-radius: 0;
  }
  @media screen and (max-width: 450px) {
    .menu-around:not(.menuVisible):not(.topBar) .menu-button {
      border-bottom-right-radius: 100%;
    }
    .menu-around.topBar .menu-button {
      border-bottom-right-radius: 0;
      height: 85%;
      width: 85%;
    }
  }
  @media screen and (min-width: 450px) and (max-width: 1000px) {
    .menu-around:not(.menuVisible) .menu-button {
      border-bottom-right-radius: 0;
      height: 85%;
      width: 85%;
    }
  }
  @media screen and (max-width: 1000px) {
    .menu-around.menuVisible .menu-button {
      height: 85%;
      width: 85%;
    }
  }
  @media screen and (min-width: 1000px) {
    .menu-button {
      border-bottom-right-radius: 0;
    }
  }

  .menu-around svg {
    transition: all 0.5s cubic-bezier(.22,.94,.54,1.07);
    position: absolute;
    top: 43%;
    left: 43%;
    width: 60%;
    height: 60%;
  }
  @media screen and (min-width: 1000px) {
    .menu-around svg {
      top: 50%;
      left: 50%;
    }
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
    height: 100vh;
    width: 100vw;

    display: flex;
    flex-direction: column;
    /* justify-content: center; */
    align-items: center;
  }

  .rod-container {
    box-shadow: 0px -1.8em 20px -1.8em rgba(0,0,0,0.2);
    overflow-y: auto;
    padding: 0 2em 2em;
  }

  nav.rod {
    padding: 2em 2em 2.4em;

    /* display: flex; */
    /* flex-direction: column; */
    /* align-items: center; */
    display: grid;
    grid-template-columns: 1fr;

    box-shadow: 0 0 20px rgba(0,0,0,0.2);

    gap: 2.4em;
  }
  @media screen and (min-width: 900px) {
    .rod-container {
      margin-top: 2em;
    }
    nav.rod {
      grid-template-columns: 1fr 1fr;
    }
  }

  .rod a {
    position: relative;
    padding: 0 1em;

    color: black;
    text-align: center;
    transition: color 0.2s;
    text-decoration: none;
    font-size: 2.5em;
  }
</style>
