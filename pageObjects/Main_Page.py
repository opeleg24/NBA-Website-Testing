import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Main_Page:

    def __init__(self, driver):
        self.driver = driver

    bucksPageButton = (By.CSS_SELECTOR, "a[href='#!Bucks']")
    bullsPageButton = (By.CSS_SELECTOR, "a[href='#!Bulls']")
    cavaliersPageButton = (By.CSS_SELECTOR, "a[href='#!Cavs']")
    celticsPageButton = (By.CSS_SELECTOR, "a[href='#!Celtics']")
    clippersPageButton = (By.CSS_SELECTOR, "a[href='#!Clippers']")
    grizzliesPageButton = (By.CSS_SELECTOR, "a[href='#!Grizzlies']")
    hawksPageButton = (By.CSS_SELECTOR, "a[href='#!Hawks']")
    heatPageButton = (By.CSS_SELECTOR, "a[href='#!Heat']")
    hornetsPageButton = (By.CSS_SELECTOR, "a[href='#!Hornets']")
    jazzPageButton = (By.CSS_SELECTOR, "a[href='#!Jazz']")
    kingsPageButton = (By.CSS_SELECTOR, "a[href='#!Kings']")
    knicksPageButton = (By.CSS_SELECTOR, "a[href='#!Knicks']")
    lakersPageButton = (By.CSS_SELECTOR, "a[href='#!Lakers']")
    magicPageButton = (By.CSS_SELECTOR, "a[href='#!Magic']")
    mavericksPageButton = (By.CSS_SELECTOR, "a[href='#!Mavs']")
    netsPageButton = (By.CSS_SELECTOR, "a[href='#!Nets']")
    nuggetsPageButton = (By.CSS_SELECTOR, "a[href='#!Nuggets']")
    pacersPageButton = (By.CSS_SELECTOR, "a[href='#!Pacers']")
    pelicansPageButton = (By.CSS_SELECTOR, "a[href='#!Pelicans']")
    pistonsPageButton = (By.CSS_SELECTOR, "a[href='#!Pistons']")
    raptorsPageButton = (By.CSS_SELECTOR, "a[href='#!Raptors']")
    rocketsPageButton = (By.CSS_SELECTOR, "a[href='#!Rockets']")
    spursPageButton = (By.CSS_SELECTOR, "a[href='#!Spurs']")
    sunsPageButton = (By.CSS_SELECTOR, "a[href='#!Suns']")
    thunderPageButton = (By.CSS_SELECTOR, "a[href='#!Thunder']")
    timberwolvesPageButton = (By.CSS_SELECTOR, "a[href='#!Timberwolves']")
    trailblazersPageButton = (By.CSS_SELECTOR, "a[href='#!Blazers']")
    warriorsPageButton = (By.CSS_SELECTOR, "a[href='#!Warriors']")
    wizardsPageButton = (By.CSS_SELECTOR, "a[href='#!Wizards']")



    TeamText = (By.XPATH, "//table[@id='TeamData']//tr[2]//td")
    ##players_roster
    rosterTab = (By.LINK_TEXT, "Roster")
    rosterPlayers = (By.XPATH, "//ul[@class='player']/li/a")
    rosterPlayerHeader = (By.LINK_TEXT, "Player")
    rosterPlayersReverse = (By.XPATH, "//ul[@class='player']/li/a")
    rosterPositionHeader = (By.LINK_TEXT, "Position")
    rosterPositions = (By.XPATH, "//tr[@id='NewRostertr']/td[2]")
    rosterPositionsReverse = (By.XPATH, "//tr[@id='NewRostertr']/td[2]")
    rosterHeightHeader = (By.LINK_TEXT, "Height (cm)")
    rosterHeights = (By.XPATH, "//tr[@id='NewRostertr']/td[3]")
    rosterHeightsReverse = (By.XPATH, "//tr[@id='NewRostertr']/td[3]")
    rosterWeightHeader = (By.LINK_TEXT, "Weight (kg)")
    rosterWeights = (By.XPATH, "//tr[@id='NewRostertr']/td[4]")
    rosterWeightsReverse = (By.XPATH, "//tr[@id='NewRostertr']/td[4]")
    rosterDobHeader = (By.LINK_TEXT, "Date of Birth")
    rosterDobs = (By.XPATH, "//tr[@id='NewRostertr']/td[5]")
    rosterDobsReverse = (By.XPATH, "//tr[@id='NewRostertr']/td[5]")
    rosterExperienceHeader = (By.LINK_TEXT, "Experience (years)")
    rosterExperiences = (By.XPATH, "//tr[@id='NewRostertr']/td[6]")
    rosterExperiencesReverse = (By.XPATH, "//tr[@id='NewRostertr']/td[6]")
    rosterCollegeHeader = (By.LINK_TEXT, "College")
    rosterColleges = (By.XPATH, "//tr[@id='NewRostertr']/td[7]")
    rosterCollegesReverse = (By.XPATH, "//tr[@id='NewRostertr']/td[7]")
    ##players_salaries
    salariesTab = (By.LINK_TEXT, "Salaries")
    salariesPlayersHeader = (By.XPATH, "//tr[@id='PayRolltr']/th[1]/a[1]")
    salariesPlayers = (By.XPATH, "//tr[@id='PayRolltr']/td[1]")
    salariesPlayersReverse = (By.XPATH, "//tr[@id='PayRolltr']/td[1]")
    salariesAgeHeader = (By.LINK_TEXT, "Age")
    agePlayers = (By.XPATH, "//tr[@id='PayRolltr']/td[2]")
    agePlayersReverse = (By.XPATH, "//tr[@id='PayRolltr']/td[2]")
    salariesEightTeenNineTeenHeader = (By.LINK_TEXT, "2018-19")
    eightTeenNineTeenPlayers = (By.XPATH, "//tr[@id='PayRolltr']/td[3]")
    eightTeenNineTeenPlayersReverse = (By.XPATH, "//tr[@id='PayRolltr']/td[3]")
    salariesNineTeenTwentyHeader = (By.LINK_TEXT, "2019-20")
    NineTeenTwentyPlayers = (By.XPATH, "//tr[@id='PayRolltr']/td[4]")
    NineTeenTwentyPlayersReverse = (By.XPATH, "//tr[@id='PayRolltr']/td[4]")
    salariesTwentyTwentyOneHeader = (By.LINK_TEXT, "2020-21")
    twentyTwentyOnePlayers = (By.XPATH, "//tr[@id='PayRolltr']/td[5]")
    twentyTwentyOnePlayersReverse = (By.XPATH, "//tr[@id='PayRolltr']/td[5]")
    salariesTwentyOneTwentyTwoHeader = (By.LINK_TEXT, "2021-22")
    TwentyOneTwentyTwoPlayers = (By.XPATH, "//tr[@id='PayRolltr']/td[6]")
    TwentyOneTwentyTwoPlayersReverse = (By.XPATH, "//tr[@id='PayRolltr']/td[6]")
    salariesTwentyTwoTwentyThreeHeader = (By.LINK_TEXT, "2022-23")
    TwentyTwoTwentyThreePlayers = (By.XPATH, "//tr[@id='PayRolltr']/td[7]")
    TwentyTwoTwentyThreePlayersReverse = (By.XPATH, "//tr[@id='PayRolltr']/td[7]")
    salariesGuaranteedHeader = (By.LINK_TEXT, "Guaranteed")
    guaranteedPlayers = (By.XPATH, "//tr[@id='PayRolltr']/td[10]")
    guaranteedPlayersReverse = (By.XPATH, "//tr[@id='PayRolltr']/td[10]")

    #players_stats
    isPlayer = (By.XPATH, "//table[@id='PlayerSeasonStatsTable']/tbody/tr[2]/td[1]")
    playerStatsCloseButton = (By.CLASS_NAME, "closeBtn")
    playerName = (By.ID, "PlayerNameHeadLine")
    playersStatsSeasonsHeader = (By.LINK_TEXT, "Season")
    seasonsPlayersStats = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[1]")
    seasonsPlayersStatsReverse = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[1]")
    playersStatsTeamHeader = (By.LINK_TEXT, "Team")
    teamsPlayersStats = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[2]")
    teamsPlayersStatsReverse = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[2]")
    playersStatsNumGamesHeader = (By.LINK_TEXT, "G")
    numGamesPlayersStats = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[3]")
    numGamesPlayersStatsReverse = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[3]")
    playersStatsNumGamesStartedHeader = (By.LINK_TEXT, "GS")
    NumGamesStartedPlayersStats = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[4]")
    NumGamesStartedPlayersStatsReverse = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[4]")
    playersStatsMinutesPlayedHeader = (By.LINK_TEXT, "MP")
    minutesPlayedPlayersStats = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[5]")
    minutesPlayedPlayersStatsReverse = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[5]")
    playersStatsFieldGoalsPercentageHeader = (By.LINK_TEXT, "FG%")
    FieldGoalsPercentagePlayersStats = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[6]")
    FieldGoalsPercentagePlayersStatsReverse = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[6]")
    playersStatsThreePointPercentageHeader = (By.LINK_TEXT, "3P%")
    ThreePointPercentagePlayersStats = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[7]")
    ThreePointPercentagePlayersStatsReverse = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[7]")
    playersStatsFreeThrowPercentageHeader = (By.LINK_TEXT, "FT%")
    freeThrowPercentagePlayersStats = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[8]")
    freeThrowPercentagePlayersStatsReverse = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[8]")
    playersStatsReboundsHeader = (By.LINK_TEXT, "RB")
    reboundsPlayersStats = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[9]")
    reboundsPlayersStatsReverse = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[9]")
    playersStatsAssistsHeader = (By.LINK_TEXT, "AST")
    assistsPlayersStats = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[10]")
    assistsPlayersStatsReverse = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[10]")
    playersStatsStealsHeader = (By.LINK_TEXT, "STL")
    stealsPlayersStats = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[11]")
    stealsPlayersStatsReverse = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[11]")
    playersStatsBlocksHeader = (By.LINK_TEXT, "BLK")
    blocksPlayersStats = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[12]")
    blocksPlayersStatsReverse = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[12]")
    playersStatsTurnoversHeader = (By.LINK_TEXT, "TOV")
    turnoversPlayersStats = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[13]")
    turnoversPlayersStatsReverse = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[13]")
    playersStatsPointsHeader = (By.LINK_TEXT, "PTS")
    pointsPlayersStats = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[14]")
    pointsPlayersStatsReverse = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[14]")
    playersStatsDoubleDoublesHeader = (By.LINK_TEXT, "DOUBLE-DOUBLE")
    doubleDoublesPlayersStats = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[15]")
    doubleDoublesPlayersStatsReverse = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[15]")
    playersStatsTripleDoublesHeader = (By.LINK_TEXT, "TRIPLE-DOUBLE")
    tripleDoublesPlayersStats = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[16]")
    tripleDoublesPlayersStatsReverse = (By.XPATH, "//tr[@id='PlayerSeasonStatsTabletr']/td[16]")
    gaurdPresence = (By.XPATH, "//td[text()='G']")


    #action = ActionChains(driver)
    #action.double_click(driver.find_element_by_link_text("Player")).perform()
    #bullsPageButton = (By.CSS_SELECTOR, "a[href='#!Bulls']")

    def openBucksPageButton(self):

        return self.driver.find_element(*Main_Page.bucksPageButton)

    def openBullsPageButton(self):

        return self.driver.find_element(*Main_Page.bullsPageButton)
    def openCavaliersPageButton(self):

        return self.driver.find_element(*Main_Page.cavaliersPageButton)

    def openHawksPageButton(self):

        return self.driver.find_element(*Main_Page.hawksPageButton)

    def openCelticsPageButton(self):

        return self.driver.find_element(*Main_Page.celticsPageButton)

    def openClippersPageButton(self):

        return self.driver.find_element(*Main_Page.clippersPageButton)

    def openGrizzliesPageButton(self):

        return self.driver.find_element(*Main_Page.grizzliesPageButton)

    def openHeatPageButton(self):

        return self.driver.find_element(*Main_Page.heatPageButton)

    def openHornetsPageButton(self):

        return self.driver.find_element(*Main_Page.hornetsPageButton)

    def openJazzPageButton(self):

        return self.driver.find_element(*Main_Page.jazzPageButton)

    def openKingsPageButton(self):

        return self.driver.find_element(*Main_Page.kingsPageButton)

    def openKnicksPageButton(self):

        return self.driver.find_element(*Main_Page.knicksPageButton)

    def openLakersPageButton(self):

        return self.driver.find_element(*Main_Page.lakersPageButton)

    def openMagicPageButton(self):

        return self.driver.find_element(*Main_Page.magicPageButton)

    def openMavericksPageButton(self):

        return self.driver.find_element(*Main_Page.mavericksPageButton)

    def openNuggetsPageButton(self):

        return self.driver.find_element(*Main_Page.nuggetsPageButton)

    def openNetsPageButton(self):

        return self.driver.find_element(*Main_Page.netsPageButton)

    def openPacersPageButton(self):

        return self.driver.find_element(*Main_Page.pacersPageButton)

    def openPelicansPageButton(self):

        return self.driver.find_element(*Main_Page.pelicansPageButton)

    def openPistonsPageButton(self):

        return self.driver.find_element(*Main_Page.pistonsPageButton)

    def openRaptorsPageButton(self):

        return self.driver.find_element(*Main_Page.raptorsPageButton)

    def openRocketsPageButton(self):

        return self.driver.find_element(*Main_Page.rocketsPageButton)

    def openSpursPageButton(self):

        return self.driver.find_element(*Main_Page.spursPageButton)

    def openSunsPageButton(self):

        return self.driver.find_element(*Main_Page.sunsPageButton)

    def openThunderPageButton(self):

        return self.driver.find_element(*Main_Page.thunderPageButton)

    def openTimberwolvesPageButton(self):

        return self.driver.find_element(*Main_Page.timberwolvesPageButton)


    def openTrailblazersPageButton(self):

        return self.driver.find_element(*Main_Page.trailblazersPageButton)

    def openWarriorsPageButton(self):

        return self.driver.find_element(*Main_Page.warriorsPageButton)

    def openWizardsPageButton(self):

        return self.driver.find_element(*Main_Page.wizardsPageButton)

    def verifyTeamText(self):
        return self.driver.find_element(*Main_Page.TeamText)

    def pressRosterButton(self):
        return self.driver.find_element(*Main_Page.rosterTab)


    def getRosterPlayers(self):

        roster_players_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.rosterPlayers):
            parts = player.text.split(" ")
            capitalized_parts = [p.capitalize() for p in parts]
            capitalized_message = " ".join([
                word.capitalize()
                for word in player.text.split(" ")
            ])
            roster_players_list_from_site.append(capitalized_message)

        return roster_players_list_from_site

    def clickPlayer(self):
        return self.driver.find_element(*Main_Page.rosterPlayerHeader)
        #action = ActionChains(self.driver)
        #action.double_click(self.driver.find_element(*Main_Page.rosterPlayerHeader)).perform()

    def getRosterPlayersReverse(self):

        roster_players_list_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.rosterPlayersReverse):
            parts = player.text.split(" ")
            capitalized_parts = [p.capitalize() for p in parts]
            capitalized_message = " ".join([
                word.capitalize()
                for word in player.text.split(" ")
            ])
            roster_players_list_from_site_reverse.append(capitalized_message)

        return roster_players_list_from_site_reverse
    def clickPosition(self):

        return self.driver.find_element(*Main_Page.rosterPositionHeader)

        #action = ActionChains(self.driver)
        #action.double_click(self.driver.find_element(*Main_Page.rosterPositionHeader)).perform()

    def getRosterPositions(self):

        roster_positions_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.rosterPositions):
            roster_positions_list_from_site.append(player.text)

        return roster_positions_list_from_site

    def clickPosition(self):
        return self.driver.find_element(*Main_Page.rosterPositionHeader)

    def getRosterPositionsReverse(self):

        roster_positions_Reverse_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.rosterPositionsReverse):
            roster_positions_Reverse_list_from_site.append(player.text)

        return roster_positions_Reverse_list_from_site

    def clickHeight(self):
        return self.driver.find_element(*Main_Page.rosterHeightHeader)

    def getRosterHeights(self):

        roster_heights_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.rosterHeights):
            roster_heights_list_from_site.append(player.text)

        return roster_heights_list_from_site

    def getRosterHeightsReverse(self):

        roster_heights_reverse_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.rosterHeightsReverse):
            roster_heights_reverse_list_from_site.append(player.text)

        return roster_heights_reverse_list_from_site

    def clickWeight(self):
        return self.driver.find_element(*Main_Page.rosterWeightHeader)

    def getRosterWeights(self):

        roster_weights_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.rosterWeights):
            roster_weights_list_from_site.append(player.text)

        return roster_weights_list_from_site

    def getRosterWeightsReverse(self):

        roster_weights_reverse_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.rosterWeightsReverse):
            roster_weights_reverse_list_from_site.append(player.text)

        return roster_weights_reverse_list_from_site

    def clickDob(self):
        return self.driver.find_element(*Main_Page.rosterDobHeader)

    def getRosterDob(self):

        roster_dobs_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.rosterDobs):
            roster_dobs_list_from_site.append(player.text)
        #roster_dobs_list_from_site.sort(key=lambda date: datetime.strptime(date, "%d/%m/%Y"))
        return roster_dobs_list_from_site

    def getRosterDobsReverse(self):

        roster_dobs_reverse_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.rosterDobsReverse):
            roster_dobs_reverse_list_from_site.append(player.text)

        return roster_dobs_reverse_list_from_site

    def clickExperience(self):
        return self.driver.find_element(*Main_Page.rosterExperienceHeader)

    def getRosterExperience(self):

        roster_experiences_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.rosterExperiences):
            roster_experiences_list_from_site.append(player.text)
        # roster_experiences_list_from_site.sort(key=lambda date: datetime.strptime(date, "%d/%m/%Y"))
        return roster_experiences_list_from_site

    def getRosterExperiencesReverse(self):

        roster_experiences_reverse_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.rosterExperiencesReverse):
            roster_experiences_reverse_list_from_site.append(player.text)

        return roster_experiences_reverse_list_from_site

    def clickCollege(self):
        return self.driver.find_element(*Main_Page.rosterCollegeHeader)

    def getRosterCollege(self):

        roster_colleges_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.rosterColleges):
            roster_colleges_list_from_site.append(player.text)
        # roster_colleges_list_from_site.sort(key=lambda date: datetime.strptime(date, "%d/%m/%Y"))
        return roster_colleges_list_from_site

    def getRosterCollegesReverse(self):

        roster_colleges_reverse_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.rosterCollegesReverse):
            roster_colleges_reverse_list_from_site.append(player.text)

        return roster_colleges_reverse_list_from_site

        # players_salaries_methods

    def pressSalariesButton(self):
        return self.driver.find_element(*Main_Page.salariesTab)

    def getSalariesPlayers(self):

        salaries_players_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.salariesPlayers):
                parts = player.text.split(" ")
                capitalized_parts = [p.capitalize() for p in parts]
                capitalized_message = " ".join([
                    word.capitalize()
                    for word in player.text.split(" ")
                ])

                salaries_players_list_from_site.append(capitalized_message)

        return salaries_players_list_from_site

    def pressSalariesPlayersHeader(self):
        return self.driver.find_element(*Main_Page.salariesPlayersHeader)

    def getSalariesPlayersReverse(self):

        salaries_players_reverse_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.salariesPlayersReverse):
            parts = player.text.split(" ")
            capitalized_parts = [p.capitalize() for p in parts]
            capitalized_message = " ".join([
                word.capitalize()
                for word in player.text.split(" ")
            ])

            salaries_players_reverse_list_from_site.append(capitalized_message)

        return salaries_players_reverse_list_from_site

    def pressSalariesAgeHeader(self):
        return self.driver.find_element(*Main_Page.salariesAgeHeader)

    def getAgePlayers(self):

        age_players_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.agePlayers):
            age_players_list_from_site.append(player.text)

        return age_players_list_from_site

    def getAgePlayersReverse(self):

        age_players_reverse_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.agePlayersReverse):
            age_players_reverse_list_from_site.append(player.text)

        return age_players_reverse_list_from_site

    def pressSalariesEightTeenNineTeenHeader(self):
        return self.driver.find_element(*Main_Page.salariesEightTeenNineTeenHeader)

    def getEightTeenNineTeenPlayers(self):

        eight_teen_nine_teen_players_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.eightTeenNineTeenPlayers):
            eight_teen_nine_teen_players_list_from_site.append(player.text)

        eight_teen_nine_teen_players_noDollarSign = []

        for player in eight_teen_nine_teen_players_list_from_site:
            eight_teen_nine_teen_players_noDollarSign.append(player.replace(',', '').replace('$', ''))

        eight_teen_nine_teen_players_int = [int(i) for i in eight_teen_nine_teen_players_noDollarSign]

        return eight_teen_nine_teen_players_int

    def getEightTeenNineTeenPlayersReverse(self):

        eight_teen_nine_teen_players_list_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.eightTeenNineTeenPlayersReverse):
            eight_teen_nine_teen_players_list_from_site_reverse.append(player.text)

        eight_teen_nine_teen_players_noDollarSign_reverse = []

        for player in eight_teen_nine_teen_players_list_from_site_reverse:
            eight_teen_nine_teen_players_noDollarSign_reverse.append(player.replace(',', '').replace('$', ''))

        eight_teen_nine_teen_players_int_reverse = [int(i) for i in eight_teen_nine_teen_players_noDollarSign_reverse]

        return eight_teen_nine_teen_players_int_reverse

    def pressSalariesNineTeenTwentyHeader(self):
        return self.driver.find_element(*Main_Page.salariesNineTeenTwentyHeader)

    def getNineTeenTwentyPlayers(self):

        nine_teen_twenty_players_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.NineTeenTwentyPlayers):
            nine_teen_twenty_players_list_from_site.append(player.text)

        nine_teen_twenty_players_noDollarSign = []

        for player in nine_teen_twenty_players_list_from_site:
            nine_teen_twenty_players_noDollarSign.append(player.replace(',', '').replace('$', ''))

        nine_teen_twenty_players_int = [int(i) for i in nine_teen_twenty_players_noDollarSign]

        return nine_teen_twenty_players_int

    def getNineTeenTwentyPlayersReverse(self):

        nine_teen_twenty_players_list_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.NineTeenTwentyPlayersReverse):
            nine_teen_twenty_players_list_from_site_reverse.append(player.text)

        nine_teen_twenty_players_noDollarSign_reverse = []

        for player in nine_teen_twenty_players_list_from_site_reverse:
            nine_teen_twenty_players_noDollarSign_reverse.append(player.replace(',', '').replace('$', ''))

        nine_teen_twenty_players_int_reverse = [int(i) for i in nine_teen_twenty_players_noDollarSign_reverse]

        return nine_teen_twenty_players_int_reverse

    def pressSalariesTwentyTwentyOneHeader(self):
        return self.driver.find_element(*Main_Page.salariesTwentyTwentyOneHeader)

    def getTwentyTwentyOnePlayers(self):

        twenty_twenty_one_players_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.twentyTwentyOnePlayers):
            twenty_twenty_one_players_list_from_site.append(player.text)

        twenty_twenty_one_players_noDollarSign = []

        for player in twenty_twenty_one_players_list_from_site:
            twenty_twenty_one_players_noDollarSign.append(player.replace(',', '').replace('$', ''))

        twenty_twenty_one_players_int = [int(i) for i in twenty_twenty_one_players_noDollarSign]

        return twenty_twenty_one_players_int

    def getTwentyTwentyOnePlayersReverse(self):

        twenty_twenty_one_players_list_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.twentyTwentyOnePlayersReverse):
            twenty_twenty_one_players_list_from_site_reverse.append(player.text)

        twenty_twenty_one_players_noDollarSign_reverse = []

        for player in twenty_twenty_one_players_list_from_site_reverse:
            twenty_twenty_one_players_noDollarSign_reverse.append(player.replace(',', '').replace('$', ''))

        twenty_twenty_one_players_int_reverse = [int(i) for i in twenty_twenty_one_players_noDollarSign_reverse]

        return twenty_twenty_one_players_int_reverse

    def pressSalariesTwentyOneTwentyTwoHeader(self):
        return self.driver.find_element(*Main_Page.salariesTwentyOneTwentyTwoHeader)

    def getTwentyOneTwentyTwoPlayers(self):

        twenty_one_twenty_two_players_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.TwentyOneTwentyTwoPlayers):
            twenty_one_twenty_two_players_list_from_site.append(player.text)

        twenty_one_twenty_two_players_noDollarSign = []

        for player in twenty_one_twenty_two_players_list_from_site:
            twenty_one_twenty_two_players_noDollarSign.append(player.replace(',', '').replace('$', ''))

        twenty_one_twenty_two_players_int = [int(i) for i in twenty_one_twenty_two_players_noDollarSign]

        return twenty_one_twenty_two_players_int

    def getTwentyOneTwentyTwoPlayersReverse(self):

        twenty_one_twenty_two_players_list_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.TwentyOneTwentyTwoPlayersReverse):
            twenty_one_twenty_two_players_list_from_site_reverse.append(player.text)

        twenty_one_twenty_two_players_noDollarSign_reverse = []

        for player in twenty_one_twenty_two_players_list_from_site_reverse:
            twenty_one_twenty_two_players_noDollarSign_reverse.append(player.replace(',', '').replace('$', ''))

        twenty_one_twenty_two_players_int_reverse = [int(i) for i in twenty_one_twenty_two_players_noDollarSign_reverse]

        return twenty_one_twenty_two_players_int_reverse

    def pressSalariesTwentyTwoTwentyThreeHeader(self):
        return self.driver.find_element(*Main_Page.salariesTwentyTwoTwentyThreeHeader)

    def getTwentyTwoTwentyThreePlayers(self):

        twenty_two_twenty_three_players_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.TwentyTwoTwentyThreePlayers):
            twenty_two_twenty_three_players_list_from_site.append(player.text)

        twenty_two_twenty_three_players_noDollarSign = []

        for player in twenty_two_twenty_three_players_list_from_site:
            twenty_two_twenty_three_players_noDollarSign.append(player.replace(',', '').replace('$', ''))

        twenty_two_twenty_three_players_int = [int(i) for i in twenty_two_twenty_three_players_noDollarSign]

        return twenty_two_twenty_three_players_int

    def getTwentyTwoTwentyThreePlayersReverse(self):

        twenty_two_twenty_three_players_list_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.TwentyTwoTwentyThreePlayersReverse):
            twenty_two_twenty_three_players_list_from_site_reverse.append(player.text)

        twenty_two_twenty_three_players_noDollarSign_reverse = []

        for player in twenty_two_twenty_three_players_list_from_site_reverse:
            twenty_two_twenty_three_players_noDollarSign_reverse.append(player.replace(',', '').replace('$', ''))

        twenty_two_twenty_three_players_int_reverse = [int(i) for i in
                                                       twenty_two_twenty_three_players_noDollarSign_reverse]

        return twenty_two_twenty_three_players_int_reverse

    def pressSalariesGuaranteedHeader(self):
        return self.driver.find_element(*Main_Page.salariesGuaranteedHeader)

    def getGuaranteedPlayers(self):

        guaranteed_players_list_from_site = []
        for player in self.driver.find_elements(*Main_Page.guaranteedPlayers):
            guaranteed_players_list_from_site.append(player.text)

        guaranteed_players_noDollarSign = []

        for player in guaranteed_players_list_from_site:
            guaranteed_players_noDollarSign.append(player.replace(',', '').replace('$', ''))

        guaranteed_players_int = [int(i) for i in guaranteed_players_noDollarSign]

        return guaranteed_players_int

    def getGuaranteedPlayersReverse(self):

        guaranteed_players_list_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.guaranteedPlayersReverse):
            guaranteed_players_list_from_site_reverse.append(player.text)

        guaranteed_players_noDollarSign_reverse = []

        for player in guaranteed_players_list_from_site_reverse:
            guaranteed_players_noDollarSign_reverse.append(player.replace(',', '').replace('$', ''))

        guaranteed_players_int_reverse = [int(i) for i in guaranteed_players_noDollarSign_reverse]

        return guaranteed_players_int_reverse

    def getIsPlayer(self):
        return self.driver.find_element(*Main_Page.isPlayer)

    def closePlayerStatsCloseButton(self):
        return self.driver.find_element(*Main_Page.playerStatsCloseButton)

    def getPlayerName(self):

        fullText = self.driver.find_element(*Main_Page.playerName).text
        var = fullText.split(" ")
        playerName = var[0]+" "+var[1]
        return playerName

    def getRosterPlayersForPlayerStats(self):
        return self.driver.find_elements(*Main_Page.rosterPlayers)

    def pressPlayersStatsSeasonsHeader(self):

        return self.driver.find_element(*Main_Page.playersStatsSeasonsHeader)

    def getPlayersStatsSeasons(self):

        players_stats_seasons_from_site = []
        for player in self.driver.find_elements(*Main_Page.seasonsPlayersStats):
            players_stats_seasons_from_site.append(player.text)

        return players_stats_seasons_from_site

    def getPlayersStatsSeasonsReverse(self):

        players_stats_seasons_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.seasonsPlayersStatsReverse):
            players_stats_seasons_from_site_reverse.append(player.text)

        return players_stats_seasons_from_site_reverse

    def pressPlayersStatsteamsHeader(self):

        return self.driver.find_element(*Main_Page.playersStatsTeamHeader)

    def getPlayersStatsteams(self):

        players_stats_teams_from_site = []
        for player in self.driver.find_elements(*Main_Page.teamsPlayersStats):
            players_stats_teams_from_site.append(player.text)

        return players_stats_teams_from_site

    def getPlayersStatsteamsReverse(self):

        players_stats_teams_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.teamsPlayersStatsReverse):
            players_stats_teams_from_site_reverse.append(player.text)

        return players_stats_teams_from_site_reverse

    def pressPlayersStatsnumGamesHeader(self):

        return self.driver.find_element(*Main_Page.playersStatsNumGamesHeader)

    def getPlayersStatsNumGames(self):

        players_stats_num_games_from_site = []
        for player in self.driver.find_elements(*Main_Page.numGamesPlayersStats):
            players_stats_num_games_from_site.append(player.text)

        return players_stats_num_games_from_site

    def getPlayersStatsNumGamesReverse(self):

        players_stats_num_games_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.numGamesPlayersStatsReverse):
            players_stats_num_games_from_site_reverse.append(player.text)

        return players_stats_num_games_from_site_reverse

    def pressPlayersStatsNumGamesStartedHeader(self):

        return self.driver.find_element(*Main_Page.playersStatsNumGamesStartedHeader)

    def getPlayersStatsNumGamesStarted(self):

        players_stats_num_games_started_from_site = []
        for player in self.driver.find_elements(*Main_Page.NumGamesStartedPlayersStats):
            players_stats_num_games_started_from_site.append(player.text)

        return players_stats_num_games_started_from_site

    def getPlayersStatsNumGamesStartedReverse(self):

        players_stats_num_games_started_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.NumGamesStartedPlayersStatsReverse):
            players_stats_num_games_started_from_site_reverse.append(player.text)

        return players_stats_num_games_started_from_site_reverse

    def pressPlayersStatsMinutesPlayedHeader(self):

        return self.driver.find_element(*Main_Page.playersStatsMinutesPlayedHeader)

    def getPlayersStatsMinutesPlayed(self):

        players_stats_minutes_played_from_site = []
        for player in self.driver.find_elements(*Main_Page.minutesPlayedPlayersStats):
            players_stats_minutes_played_from_site.append(player.text)

        return players_stats_minutes_played_from_site

    def getPlayersStatsMinutesPlayedReverse(self):

        players_stats_minutes_played_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.minutesPlayedPlayersStatsReverse):
            players_stats_minutes_played_from_site_reverse.append(player.text)

        return players_stats_minutes_played_from_site_reverse

    def pressPlayersStatsFieldGoalsPercentageHeader(self):

        return self.driver.find_element(*Main_Page.playersStatsFieldGoalsPercentageHeader)

    def getPlayersStatsFieldGoalsPercentage(self):

        players_stats_field_goals_percentage_from_site = []
        for player in self.driver.find_elements(*Main_Page.FieldGoalsPercentagePlayersStats):
            players_stats_field_goals_percentage_from_site.append(player.text)

        return players_stats_field_goals_percentage_from_site

    def getPlayersStatsFieldGoalsPercentageReverse(self):

        players_stats_field_goals_percentage_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.FieldGoalsPercentagePlayersStatsReverse):
            players_stats_field_goals_percentage_from_site_reverse.append(player.text)

        return players_stats_field_goals_percentage_from_site_reverse

    def pressPlayersStatsThreePointPercentageHeader(self):

        return self.driver.find_element(*Main_Page.playersStatsThreePointPercentageHeader)

    def getPlayersStatsThreePointPercentage(self):

        players_stats_three_point_percentage_from_site = []
        for player in self.driver.find_elements(*Main_Page.ThreePointPercentagePlayersStats):
            players_stats_three_point_percentage_from_site.append(player.text)

        return players_stats_three_point_percentage_from_site

    def getPlayersStatsThreePointPercentageReverse(self):

        players_stats_three_point_percentage_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.ThreePointPercentagePlayersStatsReverse):
            players_stats_three_point_percentage_from_site_reverse.append(player.text)

        return players_stats_three_point_percentage_from_site_reverse

    def pressPlayersStatsFreeThrowPercentageHeader(self):

        return self.driver.find_element(*Main_Page.playersStatsFreeThrowPercentageHeader)

    def getPlayersStatsFreethrowPercentage(self):

        players_stats_free_throw_percentage_from_site = []
        for player in self.driver.find_elements(*Main_Page.freeThrowPercentagePlayersStats):
            players_stats_free_throw_percentage_from_site.append(player.text)

        return players_stats_free_throw_percentage_from_site

    def getPlayersStatsFreethrowPercentageReverse(self):
        players_stats_free_throw_percentage_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.freeThrowPercentagePlayersStatsReverse):
            players_stats_free_throw_percentage_from_site_reverse.append(player.text)

        return players_stats_free_throw_percentage_from_site_reverse

    def pressPlayersStatsReboundsHeader(self):

        return self.driver.find_element(*Main_Page.playersStatsReboundsHeader)

    def getPlayersStatsRebounds(self):

        players_stats_rebounds_from_site = []
        for player in self.driver.find_elements(*Main_Page.reboundsPlayersStats):
            players_stats_rebounds_from_site.append(player.text)

        return players_stats_rebounds_from_site

    def getPlayersStatsReboundsReverse(self):

        players_stats_rebounds_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.reboundsPlayersStatsReverse):
            players_stats_rebounds_from_site_reverse.append(player.text)

        return players_stats_rebounds_from_site_reverse

    def pressPlayersStatsAssistsHeader(self):

        return self.driver.find_element(*Main_Page.playersStatsAssistsHeader)

    def getPlayersStatsAssists(self):

        players_stats_assists_from_site = []
        for player in self.driver.find_elements(*Main_Page.assistsPlayersStats):
            players_stats_assists_from_site.append(player.text)

        return players_stats_assists_from_site

    def getPlayersStatsAssistsReverse(self):

        players_stats_assists_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.assistsPlayersStatsReverse):
            players_stats_assists_from_site_reverse.append(player.text)

        return players_stats_assists_from_site_reverse

    def pressPlayersStatsStealsHeader(self):

        return self.driver.find_element(*Main_Page.playersStatsStealsHeader)

    def getPlayersStatsSteals(self):

        players_stats_steals_from_site = []
        for player in self.driver.find_elements(*Main_Page.stealsPlayersStats):
            players_stats_steals_from_site.append(player.text)

        return players_stats_steals_from_site

    def getPlayersStatsStealsReverse(self):

        players_stats_steals_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.stealsPlayersStatsReverse):
            players_stats_steals_from_site_reverse.append(player.text)

        return players_stats_steals_from_site_reverse

    def pressPlayersStatsBlocksHeader(self):

        return self.driver.find_element(*Main_Page.playersStatsBlocksHeader)

    def getPlayersStatsBlocks(self):

        players_stats_blocks_from_site = []
        for player in self.driver.find_elements(*Main_Page.blocksPlayersStats):
            players_stats_blocks_from_site.append(player.text)

        return players_stats_blocks_from_site

    def getPlayersStatsBlocksReverse(self):

        players_stats_blocks_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.blocksPlayersStatsReverse):
            players_stats_blocks_from_site_reverse.append(player.text)

        return players_stats_blocks_from_site_reverse

    def pressPlayersStatsTurnoversHeader(self):

        return self.driver.find_element(*Main_Page.playersStatsTurnoversHeader)

    def getPlayersStatsTurnovers(self):

        players_stats_turnovers_from_site = []
        for player in self.driver.find_elements(*Main_Page.turnoversPlayersStats):
            players_stats_turnovers_from_site.append(player.text)

        return players_stats_turnovers_from_site

    def getPlayersStatsTurnoversReverse(self):

        players_stats_turnovers_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.turnoversPlayersStatsReverse):
            players_stats_turnovers_from_site_reverse.append(player.text)

        return players_stats_turnovers_from_site_reverse

    def pressPlayersStatsPointsHeader(self):

        return self.driver.find_element(*Main_Page.playersStatsPointsHeader)

    def getPlayersStatsPoints(self):

        players_stats_points_from_site = []
        for player in self.driver.find_elements(*Main_Page.pointsPlayersStats):
            players_stats_points_from_site.append(player.text)

        return players_stats_points_from_site

    def getPlayersStatsPointsReverse(self):

        players_stats_points_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.pointsPlayersStatsReverse):
            players_stats_points_from_site_reverse.append(player.text)

        return players_stats_points_from_site_reverse

    def pressPlayersStatsDoubleDoublesHeader(self):

        return self.driver.find_element(*Main_Page.playersStatsDoubleDoublesHeader)

    def getPlayersStatsDoubleDoubles(self):

        players_stats_double_doubles_from_site = []
        for player in self.driver.find_elements(*Main_Page.doubleDoublesPlayersStats):
            players_stats_double_doubles_from_site.append(player.text)

        return players_stats_double_doubles_from_site

    def getPlayersStatsDoubleDoublesReverse(self):

        players_stats_double_doubles_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.doubleDoublesPlayersStatsReverse):
            players_stats_double_doubles_from_site_reverse.append(player.text)

        return players_stats_double_doubles_from_site_reverse

    def pressPlayersStatsTripleDoublesHeader(self):

        return self.driver.find_element(*Main_Page.playersStatsTripleDoublesHeader)

    def getPlayersStatsTripleDoubles(self):

        players_stats_triple_doubles_from_site = []
        for player in self.driver.find_elements(*Main_Page.tripleDoublesPlayersStats):
            players_stats_triple_doubles_from_site.append(player.text)

        return players_stats_triple_doubles_from_site

    def getPlayersStatsTripleDoublesReverse(self):

        players_stats_triple_doubles_from_site_reverse = []
        for player in self.driver.find_elements(*Main_Page.tripleDoublesPlayersStatsReverse):
            players_stats_triple_doubles_from_site_reverse.append(player.text)

        return players_stats_triple_doubles_from_site_reverse

    def getGaurd(self):

        return self.driver.find_element(*Main_Page.gaurdPresence)

    def getTeamText(self):
        return self.driver.find_elements(*Main_Page.TeamText)















