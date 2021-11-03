/*Javascript*/
var num;
var attempts = 0;
var maxAttempts = 10;
var userGuess = [];

function resetGame()
{
	document.getElementById("play-again").className = "hide";
	document.getElementById("submit-guess").className = "show";
	document.getElementById("game-image").src = "img/sailormoon/main.jpg";
	document.getElementById("game-message").innerText = "Let's Get Started! You have 10 guesses.";
	num = Math.ceil(Math.random() * 99);
	document.getElementById("user-input").value = "";
	maxAttempts = 10;
	document.getElementById("num-guess").innerHTML = "";
	empty();
}


function playGame()
{
	maxAttempts--;
	if(attempts > maxAttempts)
	{
		changeDisplay("lose", "You lose....");
	}
	else
	{
		var user = document.getElementById("user-input").value;
		
		if (user > num) //do high stuff
		{
			changeDisplay("high", "The number is too high! You have " + maxAttempts + " guess(es) left.");
		}
		else if(user < num) //do low stuff
		{
			changeDisplay("low", "The number is too low! You have " + maxAttempts + " guess(es) left");
		}
		else if(user == num) //do win stuff
		{
			if(maxAttempts == 9)
			{
				changeDisplay("firstwin", "You won on the first try!");
			}
			else
			{
				changeDisplay("win", "You win! You had " + maxAttempts + " guess(es) left");
			}
		}
		else //do error stuff
		{
			changeDisplay("error", "Error: That's not a number! You have " + maxAttempts + " guess(es) left");
		}
		userGuess.push(user);
		document.getElementById("num-guess").innerHTML = userGuess.join(' \u2665 ');
		
		document.getElementById("user-input").select();
	}
}

function changeDisplay(status, message)
{
	var image;
	
	switch(status)
	{
		case "high":
			image = "img/sailormoon/high.jpg"
			break;
		case "low":
			image = "img/sailormoon/low.jpg"
			break;
		case "win": 
			image = "img/sailormoon/win.png"
			document.getElementById("play-again").className = "show";
			document.getElementById("submit-guess").className = "hide";
			break;
		case "firstwin":
			image = "img/sailormoon/firstwin.jpg"
			document.getElementById("play-again").className = "show";
			document.getElementById("submit-guess").className = "hide";
			break;
		case "lose":
			image = "img/sailormoon/lose.jpg"
			document.getElementById("play-again").className = "show";
			document.getElementById("submit-guess").className = "hide";
			break;
		default:
			image = "img/sailormoon/error.jpg"
	}
	
	document.getElementById("game-message").innerText = message;
	document.getElementById("game-image").src = image;
}

function empty()
{
	userGuess = [];
}

function playAudio()
{
	var x = document.getElementById("music");
	x.play();
}
