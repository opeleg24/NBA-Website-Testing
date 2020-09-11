import inspect
import logging
import time

import pytest
from selenium.common.exceptions import WebDriverException, ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Main_Page import Main_Page


@pytest.mark.usefixtures("setup")
class BaseClass:
    #pass

    def waitForElement(self, Text):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, Text)))

    def waitForPageComplete(self):

        source = self.driver.page_source

        def compare_source(driver):
            try:
                return source != driver.page_source
            except WebDriverException:
                pass

        WebDriverWait(self.driver, 5).until(compare_source)

    # PlayerNameHeadLine
    def waitForPlayerNameHeadLine(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "PlayerNameHeadLine")))

    def waitForTeamText(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//table[@id='TeamData']//tr[2]//td")))

    def waitForRosterList(self):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//ul[@class='player']/li/a")))

    def waitForRosterPlayerHeaderClickable(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Player")))

    def waitForSalariesPlayerHeaderClickable(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//tr[@id='PayRolltr']/th[1]/a[1]")))

    def waitForTeamClickable(self, Team):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, Team)))


    def waitForIsPlayer(self):
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//table[@id='PlayerSeasonStatsTable']/tbody/tr[2]/td[1]")))

    def waitForGaurd(self, Text):
            wait = WebDriverWait(self.driver, 5)
            wait.until(expected_conditions.presence_of_element_located((By.XPATH, Text)))


    def implicitlyWait(self):
        self.driver.implicitly_wait(5)

    def Bucks_Page(self):
        buckspage = Main_Page(self.driver)
        return buckspage

    def Bulls_Page(self):
        bullspage = Main_Page(self.driver)
        return bullspage

    def Cavaliers_Page(self):
        cavalierspage = Main_Page(self.driver)
        return cavalierspage

    def Celtics_Page(self):
        celticspage = Main_Page(self.driver)
        return celticspage

    def Clippers_Page(self):
        clipperspage = Main_Page(self.driver)
        return clipperspage

    def Grizzlies_Page(self):
        grizzliespage = Main_Page(self.driver)
        return grizzliespage

    def Hawks_Page(self):
        hawkspage = Main_Page(self.driver)
        return hawkspage

    def Heat_Page(self):
        heatpage = Main_Page(self.driver)
        return heatpage

    def Hornets_Page(self):
        hornetspage = Main_Page(self.driver)
        return hornetspage

    def Jazz_Page(self):
        jazzpage = Main_Page(self.driver)
        return jazzpage

    def Kings_Page(self):
        kingspage = Main_Page(self.driver)
        return kingspage

    def Knicks_Page(self):
        knickspage = Main_Page(self.driver)
        return knickspage

    def Lakers_Page(self):
        lakerspage = Main_Page(self.driver)
        return lakerspage

    def Magic_Page(self):
        magicpage = Main_Page(self.driver)
        return magicpage

    def Mavericks_Page(self):
        maverickspage = Main_Page(self.driver)
        return maverickspage

    def Nets_Page(self):
        netspage = Main_Page(self.driver)
        return netspage

    def Nuggets_Page(self):
        nuggetspage = Main_Page(self.driver)
        return nuggetspage

    def Pacers_Page(self):
        pacerspage = Main_Page(self.driver)
        return pacerspage

    def Pelicans_Page(self):
        pelicanspage = Main_Page(self.driver)
        return pelicanspage

    def Pistons_Page(self):
        pistonspage = Main_Page(self.driver)
        return pistonspage

    def Raptors_Page(self):
        raptorspage = Main_Page(self.driver)
        return raptorspage

    def Rockets_Page(self):
        rocketspage = Main_Page(self.driver)
        return rocketspage

    def Spurs_Page(self):
        spurspage = Main_Page(self.driver)
        return spurspage

    def Suns_Page(self):
        sunspage = Main_Page(self.driver)
        return sunspage

    def Thunder_Page(self):
        thunderpage = Main_Page(self.driver)
        return thunderpage

    def Timberwolves_Page(self):
        timberwolvespage = Main_Page(self.driver)
        return timberwolvespage

    def Trailblazers_Page(self):
        trailblazers = Main_Page(self.driver)
        return trailblazers

    def Warriors_Page(self):
        warriors = Main_Page(self.driver)
        return warriors

    def Wizards_Page(self):
        wizards = Main_Page(self.driver)
        return wizards




    def getLogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)

        return logger

    def actionObject(self):
        action = ActionChains(self.driver)

        return action

    @pytest.fixture()
    def grizzlies_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Grizzlies_Page().openGrizzliesPageButton().click()
        self.waitForElement("Salaries")
        self.Grizzlies_Page().pressSalariesButton().click()

        

    @pytest.fixture()
    def grizzlies_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Grizzlies_Page().openGrizzliesPageButton().click()
        self.waitForElement("Roster")
        self.Grizzlies_Page().pressRosterButton().click()
        

    @pytest.fixture()
    def bulls_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Bulls_Page().openBullsPageButton().click()
        self.waitForElement("Salaries")
        self.Bulls_Page().pressSalariesButton().click()
        
        #self.waitForElement("//td[text()='$0']")

    @pytest.fixture()
    def bulls_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Bulls_Page().openBullsPageButton().click()
        self.waitForElement("Roster")
        self.Bulls_Page().pressRosterButton().click()
        

    @pytest.fixture()
    def hawks_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Hawks_Page().openHawksPageButton().click()
        self.waitForElement("Roster")
        self.Hawks_Page().pressRosterButton().click()
        #
        #self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def hawks_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Hawks_Page().openHawksPageButton().click()
        self.waitForElement("Salaries")
        self.Hawks_Page().pressSalariesButton().click()
        #


    @pytest.fixture()
    def bucks_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Bucks_Page().openBucksPageButton().click()
        self.waitForElement("Roster")
        self.Bucks_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def bucks_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Bucks_Page().openBucksPageButton().click()
        self.waitForElement("Salaries")
        self.Bucks_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def cavaliers_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Cavaliers_Page().openCavaliersPageButton().click()
        self.waitForElement("Roster")
        self.Cavaliers_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def cavaliers_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Cavaliers_Page().openCavaliersPageButton().click()
        self.waitForElement("Salaries")
        self.Cavaliers_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def celtics_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Celtics_Page().openCelticsPageButton().click()
        self.waitForElement("Roster")
        self.Celtics_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def celtics_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Celtics_Page().openCelticsPageButton().click()
        self.waitForElement("Salaries")
        self.Celtics_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def clippers_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Clippers_Page().openClippersPageButton().click()
        self.waitForElement("Roster")
        self.Clippers_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def clippers_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Clippers_Page().openClippersPageButton().click()
        self.waitForElement("Salaries")
        self.Clippers_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def heat_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Heat_Page().openHeatPageButton().click()
        self.waitForElement("Roster")
        self.Heat_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def heat_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Heat_Page().openHeatPageButton().click()
        self.waitForElement("Salaries")
        self.Heat_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def hornets_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Hornets_Page().openHornetsPageButton().click()
        self.waitForElement("Roster")
        self.Hornets_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def hornets_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Hornets_Page().openHornetsPageButton().click()
        self.waitForElement("Salaries")
        self.Hornets_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def jazz_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Jazz_Page().openJazzPageButton().click()
        self.waitForElement("Roster")
        self.Jazz_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def jazz_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Jazz_Page().openJazzPageButton().click()
        self.waitForElement("Salaries")
        self.Jazz_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def kings_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Kings_Page().openKingsPageButton().click()
        self.waitForElement("Roster")
        self.Kings_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def kings_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Kings_Page().openKingsPageButton().click()
        self.waitForElement("Salaries")
        self.Kings_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def knicks_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Knicks_Page().openKnicksPageButton().click()
        self.waitForElement("Roster")
        self.Knicks_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def knicks_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Knicks_Page().openKnicksPageButton().click()
        self.waitForElement("Salaries")
        self.Knicks_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def lakers_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Lakers_Page().openLakersPageButton().click()
        self.waitForElement("Roster")
        self.Lakers_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def lakers_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Lakers_Page().openLakersPageButton().click()
        self.waitForElement("Salaries")
        self.Lakers_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def magic_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Magic_Page().openMagicPageButton().click()
        self.waitForElement("Roster")
        self.Magic_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def magic_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Magic_Page().openMagicPageButton().click()
        self.waitForElement("Salaries")
        self.Magic_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def mavericks_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Mavericks_Page().openMavericksPageButton().click()
        self.waitForElement("Roster")
        self.Mavericks_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def mavericks_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Mavericks_Page().openMavericksPageButton().click()
        self.waitForElement("Salaries")
        self.Mavericks_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def nets_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Nets_Page().openNetsPageButton().click()
        self.waitForElement("Roster")
        self.Nets_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def nets_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Nets_Page().openNetsPageButton().click()
        self.waitForElement("Salaries")
        self.Nets_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def nuggets_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Nuggets_Page().openNuggetsPageButton().click()
        self.waitForElement("Roster")
        self.Nuggets_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def nuggets_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Nuggets_Page().openNuggetsPageButton().click()
        self.waitForElement("Salaries")
        self.Nuggets_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def pacers_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Pacers_Page().openPacersPageButton().click()
        self.waitForElement("Roster")
        self.Pacers_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def pacers_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Pacers_Page().openPacersPageButton().click()
        self.waitForElement("Salaries")
        self.Pacers_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def pelicans_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Pelicans_Page().openPelicansPageButton().click()
        self.waitForElement("Roster")
        self.Pelicans_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def pelicans_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Pelicans_Page().openPelicansPageButton().click()
        self.waitForElement("Salaries")
        self.Pelicans_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def pistons_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Pistons_Page().openPistonsPageButton().click()
        self.waitForElement("Roster")
        self.Pistons_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def pistons_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Pistons_Page().openPistonsPageButton().click()
        self.waitForElement("Salaries")
        self.Pistons_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def raptors_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Raptors_Page().openRaptorsPageButton().click()
        self.waitForElement("Roster")
        self.Raptors_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def raptors_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Raptors_Page().openRaptorsPageButton().click()
        self.waitForElement("Salaries")
        self.Raptors_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def rockets_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Rockets_Page().openRocketsPageButton().click()
        self.waitForElement("Roster")
        self.Rockets_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def rockets_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Rockets_Page().openRocketsPageButton().click()
        self.waitForElement("Salaries")
        self.Rockets_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def spurs_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Spurs_Page().openSpursPageButton().click()
        self.waitForElement("Roster")
        self.Spurs_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def spurs_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Spurs_Page().openSpursPageButton().click()
        self.waitForElement("Salaries")
        self.Spurs_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def suns_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Suns_Page().openSunsPageButton().click()
        self.waitForElement("Roster")
        self.Suns_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def suns_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Suns_Page().openSunsPageButton().click()
        self.waitForElement("Salaries")
        self.Suns_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def thunder_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Thunder_Page().openThunderPageButton().click()
        self.waitForElement("Roster")
        self.Thunder_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def thunder_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Thunder_Page().openThunderPageButton().click()
        self.waitForElement("Salaries")
        self.Thunder_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def timberwolves_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Timberwolves_Page().openTimberwolvesPageButton().click()
        self.waitForElement("Roster")
        self.Timberwolves_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def timberwolves_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Timberwolves_Page().openTimberwolvesPageButton().click()
        self.waitForElement("Salaries")
        self.Timberwolves_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def trailblazers_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Trailblazers_Page().openTrailblazersPageButton().click()
        self.waitForElement("Roster")
        self.Trailblazers_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def trailblazers_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Trailblazers_Page().openTrailblazersPageButton().click()
        self.waitForElement("Salaries")
        self.Trailblazers_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def warriors_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Warriors_Page().openWarriorsPageButton().click()
        self.waitForElement("Roster")
        self.Warriors_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def warriors_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Warriors_Page().openWarriorsPageButton().click()
        self.waitForElement("Salaries")
        self.Warriors_Page().pressSalariesButton().click()
        

    @pytest.fixture()
    def wizards_roster_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Wizards_Page().openWizardsPageButton().click()
        self.waitForElement("Roster")
        self.Wizards_Page().pressRosterButton().click()
        
        # self.waitForElement("//td[text()='C']")

    @pytest.fixture()
    def wizards_salaries_team_setup(self):
        # log.info("Opening Grizzlies Page")
        self.Wizards_Page().openWizardsPageButton().click()
        self.waitForElement("Salaries")
        self.Wizards_Page().pressSalariesButton().click()
        







