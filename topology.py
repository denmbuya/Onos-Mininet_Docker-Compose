from mininet.node import CPULimitedHost
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.cli import CLI


class SimplePktSwitch(Topo):
    """Simple topology example."""

    def __init__(self, **opts):
        """Create custom topo."""

        # Initialize topology
        super(SimplePktSwitch, self).__init__(**opts)

        # Add hosts and switches
        h1 = self.addHost('h1', ip='10.10.1.1')
        h2 = self.addHost('h2', ip='10.10.2.1')
        h3 = self.addHost('h3', ip='10.10.3.1')
        h4 = self.addHost('h4', ip='10.10.4.1')
        h5 = self.addHost('h5', ip='10.10.5.1')
        h6 = self.addHost('h6', ip='10.10.6.1')
        h7 = self.addHost('h7', ip='10.10.7.1')
        h8 = self.addHost('h8', ip='10.10.8.1')
        h9 = self.addHost('h9', ip='10.10.9.1')
        h0 = self.addHost('h0', ip='10.10.10.1')

        # Adding switches
        s1 = self.addSwitch('s1', dpid="0000000000000001", protocols='OpenFlow13')
        s2 = self.addSwitch('s2', dpid="0000000000000002", protocols='OpenFlow13')
        s3 = self.addSwitch('s3', dpid="0000000000000003", protocols='OpenFlow13')
        s4 = self.addSwitch('s4', dpid="0000000000000004", protocols='OpenFlow13')
        s5 = self.addSwitch('s5', dpid="0000000000000005", protocols='OpenFlow13')
        s6 = self.addSwitch('s6', dpid="0000000000000006", protocols='OpenFlow13')
        s7 = self.addSwitch('s7', dpid="0000000000000007", protocols='OpenFlow13')
        s8 = self.addSwitch('s8', dpid="0000000000000008", protocols='OpenFlow13')
        s9 = self.addSwitch('s9', dpid="0000000000000009", protocols='OpenFlow13')
        s0 = self.addSwitch('s0', dpid="0000000000000010", protocols='OpenFlow13')

        # Add links
        self.addLink(h1, s2)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s4)
        self.addLink(h5, s5)
        self.addLink(h6, s5)
        self.addLink(h7, s7)
        self.addLink(h8, s8)
        self.addLink(h9, s9)
        self.addLink(h0, s0)

        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s1, s4)
        self.addLink(s4, s5)
        self.addLink(s4, s6)
        self.addLink(s3, s5)
        self.addLink(s5, s7)
        self.addLink(s6, s7)
        self.addLink(s5, s8)
        self.addLink(s7, s0)
        self.addLink(s8, s9)
        self.addLink(s9, s0)


def run():
    # Set up a remote controller with the correct IP
    c = RemoteController('c', '10.5.0.2')
    
    # Create a Mininet instance with the custom topology and no controller (adding it later)
    net = Mininet(topo=SimplePktSwitch(), host=CPULimitedHost, controller=None)
    
    # Add the remote controller to the network
    net.addController(c)
    
    # Start the network
    net.start()
    
    # Drop the user into the CLI
    CLI(net)
    
    # Stop the network after exiting the CLI
    net.stop()


# Entry point for the script
if __name__ == '__main__':
    setLogLevel('info')
    run()
