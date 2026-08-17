FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
COPY plano.html /usr/share/nginx/html/plano.html
COPY metodo-builder.pdf /usr/share/nginx/html/metodo-builder.pdf
EXPOSE 80
