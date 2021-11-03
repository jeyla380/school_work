var choose;

while (choose !== "1" && choose !== "2") //while loops can't take || but can take && as an 'or' statement instead
{
	choose = prompt("Enter '1' for the first story and '2' for the second story"); 
	
	if(choose == "1")
	{
		alert("Story One");
		
		var noun1 = prompt("Input a Noun (a person, place, or thing)");
		var name1 = prompt("Input a Name");
		var adj1 = prompt("Input an Adjective (describes a noun)");
		var noun2 = prompt("Input a Noun (a person, place, or thing)");
		var name2 = prompt("Input a Name");
		var adj2 = prompt("Input an Adjective (describes a noun)");
		var verb1 = prompt("Input a Past Verb (something you did)");
		var noun3 = prompt("Input a Noun (a person, place, or thing)");
		var name3 = prompt("Input a Name");
		var verb2 = prompt("Input a Past Verb (something you did)");
		var adv1 = prompt("Input an Adverb without -ly (describes a verb)");
		var verb3 = prompt("Input a Past Verb (something you did)");
		var noun4 = prompt("Input a Noun (a person, place, or thing)");
		var noun5 = prompt("Input a Noun (a person, place, or thing)");
		var cityname1 = prompt("Input a City Name");
		
		var paragraph1 = "Once, in a[n] " + noun1 + " on " + name1 + " street, there lived a[n] " + adj1 + " " + noun2 + " named " + name2 + ". The " + noun2 + " was very " + adj2 + " with themselves, and for good reason: they were " + verb1 + " by a " + noun3 + " named " + name3 + ", who " + verb2 + " them with " + adv1 + " care and " + verb3 + " them completely; but one day, " + name2 + " was lost. From the depths of the " + noun4 + " to the " + noun5 + " of " + cityname1 + "; this is the story of how " + name2 + ", the " + noun2 + " makes their way back home." 
		
		function storyOne()
		{
			document.getElementById("story-one").innerHTML = paragraph1;
		}
	}
	
	else if(choose == "2")
	{
		alert("Story Two")

		var tname1 = prompt("Input a Name");
		var tnoun1 = prompt("Input a Noun (a person, place, or thing)");
		var tverb1 = prompt("Input a Verb with -ing (something you are doing)");
		var tnoun2 = prompt("Input a Noun (a person, place, or thing)");
		var tadj1 = prompt("Input an Adjective (describes a noun)");
		var tadj2 = prompt("Input an Adjective (describes a noun)");
		var tnoun3 = prompt("Input a Noun (a person, place, or thing)");
		var tnoun4 = prompt("Input a Noun (a person, place, or thing)");
		var tverb2 = prompt("Input a Past Verb (something you did)");
		var tpluralnoun1 = prompt("Input a Plural Noun (multiple people, places, or things)");
		var tverb3 = prompt("Input a Verb (something you do)");
		var tverb4 = prompt("Input a Verb (something you do)");
		
		var paragraph2 = tname1 + " had been a[n] " + tnoun1 + " for ten years, and they had never questioned the joy of (a[n]) " + tverb1 + " " + tnoun2 + " being consumed by " + tadj1 + " flames, never questioned anything until they met a[n] " + tadj2 + " " + tnoun3 + " who told them of the past. " + tname1 + " met a " + tnoun4 + " who " + tverb2 + " them of a future where " + tpluralnoun1 + " could think on their own; and " + tname1 + " realized what he had to do. They had to " + tverb3 + " everything they knew and " +  tverb4 + " humanity."
		
		function storyTwo()
		{
			document.getElementById("story-two").innerHTML = paragraph2;
		}

	}
	
	else
	{
		alert("This story doesn't exist, please input '1' for the first story and '2' for the second story")
	}
}
