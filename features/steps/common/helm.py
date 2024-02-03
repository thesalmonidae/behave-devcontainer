from subprocess import Popen, PIPE
from json import loads

def is_helm_chart_installed(context, release_name):
    cmd = f'helm ls -o json'
    sp = Popen(
        cmd,
        stdout=PIPE,
        stderr=PIPE,
        text=True,
        shell=True
    )
    returncode = sp.wait()
    stdout = sp.stdout.read()
    stderr = sp.stderr.read()
    if returncode != 0:
        context.log.error(f'returncode: {returncode}\nstderr:{stderr}')
        return None
    json_stdout = loads(stdout)
    is_installed = False
    for element in json_stdout:
        if element['name'] == release_name:
            is_installed = True
    return is_installed

def helm_release_status_is_deployed(context, release_name):
    cmd = f'helm history {release_name} -o json'
    sp = Popen(
        cmd,
        stdout=PIPE,
        stderr=PIPE,
        text=True,
        shell=True
    )
    returncode = sp.wait()
    stdout = sp.stdout.read()
    stderr = sp.stderr.read()
    json_stdout = loads(stdout)
    status = json_stdout[-1]['status']
    description = json_stdout[-1]['description']
    if status != 'deployed' or description != 'Install complete':
        context.log.error(f'returncode: {returncode}\nstderr:{stderr}')
        return False
    context.log.info(f'stdout: {stdout}')
    return True

def add_helm_repo(context, name, url):
    cmd = f'helm repo add {name} {url}'
    sp = Popen(
        cmd,
        stdout=PIPE,
        stderr=PIPE,
        text=True,
        shell=True
    )
    returncode = sp.wait()
    stdout = sp.stdout.read()
    stderr = sp.stderr.read()
    if returncode != 0:
        context.log.error(f'returncode: {returncode}\nstderr:{stderr}')
        return False
    context.log.info(f'stdout: {stdout}')
    return True

def install_helm_chart(
        context,
        release_name,
        helm_chart,
        version
    ):
    cmd = f'helm install {release_name} {helm_chart} --version {version} --set service.type="LoadBalancer" --set env.open.DISABLE_API=false --wait'
    sp = Popen(
        cmd,
        stdout=PIPE,
        stderr=PIPE,
        text=True,
        shell=True
    )
    returncode = sp.wait()
    stdout = sp.stdout.read()
    stderr = sp.stderr.read()
    if returncode != 0:
        context.log.error(f'returncode: {returncode}\nstderr:{stderr}')
        return False
    context.log.info(f'stdout: {stdout}')
    return True

def uninstall_helm_chart(
        context,
        release_name
    ):
    cmd = f'helm uninstall {release_name} --wait'
    sp = Popen(
        cmd,
        stdout=PIPE,
        stderr=PIPE,
        text=True,
        shell=True
    )
    returncode = sp.wait()
    stdout = sp.stdout.read()
    stderr = sp.stderr.read()
    if returncode != 0:
        context.log.error(f'returncode: {returncode}\nstderr:{stderr}')
        return False
    context.log.info(f'stdout: {stdout}')
    return True

def helm_chart_is_installed(context, helm_release):
    helm_releases = get_helm_releases(context)
    if helm_releases == None:
        context.log.error(f'could not get helm releases')
        return False
    if helm_release in helm_releases:
        context.log.error(f'helm release {helm_release} already exists')
        return False
    return True

def get_helm_releases(context):
    cmd = 'helm ls -o json'
    sp = Popen(
        cmd,
        stdout=PIPE,
        stderr=PIPE,
        text=True,
        shell=True
    )
    returncode = sp.wait()
    stdout = sp.stdout.read()
    stderr = sp.stderr.read()
    if returncode != 0:
        context.log.error(f'returncode: {returncode}\nstderr:{stderr}')
        return None
    return parse_helm_releases(stdout)

def parse_helm_releases(stdout):
    helm_releases = []
    json_stdout = loads(stdout)
    for element in json_stdout:
        helm_releases.append(element['name'])
    return helm_releases