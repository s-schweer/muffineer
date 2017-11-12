FROM centos:7

RUN yum -y install bind

ADD assets/named.conf /etc/named.conf

ADD assets/example.net /var/named/example.net

RUN chown -R named:named /var/named

CMD ["/sbin/named", "-u", "named", "-c", "/etc/named.conf", "-f"]

