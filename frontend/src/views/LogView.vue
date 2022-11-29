<script lang="ts">
import {defineComponent} from "vue";
import axios from 'axios'

interface LogData{
  id: number
  added_on: string
  api: string
  headers: string
  body: string
  method: string
  client_ip_address: string
  response: string
  status_code: number
  execution_time: string
}

export default defineComponent({
  name: 'Logs',
  data(){
    return {
      logs: [] as LogData[],
      fetchingData: false,
      headers: [
        {'text': 'ID', value: 'id'},
        {'text': 'API', value: 'api'},
        {'text': 'Method', value: 'method'},
        {'text': 'Client IP', value: 'client_ip_address'},
        {'text': 'Status Code', value: 'status_code'}
      ]
    }
  },
  methods: {
    async loadLogs(){
      this.fetchingData = true

      try{
        const response = await axios.get<LogData[]>('/api-logs/', {
          baseURL: 'http://localhost:8000/api/v1'
        })
        this.logs = response.data
      }catch(error){
        console.log(error.response);
      }

      this.fetchingData = false
    },
  },
  async mounted(){
    await this.loadLogs()
  }
})

</script>

<template>
  <div class="row">
    <div class="col-12">
      <b-overlay :show="fetchingData" rounded="sm">
        <EasyDataTable :headers='headers' :items='logs'/>
      </b-overlay>
    </div>
  </div>
</template>

<style>
</style>
