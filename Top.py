#! /usr/bin/python


from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():

    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch)

    c1 = net.addController('c1', controller=RemoteController, ip="127.0.0.1", port=6633)

    h1 = net.addHost( 'h1', ip='10.0.0.1' )
    h2 = net.addHost( 'h2', ip='10.0.0.2' )
#    h3 = net.addHost( 'h3', ip='10.0.0.3')
#    h4 = net.addHost( 'h4', ip='10.0.0.4')
#    h5 = net.addHost( 'h5', ip='10.0.0.5')
#    h6 = net.addHost( 'h6', ip='10.0.0.6')


    s1 = net.addSwitch( 's1' )
#    s2 = net.addSwitch( 's2' )
#    s3 = net.addSwitch( 's3' )

    s1.linkTo( h1 )
    s1.linkTo( h2 )
#    s2.linkTo( h3 )
#    s2.linkTo( h4 )
#    s3.linkTo( h5 )
#    s3.linkTo( h6 )

    net.build()
    c1.start()
    s1.start([c1])
#    s2.start([c1])
#    s3.start([c1])

    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()




