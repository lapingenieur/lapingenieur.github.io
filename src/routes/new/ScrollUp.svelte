<script lang="ts">
  // ScrollUp-lp06b v1.0 - made by lapingenieur
  // a dynamic button for scrolling stsrait up

  function scrollUp() {
    visible = "shown";
    window.scrollTo({
      left: window.scrollX,
      top: 0,
      behavior: "smooth"
    });
  }

  // set the offsets, in px units
  export let topOffset = 60;      // hide the button at the top
  export let bottomOffset = 120;  // show the button at the bottom
  export let scrollOffset = 200;  // how much you need to scroll before reevaluating the button's state

  let visible = ""; // adds a class to the button ("shown" or "semi", and an empty string means hidden)
  let scrollY: number;

  let hashChanged = false;
  let lastChange = 0;

  function handleScroll() {
    // show or hide scrollup button wether scrolled up or down or at the top of the page
    setTimeout(() => {
        if (hashChanged && scrollY > topOffset) {
          // we just jumped and changed the hash AND we are not at the top
          visible = "semi";

        } else {
          // get the height of the footer
          const footer = document.getElementsByClassName("footer").item(0);
          let footerHeight;
          if (footer !== null) {
            footerHeight = footer.clientHeight;
          } else {
            footerHeight = 0;
          }

            console.log(document.documentElement.scrollHeight - document.documentElement.clientHeight, scrollY)
          if (scrollY <= topOffset) {
            // at the top
            visible = "";
            lastChange = scrollY;
          } else if (window.innerHeight + Math.round(scrollY) + 2 >= document.body.offsetHeight) {
            // at the very very bottom of the page (only for small screens)
            visible = "verybottom";
            lastChange = scrollY;
          } else if (document.body.offsetHeight - window.innerHeight - Math.round(scrollY) - footerHeight <= bottomOffset) {
            // at the bottom
            visible = "shown";
            lastChange = scrollY;
          } else if (lastChange - scrollY - scrollOffset > 0) {
            // scrolled up for a while
            visible = "shown";
            lastChange = scrollY;
          } else if (scrollY - lastChange - topOffset > 0) {
            // scrolled down for a while (only for big enough screens)
            visible = "semi";
            lastChange = scrollY;
          }
        }
      }, 50); // lil' hack so hashchange is correctly set
  }
</script>
<svelte:window
  on:hashchange={() => hashChanged = true}
  on:scroll={handleScroll}
  bind:scrollY={scrollY}
/>

<button on:click={scrollUp} class="{visible}">
  <div class="virtual">
    <svg viewBox="220 220 560 560">
      <path d="M549,780V402l168,168l63-70L500,220L220,500l63,70l168-168v378H549z"/>
    </svg>
  </div>
</button>

<style>
  button {
    --inner-width: 2em;

    position: fixed;
    right: 0;
    width: calc(var(--inner-width) + 3em);
    height: calc(var(--inner-width) + 3em);
    cursor: pointer;

    bottom: calc(-1 * var(--inner-width) - 3em - 10px );
    transition:
      bottom 0.5s ease,
      right 0.5s ease;

    border: none;
    border-top-left-radius: 50%;
    padding: 0;
    background: none;
  }
  button.shown {
    bottom: 0;
  }
  button.semi:hover {
    bottom: 0;
  }
  button.verybottom {
    /* when the screen is small, hide a bit the button at the very bottom */
    bottom: calc(-0.3833 * (var(--inner-width) + 6em));
    right: calc(-0.3833 * (var(--inner-width) + 6em));
  }


  .virtual {
    width: var(--inner-width);
    height: var(--inner-width);
    position: absolute;
    top: 0;
    left: 0;

    padding: 0.9em;
    border-radius: 100%;
    background: white;

    transition: background-color 0.2s;
    box-shadow: 1.5px 1.5px 5px 1px rgba(0,0,0,0.35);
  }
  .virtual:hover {
    background-color: #fffcfc;
  }

  path {
    fill: black;
    transition: fill 0.2s;
  }
  button:hover path {
    fill: black;
  }
  
  @media screen and (min-width: 1200px) {
    button.verybottom {
      /* when the screen is big enough, don't hide the button at the very bottom */
      bottom: 0;
      right: 0;
    }
    button.semi {
      bottom: calc(-0.3833 * (var(--inner-width) + 3em));
    }

    path {
      fill: #909bb4;
    }
    button:hover path {
      fill: #2b2e36;
    }
  }
</style>
