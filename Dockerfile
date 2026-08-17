FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
COPY plano.html /usr/share/nginx/html/plano.html
COPY pivo.html /usr/share/nginx/html/pivo.html
COPY metodo-builder.pdf /usr/share/nginx/html/metodo-builder.pdf
COPY pivo-b2b.pdf /usr/share/nginx/html/pivo-b2b.pdf
EXPOSE 80
