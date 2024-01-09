<script lang="ts">
  import Blockon from "./Blockon.svelte";
</script>

<Blockon id="sommaire">
  <h1>Sommaire</h1>

  <p>
    Bienvenue sur <span class="emphase">lapingenieur.github.io</span>&nbsp;!
  </p>
  <p>
    Ce site, écrit lors de la campagne <span class="emphase">Parcoursup de 2023</span>,
    introduit les différents pans de l'informatique que j'ai expérimentés.
    <br />
    Le code-source des programmes décrits plus bas est disponible soit sur ce site,
    soit sur mon <a href="https://github.com/lapingenieur">GitHub</a>.
  </p>
  <p>
    Bonne lecture&nbsp;!
  </p>

  <ul>
    <li><a href="#self">Présentation</a></li>
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

    text-decoration: none;
    font-size: 1.5em;

    text-align: left;
  }

  a:visited:not(:hover) {
    color: #535ed6;
  }
</style>
