<template>
  <form id="movieForm" @submit.prevent="saveMovie">
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input type="text" name="title" class="form-control" />
    </div>

    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea name="description" class="form-control" rows="5"></textarea>
    </div>

    <div class="form-group mb-3">
      <label for="poster" class="form-label">Poster</label>
      <input type="file" name="poster" class="form-control" @change="handlePosterChange" />
    </div>

    <button type="submit" class="btn btn-primary">Save</button>
  </form>
</template>

<script setup>
import { ref, onMounted } from "vue";

let csrf_token = ref("");

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
    });
}

onMounted(() => {
  getCsrfToken();
});

const saveMovie = () => {
  const movieForm = document.getElementById('movieForm');
  const form_data = new FormData(movieForm);

  fetch("/api/v1/movies", {
    method: 'POST',
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
  .then(response => response.json())
  .then(data => {
    // Display a success message
    console.log(data);
  })
  .catch(error => {
    console.error('Error:', error);
  });
};
</script>
