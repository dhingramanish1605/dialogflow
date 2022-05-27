Feature: Login Feature
  Scenario Outline: Validating the create intent functionality
    Given Navigate to Create a intent
    When Enter details "<intent_name>"
    Then Validate message "<message>"
    Examples:
    |intent_name      |message|
    |intent A         |com.google.apps.framework.request.BadRequestException: Intent with the display name 'intent A' already exists.    |
    |intent Y         |Intent saved|
    |intent D         |com.google.apps.framework.request.BadRequestException: Intent with the display name 'intent D' already exists.    |
    |intent Z         |Intent saved|


