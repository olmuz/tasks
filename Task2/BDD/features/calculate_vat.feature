Feature: Task2

Scenario: Calculate
	Given form that uses method from task1
	When Fill text form:
		| name          | value   |
		| fill_sum      | 125     |
		| fill_percent  | 23      |
		| fill_boolen   | True    |
	When user press 'Calculate' button
	Then new form appeared below with return values