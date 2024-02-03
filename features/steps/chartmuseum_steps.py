from behave import *
from common.helm import install_helm_chart, \
    uninstall_helm_chart, \
    helm_chart_is_installed, \
    helm_release_status_is_deployed, \
    is_helm_chart_installed
from common.chartmuseum import is_chartmuseum_empty, \
    upload_helm_chart_into_chartmuseum, \
    check_if_helm_chart_exists_in_chartmuseum, \
    get_specific_version_of_a_helm_chart_in_chartmuseum, \
    delete_specific_version_of_a_helm_chart_from_chartmuseum
from environment import HELM_RELEASE_NAME, \
    HELM_REPOSITORY, \
    HELM_CHART_VERSION, \
    CHARTMUSEUM_BASE_URL, \
    TEST_HELM_CHART_FILENAME, \
    TEST_HELM_CHART_NAME, \
    TEST_HELM_CHART_VERSION

@given('chartmuseum is not installed')
def step_impl(context):
    result = helm_chart_is_installed(context, HELM_RELEASE_NAME)
    assert result

@when('chartmuseum is installed')
def step_impl(context):
    is_installed = is_helm_chart_installed(
        context,
        HELM_RELEASE_NAME
    )

    # No proper response from the cluster, fail.
    if is_installed == None:
        assert False

    # Helm chart is not installed, try to install it.
    if not is_installed:
        result = install_helm_chart(
            context,
            HELM_RELEASE_NAME,
            HELM_REPOSITORY,
            HELM_CHART_VERSION
        )

        if not result:
            context.log.error('could not install chartmuseum helm chart')
            assert False

        assert True

    assert True

@then('chartmuseum installation is valid')
def step_impl(context):
    result = helm_release_status_is_deployed(
        context,
        HELM_RELEASE_NAME
    )

    assert result

@given('chartmuseum is installed')
def step_impl(context):
    is_installed = is_helm_chart_installed(
        context,
        HELM_RELEASE_NAME
    )

    # No proper response from the cluster, fail.
    if is_installed == None:
        assert False

    # Helm chart is not installed, try to install it.
    if not is_installed:
        result = install_helm_chart(
            context,
            HELM_RELEASE_NAME,
            HELM_REPOSITORY,
            HELM_CHART_VERSION
        )

        # Helm chart is not installed, fail.
        if not result:
            context.log.error('could not install chartmuseum helm chart')
            assert False

        # Helm chart is installed, success.
        assert True

    # Helm chart is installed, success.
    assert True

@when('chartmuseum is uninstalled')
def step_impl(context):
    result = uninstall_helm_chart(context, HELM_RELEASE_NAME)
    assert result

@then('chartmuseum uninstallation is valid')
def step_impl(context):
    is_installed = is_helm_chart_installed(
        context,
        HELM_RELEASE_NAME
    )

    # No proper response from the cluster, fail.
    if is_installed == None:
        assert False

    # Helm chart is still installed, fail.
    if is_installed:
        assert False

    # Helm chart is not installed, success.
    assert True

@when('chartmuseum does not have any helm charts')
def step_impl(context):
    is_empty = is_chartmuseum_empty(context, CHARTMUSEUM_BASE_URL)

    # No proper response from the chartmuseum, fail.
    if is_empty == None:
        assert False

    # There is already helm chart in the chartmuseum.
    if not is_empty:
        assert False

    # The chartmuseum was empty, as expected.
    assert True

@then('upload helm chart test into chartmuseum')
def step_impl(context):
    upload_success = upload_helm_chart_into_chartmuseum(
        context,
        CHARTMUSEUM_BASE_URL,
        TEST_HELM_CHART_FILENAME
    )

    # No proper response from the chartmuseum, fail.
    if upload_success == None:
        assert False

    # There is already helm chart in the chartmuseum.
    if not upload_success:
        assert False

    # The chartmuseum was empty, as expected.
    assert True

@when('helm chart test is in chartmuseum')
def step_impl(context):
    helm_chart_exists = check_if_helm_chart_exists_in_chartmuseum(
        context,
        CHARTMUSEUM_BASE_URL,
        TEST_HELM_CHART_NAME
    )

    # No proper response from the chartmuseum, fail.
    if helm_chart_exists == None:
        assert False

    # Helm chart test is not in the chartmuseum.
    if not helm_chart_exists:
        assert False

    # Helm chart test is in the chartmuseum, as expected.
    assert True

@then('list specific version of the helm chart test from the chartmuseum')
def step_impl(context):
    version_exists = get_specific_version_of_a_helm_chart_in_chartmuseum(
        context,
        CHARTMUSEUM_BASE_URL,
        TEST_HELM_CHART_NAME,
        TEST_HELM_CHART_VERSION
    )

    # No proper response from the chartmuseum, fail.
    if version_exists == None:
        assert False

    # Specific version of the Helm chart test is not in the chartmuseum.
    if not version_exists:
        assert False

    # Specific version of the Helm chart test is in the chartmuseum, as expected.
    assert True


@then('delete helm chart test from chartmuseum')
def step_impl(context):
    delete_success = delete_specific_version_of_a_helm_chart_from_chartmuseum(
        context,
        CHARTMUSEUM_BASE_URL,
        TEST_HELM_CHART_NAME,
        TEST_HELM_CHART_VERSION  
    )

    # No proper response from the chartmuseum, fail.
    if delete_success == None:
        assert False

    # Specific version of the Helm chart test was not deleted from the chartmuseum.
    if not delete_success:
        assert False

    # Specific version of the Helm chart test was deleted from the chartmuseum, as expected.
    assert True
