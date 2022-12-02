Feature: Log into the Westfield Application and Creation of a new Lead

  Scenario Outline: Log into the SIT landing page with Single parameter
  	Given launch chrome browser
    When open the Salesforce login page <Url>
    And enter username <Username> and password <Password>
    And click on Login button
    Then verify the landing page

    Examples: 
      | Username                        | Password                          | Url                                                     |
      | senthilkumar.k@tavant.com.sitdm | welcomewelcomewelcomewelcome2022@ | https://westfield--sit.sandbox.my.salesforce.com/?login |
      
      

