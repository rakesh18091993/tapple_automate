import subprocess


def pingOk(Host):
    try:
        output = subprocess.check_output(
            "ping -t 1 -c 1 {}".format(Host), shell=True)
    except Exception as e:
        return False

    return True


with open('raw.txt', 'r') as raw, open('pingable.txt', 'w') as pingable, open('not_pingable.txt', 'w') as not_pingable:
    hosts = raw.readlines()
    for host in hosts:
        if pingOk(host):
            pingable.write(host)
        else:
            not_pingable.write(host)
