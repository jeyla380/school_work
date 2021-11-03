/*Javascript*/

var numbers = [];
var lotteryNumbers = "";

function submitInfo()
{
	var lotteryQuestion = document.getElementById("lottery-question").value;
	
	if (lotteryQuestion < 9)
	{
		if(lotteryQuestion == "")
		{
			alert("Space cannot be blank, please enter a number less than 9");
		}
		else
		{
			document.getElementById("button").disabled = true;
			
			//creates numbers arrays, fills with numbers
			for(var i = 0; i < lotteryQuestion; i++)
			{
				numbers[i] = Math.ceil(Math.random() * 99);
			}
			
			//displays numbers array
			for(var i = 0; i < numbers.length; i++)
			{
				if(i == numbers.length - 1)
				{
					(lotteryNumbers += numbers[i]);
				}
				
				else
				{
					(lotteryNumbers += numbers[i] + " - ");
				}	
				document.getElementById("lottery-num1").innerHTML = lotteryNumbers;
			}
		}
	}
	else
	{
		alert("The number is too high, please input a number less than 9");
	}
	
}

function playAudio()
{
	var x = document.getElementById("music");
	x.play();
}



