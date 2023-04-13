<script lang="ts">
  import Blockon from "$lib/blockons/Blockon.svelte";
  import Plate from "$lib/blockons/Plate.svelte";
</script>

<Blockon id="webdev">
  <h1>Développement Web</h1>

  <div class="icons">
    <a href="https://svelte.dev">
      <img src="/images/svelte-logo.png" alt="Svelte"/>
    </a>
    <a href="https://www.markdownguide.org/">
      <img src="/images/markdown-logo.webp" alt="Markdown"/>
    </a>
    <a href="https://developer.mozilla.org/fr/docs/Web/HTML">
      <img src="/images/html-logo.png" alt="HTML"/>
    </a>
    <a href="https://developer.mozilla.org/fr/docs/Web/CSS">
      <img src="/images/css-logo.png" alt="CSS"/>
    </a>
    <a href="https://www.sass-lang.com/">
      <img src="/images/sass-logo.png" alt="Sass (SCSS)"/>
    </a>
    <a href="https://typescriptlang.org">
      <img src="/images/typescript-logo.png" alt="Typescript"/>
    </a>
    <a href="https://github.com">
      <svg viewBox="0 0 16 16">
        <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z" />
      </svg>
    </a>
    <a href="https://pocketbase.io">
      <img src="/images/pocketbase-logo.svg" alt="Pocketbase"/>
    </a>
  </div>

  <hr/>
  <p>
    Je manie les technologies modernes nécessaires à la création d'une application web&nbsp;:
  </p>

  <div class="plates">

    <Plate
        imgsrc="/images/framework.png"
        imgalt="Illustration framework"
        rightRatio="3"
        padding="1em"
      >
      <h2 class="title">Framework</h2>
      <p class="desc">
        <a href="https://kit.svelte.dev">SvelteKit</a> est un framework simpliste et intuitif, à rendu côté serveur (SSR).
        Ce site est écrit avec Svelte et son code est exposé
        <a href="https://github.com/lapingenieur/lapingenieur.github.io">ici</a>.
      </p>
    </Plate>

    <Plate
        imgsrc="/images/contenu.png"
        imgalt="Illustration fichier"
        rightRatio="3"
        padding="1em"
      >
      <h2 class="title">Contenu</h2>
      <p class="desc">
        Des outils tels que <a href="https://www.markdownguide.org/">Markdown</a>
        ou <a href="https://www.sass-lang.com/">Sass</a>
        facilitent le maniement et la mise en page des langages
        <a href="https://developer.mozilla.org/fr/docs/Web/HTML">HTML</a> et
        <a href="https://developer.mozilla.org/fr/docs/Web/CSS">CSS</a>.
      </p>
    </Plate>

    <Plate
        imgsrc="/images/logique.png"
        imgalt="Illustration engrenages"
        rightRatio="3"
        padding="1em"
      >
      <h2 class="title">Partie logique</h2>
      <p class="desc">
        La syntaxe <a href="https://typescriptlang.org">Typescript</a>
        assure le typage et avorte de nombreuses erreurs d'incohérence.
      </p>
    </Plate>

    <Plate
        imgsrc="/images/backend.png"
        imgalt="Illustration serveur"
        rightRatio="3"
        padding="1em"
      >
      <h2 class="title">Backend</h2>
      <p class="desc">
        Des librairies diverses permettent aux applications de parfaire leurs tâches,
        comme la base de donnée <a href="https://pocketbase.io">PocketBase</a>.
      </p>
    </Plate>

    <Plate
        imgsrc="/images/git-logo.png"
        imgalt="Logo Git"
        rightRatio="3"
        padding="1em"
      >
      <h2 class="title">Gestion de versions</h2>
      <p class="desc">
        <a href="https://git-scm.com/">Git</a> permet une gestion de versions solide et efficace,
        il peut être couplé à un hébergeur comme <a href="https://github.com">GitHub</a>.
      </p>
    </Plate>

    <Plate
        imgsrc="/images/stackoverflow-logo.png"
        imgalt="Logo Stack Overflow"
        rightRatio="3"
        padding="1em"
      >
      <h2 class="title">Documentation</h2>
      <p class="desc">
        Les documentations, comme <a href="https://developer.mozilla.org">MDN</a>,
        mais aussi les forums, tels que <a href="https://stackoverflow.com/">Stack Overflow</a>,
        sont une source essentielle d'informations.
      </p>
    </Plate>
  </div>

  <p>
    Toutes ces technologies peuvent être utilisées également dans d'autres optiques,
    comme la gestion de l'interface graphique via des interfaces comme
    <a href="https://tauri.app">Tauri</a> en langage <a href="https://rust-lang.org">Rust</a>.
  </p>
</Blockon>

<style>
  :root {
    --webdev-smart-margin: 0px;
  }

  .icons {
    /* height: 3rem; */
    margin: 0 calc(var(--webdev-smart-margin) * 0.5);

    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0.4em;
    /*** below buggy => using before/after auto margins ***/
    /* justify-content: space-around; */
    /* align-items: center; */
    overflow-x: scroll;

    scrollbar-width: none;
    -ms-overflow-style: none;
  }
  .icons::-webkit-scrollbar {
    display: none
  }

  .icons a {
    margin: 0 auto;

    display: flex;
    justify-content: center;
    align-items: center;

    height: 2em;
    padding: 0.5em 0.8em;
    border-radius: 0.5em;
    transition: background-color 300ms;
  }
  .icons a:hover,
  .icons a:focus-visible {
    background-color: #d7dde4;
  }
  .icons img,
  .icons svg {
    height: 75%;
  }

  hr {
    width: calc(85% - var(--webdev-smart-margin));
    border-top: 2px solid black;
  }

  .plates {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1em;
  }

  @media screen and (max-width: 400px) {
    .icons {
      gap: 0.2em;
    }
  }
  @media screen and (min-width: 750px) {
    .icons {
      grid-template-columns: repeat(8, 1fr);
      margin: 0 calc(var(--webdev-smart-margin) * 0.5);
    }
  }

  @media screen and (min-width: 960px) {
    .plates { grid-template-columns: 1fr 1fr; }
  }

  /* would've liked to put max=1em here but calc is messy with units */
  @media screen and (min-width: 750px) and (max-width: 1000px) {
    :root {
      --webdev-smart-margin: calc((100vw - 750px) / 5);
    }
  }
  @media screen and (min-width: 1000px) {
    :root {
      --webdev-smart-margin: 50px;
    }
  }
</style>
