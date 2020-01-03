FROM docker-reg.basebit.me:5000/base/centos7_py3_dev:1.0.0 as builder
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
ENV PYTHONIOENCODING utf-8
ENV LANG en_US.UTF-8
RUN mkdir -p /root/.ssh
ADD ./id_rsa /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa \
	&& ssh-keyscan -t rsa 172.18.0.108 >> ~/.ssh/known_hosts
WORKDIR /data/project
ADD ./resource/nginx.conf ./nginx.conf
ADD ./resource/default.conf ./default.conf
ADD ./resource/pip.conf /root/.pip/
ADD ./requirements.txt ./requirements.txt

RUN source ~/.bash_profile \
    && pyenv shell py3_env \
    && pip install --upgrade pip && pip install Cython && pip install path.py \
	&& pip install -r ./requirements.txt
ADD ./ ./
RUN source ~/.bash_profile \
    && pyenv shell py3_env\
    && pyinstaller --onefile server.spec --hidden-import=gunicorn.workers.ggevent; \
    pyinstaller --onefile bg_service/collect_dayjob.spec
RUN rm -rf /root/.ssh/id_rsa \
	&& rm -rf /root/.ssh/known_hosts

FROM docker-reg.basebit.me:5000/base/centos_java:1.0.0
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN yum install -y epel-release && yum install -y nginx
ENV LANG en_US.UTF-8
WORKDIR /project
RUN yum install -y cronie && sed -i '/session    required   pam_loginuid.so/c\#session    required   pam_loginuid.so' /etc/pam.d/crond \
	&& echo "00 * * * * /project/collect_dayjob.sh >> /data/cronlogs/dayjob.log 2>&1" >> /var/spool/cron/root
RUN mkdir /project/config && mkdir -p /data/logs && mkdir /data/cronlogs
COPY --from=builder /data/project/nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /data/project/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /data/project/dist/server ./
COPY --from=builder /data/project/start.sh ./
COPY --from=builder /data/project/service.conf ./config
COPY --from=builder /data/project/cron/collect_dayjob.sh ./
COPY --from=builder /data/project/dist/collect_dayjob ./

CMD ["/project/start.sh"]