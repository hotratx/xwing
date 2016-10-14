import asyncio

from xwing.mailbox import init_node, start_node, spawn


async def ping(mailbox, n, pong_node):
    for _ in range(n):
        await mailbox.send(pong_node, 'ping', mailbox.pid)
        message = await mailbox.recv()
        if message[0] == 'pong':
            print('Ping received pong')

    await mailbox.send('pong', 'finished')

    # FIXME right now we need this to make sure that
    # the finished messages is sent before the actor
    # exit and its mailbox gets garbaged. How does
    # erlang fix this problem?
    await asyncio.sleep(1)


if __name__ == '__main__':
    # python examples/mailbox/distributed/ping.py
    init_node()
    spawn(ping, 3, 'pong@127.0.0.1')
    start_node()
