# -*- coding: utf-8 -*-
import os
import sys
from json import dumps, loads
from time import sleep, time

try:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_DIR)
    from util import util_gen
    from util import util_log
    from util import util_odb
except ImportError:
    raise Exception("import util files failed")

# -----------------------------
__author__ = 'Ishafizan'
__date__ = "2018-09-06"
# -----------------------------

log = util_log.logger()
start = time()
log.info("start: %s" % util_gen.getcurrdt())
log.info("*-" * 40)

# --------------------------------------
# QUERY via rest
# --------------------------------------

log.info("query: Find all Attractions connected with Customer with OrderedId 1")
query_str = "MATCH {class: Customers, as: customer, " \
            "where: (OrderedId=1)}" \
            "--{Class: Attractions, as: attraction} " \
            "RETURN $pathelements"

log.info("---*" * 20)
res = util_odb.post_command(log, query_str)
log.info(dumps(res["result"]))

# -- END
end = time()
elapsed_time = end - start
log.info("*-" * 40)
log.info("time taken: %ss" % elapsed_time)
log.info("FINISH")
