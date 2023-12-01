import util, logging, sys
logger = logging.getLogger('AoC')

handler = logging.StreamHandler()
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

lines = util.parse('input.txt')
for i in range(len(lines)):
    l = lines[i]
