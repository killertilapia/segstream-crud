<script lang="ts">
import {defineComponent} from "vue";
import axios from 'axios'

interface UserData {
  id: number
  password: string
  username: string
  first_name: string
  last_name: string
  email: string
}

export default defineComponent({
  name: 'Home',
  data() {
    return {
      users: [] as UserData[],
      fetchingData: false,
      headers: [
        {'text': 'ID', value: 'id'},
        {'text': 'Username', value: 'username'},
        {'text': 'First Name', value: 'first_name'},
        {'text': 'Last Name', value: 'last_name'},
        {'text': 'Email', value: 'email'}
      ],
      userId: '',
      post_form: {
        first_name: '',
        last_name: '',
        email: '',
        username: '',
      },
      put_form: {
        id: 0,
        first_name: '',
        last_name: '',
        email: '',
        username: '',
      },
      get_api_response: null,
      post_api_response: null,
      put_api_response: null,
      del_api_response: null,
    }
  },
  methods: {
    async loadUsers() {
      this.fetchingData = true

      const apiResponse = await axios.get<UserData[]>('/users/', {
        baseURL: 'http://localhost:8000/api/v1'
      })
      this.users = apiResponse.data

      this.fetchingData = false
    },
    async getUserById(id: number) {
      this.fetchingData = true

      try {
        const apiResponse = await axios.get<UserData[]>(`/users/${id}/`, {
          baseURL: 'http://localhost:8000/api/v1'
        })
        this.get_api_response = apiResponse

      } catch (error) {
        this.get_api_response = error.response
      }

      this.fetchingData = false
    },
    async addUser() {
      this.fetchingData = true

      try {
        const api_response = await axios.post<UserData>('/users/', this.post_form, {
          baseURL: 'http://localhost:8000/api/v1'
        })
        this.post_api_response = api_response

        await this.loadUsers()

      } catch (error) {
        this.post_api_response = error.response
      }

      this.fetchingData = false
    },
    async updateUser() {
      this.fetchingData = true

      try {
        const api_response = await axios.put<UserData>(`/users/${this.put_form['id']}/`, this.put_form, {
          baseURL: 'http://localhost:8000/api/v1'
        })
        this.put_api_response = api_response

        await this.loadUsers()

      } catch (error) {
        this.put_api_response = error.response
      }

      this.fetchingData = false
    },
    async deleteUser(id: number) {
      this.fetchingData = true

      try {
        const api_response = await axios.delete(`/users/${id}/`, {
          baseURL: 'http://localhost:8000/api/v1'
        })
        this.del_api_response = api_response

        await this.loadUsers()

      } catch (error) {
        this.del_api_response = error.response
      }

      this.fetchingData = false
    },
  },
  async mounted() {
    await this.loadUsers()
  }
})

</script>

<template>
  <main>
    <div class="row">
      <b-overlay :show="fetchingData" rounded="sm">
        <EasyDataTable :headers='headers'
                       :items='users'/>
      </b-overlay>
    </div>
    <div class="row mt-5">
      <div class="col-8">
        <div>
          <b-tabs pills content-class="mt-3">
            <b-tab title="GET" active>
              <div class="row">
                <div class="col-4">
                  <b-form-group label="User ID" label-for="input-get-id">
                    <b-form-input v-model="userId" id="input-get-id"></b-form-input>
                  </b-form-group>
                  <b-button @click="getUserById(userId)" variant="secondary">Submit</b-button>
                </div>
                <div class="col-8">
                  <h4>API Response</h4>
                  {{ get_api_response ? get_api_response : 'No Data' }}
                </div>
              </div>
            </b-tab>
            <b-tab title="POST">

              <div class="row">
                <div class="col-4">
                  <div>
                <b-form @submit="addUser">
                  <b-form-group
                      id="input-group-1"
                      label="First Name"
                      label-for="input-first-name"
                  >
                    <b-form-input
                        id="input-first-name"
                        v-model="post_form.first_name"
                        placeholder="Enter First Name"
                    ></b-form-input>
                  </b-form-group>
                  <b-form-group
                      id="input-group-2"
                      label="Last Name"
                      label-for="input-last-name"
                  >
                    <b-form-input
                        id="input-last-name"
                        v-model="post_form.last_name"
                        placeholder="Enter Last Name"
                    ></b-form-input>
                  </b-form-group>
                  <b-form-group
                      id="input-group-3"
                      label="Email"
                      label-for="input-email"
                  >
                    <b-form-input
                        id="input-email"
                        v-model="post_form.email"
                        type="email"
                        placeholder="Email"
                    ></b-form-input>
                  </b-form-group>

                  <b-form-group
                      id="input-group-4"
                      label="Username"
                      label-for="input-user-name"
                  >
                    <b-form-input
                        id="input-user-name"
                        v-model="post_form.username"
                        placeholder="Enter Username"
                    ></b-form-input>
                  </b-form-group>

                  <b-form-group
                      id="input-group-5"
                      label="Password"
                      label-for="input-password"
                  >
                    <b-form-input
                        id="input-password"
                        v-model="post_form.password"
                        placeholder="Enter Password"
                    ></b-form-input>
                  </b-form-group>

                  <b-button type="submit" variant="primary">Submit</b-button>
                </b-form>
              </div>
                </div>
                <div class="col-8">
                  <h4>API Response</h4>
                  {{ post_api_response ? post_api_response : 'No Data' }}
                </div>
              </div>
            </b-tab>
            <b-tab title="PUT">
              <div class="row">
                <div class="col-4">
                  <div>
                <b-form @submit="updateUser">
                  <b-form-group
                      id="input-group-id"
                      label="User ID"
                      label-for="input-user-id"
                  >
                    <b-form-input
                        id="input-user-id"
                        v-model="put_form.id"
                        placeholder="Enter ID"
                    ></b-form-input>
                  </b-form-group>
                  <b-form-group
                      id="input-group-1"
                      label="First Name"
                      label-for="input-first-name"
                  >
                    <b-form-input
                        id="input-first-name"
                        v-model="put_form.first_name"
                        placeholder="Enter First Name"
                    ></b-form-input>
                  </b-form-group>
                  <b-form-group
                      id="input-group-2"
                      label="Last Name"
                      label-for="input-last-name"
                  >
                    <b-form-input
                        id="input-last-name"
                        v-model="put_form.last_name"
                        placeholder="Enter Last Name"
                    ></b-form-input>
                  </b-form-group>
                  <b-form-group
                      id="input-group-3"
                      label="Email"
                      label-for="input-email"
                  >
                    <b-form-input
                        id="input-email"
                        v-model="put_form.email"
                        type="email"
                        placeholder="Email"
                    ></b-form-input>
                  </b-form-group>

                  <b-form-group
                      id="input-group-4"
                      label="Username"
                      label-for="input-user-name"
                  >
                    <b-form-input
                        id="input-user-name"
                        v-model="put_form.username"
                        placeholder="Enter Username"
                    ></b-form-input>
                  </b-form-group>

                  <b-form-group
                      id="input-group-5"
                      label="Password"
                      label-for="input-password"
                  >
                    <b-form-input
                        id="input-password"
                        v-model="put_form.password"
                        placeholder="Enter Password"
                    ></b-form-input>
                  </b-form-group>

                  <b-button type="submit" variant="primary">Update</b-button>
                </b-form>
              </div>
                </div>
                <div class="col-8">
                  <h4>API Response</h4>
                  {{ put_api_response ? put_api_response : 'No Data' }}
                </div>
              </div>
            </b-tab>
            <b-tab title="DEL">
              <div class="row">
                <div class="col-4">
                  <b-form-group label="User ID" label-for="input-get-id">
                    <b-form-input v-model="userId" id="input-get-id"></b-form-input>
                  </b-form-group>
                  <b-button @click="deleteUser(userId)" variant="danger">Delete</b-button>
                </div>
                <div class="col-8">
                  <h4>API Response</h4>
                  {{ del_api_response ? del_api_response : 'No Data' }}
                </div>
              </div>
            </b-tab>
          </b-tabs>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
</style>