<template>
  <h1>Hello world</h1>
  {{ response_data.name }}
  <br>
  {{ response_data.employee_number }}
  <br>
  {{ response_data.locations }}
  <br>
  {{ response_data.website_url }}
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      response_data: null
    }
  },
  created() {
    axios.get('http://127.0.0.1:1234/company/google').then(response => {
      this.response_data = response.data
    }).catch(error => {
      console.log(error)
    })
  }
}
</script>

<style>
</style>
