"""
List of the common Cisco IOS commands

"""
type = {
    'ios' : 'cisco_ios',
}
commands = {
    'uptime'    : "show version | include uptime",
    'version'   : "show version",
    'log'       : "show logging",
    'vc_status' : "show mpls l2transport vc ",
    'interfaces' : "show interface description"
}
