Feature: combine number

  Scenario Outline: combine number
    Given I have a list of positive integers <list>
    When the list is sorted from largest to smallest <sort>
    And the sorted list is converted to a string <s>
    Then I should convert the string to a integer <i>


    Examples: combine number
      | list         | sort         | s       | i       |
      | [20,1,43,2]  | [43,20,2,1]  | 432021  | 432021  |
      | [4,3,5,4]    | [5,4,4,3]    | 5443    | 5443    |
      | [432,4,6,43] | [432,43,6,4] | 4324364 | 4324364 |
