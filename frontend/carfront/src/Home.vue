<template>
  <div>
    <p>Home page</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  props: ['FIELD1'],
  data () {
    return {
      cars: ''
    }
  },
  mounted () {
    axios
      .get('http://127.0.0.1:5000/api/cars')
      .then(response => {
        this.cars = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

