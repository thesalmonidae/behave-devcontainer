import logging

LOG_FORMAT = '%(asctime)s %(message)s'

HELM_RELEASE_NAME = 'test-chartmuseum'
HELM_REPOSITORY = 'chartmuseum/chartmuseum'
HELM_CHART_VERSION = '3.10.2'
CHARTMUSEUM_BASE_URL = 'kubernetes.docker.internal:8080'
TEST_HELM_CHART_FILENAME = 'test-0.1.0.tgz'
TEST_HELM_CHART_NAME = 'test'
TEST_HELM_CHART_VERSION = '0.1.0'

def before_all(context):
    context.config.logging_format = LOG_FORMAT
    context.log = logging.getLogger()
