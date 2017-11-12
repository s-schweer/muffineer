import json
import logging

import dns.query
import dns.zone
import dns.update
import dns.rdatatype

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class DnsZone(object):
    def __init__(self, name=None, dns_server=None):
        self.name = name
        self.zone = self._domain_xfer(name, dns_server)
        self.a_records = self._parse_a_records(self.zone)
        self.cname_records = self._parse_cname_records(self.zone)
        self.dns_server = dns_server

    def _domain_xfer(self, name, dns_server):
        try:
            return dns.zone.from_xfr(dns.query.xfr(dns_server, name))
        except Exception as e:
            raise Exception(e)

    def _parse_a_records(self, zone):
        a_records = []
        for (name, ttl, rdata) in zone.iterate_rdatas('A'):
            a_records.append(DnsRecord(str(name), str(ttl), str(rdata), record_type='A'))
        return a_records

    def _parse_cname_records(self, zone):
        cnames = []
        for (name, ttl, rdata) in zone.iterate_rdatas('CNAME'):
            cnames.append(DnsRecord(str(name), str(ttl), str(rdata), record_type='CNAME'))
        return cnames

    def as_dict(self):
        a_records = []
        for record in self.a_records:
            a_records.append(dict(name=record.name, ttl=record.ttl, address=record.address))
        cname_records = []
        for record in self.cname_records:
            cname_records.append(dict(name=record.name, ttl=record.ttl, address=record.address))
        records = dict(a_records=a_records, cname_records=cname_records)
        return records

    def as_json(self):
        return json.dumps(self.as_dict())

    def add(self, doc):
        name = doc.get('name')
        ttl = doc.get('ttl')
        address = doc.get('address')
        record_type = doc.get('record_type')
        if record_type == 'A':
            rdtype = dns.rdatatype.A
        elif record_type == 'CNAME':
            rdtype = dns.rdatatype.CNAME
        try:
            record = DnsRecord(name, ttl, address)
            update = dns.update.Update(self.name)
            update.absent(name)
            update.add(name, ttl, rdtype, address)
            dns.query.tcp(update, self.dns_server)
            if record_type == 'A':
                self.a_records.append(record)
            elif record_type == 'CNAME':
                self.cnames_records.append(record)
            return name
        except Exception as e:
            raise Exception(e)


    def exists(self, name):
        for a_record in self.a_records:
            if a_record.name == name:
                return True
            for cname_record in self.cname_records:
                if cname_record.name == name:
                    return True

    def get(self, name):
        if self.exists(name):
            for record in self.a_records:
                if record.name == name:
                    return record
            for record in self.cname_records:
                if record.name == name:
                    return record
        else:
            return None

    def modify(self, name, data):
        dns_record = self.get(name)
        ttl = data.get('ttl', dns_record.ttl)
        address = data.get('address', dns_record.address)
        old_record_type = dns_record.record_type
        record_type = data.get('record_type', dns_record.record_type)
        if record_type == 'A':
            rdtype = dns.rdatatype.A
        elif record_type == 'CNAME':
            rdtype = dns.rdatatype.CNAME
        try:
            dns_record.ttl = ttl
            dns_record.address = address
            update = dns.update.Update(self.name)
            update.present(name)
            if old_record_type == record_type:
                update.replace(name, ttl, rdtype, address)
            else:
                update.delete(name)
                update.add(name, ttl, rdtype, address)
            dns.query.tcp(update, self.dns_server)
            return name
        except Exception as e:
            raise Exception(e)
        return name

    def delete(self, name):
        record = self.get(name)
        try:
            update = dns.update.Update(self.name)
            update.present(name)
            update.delete(name)
            dns.query.tcp(update, self.dns_server)
            if record.record_type == 'A':
                self.a_records.remove(record)
            elif record.record_type == 'CNAME':
                self.cname_records.remove(record)
            return True
        except Exception as e:
            raise Exception(e)


class DnsRecord(object):
    def __init__(self, name, ttl, address, record_type='A'):
        self.name = name
        self.ttl = ttl
        self.address = address
        self.record_type = record_type

    def as_dict(self):
        return dict(name=self.name, ttl=self.ttl, address=self.address, record_type=self.record_type)

    def as_json(self):
        return json.dumps(self.as_dict())



