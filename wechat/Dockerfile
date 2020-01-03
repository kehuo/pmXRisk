FROM docker-reg.basebit.me:5000/basebit/nginx-include-nvm
WORKDIR /data/www
COPY ./ ./
RUN node --version && \
    npm install && \
    ./node_modules/gulp/bin/gulp.js release && \
    mkdir -p /etc/nginx/data/run/ && \
    mkdir -p /usr/share/nginx/data/www && \
    mv dist/* /usr/share/nginx/data/www
COPY resource/nginx.conf /etc/nginx/
COPY resource/default.conf /etc/nginx/conf.d/
WORKDIR /usr/share/nginx/data/www
RUN mkdir -p /data/logs; \
    mv ./config /data; \
    ln -s /data/config ./config; \
    rm -rf /var/log/nginx; \
    ln -s /data/logs /var/log/nginx; 
RUN rm -rf /data/www
