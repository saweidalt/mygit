import orm
import asyncio
import sys
from models import User, Blog, Comment



@asyncio.coroutine
def test(loop): #TypeError: create_pool() missing 1 required positional argument: 'loop' -> loop=loop
    yield from orm.create_pool(loop=loop, host='localhost', port=3306, user='www-data', password='www-data', db='awesome',charset='utf8')
    u = User(name='test5',email='test5@test.com',passwd='test',image='about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)
