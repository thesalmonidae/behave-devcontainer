# Behave Devcontainer

This is an example devcontainer for Behave library which is written with Python and used for Behavior Driven Development (BDD). It contains all the necessary Python dependencies, but also Kubectl, Helm and K9s for Kubernetes. It is assumed that Docker Desktop Kubernetes is used with WSL2 backend. There are VSCode extensions for Python and Cucumber in the devcontainer.

## Target of the Testing

The Chartmuseum is an opensource Helm chart repository ([https://chartmuseum.com/](https://chartmuseum.com/)). In this example we deploy the Chartmuseum into the Kubernetes, and then run Behave tests against it, to verify that the deployment is functioning as expected.

## Behave

The Behave is a Python library for testing ([https://github.com/behave/behave](https://github.com/behave/behave)).

## Cucumber

The Cucumber uses Gherkin language for defining the BDD testing workflow ([https://cucumber.io/](https://cucumber.io/)).

## Run Tests

### Features

There exists one feature file with five different scenarios in which the functionality of the Chartmuseum is tested.

```gherkin
Feature: Chartmuseum
   Scenario: Install
      Given chartmuseum is not installed
      When chartmuseum is installed
      Then chartmuseum installation is valid
   Scenario: API upload
      Given chartmuseum is installed
      When chartmuseum does not have any helm charts
      Then upload helm chart test into chartmuseum
   Scenario: API list
      Given chartmuseum is installed
      When helm chart test is in chartmuseum
      Then list specific version of the helm chart test from the chartmuseum
   Scenario: API delete
      Given chartmuseum is installed
      When helm chart test is in chartmuseum
      Then delete helm chart test from chartmuseum
   Scenario: Uninstall
      Given chartmuseum is installed
      When chartmuseum is uninstalled
      Then chartmuseum uninstallation is valid

```

The Makefile includes two make targets, one for initializing the test and then second for running the test.

### Init

The `features/init` make target adds the Chartmuseum Helm repository in the local Helm, and then builds the Helm chart test Helm chart for the tests.

```
make features/init
```

```
[dev@9e6f7bd47f6d behave-devcontainer]$ make features/init
"chartmuseum" already exists with the same configuration, skipping
Successfully packaged chart and saved it to: /workspaces/behave-devcontainer/test-0.1.0.tgz
```

### Run

The `features/run` make target executes the tests.

```
make features/run
```

```
[dev@9e6f7bd47f6d behave-devcontainer]$ make features/run
Feature: Chartmuseum # features/chartmuseum.feature:1

  Scenario: Install                        # features/chartmuseum.feature:2
    Given chartmuseum is not installed     # features/steps/chartmuseum_steps.py:20 0.071s
    When chartmuseum is installed          # features/steps/chartmuseum_steps.py:25 13.062s
    Then chartmuseum installation is valid # features/steps/chartmuseum_steps.py:53 0.070s

  Scenario: API upload                             # features/chartmuseum.feature:6
    Given chartmuseum is installed                 # features/steps/chartmuseum_steps.py:62 0.071s
    When chartmuseum does not have any helm charts # features/steps/chartmuseum_steps.py:116 0.009s
    Then upload helm chart test into chartmuseum   # features/steps/chartmuseum_steps.py:131 0.011s

  Scenario: API list                                                       # features/chartmuseum.feature:10
    Given chartmuseum is installed                                         # features/steps/chartmuseum_steps.py:62 0.072s
    When helm chart test is in chartmuseum                                 # features/steps/chartmuseum_steps.py:150 0.009s
    Then list specific version of the helm chart test from the chartmuseum # features/steps/chartmuseum_steps.py:169 0.013s

  Scenario: API delete                           # features/chartmuseum.feature:14
    Given chartmuseum is installed               # features/steps/chartmuseum_steps.py:62 0.071s
    When helm chart test is in chartmuseum       # features/steps/chartmuseum_steps.py:150 0.010s
    Then delete helm chart test from chartmuseum # features/steps/chartmuseum_steps.py:190 0.014s

  Scenario: Uninstall                        # features/chartmuseum.feature:18
    Given chartmuseum is installed           # features/steps/chartmuseum_steps.py:62 0.076s
    When chartmuseum is uninstalled          # features/steps/chartmuseum_steps.py:93 0.181s
    Then chartmuseum uninstallation is valid # features/steps/chartmuseum_steps.py:98 0.082s

1 feature passed, 0 failed, 0 skipped
5 scenarios passed, 0 failed, 0 skipped
15 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m13.821s
```
