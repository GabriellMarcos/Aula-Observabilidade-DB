FROM nginx:stable-alpine
COPY default.conf /etc/nginx/conf.d/default.conf
COPY cert.pem /etc/nginx/cert.pem
COPY key.pem /etc/nginx/key.pem
COPY htpasswd /etc/nginx/.htpasswd
