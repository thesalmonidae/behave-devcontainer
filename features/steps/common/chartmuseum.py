from subprocess import Popen, PIPE
from json import loads

def is_chartmuseum_empty(context, chartmuseum_base_url):
    cmd = f'curl {chartmuseum_base_url}/api/charts'
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
    is_empty = False
    if len(json_stdout.keys()) == 0:
        is_empty = True
    return is_empty

def upload_helm_chart_into_chartmuseum(
        context,
        chartmuseum_base_url,
        helm_chart_filename
):
    cmd = f'curl -X POST --data-binary "@{helm_chart_filename}" {chartmuseum_base_url}/api/charts'
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
    upload_success = False
    if 'saved' in json_stdout.keys():
        if json_stdout['saved']:
            upload_success = True
    return upload_success

def check_if_helm_chart_exists_in_chartmuseum(
        context,
        chartmuseum_base_url,
        helm_chart_name        
):
    cmd = f'curl --head {chartmuseum_base_url}/api/charts/{helm_chart_name}'
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
    helm_chart_exists = False
    if 'HTTP/1.1 200 OK' in stdout:
        helm_chart_exists = True
    return helm_chart_exists

def get_specific_version_of_a_helm_chart_in_chartmuseum(
        context,
        chartmuseum_base_url,
        helm_chart_name,
        helm_chart_version
):
    cmd = f'curl {chartmuseum_base_url}/api/charts/{helm_chart_name}/{helm_chart_version}'
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
    version_exists = False
    if all(key in json_stdout.keys() for key in ('name', 'version')):
        if json_stdout['name'] == helm_chart_name \
            and json_stdout['version'] == helm_chart_version:
            version_exists = True
    return version_exists

def delete_specific_version_of_a_helm_chart_from_chartmuseum(
        context,
        chartmuseum_base_url,
        helm_chart_name,
        helm_chart_version
):
    cmd = f'curl -X DELETE {chartmuseum_base_url}/api/charts/{helm_chart_name}/{helm_chart_version}'
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
    delete_success = False
    if 'deleted' in json_stdout.keys():
        if json_stdout['deleted']:
            delete_success = True
    return delete_success
