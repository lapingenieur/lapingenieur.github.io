<script lang="ts">
  import Blockon from "./Blockon.svelte";
  import PlateAlways from "./PlateAlways.svelte";
  import Plate from "./Plate.svelte";
</script>

<Blockon id="self">
  <h1>Présentation</h1>

  <div class="plates">
    <PlateAlways
        imgsrc="/images/self.jpg"
        imgalt="Photo de moi"
        rightRatio="3"
        padding="1em"
      >
      <h1 class="title">Bonjour&nbsp;!</h1>
      <p class="desc">
        Je suis <span class="emphase">Elio Poletti</span>,
        étudiant en première année à l'<a href="https://insa-strasbourg.fr">INSA Strasbourg</a>.
      </p>
    </PlateAlways>
    <Plate
        imgsrc="/images/academic-hat.png"
        imgalt="Études"
        minHeight="0"
        rightRatio="5"
        padding="1em"
      >
      <p class="desc">
        J'ai présenté le Bacalauréat au lycée général <a href="https://mauriac-desgranges.ent.auvergnerhonealpes.fr">Mauriac</a>
        d'Andrézieux-Bouthéon&nbsp;:
      </p>
      <ul class="desc">
        <li>note finale de <span class="emphase">17,76/20</span></li>
        <li>spécialités <span class="emphase">mathématiques</span>, <span class="emphase">physique-chimie</span> et <span class="emphase">informatique</span> <i>(NSI)</i></li>
        <li>options <span class="emphase">DNL anglais</span> et <span class="emphase">mathématiques expertes</span></li>
        <li>mentions <span class="emphase">Très Bien</span> et <span class="emphase">Section Européenne</span> <i>(Anglais)</i></li>
      </ul>
      <p class="desc">
        J'ai également suivit des enseignements de <span class="emphase">latin</span> et de <span class="emphase">grec ancien</span> jusqu'en classe de première.
      </p>
    </Plate>
  </div>
</Blockon>

<style>
  .emphase {
    font-style: italic;
    font-weight: bold;
  }

  .plates {
    display: flex;
    flex-direction: column;
    gap: 1em;
  }
</style>
