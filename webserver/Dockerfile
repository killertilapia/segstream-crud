# Some ideas from https://vuejs.org/v2/cookbook/dockerize-vuejs-app.html

# Stage 1 - build frontend app
FROM node:18-alpine as build-deps

WORKDIR /app/

COPY frontend/package*.json ./
RUN npm install

COPY frontend /app/
RUN npm run build

# Stage 2 - nginx & frontend dist
FROM nginx:alpine

COPY webserver/nginx.conf /etc/nginx/nginx.conf
COPY --from=build-deps /app/dist/ /dist/

CMD ["nginx", "-g", "daemon off;"]