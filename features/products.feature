# features/products.feature
Feature: Product management

  Scenario: Read a product
    Given the following products
      | name  | category | available | price |
      | apple | fruit    | True      | 1.00  |
    When I request the product with id 1
    Then the response should be 200

  Scenario: Update a product
    Given the following products
      | name  | category | available | price |
      | apple | fruit    | True      | 1.00  |
    When I update the product with id 1 with the name "orange"
    Then the response should be 200

  Scenario: Delete a product
    Given the following products
      | name  | category | available | price |
      | apple | fruit    | True      | 1.00  |
    When I delete the product with id 1
    Then the response should be 204

  Scenario: List all products
    Given the following products
      | name  | category | available | price |
      | apple | fruit    | True      | 1.00  |
    When I request all products
    Then the response should be 200

  Scenario: Search by name
    Given the following products
      | name  | category | available | price |
      | apple | fruit    | True      | 1.00  |
    When I search for products with name "apple"
    Then the response should be 200

  Scenario: Search by category
    Given the following products
      | name  | category | available | price |
      | apple | fruit    | True      | 1.00  |
    When I search for products with category "fruit"
    Then the response should be 200

  Scenario: Search by availability
    Given the following products
      | name  | category | available | price |
      | apple | fruit    | True      | 1.00  |
    When I search for products with availability "True"
    Then the response should be 200