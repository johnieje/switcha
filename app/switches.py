"""
Switch class:
Attributes: Name, Type, IP-address

Author: John Murungi
"""
from netmiko import ConnectHandler
from app.commands import commands, type
from app.cisco_devices import user

class Switch:
    """docstring for Switch."""

    def __init__(self, ip_address):
        super(Switch, self).__init__()
        self.ip_address = ip_address

    def connection(self, ip_address):
        #Establish SSH connection to the switch
        con = ConnectHandler(
            device_type=type['ios'],
            ip=ip_address,
            username=user['username'],
            password=user['password']
        )
        #Try/Except block to catch any errors: otherwise return connection
        try:
            return con
        except Exception as e:
            raise ("Error: Connection failed!")

    def close_connection(self, connection):
        #Close SSH conenction
        return connection.disconnect()

    def uptime(self, connection):
        #show version | i uptime command
        uptime = connection.send_command(commands['uptime'])

        #Try/Except to catch errors - return switch uptime
        try:
            return uptime
        except Exception as e:
            raise ("Error: Command Failed!")

    def log(self, connection):
        #show logging
        log = connection.send_command(commands['log'])
        return log

    def vc_status(self, connection, vlan):
        #show pseudowire status
        vc_status = connection.send_command(commands['vc_status'] + vlan)
        return vc_status

    def interfaces(self, connection):
        interfaces = connection.send_command(commands['interfaces'])
        return interfaces




#statistics = Switch("41.222.1.105")
#nakawa =  Switch("41.222.1.106")

#print(Switch.uptime(Switch.connection(nakawa.ip_address)))
#print(Switch.log(Switch.connection(nakawa.ip_address)))
#print(Switch.uptime(nakawa.ip_address))
#Close SSH connection
