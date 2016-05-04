import re
from datetime import datetime, timedelta
from dateutil.parser import parse as parse_datestr
from dateutil.tz import tzutc


# accept-dt-value = rfc1123-date
DATE_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'


def time_now():
    return datetime.utcnow().replace(tzinfo=tzutc())


def validate_req_datetime(datestr, strict=True):
    try:
        if strict:
            date = datetime.strptime(datestr, DATE_FORMAT)
        else:
            date = parse_datestr(datestr, fuzzy=True)
        return date.replace(tzinfo=tzutc())
    except Exception as e:
        raise DateTimeError("Error parsing 'Accept-Datetime: %s' \n"
                            "Message: %s" % (datestr, e),400)



class DateTimeError(Exception):
    def __init__(self, msg, status):
        self.status = status
        super(DateTimeError, self).__init__(msg)
