"""
Class Questions list 158 questions to be used towards the game. Questions 1-79 are fielding questions (True or False) while
questions 80-158 are batting questions (one-word responses). A list after the class assigns the numbered questions to their
appropiate inning part (fielding/batting).
"""
class Questions(object):
    def __init__(self):
        self.question1 = {'question' : 'Dean was born in 1979. ' , 'answer' : 'True'}
        self.question2 = {'question' : 'The real name of the Yellow-Eyed Demon is Azazel. ' , 'answer' : 'True'}
        self.question3 = {'question' : 'The demon-killing knife that Sam and Dean use on all of their hunts was first wielded by Crowley. ' , 'answer' : 'False'}
        self.question4 = {'question' : 'Cassie is the first girl Dean ever loved and told the truth about his being a hunter to. ' , 'answer' : 'True'}
        self.question5 = {'question' : 'The Horseman War’s vehicle of choice is a red Jeep. ' , 'answer' : 'False'}
        self.question6 = {'question' : 'Dean made a sawed-off shotgun when he was in the seventh grade. ' , 'answer' : 'False'}
        self.question7 = {'question' : 'Skinwalkers are humans that can transform into dogs. ' , 'answer' : 'True'}
        self.question8 = {'question' : 'Demons refer to their human vessels as meatsuits. ' , 'answer' : 'True'}
        self.question9 = {'question' : 'Sam uses antibacterial spray to erase the viral infection cause by the Darkness. ' , 'answer' : 'False'}
        self.question10 = {'question' : 'Kevin lives in Neighbor, Michigan when he becomes a prophet. ' , 'answer' : 'True'}
        self.question11 = {'question' : 'Dean is listed as “Not Moose” in Crowley’s cellphone. ' , 'answer' : 'True'}
        self.question12 = {'question' : 'Nick is the name of the human Lucifer uses as his vessel during his plan to unleash the Apocalypse. ' , 'answer' : 'True'}
        self.question13 = {'question' : 'Purgatory was originally created to house the deadly creatures Leviathan. ' , 'answer' : 'True'}
        self.question14 = {'question' : 'An angel banishing sigil must be drawn in blood in order to work. ' , 'answer' : 'True'}
        self.question15 = {'question' : 'Sam loses his phone down a drain in Season 3 episode “Bad Day at Black Rock”. ' , 'answer' : 'False'}
        self.question16 = {'question' : 'Sam and Dean pose as cops during their investigations. ' , 'answer' : 'False'}
        self.question17 = {'question' : 'Bobby Singer’s dead wife Catherine temporarily returns as a zombie. ' , 'answer' : 'False'}
        self.question18 = {'question' : 'Sam is wanted by Azazel to lead his demon army on Earth. ' , 'answer' : 'True'}
        self.question19 = {'question' : 'Ellen is married to Bobby when angel Balthazar creates an alternate timeline. ' , 'answer' : 'True'}
        self.question20 = {'question' : 'Bobby calls Sam and Dean Idjits. ' , 'answer' : 'True'}
        self.question21 = {'question' : 'Crowley sends unruly souls to Bimbo which is a place in Hell for a “time-out”. ' , 'answer' : 'False'}
        self.question22 = {'question' : 'Dean kills Zachariah using Cain’s blade. ' , 'answer' : 'False'}
        self.question23 = {'question' : 'A binding spell has been used on Death three times. ' , 'answer' : 'False'}
        self.question24 = {'question' : 'Crowley’s favorite drink is rum. ' , 'answer' : 'False'}
        self.question25 = {'question' : 'Eve alters her shape to appear like Mary when the brothers refuse to cooperate with her. ' , 'answer' : 'True'}
        self.question26 = {'question' : 'Sam played soccer as a child. ' , 'answer' : 'True'}
        self.question27 = {'question' : 'Amara is the name given to the Darkness. ' , 'answer' : 'True'}
        self.question28 = {'question' : 'Dean becomes trapped in Purgatory while trying to rescue Bobby’s soul from Hell. ' , 'answer' : 'False'}
        self.question29 = {'question' : 'Lilith kills Dean by having him torn apart by hellhounds. ' , 'answer' : 'True'}
        self.question30 = {'question' : 'Sam and Dean are forced to participate in the Japanese show Nutracer! when they are sent into TV land by the Trickster. ' , 'answer' : 'False'}
        self.question31 = {'question' : 'Pishtaco feed on muscles from humans. ' , 'answer' : 'False'}
        self.question32 = {'question' : 'Dean lives with Lisa when he temporarily gives up hunting. ' , 'answer' : 'True'}
        self.question33 = {'question' : 'The Men of Letters’ bunker took four years to build. ' , 'answer' : 'False'}
        self.question34 = {'question' : 'Metatron kills Naomi. ' , 'answer' : 'True'}
        self.question35 = {'question' : 'George Winchester gives his grandsons Dean and Sam the key to the Men of Letters’ bunker before his death. ' , 'answer' : 'False'}
        self.question36 = {'question' : 'Rachel serves as Castiel’s lieutenant during the civil war in Heaven. ' , 'answer' : 'True'}
        self.question37 = {'question' : 'A siren’s call is transmitted through eye contact. ' , 'answer' : 'False'}
        self.question38 = {'question' : 'Castiel steals Theo’s grace before smiting him. ' , 'answer' : 'True'}
        self.question39 = {'question' : 'The second angel that Sam and Dean meet is Uriel. ' , 'answer' : 'True'}
        self.question40 = {'question' : 'Ghouls are only killed from a silver bullet to the heart. ' , 'answer' : 'False'}
        self.question41 = {'question' : 'Mary Winchester’s biggest fear was having her sons being raised to be hunters. ' , 'answer' : 'True'}
        self.question42 = {'question' : 'A qareen must be stabbed in the heart in order to be killed. ' , 'answer' : 'True'}
        self.question43 = {'question' : 'Crowley once had a romantic relationship with Castiel. ' , 'answer' : 'False'}
        self.question44 = {'question' : 'Crowley has only two nicknames for Sam. ' , 'answer' : 'False'}
        self.question45 = {'question' : 'Bobby Singer appeared in two episodes during season one. ' , 'answer' : 'False'}
        self.question46 = {'question' : 'Lucifer’s cage is in Limbo, a part of hell. ' , 'answer' : 'True'}
        self.question47 = {'question' : 'Dean spent three months in a boys home from stealing food. ' , 'answer' : 'False'}
        self.question48 = {'question' : 'Lisa’s occupation when Dean first meets her is a yoga instructor. ' , 'answer' : 'True'}
        self.question49 = {'question' : 'Amara is healed by Rowena after being smited by all of Heaven’s angels. ' , 'answer' : 'True'}
        self.question50 = {'question' : 'Sam is immune to the Croatoan virus. ' , 'answer' : 'True'}
        self.question51 = {'question' : 'The spell to open the door to Purgatory must be recited during a solar eclipse. ' , 'answer' : 'False'}
        self.question52 = {'question' : 'The djinn that poisons Charlie feeds off of happiness. ' , 'answer' : 'False'}
        self.question53 = {'question' : 'Rowena blasts Amara with lightning during their last confrontation. ' , 'answer' : 'True'}
        self.question54 = {'question' : 'Zacharia tells Dean he is the vessel for the archangel Gabriel. ' , 'answer' : 'False'}
        self.question55 = {'question' : 'Rowena wants to travel back in time to Ancient Rome to avoid the end of the world. ' , 'answer' : 'False'}
        self.question56 = {'question' : 'Dean loses to the witch Patrick at poker. ' , 'answer' : 'True'}
        self.question57 = {'question' : 'Dean was given the occupation of torturing souls while trapped in Hell. ' , 'answer' : 'True'}
        self.question58 = {'question' : 'A demon is expelled from its human vessel through holy water. ' , 'answer' : 'False'}
        self.question59 = {'question' : 'Adam is the name of Sam and Dean’s half-brother. ' , 'answer' : 'True'}
        self.question60 = {'question' : 'Sam and Dean need phoenix ash to kill Eve. ' , 'answer' : 'True'}
        self.question61 = {'question' : 'Crowley’s demon eyes are yellow. ' , 'answer' : 'False'}
        self.question62 = {'question' : 'Crowley’s name before he became a demon was Fergus. ' , 'answer' : 'True'}
        self.question63 = {'question' : 'Dean becomes an angel after he is resurrected by the Mark of Cain. ' , 'answer' : 'False'}
        self.question64 = {'question' : 'After John returned from war, he was a car mechanic. ' , 'answer' : 'True'}
        self.question65 = {'question' : 'Eric Singer is the main executive producer', 'answer' : 'False'}
        self.question66 = {'question' : 'Mark Sheppard plays Crowley', 'answer' : 'True'}
        self.question67 = {'question' : 'Castiel is played by Misha Singer.', 'answer' : 'False'}
        self.question68 = {'question' : 'Jared Padalecki plays Sam Winchester.', 'answer' : 'True'}
        self.question69 = {'question' : 'Dean Winchester is played by Jensen Ackles.', 'answer' : 'True'}
        self.question70 = {'question' : 'Tom Benedict plays as God.', 'answer' : 'False'}
        self.question71 = {'question' : 'Kevin Tran is played by Osric Chau.', 'answer' : 'True'}
        self.question72 = {'question' : 'Jo Harvelle is played by Alana Tal.', 'answer' : 'False'}
        self.question73 = {'question' : 'The Latin enscription on the barrel of the Colt gun says "I will fear no evil".', 'answer' : 'True'}
        self.question74 = {'question' : '"Carry on Wayward Child" is a famous song used in Supernatural.', 'answer' : 'False'}
        self.question75 = {'question' : 'Dean\'s birthday month is March.', 'answer' : 'False'}
        self.question76 = {'question' : 'Dean Winchester\'s natural eye color is hazel brown.', 'answer' : 'True'}
        self.question77 = {'question' : 'Sam is souless in season 7.', 'answer' : 'False'}
        self.question78 = {'question' : 'Dean gets gripped tight on his right arm when he was raised from perdition.', 'answer' : 'False'}
        self.question79 = {'question' : 'Dean and Sam get tattoos on the left side of their chest.', 'answer' : 'True'}
        self.question80 = {'question' : 'Which angel works with Castiel to help him track down all the rougue angels who fell from Heaven? ', 'answer' : 'Hannah'}
        self.question81 = {'question' : 'What is the name of the Greek god of time that Dean encounters when he time-travels to 1940s Chicago? ', 'answer' : 'Chronos'}
        self.question82 = {'question' : 'Gavin MacLeod is preparing to leave Scotland for which country in 1723 when Abaddon appears and sends him to the year 2014? ', 'answer' : 'America'}
        self.question83 = {'question' : 'What year was Sam born? ', 'answer' : '1983'}
        self.question84 = {'question' : 'Dean tortured souls in Hell under the tutelage of which demon? ', 'answer' : 'Alastair'}
        self.question85 = {'question' : 'What distinct smell do demons leave behind? ', 'answer' : 'Sulfur'}
        self.question86 = {'question' : 'Which angel does Dean succeed in killing after Sam fails to do so? ', 'answer' : 'Zachariah'}
        self.question87 = {'question' : 'What nickname does Dean give his beloved vehicle? ', 'answer' : 'Baby'}
        self.question88 = {'question' : 'What is the name of the angel that Lucifer smites when he visits Heaven in Castiel\'s vessel? ', 'answer' : 'Jofiel'}
        self.question89 = {'question' : 'A Leshii must be beheaded by an axe made of what substance? ', 'answer' : 'Iron'}
        self.question90 = {'question' : 'What is Crowley\'s nickanme for Sam? ', 'answer' : 'Moose'}
        self.question91 = {'question' : 'What is the true name of the archangel known as the Trickster? ', 'answer' : 'Gabriel'}
        self.question92 = {'question' : 'What was Vesta, the Roman goddess of the hearth, looking for as sacrifices to be made in her name? ', 'answer' : 'Virgins'}
        self.question93 = {'question' : 'A shapeshifter is killed when stabbed in the heart with this metal? ', 'answer' : 'Silver'}
        self.question94 = {'question' : 'As a result of his abduction by them, what creatures can Dean now see when they are in the human realm? ', 'answer' : 'Fairies'}
        self.question95 = {'question' : 'Silver bullets can kill all but which one of these four entities: zombies, witches, giants, and werewolves? ', 'answer' : 'Zombies'}
        self.question96 = {'question' : 'Which former hunter becomes a werewolf after being bitten by one during a hunt? ', 'answer' : 'Garth'}
        self.question97 = {'question' : 'What is the name of the demonic virus that is passed through blood-to-blood contact? ', 'answer' : 'Croatoan'}
        self.question98 = {'question' : 'What is the name of Lisa Braeden\'s son, who looks suspiciously like Dean? ', 'answer' : 'Ben'}
        self.question99 = {'question' : 'WHO KILLS HITLER IN SEASON 12?!?!?! ', 'answer' : 'Dean'}
        self.question100 = {'question' : 'What is the name of the witch that Rowena visits to ask for help with her time-traveling spell? ', 'answer' : 'Clea'}
        self.question101 = {'question' : 'Where did the cicada-like creatures known as Bisaan originate? ', 'answer' : 'Malaysia'}
        self.question102 = {'question' : 'What do Bobby and his wife Karen aruge about before she is possessed by a demon? ', 'answer' : 'Children'}
        self.question103 = {'question' : 'Djinn are killed by weapons dipped in this animal\'s blood. ', 'answer' : 'Lamb'}
        self.question104 = {'question' : 'Who is prepared to take on the Mark of Cain in order to defeat the Darkness? ', 'answer' : 'Sam'}
        self.question105 = {'question' : 'The Mark of Cain creates in its wearer the insatiable desire to do what? ', 'answer' : 'Kill'}
        self.question106 = {'question' : 'Lucifer was confined in a cage that could only open if how many of the 600 seals were broken? (in numerical form) ', 'answer' : '66'}
        self.question107 = {'question' : 'How many trials must be completed in order to close the gates of Hell forever? (in numerical form) ', 'answer' : '3'}
        self.question108 = {'question' : 'What weapon does Dean mount on the wall of his bedroom in the Men of Letters\' bunker? ', 'answer' : 'Axe'}
        self.question109 = {'question' : 'What demon does Sam set aflame, forcing her to abandon her human vessel? ', 'answer' : 'Abaddon'}
        self.question110 = {'question' : 'What is the manufacturing year of Dean\'s famous car? ', 'answer' : '1967'}
        self.question111 = {'question' : 'Lilith was the first what ever created? ', 'answer' : 'Demon'}
        self.question112 = {'question' : 'The first time Sam and Dean learned of the existence of angel blades was when the angel Uriel tried to kill which of his fellow angels? ', 'answer' : 'Castiel'}
        self.question113 = {'question' : 'Dean encounters this group of ancient superhuman women after a one-night stand with a woman named Lydia. ', 'answer' : 'Amazons'}
        self.question114 = {'question' : 'What was the name of the dog Sam adopted as a teenager? ', 'answer' : 'Bones'}
        self.question115 = {'question' : 'Which demon kills Meg when she sacrifices herself so that Sam and Dean can escape with the angel tablet? ', 'answer' : 'Crowley'}
        self.question116 = {'question' : 'Which of the Four Horsemen of the Apocalypse do Dean and Sam encounter first? ', 'answer' : 'War'}
        self.question117 = {'question' : 'These creatures have bony spikes that protrude from their wrists when they feed. ', 'answer' : 'Wraiths'}
        self.question118 = {'question' : 'A case involving what kind of monsters is Sheriff Donna Hanscum\'s first foray into the world of the supernatural? ', 'answer' : 'Vampires'}\

        self.question119 = {'question' : 'Dean irons Sam\'s shirts using what beverage instead of water? ', 'answer' : 'Beer'}
        self.question120 = {'question' : 'Which angel\'s grace does Metatron use to complete his spell to close the gates of Heaven forever? ', 'answer' : 'Castiel'}
        self.question121 = {'question' : 'Which demon possesses Sam and almost kills Dean? ', 'answer' : 'Meg'}
        self.question122 = {'question' : 'John Winchester and Mary Campbell\'s first meeting is arranged by which celestial being? ', 'answer' : 'Cupid'}
        self.question123 = {'question' : 'Who is the first hunter to summon Crowley via spell? ', 'answer' : 'Bobby'}
        self.question124 = {'question' : 'What is the name of Sam\'s childhood imaginery friend? ', 'answer' : 'Sully'}
        self.question125 = {'question' : 'Dean is trapped in pergatory for __ year. ', 'answer' : '1'}
        self.question126 = {'question' : 'The time god Chronos can be killed with a stake carved from a branch of this type of tree. ', 'answer' : 'Olive'}
        self.question127 = {'question' : 'Who kills the Yellow-Eyed Demon? ', 'answer' : 'Dean'}
        self.question128 = {'question' : 'What is Crowley\'s mother\'s name? ', 'answer' : 'Rowena'}
        self.question129 = {'question' : 'When Castiel sends Sam and Dean back to 1861 Wyoming, who kills the phoenix they encounter? ', 'answer' : 'Dean'}
        self.question130 = {'question' : 'What nickname does Meg give to Castiel? ', 'answer' : 'Clarence'}
        self.question131 = {'question' : 'The ritual to summon the archangel Raphel must be performed at what time of day? ', 'answer' : 'Sunrise'}
        self.question132 = {'question' : 'Who does Rowena ask Sam to kill if she decodes the Book of the Damned for him? ', 'answer' : 'Crowley'}
        self.question133 = {'question' : 'In order for Dean to be cured after he is turned into a vampire, he must not drink any human blood, as well as obtain what from the vampire who turned him? ', 'answer' : 'Blood'}
        self.question134 = {'question' : 'Which of the following angels was not held in Heaven\'s prison at some point in their history: Castiel, Naomi, Anna, or Gadreel? ', 'answer' : 'Naomi'}
        self.question135 = {'question' : 'What are the supernatural beings responsible for escorting the souls of the eparted to the afterlife called? ', 'answer' : 'Reapers'}
        self.question136 = {'question' : 'How many years does a person typically get to live in exchange for selling their soul to a Crossroads Demon? (in numerical form) ', 'answer' : '10'}
        self.question137 = {'question' : 'While investigating a possible alien abduciton, Dean is taken captive and studied by what magical species? ', 'answer' : 'Fairies'}
        self.question138 = {'question' : 'Hex bags are used primarily by these types of supernatural people. ', 'answer' : 'Witches'}
        self.question139 = {'question' : 'Sunlight does not kill a vampire; just weakens it. What is the only way to kill a vampire? (one word) ', 'answer' : 'Decapitation'}
        self.question140 = {'question' : 'Who does Dean kill right before the Mark of Cain is removed from him? ', 'answer' : 'Death'}
        self.question141 = {'question' : 'How many times does Dean specifically summon Death? (in numerical form) ', 'answer' : '2'}
        self.question142 = {'question' : 'How many years (in Hell time) did Dean spend in Hell? (in numerical form) ', 'answer' : '40'}
        self.question143 = {'question' : 'In season 10 episode "About a Boy", Dean is magically transformed into a teenager. What is his exact age? (in numerical form). ', 'answer' : '14'}
        self.question144 = {'question' : 'What is Charlie Bradbury\'s real first name? ', 'answer' : 'Celeste'}
        self.question145 = {'question' : 'Who does Sam ask to keep an eye on Dean\'s Purgatory friend Benny? ', 'answer' : 'Martin'}
        self.question146 = {'question' : 'In Season 4 episode 6 "Yellow Fever", what in the lumber mill makes Dean scream? ', 'answer' : 'Cat'}
        self.question147 = {'question' : 'What state does Dean take Sam for their first case of the show? ', 'answer' : 'California'}
        self.question148 = {'question' : 'Who has said "I lost my shoe"? ', 'answer' : 'Sam'}
        self.question149 = {'question' : 'Who has said "Wait, there\'s no such thing as unicorns?"? ', 'answer' : 'Sam'}
        self.question150 = {'question' : 'Who has said "I found a liquor store. And I drank it."? ', 'answer' : 'Castiel'}
        self.question151 = {'question' : 'What state was Sam and Dean born in? ', 'answer' : 'Kansas'}
        self.question152 = {'question' : 'Who possessed the 80\'s rock star Rick Springfield? ', 'answer' : 'Lucifer'}
        self.question153 = {'question' : 'What was the title of the show originally going to be? ', 'answer' : 'Unnatural'}
        self.question154 = {'question' : 'What angel wrote the Word of God tablets? ', 'answer' : 'Metatron'}
        self.question155 = {'question' : 'What hunter married a werewolf named Bess? ', 'answer' : 'Garth'}
        self.question156 = {'question' : 'What is God\'s name? ', 'answer' : 'Chuck'}
        self.question157 = {'question' : 'What did Sam study during his time in college? ', 'answer' : 'Law'}
        self.question158 = {'question' : 'Which actor accidentally hurt himself while trying to do his own stunts? ', 'answer' : 'Jared'}
s = Questions()
questions_fielding = [s.question1, s.question2, s.question3, s.question4, s.question5, s.question6, s.question7, s.question8, s.question9, s.question10, s.question11, s.question12, s.question13, s.question14, s.question15, s.question16, s.question17, s.question18, s.question19, s.question20, s.question21, s.question22, s.question23, s.question24, s.question25, s.question26, s.question27, s.question28, s.question29, s.question30, s.question31, s.question32, s.question33, s.question34, s.question35, s.question36, s.question37, s.question38, s.question39, s.question40, s.question41, s.question42, s.question43, s.question44, s.question45, s.question46, s.question47, s.question48, s.question49, s.question50, s.question51, s.question52, s.question53, s.question54, s.question55, s.question56, s.question57, s.question58, s.question59, s.question60, s.question61, s.question62, s.question63, s.question64, s.question65, s.question66, s.question67, s.question68, s.question69, s.question70, s.question71, s.question72, s.question73, s.question74, s.question75, s.question76, s.question77, s.question78, s.question79]
questions_batting = [s.question80, s.question81, s.question82, s.question83, s.question84, s.question85, s.question86, s.question87, s.question88, s.question89, s.question90, s.question91, s.question92, s.question93, s.question94, s.question95, s.question96, s.question97, s.question98, s.question99, s.question100, s.question101, s.question102, s.question103, s.question104, s.question105, s.question106, s.question107, s.question108, s.question109, s.question110, s.question111, s.question112, s.question113, s.question114, s.question115, s.question116, s.question117, s.question118, s.question119, s.question120, s.question121, s.question122, s.question123, s.question124, s.question125, s.question126, s.question127, s.question128, s.question129, s.question130, s.question131, s.question132, s.question133, s.question134, s.question135, s.question136, s.question137, s.question138, s.question139, s.question140, s.question141, s.question142, s.question143, s.question144, s.question145, s.question146, s.question147, s.question148, s.question149, s.question150, s.question151, s.question152, s.question153, s.question154, s.question155, s.question156, s.question157, s.question158]


#keeps track of question number for fielding
questioncounterfielding = 0
#keeps track of question number for batting
questioncounterbatting = 0
#keeps total score for opposing team
total_runs_away = 0
#keeps total score for your team
total_runs_home = 0
#keeps track of inning number
inningcounter = 1
#keeps track of total number of fielding questions used
x = 1
#keeps track of total number of batting questions used
y = 1


"""
Function is used when the game is over. It prints your score to the opposing team's score. Whether it prints that you won,
lost, or tied depends on which number has the greater value.
"""
def game_score():
    if total_runs_home > total_runs_away:
        print(f'The game is over! The score was {total_runs_home} to {total_runs_away}. You won!')
    elif total_runs_home == total_runs_away:
        print(f'The game is over! The score was {total_runs_home} to {total_runs_away}. It was a tie!')
    else:
        print(f'The game is over! The score was {total_runs_home} to {total_runs_away}. You lost!')


"""
Function is for the batting inning of the game. While y is under a certiain limit, it keeps track of the question counter for batting,
amount of questions wrong, the inning, your runs, and the variables x and y. What is printed depends on the situation of the game.
"""
def batting_inning():

    #keeps track of batting questions answered incorrectly
    questions_wrong_batting = 0
    #keeps track of your runs per inning
    runs_home = -3
    #global calls variables already valued outside of function
    global questioncounterbatting
    global total_runs_home
    global inningcounter
    global y
    global x

    while y <= 79:
        #When other team has scored 10 runs, x and y variables are set past initial limit to end the game.
        if total_runs_away == 10:
            y = 80
            x = 80
        answer = input(questions_batting[questioncounterbatting]['question']).title()
        #When the answer is correct, the number of batting questions, batting question counter, and runs home for the inning increases by 1.
        if answer == questions_batting[questioncounterbatting]['answer']:
            y += 1
            questioncounterbatting += 1
            runs_home += 1
            #When runs home is 0 or less, prints a string and continues to ask batting questions.
            if runs_home <= 0:
                print('You got on base!')
                print(f" ")
            #When runs home is 1 or more, adds to your total score and prints a string. Batting inning continues to run.
            else:
                total_runs_home += 1
                print(f'You got on base! You have {runs_home} run(s).')
                print(f' ')
                #When runs home is 5, increases the inning by 1
                if runs_home == 5:
                    inningcounter += 1
                    #When the inning counter is 6, prompts user if they would like to keep playing or not. User input decides whether it runs the fielding function or ends the game.
                    if inningcounter == 6:
                        playon = input(f'It is the {inningcounter}th inning. Would you like to keep playing? ').lower()
                        if playon == ('yes'):
                            print(f' ')
                            print(f'You have decided to keep plaiyng. It is inning 6. The score is {total_runs_home} to {total_runs_away}. You are fielding.')
                            fielding_inning()
                        else:
                            game_score()
                            y = 80
                            x = 80
                    #When it is the 9th inning, it tells the user it is the last inning. It runs the fielding function.
                    elif inningcounter == 9:
                        print(f'It is inning 9! This is the last inning! The score is {total_runs_home} to {total_runs_away}. Switch sides to fielding! (True or False).')
                        fielding_inning()
                    #When it is the 10th inning, the game ends.
                    elif inningcounter == 10:
                        game_score()
                        y = 80
                        x = 80
                    #When non of the other loops work, it repeats the inning number, the total score, and runs the fielding function.
                    else:
                        print(f'You have gotten 5 runs! It is inning {inningcounter}! The score is {total_runs_home} to {total_runs_away}. Switch sides to fielding! (True or False).')
                        fielding_inning()
        #When the answer is incorrect, the number of batting questions, batting question counter, and batting questions wrong increases by 1.
        else:
            y += 1
            questioncounterbatting += 1
            questions_wrong_batting += 1
            print(f'You got out! You have {questions_wrong_batting} out(s) against you! ')
            print(f" ")
            #When the number of questions wrong is 3, the inning counter increases by 1.
            if questions_wrong_batting == 3:
                inningcounter += 1
                #When the inning counter is 6, it asks the user if they would like to keep playing. Depending on the user input determines whether it runs the fielding inning or ends the game.
                if inningcounter == 6:
                    playon = input(f'It is the {inningcounter}th inning. Would you like to keep playing? ').lower()
                    if playon == ('yes'):
                        print(f' ')
                        print(f'You have decided to keep plaiyng. It is inning 6. The score is {total_runs_home} to {total_runs_away}. You are fielding.')
                        fielding_inning()
                    else:
                        game_score()
                        y = 80
                        x = 80
                #When it is the 9th inning, it tells the user it is the last inning
                elif inningcounter == 9:
                    print(f'It is inning 9! This is the last inning! The score is {total_runs_home} to {total_runs_away}. Switch sides to fielding! (True or False).')
                    fielding_inning()
                #When it is the 10th inning, the game ends
                elif inningcounter == 10:
                    game_score()
                    y = 80
                    x = 80
                #When non of the other loops work, it repeats the inning number, the total score, and runs the fielding function.
                else:
                    print(f'You got 3 outs against you! It is inning {inningcounter}. The score is {total_runs_home} to {total_runs_away}. Switch sides to fielding! (True or False).')
                    fielding_inning()



"""
Function is for the fielding inning of the game. While x is under a certiain limit, it keeps track of the question counter for fielding,
the inning, the opposing team's runs, and the variables x and y. What is printed depends on the situation of the game.
"""
def fielding_inning():

    #keeps track of questions right during fielding
    questions_right_fielding = 0
    #keeps track of opposing team's runs per inning
    runs_away = -3
    #global calls variables already valued outside of the function
    global x
    global y
    global inningcounter
    global total_runs_away
    global questioncounterfielding

    while x <= 79:
        #When other team has scored 10 runs, x and y variables are set past initial limit to end the game.
        if total_runs_away == 10:
            y = 80
            x = 80
        else:
            answer = input(questions_fielding[questioncounterfielding]['question']).title()
            #When the answer is correct, the number of fielding questions, the fielding questions counter, and the number of questions right increases by 1 and prints.
            if answer == questions_fielding[questioncounterfielding]['answer']:
                questioncounterfielding += 1
                questions_right_fielding += 1
                x += 1
                print(f'You got an out! You have {questions_right_fielding} out(s)!')
                print(f" ")
                #When the number of questions right is 3, it ends the inning and runs the batting function.
                if questions_right_fielding == 3:
                    print('You got three outs. Switch sides to batting! (One-word responses)')
                    batting_inning()
            #When the answer is incorrect, the number of fielding questions, the fielding questions counter, and runs away is increased by 1.
            else:
                x += 1
                questioncounterfielding += 1
                runs_away += 1
                #When the runs for the other team (per inning) is 0 or less, it prints. The fielding running continues to run.
                if runs_away <= 0:
                    print(f'The runner has taken the base!')
                    print(f' ')
                #When the runs for the other team (per inning) is 1 or more, the total runs for the other team increases by 1.
                else:
                    total_runs_away += 1
                    #When the total runs of the opposing team is 10, the game ends
                    if total_runs_away == 10:
                        game_score()
                        x == 80
                        y == 80
                    #When the runs for the other team (per inning) is 5, it prints and runs the batting inning.
                    elif runs_away == 5:
                        print(f'Runner has taken the base! The other team has scored {runs_away} run(s) this inning.')
                        print(f' ')
                        print('The other team has scored 5 runs! Switch sides to batting! (True or False)')
                        batting_inning()
                    #When none of the otehr loops work, it prints and continues to run the batting function until conditions change.
                    else:
                        print(f'The runner has taken the base! The other team has {runs_away} run(s) this inning.')
                        print(f' ')


#Gives the player an understanding of the game.
print("""Warning: This game requires extreme knowledge of the show Supernatural. Spelling counts and watch out for plurals!

Welcome to the Supernatural Baseball Derby! Soon you will pick a team to play for, but first, let's go over how to play!

You will start off in the field where you will be asked questions about the Supernatural TV Show which requires a True or False response.
In order to continue on to the next inning, you must answer three questions correctly, as each correct answer counts as a ball fielded.
However, everytime you get a question wrong, the batter takes a base. The inning is over when you have finally answered three questions correctly
or when the other team has scored 5 runs.

When up to bat, you will be asked questions about the TV show which require a one-word typed response.
Every correct answer will be counted as a hit and you will proceed to the base. If you answer incorrectly, it will be counted as an out.
The inning is over when you get 3 outs against you or when you score 5 runs.

Ending the Game:
When the other team scores 10 runs in total against you, the game will end no matter your score. Both you and the opposing team can only
get 5 runs per inning. The game in general lasts five innings, however by the sixth inning, you will be given a choice to either
continue playing until the ninth inning or end the game. Enjoy and good luck!
""")

#Sets variable up for user input
continue_game = input("Are you ready? ").lower()
#When the user answers yes, prompts user to choose a team. Depending on the letter chosen determines what is printed. After print, the fielding inning begins to run.
if continue_game == ("yes"):
    team = input("""Please choose your team:
    A Castiel's Fergalicious Angels
    B Dean's Hellhounds
    C Sam's So Get This's
    D Crawley's Darlings'
    E Bobby's Idjits'
    """).lower()
    if team == ("a"):
        print(f"You chose the team Castiel's Fergalicious Angels.")
    elif team == ("b"):
        print(f"You chose the team Dean's Hellhounds.")
    elif team == ("c"):
        print(f"You chose the team Sam's So Get This's.")
    elif team == ("d"):
        print(f"You chose the team Crawley's Darlings'")
    elif team == ("e"):
        print(f"You chose the team Bobby's Idjits'")
    print(f'')
    print("Welcome to inning 1! You are in the field!")
    fielding_inning()
#When the user answers with anything else, it prints and does not run anything.
else:
    print('Suit yourself!')
