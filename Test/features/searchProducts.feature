Feature: Search Results
  As a user
  I want to search a product
  So can check to the title of the product related

  Scenario Outline: Check product title
    Given the search is in the header
    When complete "<product>"
    And press the search button
    Then can check the product "<title>"

    Examples: Products Name
      | product  | title                                                                            |
      | french   | New French With Ease (1 book + 1 mp3 CD)                                         |
      | morning  | The Miracle Morning: The Not-So-Obvious Secret Guaranteed to Transform Your Life |
      | baseball | Casual 3/4 Sleeve Baseball T-Shirt                                               |
      | stiletto | Womens high heel point toe stiletto sandals ankle strap court shoes              |