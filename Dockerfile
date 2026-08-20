FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
COPY plano.html /usr/share/nginx/html/plano.html
COPY pivo.html /usr/share/nginx/html/pivo.html
COPY visao.html /usr/share/nginx/html/visao.html
COPY nova-fase.pdf /usr/share/nginx/html/nova-fase.pdf
COPY briefing-financeiro.html /usr/share/nginx/html/briefing-financeiro.html
COPY briefing-treinamento.html /usr/share/nginx/html/briefing-treinamento.html
COPY briefing-produto.html /usr/share/nginx/html/briefing-produto.html
COPY metodo-builder.pdf /usr/share/nginx/html/metodo-builder.pdf
COPY pivo-b2b.pdf /usr/share/nginx/html/pivo-b2b.pdf
COPY spec-b2b.html /usr/share/nginx/html/spec-b2b.html
COPY spec-hub-b2b.md /usr/share/nginx/html/spec-hub-b2b.md
COPY spec-hub-b2b.pdf /usr/share/nginx/html/spec-hub-b2b.pdf
EXPOSE 80
