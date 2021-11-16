package LabCountry;

public class Country
{
	// fields
	private final String name;
	private final Continent continent;
	private final int num = 4;

	public Country(String n, Continent c) {

		// constructor
		name = n;
		continent = c;
	}

	
	// methods
	public String getName(){

		return name;
	}

	public Continent getContinent(){

		return continent;
	}

	
	@Override
	public String toString()
	{
		return String.format("%s (%s), %d ", name, continent, num);
	}
}