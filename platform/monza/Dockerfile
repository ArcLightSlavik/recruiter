FROM node:14.15.1-alpine3.11 as build-stage

COPY package*.json ./
RUN npm install
EXPOSE ${PORT}
CMD ["npm", "run", "serve" , "--", "--port", "$PORT"]

## build stage
#FROM node:14.15.1-alpine3.11 as build-stage
#COPY package*.json ./
#RUN npm install
#COPY . .
#RUN npm run build

## production stage
#FROM nginx:stable-alpine as production-stage
#COPY ./nginx.conf /etc/nginx/nginx.conf
#COPY --from=build-stage /dist /usr/share/nginx/html
#EXPOSE ${PORT}
#CMD ["nginx", "-g", "daemon off;"]
