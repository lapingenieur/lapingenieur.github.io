<script lang="ts">
  import Blockon from "./Blockon.svelte";
</script>

<Blockon id="sommaire">
  <h1>Sommaire</h1>

  <p>
    Ce site introduit les différents pans de l'informatique que j'ai expérimentés.
  </p>
  <p>
    Le code-source des programmes décrits plus bas est disponible soit sur ce site,
    soit sur mon <a href="https://github.com/lapingenieur">GitHub</a>.
  </p>

  <ul>
    <li><a href="#webdev">Développement Web</a></li>
    <li><a href="#bits">Élaboration d'un ordinateur 8-bits</a></li>
    <li><a href="#lowlevel">Programmation Bas Niveau</a></li>
    <li><a href="#workflow">Linux, Neovim, scripts shell et environnement de travail</a></li>
    <li><a href="#python">Scripts python</a></li>
    <li><a href="#milky">Chiptune (MilkyTracker)</a></li>
  </ul>
</Blockon>

<style>
  ul {
    padding: 0 1.5em;
  }
  li::marker {
    color: transparent;
  }

  ul a {
    display: block;
    width: 100%;
    padding: 0.3em 0;

    color: #535ed6;
    text-decoration: none;
    font-size: 1.5em;

    transition: color 0.18s;
  }
  a:hover {
    color: #9198e5;
  }
</style>
