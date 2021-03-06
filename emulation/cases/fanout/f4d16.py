
import docker
import mininet.cli
import mininet.node
import mininet.link
import mininet.log
import mininet.net
import os
import sys
import time
from functools import partial

mininet.log.setLogLevel('info')

Switch = partial(mininet.node.OVSSwitch, protocols='OpenFlow13')
net = mininet.net.Containernet(switch=Switch)
net.addController('c0', controller=mininet.node.RemoteController, ip='172.17.42.1', port=6652)

# runtime_id = os.urandom(2).encode('hex')
runtime_id = sys.argv[1]
s0 = net.addSwitch("s0")
s1 = net.addSwitch("s1")
s2 = net.addSwitch("s2")
s3 = net.addSwitch("s3")
s4 = net.addSwitch("s4")
net.addLink(s0, s1, cls=mininet.link.TCLink, delay="100ms", bw=40)
net.addLink(s1, s2, cls=mininet.link.TCLink, delay="10ms", bw=20)
net.addLink(s0, s3, cls=mininet.link.TCLink, delay="100ms", bw=40)
net.addLink(s3, s4, cls=mininet.link.TCLink, delay="10ms", bw=20)

c0 = net.addDocker(
    'c0' + runtime_id,
    ip='10.0.1.1/8',
    dimage='dx_cloud_deploy',
    dcmd='python deploy-service/main.py',
    environment={
        'TOPO_NAME': 'f4d16',
        'CADVISOR_HOST': '172.17.42.1',
        'CADVISOR_PORT': 9001
    },
    volumes=['/home/hujuntao/gitrepo/dx-proto/emulation/cases/fanout:/data/topos'],
    cpu_quota=400000,
    mem_limit='4096m')
net.addLink(c0, s0, cls=mininet.link.TCLink, delay="1ms", bw=40)

f0 = net.addDocker(
    'f0' + runtime_id,
    ip='10.0.2.1/8',
    dimage='dx_edge',
    dcmd='bash boot.sh',
    environment={
        'MY_IP': '10.0.2.1',
        'SERVER_HOST': '10.0.1.1',
        'SERVER_PORT_NODE': 7000,
        'START_DELAY': 60,
        'AGENT_MODE': 'dev',
        'FUNCTION_WAREHOUSE': '/home/hujuntao/deploy/functions'
    },
    volumes=[
        '/var/run/docker.sock:/var/run/docker.sock',
        '/home/hujuntao/deploy/functions:/home/hujuntao/deploy/functions',
    ],
    cpu_quota=200000,
    mem_limit='2048m')
net.addLink(f0, s1, cls=mininet.link.TCLink, delay="1ms", bw=20)

f1 = net.addDocker(
    'f1' + runtime_id,
    ip='10.0.2.2/8',
    dimage='dx_edge',
    dcmd='bash boot.sh',
    environment={
        'MY_IP': '10.0.2.2',
        'SERVER_HOST': '10.0.1.1',
        'SERVER_PORT_NODE': 7000,
        'START_DELAY': 60,
        'AGENT_MODE': 'dev',
        'FUNCTION_WAREHOUSE': '/home/hujuntao/deploy/functions'
    },
    volumes=[
        '/var/run/docker.sock:/var/run/docker.sock',
        '/home/hujuntao/deploy/functions:/home/hujuntao/deploy/functions',
    ],
    cpu_quota=200000,
    mem_limit='2048m')
net.addLink(f1, s3, cls=mininet.link.TCLink, delay="1ms", bw=20)

f2 = net.addDocker(
    'f2' + runtime_id,
    ip='10.0.2.3/8',
    dimage='dx_edge',
    dcmd='bash boot.sh',
    environment={
        'MY_IP': '10.0.2.3',
        'SERVER_HOST': '10.0.1.1',
        'SERVER_PORT_NODE': 7000,
        'START_DELAY': 60,
        'AGENT_MODE': 'dev',
        'FUNCTION_WAREHOUSE': '/home/hujuntao/deploy/functions'
    },
    volumes=[
        '/var/run/docker.sock:/var/run/docker.sock',
        '/home/hujuntao/deploy/functions:/home/hujuntao/deploy/functions',
    ],
    cpu_quota=200000,
    mem_limit='2048m')
net.addLink(f2, s1, cls=mininet.link.TCLink, delay="1ms", bw=20)

f3 = net.addDocker(
    'f3' + runtime_id,
    ip='10.0.2.4/8',
    dimage='dx_edge',
    dcmd='bash boot.sh',
    environment={
        'MY_IP': '10.0.2.4',
        'SERVER_HOST': '10.0.1.1',
        'SERVER_PORT_NODE': 7000,
        'START_DELAY': 60,
        'AGENT_MODE': 'dev',
        'FUNCTION_WAREHOUSE': '/home/hujuntao/deploy/functions'
    },
    volumes=[
        '/var/run/docker.sock:/var/run/docker.sock',
        '/home/hujuntao/deploy/functions:/home/hujuntao/deploy/functions',
    ],
    cpu_quota=200000,
    mem_limit='2048m')
net.addLink(f3, s3, cls=mininet.link.TCLink, delay="1ms", bw=20)

d0 = net.addDocker(
    'd0' + runtime_id,
    ip='10.0.3.1/8',
    dimage='dx_device:latest',
    dcmd='python -m dx_emulation.image',
    environment={
        'MY_IP': '10.0.3.1',
        'CLOUD_HOST': '10.0.1.1',
        'CLOUD_PORT': 8883,
        'START_TIME': 96,
        'RUN_INTERVAL': 1,
        'RUN_COUNT': 50,
        'EMULATION_MODE': 'dev',
        'LOG_FILE': '/data/log/d0' + runtime_id + '.log'
    },
    volumes=['/home/hujuntao/log/device:/data/log'],
    cpu_quota=100000,
    mem_limit='128m')
net.addLink(d0, s2, cls=mininet.link.TCLink, delay="1ms", bw=10)

d1 = net.addDocker(
    'd1' + runtime_id,
    ip='10.0.3.2/8',
    dimage='dx_device:latest',
    dcmd='python -m dx_emulation.image',
    environment={
        'MY_IP': '10.0.3.2',
        'CLOUD_HOST': '10.0.1.1',
        'CLOUD_PORT': 8883,
        'START_TIME': 101,
        'RUN_INTERVAL': 1,
        'RUN_COUNT': 50,
        'EMULATION_MODE': 'dev',
        'LOG_FILE': '/data/log/d1' + runtime_id + '.log'
    },
    volumes=['/home/hujuntao/log/device:/data/log'],
    cpu_quota=100000,
    mem_limit='128m')
net.addLink(d1, s4, cls=mininet.link.TCLink, delay="1ms", bw=10)

d2 = net.addDocker(
    'd2' + runtime_id,
    ip='10.0.3.3/8',
    dimage='dx_device:latest',
    dcmd='python -m dx_emulation.image',
    environment={
        'MY_IP': '10.0.3.3',
        'CLOUD_HOST': '10.0.1.1',
        'CLOUD_PORT': 8883,
        'START_TIME': 115,
        'RUN_INTERVAL': 1,
        'RUN_COUNT': 50,
        'EMULATION_MODE': 'dev',
        'LOG_FILE': '/data/log/d2' + runtime_id + '.log'
    },
    volumes=['/home/hujuntao/log/device:/data/log'],
    cpu_quota=100000,
    mem_limit='128m')
net.addLink(d2, s2, cls=mininet.link.TCLink, delay="1ms", bw=10)

d3 = net.addDocker(
    'd3' + runtime_id,
    ip='10.0.3.4/8',
    dimage='dx_device:latest',
    dcmd='python -m dx_emulation.image',
    environment={
        'MY_IP': '10.0.3.4',
        'CLOUD_HOST': '10.0.1.1',
        'CLOUD_PORT': 8883,
        'START_TIME': 139,
        'RUN_INTERVAL': 1,
        'RUN_COUNT': 50,
        'EMULATION_MODE': 'dev',
        'LOG_FILE': '/data/log/d3' + runtime_id + '.log'
    },
    volumes=['/home/hujuntao/log/device:/data/log'],
    cpu_quota=100000,
    mem_limit='128m')
net.addLink(d3, s4, cls=mininet.link.TCLink, delay="1ms", bw=10)

d4 = net.addDocker(
    'd4' + runtime_id,
    ip='10.0.3.5/8',
    dimage='dx_device:latest',
    dcmd='python -m dx_emulation.image',
    environment={
        'MY_IP': '10.0.3.5',
        'CLOUD_HOST': '10.0.1.1',
        'CLOUD_PORT': 8883,
        'START_TIME': 98,
        'RUN_INTERVAL': 1,
        'RUN_COUNT': 50,
        'EMULATION_MODE': 'dev',
        'LOG_FILE': '/data/log/d4' + runtime_id + '.log'
    },
    volumes=['/home/hujuntao/log/device:/data/log'],
    cpu_quota=100000,
    mem_limit='128m')
net.addLink(d4, s2, cls=mininet.link.TCLink, delay="1ms", bw=10)

d5 = net.addDocker(
    'd5' + runtime_id,
    ip='10.0.3.6/8',
    dimage='dx_device:latest',
    dcmd='python -m dx_emulation.image',
    environment={
        'MY_IP': '10.0.3.6',
        'CLOUD_HOST': '10.0.1.1',
        'CLOUD_PORT': 8883,
        'START_TIME': 127,
        'RUN_INTERVAL': 1,
        'RUN_COUNT': 50,
        'EMULATION_MODE': 'dev',
        'LOG_FILE': '/data/log/d5' + runtime_id + '.log'
    },
    volumes=['/home/hujuntao/log/device:/data/log'],
    cpu_quota=100000,
    mem_limit='128m')
net.addLink(d5, s4, cls=mininet.link.TCLink, delay="1ms", bw=10)

d6 = net.addDocker(
    'd6' + runtime_id,
    ip='10.0.3.7/8',
    dimage='dx_device:latest',
    dcmd='python -m dx_emulation.image',
    environment={
        'MY_IP': '10.0.3.7',
        'CLOUD_HOST': '10.0.1.1',
        'CLOUD_PORT': 8883,
        'START_TIME': 109,
        'RUN_INTERVAL': 1,
        'RUN_COUNT': 50,
        'EMULATION_MODE': 'dev',
        'LOG_FILE': '/data/log/d6' + runtime_id + '.log'
    },
    volumes=['/home/hujuntao/log/device:/data/log'],
    cpu_quota=100000,
    mem_limit='128m')
net.addLink(d6, s2, cls=mininet.link.TCLink, delay="1ms", bw=10)

d7 = net.addDocker(
    'd7' + runtime_id,
    ip='10.0.3.8/8',
    dimage='dx_device:latest',
    dcmd='python -m dx_emulation.image',
    environment={
        'MY_IP': '10.0.3.8',
        'CLOUD_HOST': '10.0.1.1',
        'CLOUD_PORT': 8883,
        'START_TIME': 128,
        'RUN_INTERVAL': 1,
        'RUN_COUNT': 50,
        'EMULATION_MODE': 'dev',
        'LOG_FILE': '/data/log/d7' + runtime_id + '.log'
    },
    volumes=['/home/hujuntao/log/device:/data/log'],
    cpu_quota=100000,
    mem_limit='128m')
net.addLink(d7, s4, cls=mininet.link.TCLink, delay="1ms", bw=10)

d8 = net.addDocker(
    'd8' + runtime_id,
    ip='10.0.3.9/8',
    dimage='dx_device:latest',
    dcmd='python -m dx_emulation.image',
    environment={
        'MY_IP': '10.0.3.9',
        'CLOUD_HOST': '10.0.1.1',
        'CLOUD_PORT': 8883,
        'START_TIME': 114,
        'RUN_INTERVAL': 1,
        'RUN_COUNT': 50,
        'EMULATION_MODE': 'dev',
        'LOG_FILE': '/data/log/d8' + runtime_id + '.log'
    },
    volumes=['/home/hujuntao/log/device:/data/log'],
    cpu_quota=100000,
    mem_limit='128m')
net.addLink(d8, s2, cls=mininet.link.TCLink, delay="1ms", bw=10)

d9 = net.addDocker(
    'd9' + runtime_id,
    ip='10.0.3.10/8',
    dimage='dx_device:latest',
    dcmd='python -m dx_emulation.image',
    environment={
        'MY_IP': '10.0.3.10',
        'CLOUD_HOST': '10.0.1.1',
        'CLOUD_PORT': 8883,
        'START_TIME': 106,
        'RUN_INTERVAL': 1,
        'RUN_COUNT': 50,
        'EMULATION_MODE': 'dev',
        'LOG_FILE': '/data/log/d9' + runtime_id + '.log'
    },
    volumes=['/home/hujuntao/log/device:/data/log'],
    cpu_quota=100000,
    mem_limit='128m')
net.addLink(d9, s4, cls=mininet.link.TCLink, delay="1ms", bw=10)

d10 = net.addDocker(
    'd10' + runtime_id,
    ip='10.0.3.11/8',
    dimage='dx_device:latest',
    dcmd='python -m dx_emulation.image',
    environment={
        'MY_IP': '10.0.3.11',
        'CLOUD_HOST': '10.0.1.1',
        'CLOUD_PORT': 8883,
        'START_TIME': 94,
        'RUN_INTERVAL': 1,
        'RUN_COUNT': 50,
        'EMULATION_MODE': 'dev',
        'LOG_FILE': '/data/log/d10' + runtime_id + '.log'
    },
    volumes=['/home/hujuntao/log/device:/data/log'],
    cpu_quota=100000,
    mem_limit='128m')
net.addLink(d10, s2, cls=mininet.link.TCLink, delay="1ms", bw=10)

d11 = net.addDocker(
    'd11' + runtime_id,
    ip='10.0.3.12/8',
    dimage='dx_device:latest',
    dcmd='python -m dx_emulation.image',
    environment={
        'MY_IP': '10.0.3.12',
        'CLOUD_HOST': '10.0.1.1',
        'CLOUD_PORT': 8883,
        'START_TIME': 92,
        'RUN_INTERVAL': 1,
        'RUN_COUNT': 50,
        'EMULATION_MODE': 'dev',
        'LOG_FILE': '/data/log/d11' + runtime_id + '.log'
    },
    volumes=['/home/hujuntao/log/device:/data/log'],
    cpu_quota=100000,
    mem_limit='128m')
net.addLink(d11, s4, cls=mininet.link.TCLink, delay="1ms", bw=10)

d12 = net.addDocker(
    'd12' + runtime_id,
    ip='10.0.3.13/8',
    dimage='dx_device:latest',
    dcmd='python -m dx_emulation.image',
    environment={
        'MY_IP': '10.0.3.13',
        'CLOUD_HOST': '10.0.1.1',
        'CLOUD_PORT': 8883,
        'START_TIME': 101,
        'RUN_INTERVAL': 1,
        'RUN_COUNT': 50,
        'EMULATION_MODE': 'dev',
        'LOG_FILE': '/data/log/d12' + runtime_id + '.log'
    },
    volumes=['/home/hujuntao/log/device:/data/log'],
    cpu_quota=100000,
    mem_limit='128m')
net.addLink(d12, s2, cls=mininet.link.TCLink, delay="1ms", bw=10)

d13 = net.addDocker(
    'd13' + runtime_id,
    ip='10.0.3.14/8',
    dimage='dx_device:latest',
    dcmd='python -m dx_emulation.image',
    environment={
        'MY_IP': '10.0.3.14',
        'CLOUD_HOST': '10.0.1.1',
        'CLOUD_PORT': 8883,
        'START_TIME': 102,
        'RUN_INTERVAL': 1,
        'RUN_COUNT': 50,
        'EMULATION_MODE': 'dev',
        'LOG_FILE': '/data/log/d13' + runtime_id + '.log'
    },
    volumes=['/home/hujuntao/log/device:/data/log'],
    cpu_quota=100000,
    mem_limit='128m')
net.addLink(d13, s4, cls=mininet.link.TCLink, delay="1ms", bw=10)

d14 = net.addDocker(
    'd14' + runtime_id,
    ip='10.0.3.15/8',
    dimage='dx_device:latest',
    dcmd='python -m dx_emulation.image',
    environment={
        'MY_IP': '10.0.3.15',
        'CLOUD_HOST': '10.0.1.1',
        'CLOUD_PORT': 8883,
        'START_TIME': 139,
        'RUN_INTERVAL': 1,
        'RUN_COUNT': 50,
        'EMULATION_MODE': 'dev',
        'LOG_FILE': '/data/log/d14' + runtime_id + '.log'
    },
    volumes=['/home/hujuntao/log/device:/data/log'],
    cpu_quota=100000,
    mem_limit='128m')
net.addLink(d14, s2, cls=mininet.link.TCLink, delay="1ms", bw=10)

d15 = net.addDocker(
    'd15' + runtime_id,
    ip='10.0.3.16/8',
    dimage='dx_device:latest',
    dcmd='python -m dx_emulation.image',
    environment={
        'MY_IP': '10.0.3.16',
        'CLOUD_HOST': '10.0.1.1',
        'CLOUD_PORT': 8883,
        'START_TIME': 106,
        'RUN_INTERVAL': 1,
        'RUN_COUNT': 50,
        'EMULATION_MODE': 'dev',
        'LOG_FILE': '/data/log/d15' + runtime_id + '.log'
    },
    volumes=['/home/hujuntao/log/device:/data/log'],
    cpu_quota=100000,
    mem_limit='128m')
net.addLink(d15, s4, cls=mininet.link.TCLink, delay="1ms", bw=10)

net.start()
net.ping([c0, f0, f1, f2, f3, d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15])
client = docker.from_env().api
while True:
    device_count = 0
    for c in client.containers():
        if 'dx_device' in c['Image']:
            device_count += 1
    if device_count == 0:
        break
    else:
        time.sleep(60)
# mininet.cli.CLI(net)
net.stop()
