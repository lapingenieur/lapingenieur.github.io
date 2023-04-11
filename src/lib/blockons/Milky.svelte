<script lang="ts">
  import Blockon from "$lib/blockons/Blockon.svelte";
</script>

<Blockon id="milky">
  <h1>Chiptune : MilkyTracker</h1>

  <p>
    J'ai découvert la programmation de musique dite "chiptune" ou plus couramment "8-bits" pendant le confinement
    de 2020, via le logiciel <a href="https://milkytracker.org/">MilkyTracker</a>.
    Le musicien programme sa création dans une sorte de tableau/matrice avec des valeurs hexadécimales,
    avec une colonne par piste et les lignes représentant l'avancement dans le temps.
    Chaque piste peut jouer de différents instruments, et chaque instrument peut être composé d'un ou plusieurs samples.
    Des effets rudimentaires tels que le vibrato ou glissando peuvent être indiqués.
  </p>

  <div class="img-1">
    <img src="https://doc.ubuntu-fr.org/_media/tutoriel/tracker/milkytracker_01.png" alt="Logiciel MilkyTracker" />
  </div>

  <p>
    Voici une reprise du <a href="https://youtu.be/hN-HSJU6G18">thème de Riju</a> que j'ai écrite avec ce logiciel.
  </p>

  <p>
    Ce genre musical offre un très grande variété de complexité&nbsp;: il a émergé avec les débuts de l'informatique
    et les limitations matérielles de stockage, ce pourquoi les artistes de l'époque optimisaient au plus possible
    leurs audios (comme <a href="https://youtu.be/thnXzUFJnfQ">Captain - Space Debris</a> de Markus Kaarlonen)
    quite à les rendre peu plaisants à l'oreille (par exemple, Rob Hubbards avec <a href="https://youtu.be/pgPEaI0GHBI">Commando</a>).
  </p>

  <p>
    Mais on retrouve également des pièces plus agréables, et plus complexes, comme
    <a href="/chiptune/to_norway_with_love">To Norway with Love</a> de Brandon Walsh, ou
    <a href="https://youtu.be/SEeALyvkMIQ">Escape Velocity</a> de gusse ^ digisonix.
  </p>
</Blockon>

<style>
  .img-1 {
    max-width: 100%;
    max-height: 100%;

    display: flex;
    justify-content: center;
  }
  .img-1 img {
    max-height: 30em;
    max-width: 100%;
  }
</style>
