FROM haproxy:1.7

COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
COPY secret/both.pem /usr/local/etc/haproxy/chainkey.pem
RUN apt-get update
RUN chmod 000 /usr/local/etc/haproxy/chainkey.pem
RUN cat /usr/local/etc/haproxy/chainkey.pem; cat /usr/local/etc/haproxy/haproxy.cfg
CMD eval "echo \"$(cat /usr/local/etc/haproxy/haproxy.cfg)\"" > /usr/local/etc/haproxy/haproxy.cfg; \
    cat /usr/local/etc/haproxy/haproxy.cfg; \
    /usr/local/sbin/haproxy -p /run/haproxy.pid -db -f /usr/local/etc/haproxy/haproxy.cfg -Ds
