import frappe
from toolz import keyfilter, curry, compose


@curry
def pick(whitelist, d=None):
    return keyfilter(lambda k: k in whitelist, d)


def handle_error(fn):
    def wrapper(*args, **kwargs):
        del kwargs["cmd"]
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            frappe.logger("leiteng").error(e)

    return wrapper


transform_route = compose(lambda x: x.replace("/", "__"), lambda x: x.get("route"))
