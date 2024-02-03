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
