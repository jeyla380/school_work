/*Javascript*/
var markers = [];
markers[0];
markers[1];
var players = [];
players[0];
players[1];
var totals = [];
var winCodes = [7, 56, 73, 84, 146, 273, 292, 448];
var gameOver;
var whoseTurn = 0;

function restartGame()
{
	submitPlayer();
}

function submitPlayer()
{
	//reset the board
	var counter = 1;
	var board = document.getElementById("game-board");
	var innerDivs = "";
	for(i=1; i <=3; i++)
	{
		innerDivs += '<div id="row-' + i + '">';
		for (j=1; j <=3; j++)
		{
			innerDivs +='<div onclick="playGame(this, ' + counter + ');"></div>';
			counter *= 2;
		}
		innerDivs += '</div>';
	}
	board.innerHTML = innerDivs;
	
	//choose the players
	players[0] = document.getElementById("player1").value;
	players[1] = document.getElementById("player2").value;
	
	document.getElementById("game-message").innerHTML = "It's " + players[whoseTurn] + "'s Turn";
	totals = [0, 0];
	gameOver = false;
}

function playGame(clickedDiv, divValue)
{
	if (!gameOver)
	{
		//add x or o to playing field
		clickedDiv.innerHTML = markers[whoseTurn];
		
		//increment players' total count for possible win
		totals[whoseTurn] += divValue;
		
		//call isWin() function
		if(isWin())
		{
			document.getElementById("game-message").innerText =  players[whoseTurn] + " Wins!";
		}
		else if(gameOver)
		{
			document.getElementById("game-message").innerText =  "No winner...";
		}
		else
		{
			//toggle player turn
			if (whoseTurn == 1)
			{
				whoseTurn = 0;
			}
			else
			{
				whoseTurn = 1;
			}
			//prevent clicking on same div again
			clickedDiv.attributes["0"].nodeValue = "";
			
			//toggle message to display next player
			document.getElementById("game-message").innerText = "It's " + players[whoseTurn] + "'s Turn";
		}
	}
}

function chooseKen()
{
	if(document.getElementById("ken"))
	{
		markers = new Array("<img src='img/ken.gif'>", "<img src='img/ryu.gif'>");
		document.getElementById("chosen").innerHTML = "Ken is your player";
	}
}

function chooseRyu()
{
	if(document.getElementById("ryu"))
	{
		markers = new Array("<img src='img/ryu.gif'>", "<img src='img/chun-li.gif'>");
		document.getElementById("chosen").innerHTML = "Ryu is your player";
	}
}

function chooseChunLi()
{
	if(document.getElementById("chun-li"))
	{
		markers = new Array("<img src='img/chun-li.gif'>", "<img src='img/zangief.gif'>");
		document.getElementById("chosen").innerHTML = "Chun Li is your player";
	}
}

function chooseIbuki()
{
	if(document.getElementById("ibuki"))
	{
		markers = new Array("<img src='img/ibuki.gif'>", "<img src='img/ryu.gif'>");
		document.getElementById("chosen").innerHTML = "Ibuki is your player";
	}
}

function chooseSakura()
{
	if(document.getElementById("sakura"))
	{
		markers = new Array("<img src='img/sakura.gif'>", "<img src='img/ken.gif'>");
		document.getElementById("chosen").innerHTML = "Sakura is your player";
	}
}

function chooseZangief()
{
	if(document.getElementById("zangief"))
	{
		markers = new Array("<img src='img/zangief.gif'>", "<img src='img/sakura.gif'>");
		document.getElementById("chosen").innerHTML = "Zangief is your player";
	}
}

//win code logic
function isWin()
{
	for (i=0; i < winCodes.length; i++)
	{
		if((totals[whoseTurn] & winCodes[i]) == winCodes[i])
		{
			gameOver = true;
			return true;
		}
	}
	if(totals[0] + totals[1] == 511)
		{
			gameOver = true;
		}
		return false;
}