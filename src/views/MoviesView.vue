<template>
  <div>
    <div v-if="movies.length === 0">No Images</div>
    <div v-else>
      <div class="card-container">
        <div v-for="movie in movies" :key="movie.id" class="card">
          <div class="card-content">
            <img :src="movie.poster" class="card-img-top" alt="Movie Poster">
            <div class="text">
              <h5 class="card-title">{{ movie.title }}</h5>
              <p class="card-text">{{ movie.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

const fetchMovies = () => {
  fetch("/api/v1/movies", {
    method: 'GET'
  })
    .then(response => response.json())
    .then(data => {
      movies.value = data.movies;
    })
    .catch(error => {
      console.error('Error fetching movies:', error);
    });
};

onMounted(() => {
  fetchMovies();
});
</script>

<style scoped>
.card-container {
  display: flex;
  flex-wrap: wrap;
}

.card {
  margin: 20px;
  width: 300px;
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
}

.card-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.card-img-top {
  width: 100%;
  height: 200px; 
  object-fit: cover; 
}

.text {
  flex: 1;
  padding: 15px;
}

.card-title {
  font-size: 18px;
  margin-top: 0;
}

h5{
  font-weight:bold;
}

.card-text {
  margin-bottom: 0;
}
</style>
