<!DOCTYPE html>
<?php
    $raceSelect = $_POST['Race'];
    $classSelect = $_POST['Class'];
    $genderSelect = $_POST['gender'];
    $nameSelect = $_POST['HeroName'];
    $ageSelect = $_POST['Age'];
    $kingdomSelect = $_POST['KingdomName'];
?>
<html>
    <head>
        <meta charset="utf-8">
        <title>A made Adventurer</title>
        <!-- Custom fonts for this theme -->
        <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
        <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
        <link href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css">

        <!-- Theme CSS -->

        <link href="../../../css/freelancer.min.css" rel="stylesheet" type="text/css"/>
        <style>
            img {
                height: 250px;
                padding: 3pt;
            }
            p{
                margin-left: 8px;
            }
        </style>
    </head>

    <body>
        <div id="CharacterSheet" class="container">
            <div class="row">
                <h5 class="Content">The Brave Adventurer</h5>
            </div>
            <div class="row">
                 <div class="col-md-3">
                    <?php
                    //print random stats here COMPLETED
                    for($round = 0; $round < 1; $round++)
                    //will go through 1 time
                    {
                        $str = rand(1,20);
                        $con = rand(1,20);
                        $dex = rand(1,20);
                        $wis = rand(1,20);
                        $int = rand(1,20);
                        $cha = rand(1,20);
                        
                        print("<table> <tr><td>Strength:</td><td>$str</td></tr> "
                                . "<tr><td>Constitution: </td><td>$con</td></tr>"
                                . "<tr><td>Dexterity: </td><td>$dex</td></tr>"
                                . "<tr><td>Wisdom: </td><td>$wis</td></tr>"
                                . "<tr><td>Intelligence: </td><td>$int</td></tr>"
                                . "<tr><td>Charisma: </td><td>$cha</td></tr> </table>");
                    }
                    ?>
                </div>
                <div class="col-md-5">
                    <?php
                   //print character info here COMPLETED
                    print("<br><h4>$nameSelect from the Kingdom of $kingdomSelect</h4>");
                    print("<h5>$raceSelect $classSelect at the age of $ageSelect</h5><br>");
                    
                    //descriptions based on race selected
                    switch($raceSelect)
                    {
                        case "Human":
                            print("<h6>Human Race</h6>");
                            print('<p><b>Description</b>: Humans come in a broad variety of shapes and sizes. An 
                                    average Human male in good health stands around six feet tall and weighs about 
                                    175 pounds. Most Humans live around 75 years.</p> <p><b>Restrictions</b>: Humans
                                    may be any single class. They have no minimum or maximum ability score requirements.
                                    </p><p><b> Special Abilities</b>: Humans learn unusually quickly, gaining a bonus 
                                    of 10% to all experience "points earned. Saving Throws: Humans are the ???standard,??? 
                                    and thus have no saving throw bonuses.</p><br>');
                            break;
                        case "Elf":
                            print("<h6>Elf Race</h6>");
                            print("<p><b>Description</b>: Elves are a slender race, with both genders
                                    standing around five feet tall and weighing around 130
                                    pounds. Most have dark hair, with little or no body or
                                    facial hair. Their skin is pale, and they have pointed ears
                                    and delicate features. Elves are lithe and graceful. They
                                    have keen eyesight and hearing. Elves are typically
                                    inquisitive, passionate, self-assured, and sometimes
                                    haughty. Their typical lifespan is a dozen centuries or
                                    more.</p>
                                    <p><b>Restrictions</b>: Elves may become Clerics, Fighters, MagicUsers
                                    or Thieves; they are also allowed to combine the
                                    classes of Fighter and Magic-User, and of Magic-User and
                                    Thief (see Combination Classes, below). They are
                                    required to have a minimum Intelligence of 9. Due to their
                                    generally delicate nature, they may not have a
                                    Constitution higher than 17. Elves never roll larger than
                                    six-sided dice (d6) for hit points.</p>
                                    <p><b>Special Abilities</b>: All Elves have Darkvision with a 60 foot
                                    range. They are able to find secret doors more often than
                                    normal (1-2 on 1d6 rather than the usual 1 on 1d6). An
                                    Elf is so observant that one has a 1 on 1d6 chance to find
                                    a secret door with a cursory look. Elves are immune to
                                    the paralyzing attack of ghouls. Also, they are less likely to
                                    be surprised in combat, reducing the chance of surprise by
                                    1 in 1d6.</p>
                                    <p style='color:#933bad'><b>Saving Throws</b>: Elves save at +1 vs. Paralysis or Petrify,
                                    and +2 vs. Magic Wands and Spells.</p><br>");
                            break;
                        case "Halfling":
                            print("<h6>Halfling Race</h6>");
                            print("<p><b>Description</b>: Halflings are small, slightly stocky folk who
                                    stand around three feet tall and weigh about 60 pounds.
                                    They have curly brown hair on their heads and feet, but
                                    rarely have facial hair. They are usually fair skinned, often
                                    with ruddy cheeks. Halflings are remarkably rugged for
                                    their small size. They are dexterous and nimble, capable
                                    of moving quietly and remaining very still. They usually
                                    go barefoot. Halflings are typically outgoing, unassuming
                                    and good-natured. They live about a hundred years.</p>
                                    <p><b>Restrictions</b>: Halflings may become Clerics, Fighters or
                                    Thieves. They are required to have a minimum Dexterity
                                    of 9. Due to their small stature, they may not have a
                                    Strength higher than 17. Halflings never roll larger than
                                    six-sided dice (d6) for hit points regardless of class.
                                    Halflings may not use Large weapons, and must wield
                                    Medium weapons with both hands.</p>
                                    <p><b>Special Abilities</b>: Halflings are unusually accurate with all
                                    sorts of ranged weapons, gaining a +1 attack bonus when
                                    employing them. When attacked in melee by creatures
                                    larger than man-sized, Halflings gain a +2 bonus to their
                                    Armor Class. Halflings are quick-witted, thus adding +1 to
                                    Initiative die rolls. Outdoors in their preferred forest
                                    terrain, they are able to hide very effectively; so long as
                                    they remain still there is only a 10% chance they will be
                                    detected. Even indoors, in dungeons or in non-preferred
                                    terrain they are able to hide such that there is only a 30%
                                    chance of detection. Note that a Halfling Thief will roll
                                    only once, using either the Thief ability or the Halfling
                                    ability, whichever is better.</p>
                                    <p style='color:#4d5ab8'><b>Saving Throws</b>: Halflings save at +4 vs. Death Ray or
                                    Poison, Magic Wands, Paralysis or Petrify, and Spells, and
                                    at +3 vs. Dragon Breath.</p><br>");
                            break;
                        case "Dwarf":
                            print("<h6>Dwarf Race</h6>");
                            print("<p><b>Description</b>: Dwarves are a short, stocky race; both male
                                    and female Dwarves stand around four feet tall and
                                    typically weigh around 120 pounds. Their long hair and
                                    thick beards are dark brown, gray or black. They take
                                    great pride in their beards, sometimes braiding or forking
                                    them. They have a fair to ruddy complexion. Dwarves
                                    have stout frames and a strong, muscular build. They are
                                    rugged and resilient, with the capacity to endure great
                                    hardships. Dwarves are typically practical, stubborn and
                                    courageous. They can also be introspective, suspicious
                                    and possessive. They have a lifespan of three to four
                                    centuries.</p>
                                    <p><b>Restrictions</b>: Dwarves may become Clerics, Fighters, or
                                    Thieves. They are required to have a minimum
                                    Constitution of 9. Due to their generally dour dispositions,
                                    they may not have a Charisma higher than 17. They may
                                    not employ Large weapons more than four feet in length
                                    (specifically, two-handed swords, polearms, and
                                    longbows).</p>
                                    <p><b>Special Abilities</b>: All Dwarves have Darkvision with a 60'
                                    range, and are able to detect slanting passages, traps,
                                    shifting walls and new construction on a roll of 1-2 on 1d6;
                                    a search must be performed before this roll may be made.</p>
                                    <p style='color:#bf4343'><b>Saving Throws</b>: Dwarves save at +4 vs. Death Ray or
                                    Poison, Magic Wands, Paralysis or Petrify, and Spells, and
                                    at +3 vs. Dragon Breath.</p><br>");
                            break;
                    }
                    
                    //descriptions based on class selected
                    switch($classSelect)
                    {
                        case "Cleric":
                            print("<h6>Cleric Class</h6>");
                            print('<p><b>Description</b>: Clerics are those who have devoted themselves to the
                                    service of a deity, pantheon or other belief system. Most
                                    Clerics spend their time in mundane forms of service such
                                    as preaching and ministering in a temple; but there are
                                    those who are called to go abroad from the temple and
                                    serve their deity in a more direct way, smiting undead
                                    monsters and aiding in the battle against evil and chaos.
                                    Player character Clerics are assumed to be among the
                                    latter group.</p>
                                    <p><b>Fight Style</b>: Clerics fight about as well as Thieves, but not as well as
                                    Fighters. They are hardier than Thieves, at least at lower
                                    levels, as they are accustomed to physical labor that the
                                    Thief would deftly avoid. Clerics can cast spells of divine
                                    nature starting at 2nd level, and they have the power to
                                    Turn the Undead, that is, to drive away undead monsters
                                    by means of faith alone (see the Encounter section for
                                    details).</p>
                                   <p><b>Requirements</b>: The Prime Requisite for a Cleric is Wisdom; a character
                                    must have a Wisdom score of 9 or higher to become a
                                    Cleric. They may wear any armor, but may only use blunt
                                    weapons (specifically including warhammer, mace, maul,
                                    club, quarterstaff, and sling).</p>');
                            break;
                        case "Fighter":
                            print("<h6>Fighter Class</h6>");
                            print('<p><b>Description</b>: Fighters include soldiers, guardsmen, barbarian warriors,
                                    and anyone else for whom fighting is a way of life. They
                                    train in combat, and they generally approach problems
                                    head on, weapon drawn.</p>
                                    <p><b>Fighting Style</b>: Not surprisingly, Fighters are best at fighting of all the
                                    classes. They are also the hardiest, able to take more
                                    punishment than any other class. Although they are not
                                    skilled in the ways of magic, Fighters can nonetheless use
                                    many magic items, including but not limited to magical
                                    weapons and armor.</p>
                                    <p><b>Requirements</b>: The Prime Requisite for Fighters is Strength; a character
                                    must have a Strength score of 9 or higher to become a
                                    Fighter. Members of this class may wear any armor and
                                    use any weapon.</p>');
                            break;
                        case "Magic-User":
                            print("<h6>Magic-User Class</h6>");
                            print("<p><b>Description</b>: Magic-Users are those who seek and use knowledge of the
                                    arcane. They do magic not as the Cleric does, by faith in a
                                    greater power, but rather through insight and
                                    understanding.</p>
                                    <p><b>Fight Style</b>: Magic-Users are the worst of all the classes at fighting;
                                    hours spent studying massive tomes of magic do not lead
                                    a character to become strong or adept with weapons.
                                    They are the least hardy, equal to Thieves at lower levels
                                    but quickly falling behind.</p>
                                    <p><b>Requirements</b>: The Prime Requisite for Magic-Users is Intelligence; a
                                    character must have an Intelligence score of 9 or higher to
                                    become a Magic-User. The only weapons they become
                                    proficient with are the dagger and the walking staff (or
                                    cudgel). Magic-Users may not wear armor of any sort nor
                                    use a shield as such things interfere with spellcasting.</p>");
                            break;
                        case "Thief":
                            print("<h6>Thief Class</h6>");
                            print("<p><b>Description</b>: Thieves are those who take what they want or need by
                                    stealth, disarming traps and picking locks to get to the gold
                                    they crave; or ???borrowing??? money from pockets,
                                    beltpouches, etc. right under the nose of the ???mark???
                                    without the victim ever knowing.</p>
                                    <p><b>Fight Style</b>: Thieves fight better than Magic-Users but not as well as
                                    Fighters. Avoidance of honest work leads Thieves to be
                                    less hardy than the other classes, though they do pull
                                    ahead of the Magic-Users at higher levels.</p>
                                    <p><b>Requirements</b>: The Prime Requisite for Thieves is Dexterity; a character
                                    must have a Dexterity score of 9 or higher to become a
                                    Thief. They may use any weapon, but may not wear
                                    metal armor as it interferes with stealthy activities, nor may
                                    they use shields of any sort. Leather armor is acceptable,
                                    however.</p>");
                            break;
                    }
                    ?>
                </div>
                <div class="col-md-4">
                    <?php
                    //print image here COMPLETED
                    if($raceSelect == "Human")
                    //if statement that determines race
                    {
                        if($classSelect == "Cleric")
                        //nested if statement that determines class
                        {
                            if($genderSelect == "Male")
                            //nested if statement that determines gender
                            {
                                print("<img src='images/HuClMa.jpg'>");
                            }
                            else
                            {
                                print("<img src='images/HuClFe.jpg'>");
                            }
                        }
                        elseif($classSelect == "Fighter")
                        //determines class
                        {
                            if($genderSelect == "Male")
                            //determines gender
                            {
                                print("<img src='images/HuFiMa.jpg'>");
                            }
                            else
                            {
                                print("<img src='images/HuFiFe.jpg'>");
                            }
                        }
                        elseif($classSelect == "Magic-User")
                        //determines class
                        {
                           if($genderSelect == "Male")
                           //determines gender
                            {
                                print("<img src='images/HuMaMa.jpg'>");
                            }
                            else
                            {
                                print("<img src='images/HuMaFe.jpg'>");
                            } 
                        }
                        else
                        //determines class
                        {
                           if($genderSelect == "Male")
                           //determines gender
                            {
                                print("<img src='images/HuThMa.jpg'>");
                            }
                            else
                            {
                                print("<img src='images/HuThFe.jpg'>");
                            }  
                        }
                    }
                    elseif($raceSelect == "Elf")
                    //determines race
                    {
                        if($classSelect == "Cleric")
                        {
                            if($genderSelect == "Male")
                            {
                                print("<img src='images/ElClMa.jpg'>");
                            }
                            else
                            {
                                print("<img src='images/ElClFe.jpg'>");
                            }
                        }
                        elseif($classSelect == "Fighter")
                        {
                            if($genderSelect == "Male")
                            {
                                print("<img src='images/ElFiMa.jpg'>");
                            }
                            else
                            {
                                print("<img src='images/ElFiFe.jpg'>");
                            }
                        }
                        elseif($classSelect == "Magic-User")
                        {
                           if($genderSelect == "Male")
                            {
                                print("<img src='images/ElMaMa.jpg'>");
                            }
                            else
                            {
                                print("<img src='images/ElMaFe.jpg'>");
                            } 
                        }
                        else
                        {
                           if($genderSelect == "Male")
                            {
                                print("<img src='images/ElThMa.jpg'>");
                            }
                            else
                            {
                                print("<img src='images/ElThFe.jpg'>");
                            }  
                        }
                    }
                    elseif($raceSelect == "Halfling")
                    //determines race
                    {
                        if($classSelect == "Cleric")
                        {
                            if($genderSelect == "Male")
                            {
                                print("<img src='images/HaClMa.jpg'>");
                            }
                            else
                            {
                                print("<img src='images/HaClFe.jpg'>");
                            }
                        }
                        elseif($classSelect == "Fighter")
                        {
                            if($genderSelect == "Male")
                            {
                                print("<img src='images/HaFiMa.jpg'>");
                            }
                            else
                            {
                                print("<img src='images/HaFiFe.jpg'>");
                            }
                        }
                        elseif($classSelect == "Magic-User")
                        {
                           if($genderSelect == "Male")
                            {
                                print("<img src='images/HaMaMa.jpg'>");
                            }
                            else
                            {
                                print("<img src='images/HaMaFe.jpg'>");
                            } 
                        }
                        else
                        {
                           if($genderSelect == "Male")
                            {
                                print("<img src='images/HaThMa.jpg'>");
                            }
                            else
                            {
                                print("<img src='images/HaThFe.jpg'>");
                            }  
                        }
                    }
                    else
                    //determines race
                    {
                        if($classSelect == "Cleric")
                        {
                            if($genderSelect == "Male")
                            {
                                print("<img src='images/DwClMa.jpg'>");
                            }
                            else
                            {
                                print("<img src='images/DwClFe.jpg'>");
                            }
                        }
                        elseif($classSelect == "Fighter")
                        {
                            if($genderSelect == "Male")
                            {
                                print("<img src='images/DwFiMa.jpg'>");
                            }
                            else
                            {
                                print("<img src='images/DwFiFe.jpg'>");
                            }
                        }
                        elseif($classSelect == "Magic-User")
                        {
                           if($genderSelect == "Male")
                            {
                                print("<img src='images/DwMaMa.jpg'>");
                            }
                            else
                            {
                                print("<img src='images/DwMaFe.jpg'>");
                            } 
                        }
                        else
                        {
                           if($genderSelect == "Male")
                            {
                                print("<img src='images/DwThMa.jpg'>");
                            }
                            else
                            {
                                print("<img src='images/DwThFe.jpg'>");
                            }  
                        }
                    }
                    
                    ?>
                </div>
            </div>
        </div>
        <!-- Bootstrap core JavaScript -->
        <script src="../../../vendor/jquery/jquery.min.js" type="text/javascript"></script>
        <script src="../../../vendor/bootstrap/js/bootstrap.bundle.min.js" type="text/javascript"></script>

        <!-- Plugin JavaScript -->
        <script src="../../../vendor/jquery-easing/jquery.easing.min.js" type="text/javascript"></script>

        <!-- Contact Form JavaScript -->
        <script src="../../../js/jqBootstrapValidation.min.js" type="text/javascript"></script>
        <script src="../../../js/contact_me.min.js" type="text/javascript"></script>

        <!-- Custom scripts for this template -->
        <script src="../../../js/freelancer.min.js" type="text/javascript"></script>
    </body>
</html>
