Feature: Create a new Lead 

	Scenario: Create a new Lead and convert into an account and contact
		
		Given Create a new lead 
		When Click on the Lead navigation menu 
		And Click on the New button
		And Fill all the required fields on the new lead form 
		And Click on the Save button
		Then Verify the lead that converted into account and contact
		
		
		
		
		
		