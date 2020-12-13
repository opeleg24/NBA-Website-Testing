from datetime import datetime

from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from pageObjects.Main_Page import Main_Page
from utilities.BaseClass import BaseClass


class TestLosAngelesLakersPage(BaseClass):

    def test_los_angeles_lakers_franchise_verifiy_team(self):
        log = self.getLogger()
        log.info("Opening Los Angeles Lakers Page")
        self.waitForTeamClickable("a[href='#!Lakers']")
        self.Lakers_Page().openLakersPageButton().click()
        self.waitForTeamText()
        log.info("Verify Los Angeles Lakers Page")
        assert "Los Angeles Lakers" in self.Lakers_Page().verifyTeamText().text

    @pytest.mark.usefixtures("lakers_salaries_team_setup")
    def test_los_angeles_lakers_salaries_sorted_players_column(self):
        log = self.getLogger()
        self.waitForGaurd("//td[text()='$0']")
        self.waitForSalariesPlayerHeaderClickable()
        self.Lakers_Page().pressSalariesPlayersHeader().click()
        salaries_players_sorted = sorted(self.Lakers_Page().getSalariesPlayers())
        log.info("Testing if Column 'Player' in Salaries Table is Ascending")
        assert self.Lakers_Page().getSalariesPlayers() == salaries_players_sorted

    def test_los_angeles_lakers_salaries_sorted_players_reverse_column(self):
        log = self.getLogger()

        self.Lakers_Page().pressSalariesPlayersHeader().click()
        salaries_players_sorted = sorted(self.Lakers_Page().getSalariesPlayersReverse(), reverse=True)
        log.info("Testing if Column 'Player' in Salaries Table is Descending")
        assert self.Lakers_Page().getSalariesPlayersReverse() == salaries_players_sorted

    def test_los_angeles_lakers_salaries_sorted_age_column(self):
        log = self.getLogger()

        self.Lakers_Page().pressSalariesAgeHeader().click()
        age_players_sorted = sorted(self.Lakers_Page().getAgePlayers(), reverse=True)
        log.info("Testing if Column 'Age' in Salaries Table is Descending")
        assert self.Lakers_Page().getAgePlayers() == age_players_sorted

    def test_los_angeles_lakers_salaries_sorted_age_reverse_column(self):
        log = self.getLogger()

        self.Lakers_Page().pressSalariesAgeHeader().click()
        age_players_sorted = sorted(self.Lakers_Page().getAgePlayersReverse())
        log.info("Testing if Column 'Age' in Salaries Table is Ascending")
        assert self.Lakers_Page().getAgePlayersReverse() == age_players_sorted

    def test_los_angeles_lakers_salaries_sorted_eight_teen_nine_teen_column(self):
        log = self.getLogger()

        self.Lakers_Page().pressSalariesEightTeenNineTeenHeader().click()
        eight_teen_nine_teen_players_sorted = sorted(self.Lakers_Page().getEightTeenNineTeenPlayers(), reverse=True)
        log.info("Testing if Column '2018-19' in Salaries Table is Descending")
        assert eight_teen_nine_teen_players_sorted == self.Lakers_Page().getEightTeenNineTeenPlayers()

    def test_los_angeles_lakers_salaries_sorted_eight_teen_nine_teen_reverse_column(self):
        log = self.getLogger()

        self.Lakers_Page().pressSalariesEightTeenNineTeenHeader().click()
        eight_teen_nine_teen_players_sorted_reverse = sorted(self.Lakers_Page().getEightTeenNineTeenPlayersReverse())
        log.info("Testing if Column '2018-19' in Salaries Table is Ascending")
        assert eight_teen_nine_teen_players_sorted_reverse == self.Lakers_Page().getEightTeenNineTeenPlayersReverse()

    def test_los_angeles_lakers_salaries_sorted_nine_teen_twenty_column(self):
        log = self.getLogger()

        self.Lakers_Page().pressSalariesNineTeenTwentyHeader().click()
        nine_teen_twenty_players_sorted = sorted(self.Lakers_Page().getNineTeenTwentyPlayers(), reverse=True)
        log.info("Testing if Column '2019-20' in Salaries Table is Descending")
        assert nine_teen_twenty_players_sorted == self.Lakers_Page().getNineTeenTwentyPlayers()

    def test_los_angeles_lakers_salaries_sorted_nine_teen_twenty_reverse_column(self):
        log = self.getLogger()

        self.Lakers_Page().pressSalariesNineTeenTwentyHeader().click()
        nine_teen_twenty_players_sorted_reverse = sorted(self.Lakers_Page().getNineTeenTwentyPlayersReverse())
        log.info("Testing if Column '2019-20' in Salaries Table is Ascending")
        assert nine_teen_twenty_players_sorted_reverse == self.Lakers_Page().getNineTeenTwentyPlayersReverse()

    def test_los_angeles_lakers_salaries_sorted_twenty_twenty_one_column(self):
        log = self.getLogger()

        self.Lakers_Page().pressSalariesTwentyTwentyOneHeader().click()
        twenty_twenty_one_players_sorted = sorted(self.Lakers_Page().getTwentyTwentyOnePlayers(), reverse=True)
        log.info("Testing if Column '2020-21' in Salaries Table is Descending")
        assert twenty_twenty_one_players_sorted == self.Lakers_Page().getTwentyTwentyOnePlayers()

    def test_los_angeles_lakers_salaries_sorted_twenty_twenty_one_reverse_column(self):
        log = self.getLogger()

        self.Lakers_Page().pressSalariesTwentyTwentyOneHeader().click()
        twenty_twenty_one_players_sorted_reverse = sorted(self.Lakers_Page().getTwentyTwentyOnePlayersReverse())
        log.info("Testing if Column '2020-21' in Salaries Table is Ascending")
        assert twenty_twenty_one_players_sorted_reverse == self.Lakers_Page().getTwentyTwentyOnePlayersReverse()

    def test_los_angeles_lakers_salaries_sorted_twenty_one_twenty_two_column(self):
        log = self.getLogger()

        self.Lakers_Page().pressSalariesTwentyOneTwentyTwoHeader().click()
        twenty_one_twenty_two_players_sorted = sorted(self.Lakers_Page().getTwentyOneTwentyTwoPlayers(),
                                                      reverse=True)
        log.info("Testing if Column '2021-22' in Salaries Table is Descending")

        assert twenty_one_twenty_two_players_sorted == self.Lakers_Page().getTwentyOneTwentyTwoPlayers()

    def test_los_angeles_lakers_salaries_sorted_twenty_one_twenty_two_reverse_column(self):
        log = self.getLogger()

        self.Lakers_Page().pressSalariesTwentyOneTwentyTwoHeader().click()
        twenty_one_twenty_two_players_sorted_reverse = sorted(
            self.Lakers_Page().getTwentyOneTwentyTwoPlayersReverse())
        log.info("Testing if Column '2021-22' in Salaries Table is Ascending")
        assert twenty_one_twenty_two_players_sorted_reverse == self.Lakers_Page().getTwentyOneTwentyTwoPlayersReverse()

    def test_los_angeles_lakers_salaries_sorted_twenty_two_twenty_three_column(self):
        log = self.getLogger()

        self.Lakers_Page().pressSalariesTwentyTwoTwentyThreeHeader().click()
        twenty_two_twenty_three_players_sorted = sorted(self.Lakers_Page().getTwentyTwoTwentyThreePlayers(),
                                                        reverse=True)
        log.info("Testing if Column '2022-23' in Salaries Table is Descending")

        assert twenty_two_twenty_three_players_sorted == self.Lakers_Page().getTwentyTwoTwentyThreePlayers()

    def test_los_angeles_lakers_salaries_sorted_twenty_two_twenty_threereverse_column(self):
        log = self.getLogger()

        self.Lakers_Page().pressSalariesTwentyTwoTwentyThreeHeader().click()

        twenty_two_twenty_three_players_sorted_reverse = sorted(
            self.Lakers_Page().getTwentyTwoTwentyThreePlayersReverse())
        log.info("Testing if Column '2022-23' in Salaries Table is Ascending")

        assert twenty_two_twenty_three_players_sorted_reverse == self.Lakers_Page().getTwentyTwoTwentyThreePlayersReverse()

    def test_los_angeles_lakers_salaries_sorted_guranteed_column(self):
        log = self.getLogger()

        self.Lakers_Page().pressSalariesGuaranteedHeader().click()
        guaranteed_players_sorted = sorted(self.Lakers_Page().getGuaranteedPlayers(), reverse=True)
        log.info("Testing if Column 'Guaranteed' in Salaries Table is Descending")
        assert guaranteed_players_sorted == self.Lakers_Page().getGuaranteedPlayers()

    def test_los_angeles_lakers_salaries_sorted_guranteed_reverse_column(self):
        log = self.getLogger()
        self.Lakers_Page().pressSalariesGuaranteedHeader().click()
        guaranteed_players_sorted_reverse = sorted(self.Lakers_Page().getGuaranteedPlayersReverse())
        log.info("Testing if Column 'Guaranteed' in Salaries Table is Ascending")
        assert guaranteed_players_sorted_reverse == self.Lakers_Page().getGuaranteedPlayersReverse()

    @pytest.mark.usefixtures("lakers_roster_team_setup")
    def test_los_angeles_lakers_roster_sorted_players_column(self):
        log = self.getLogger()

        self.Lakers_Page().clickPlayer().click()
        time.sleep(7)

        roster_player_sorted = sorted(self.Lakers_Page().getRosterPlayers())

        log.info("Testing if Column 'Players' in Roster Table is Descending")

        assert self.Lakers_Page().getRosterPlayers() == roster_player_sorted

    def test_los_angeles_lakers_roster_sorted_players_reverse_column(self):
        log = self.getLogger()
        self.Lakers_Page().clickPlayer().click()
        roster_player_sorted_reverse = sorted(self.Lakers_Page().getRosterPlayersReverse(), reverse=True)
        log.info("Testing if Column 'Players' in Roster Table is Ascending")
        assert self.Lakers_Page().getRosterPlayersReverse() == roster_player_sorted_reverse

    def test_los_angeles_lakers_roster_sorted_position_column(self):
        log = self.getLogger()
        self.Lakers_Page().clickPosition().click()
        roster_positions_sorted = sorted(self.Lakers_Page().getRosterPositions(), reverse=True)
        log.info("Testing if Column 'Position' in Roster Table is Descending")
        assert self.Lakers_Page().getRosterPositions() == roster_positions_sorted

        self.Lakers_Page().clickPosition().click()

    def test_los_angeles_lakers_roster_sorted_position_reverse_column(self):
        log = self.getLogger()
        roster_positions_reverse_sorted = sorted(self.Lakers_Page().getRosterPositionsReverse())
        log.info("Testing if Column 'Position' in Roster Table is Ascending")
        assert self.Lakers_Page().getRosterPositionsReverse() == roster_positions_reverse_sorted

    def test_los_angeles_lakers_roster_sorted_height_column(self):
        log = self.getLogger()
        self.Lakers_Page().clickHeight().click()
        roster_heights_sorted = sorted(self.Lakers_Page().getRosterHeights(), reverse=True)
        log.info("Testing if Column 'Height' in Roster Table is Descending")
        assert self.Lakers_Page().getRosterHeights() == roster_heights_sorted

    def test_los_angeles_lakers_roster_sorted_height_reverse_column(self):
        log = self.getLogger()
        self.Lakers_Page().clickHeight().click()

        roster_heights_sorted_reverse = sorted(self.Lakers_Page().getRosterHeightsReverse())
        log.info("Testing if Column 'Height' in Roster Table is Ascending")
        assert self.Lakers_Page().getRosterHeightsReverse() == roster_heights_sorted_reverse

    def test_los_angeles_lakers_roster_sorted_weight_column(self):
        log = self.getLogger()
        self.Lakers_Page().clickWeight().click()
        roster_weights_int = [int(i) for i in self.Lakers_Page().getRosterWeights()]
        roster_weights_sorted = sorted(roster_weights_int, reverse=True)
        log.info("Testing if Column 'Weight' in Roster Table is Descending")
        assert roster_weights_int == roster_weights_sorted

    def test_los_angeles_lakers_roster_sorted_weight_reverse_column(self):
        log = self.getLogger()
        self.Lakers_Page().clickWeight().click()
        roster_weights_reverse_int = [int(i) for i in self.Lakers_Page().getRosterWeightsReverse()]
        roster_weights_sorted_reverse = sorted(roster_weights_reverse_int)
        log.info("Testing if Column 'Weight' in Roster Table is Ascending")
        assert roster_weights_reverse_int == roster_weights_sorted_reverse

    def test_los_angeles_lakers_roster_sorted_dob_column(self):
        log = self.getLogger()
        self.Lakers_Page().clickDob().click()
        self.Lakers_Page().getRosterDob().sort(key=lambda date: datetime.strptime(date, "%d/%m/%Y"))
        log.info("Testing if Column 'Date of Birth' in Roster Table is Ascending")
        dob_sorted = self.Lakers_Page().getRosterDob()
        assert dob_sorted == self.Lakers_Page().getRosterDob()

    def test_los_angeles_lakers_roster_sorted_dob_reverse_column(self):
        log = self.getLogger()
        self.Lakers_Page().clickDob().click()
        self.Lakers_Page().getRosterDobsReverse().sort(key=lambda date: datetime.strptime(date, "%d/%m/%Y"),
                                                       reverse=True)
        log.info("Testing if Column 'Date of Birth' in Roster Table is Descending")
        dob_sorted_reverse = self.Lakers_Page().getRosterDobsReverse()
        assert dob_sorted_reverse == self.Lakers_Page().getRosterDobsReverse()

    def test_los_angeles_lakers_roster_sorted_experience_column(self):
        log = self.getLogger()
        self.Lakers_Page().clickExperience().click()
        roster_experiences_int = [int(i) for i in self.Lakers_Page().getRosterExperience()]
        roster_experiences_sorted = sorted(roster_experiences_int, reverse=True)
        log.info("Testing if Column 'Experience' in Roster Table is Descending")
        assert roster_experiences_int == roster_experiences_sorted

    def test_los_angeles_lakers_roster_sorted_experience_reverse_column(self):
        log = self.getLogger()
        self.Lakers_Page().clickExperience().click()
        roster_experiences_reverse_int = [int(i) for i in self.Lakers_Page().getRosterExperiencesReverse()]
        roster_experiences_sorted_reverse = sorted(roster_experiences_reverse_int)
        log.info("Testing if Column 'Experience' in Roster Table is Ascending")
        assert roster_experiences_reverse_int == roster_experiences_sorted_reverse

    def test_los_angeles_lakers_roster_sorted_college_column(self):
        log = self.getLogger()
        self.Lakers_Page().clickCollege().click()
        roster_colleges_sorted = sorted(self.Lakers_Page().getRosterCollege())
        log.info("Testing if Column 'College' in Roster Table is Ascending")
        assert self.Lakers_Page().getRosterCollege() == roster_colleges_sorted

    def test_los_angeles_lakers_roster_sorted_college_reverse_column(self):
        log = self.getLogger()
        self.Lakers_Page().clickCollege().click()
        roster_colleges_sorted_reverse = sorted(self.Lakers_Page().getRosterCollegesReverse(), reverse=True)
        log.info("Testing if Column 'College' in Roster Table is Descending")
        assert self.Lakers_Page().getRosterCollegesReverse() == roster_colleges_sorted_reverse

    def test_los_angeles_lakers_roster_players_stats(self):
        log = self.getLogger()
        self.Lakers_Page().openLakersPageButton().click()
        self.waitForElement("Roster")
        self.Lakers_Page().pressRosterButton().click()

        self.waitForGaurd("//td[text()='C']")
        players_with_updated_stats = []
        players_with_out_stats = []

        for player in self.Lakers_Page().getRosterPlayersForPlayerStats():
            player.click()
            self.waitForPageComplete()

            if self.Lakers_Page().getIsPlayer().text != '':  # there IS a player stats

                players_with_updated_stats.append(self.Lakers_Page().getPlayerName())

                self.Lakers_Page().pressPlayersStatsSeasonsHeader().click()
                seasons_sorted = sorted(self.Lakers_Page().getPlayersStatsSeasons())
                log.info(
                    "Testing if Column 'Season' in Player " + self.Lakers_Page().getPlayerName() + " Table is Ascending")
                assert seasons_sorted == self.Lakers_Page().getPlayersStatsSeasons()

                self.Lakers_Page().pressPlayersStatsSeasonsHeader().click()
                seasons_sorted_reverse = sorted(self.Lakers_Page().getPlayersStatsSeasonsReverse(), reverse=True)
                log.info(
                    "Testing if Column 'Season' in Player " + self.Lakers_Page().getPlayerName() + " Table is Descending")
                assert seasons_sorted_reverse == self.Lakers_Page().getPlayersStatsSeasonsReverse()

                self.Lakers_Page().pressPlayersStatsteamsHeader().click()

                teams_sorted = sorted(self.Lakers_Page().getPlayersStatsteams())
                log.info(
                    "Testing if Column 'Team' in Player " + self.Lakers_Page().getPlayerName() + " Table is Ascending")
                assert teams_sorted == self.Lakers_Page().getPlayersStatsteams()

                self.Lakers_Page().pressPlayersStatsteamsHeader().click()

                teams_sorted_reverse = sorted(self.Lakers_Page().getPlayersStatsteamsReverse(), reverse=True)
                log.info(
                    "Testing if Column 'Team' in Player " + self.Lakers_Page().getPlayerName() + " Table is Descending")
                assert teams_sorted_reverse == self.Lakers_Page().getPlayersStatsteamsReverse()

                self.Lakers_Page().pressPlayersStatsnumGamesHeader().click()

                games_int = [int(i) for i in self.Lakers_Page().getPlayersStatsNumGames()]
                num_games_sorted = sorted(games_int, reverse=True)
                log.info(
                    "Testing if Column 'Games' in Player " + self.Lakers_Page().getPlayerName() + " Table is Descending")
                assert num_games_sorted == games_int

                self.Lakers_Page().pressPlayersStatsnumGamesHeader().click()

                games_reverse_int = [int(i) for i in self.Lakers_Page().getPlayersStatsNumGamesReverse()]
                num_games_sorted_reverse = sorted(games_int)

                log.info(
                    "Testing if Column 'Games' in Player " + self.Lakers_Page().getPlayerName() + " Table is Ascending")
                assert num_games_sorted_reverse == games_reverse_int

                self.Lakers_Page().pressPlayersStatsNumGamesStartedHeader().click()

                games_started_int = [int(i) for i in self.Lakers_Page().getPlayersStatsNumGamesStarted()]
                num_games_started_sorted = sorted(games_started_int, reverse=True)
                log.info(
                    "Testing if Column 'Games Started' in Player " + self.Lakers_Page().getPlayerName() + " Table is Descending")
                assert num_games_started_sorted == games_started_int

                self.Lakers_Page().pressPlayersStatsNumGamesStartedHeader().click()

                games_started_reverse_int = [int(i) for i in self.Lakers_Page().getPlayersStatsNumGamesStartedReverse()]
                num_games_started_sorted_reverse = sorted(games_started_reverse_int)
                log.info(
                    "Testing if Column 'Games Started' in Player " + self.Lakers_Page().getPlayerName() + " Table is Ascending")
                assert num_games_started_sorted_reverse == games_started_reverse_int

                self.Lakers_Page().pressPlayersStatsMinutesPlayedHeader().click()

                minutes_played_float = [float(i) for i in self.Lakers_Page().getPlayersStatsMinutesPlayed()]
                minutes_played_sorted = sorted(minutes_played_float, reverse=True)
                log.info(
                    "Testing if Column 'Minutes Played' in Player " + self.Lakers_Page().getPlayerName() + " Table is Descending")
                assert minutes_played_sorted == minutes_played_float

                self.Lakers_Page().pressPlayersStatsMinutesPlayedHeader().click()

                minutes_played_reverse_float = [float(i) for i in
                                                self.Lakers_Page().getPlayersStatsMinutesPlayedReverse()]
                minutes_played_sorted_reverse = sorted(minutes_played_reverse_float)
                log.info(
                    "Testing if Column 'Minutes Played' in Player " + self.Lakers_Page().getPlayerName() + " Table is Ascending")
                assert minutes_played_sorted_reverse == minutes_played_reverse_float

                self.Lakers_Page().pressPlayersStatsFieldGoalsPercentageHeader().click()

                field_goals_percentage_float = [float(i) for i in
                                                self.Lakers_Page().getPlayersStatsFieldGoalsPercentage()]
                field_goals_percentage_sorted = sorted(field_goals_percentage_float, reverse=True)
                log.info(
                    "Testing if Column 'Field Goals Percentage' in Player " + self.Lakers_Page().getPlayerName() + " Table is Descending")
                assert field_goals_percentage_sorted == field_goals_percentage_float

                self.Lakers_Page().pressPlayersStatsFieldGoalsPercentageHeader().click()

                field_goals_percentage_reverse_float = [float(i) for i in
                                                        self.Lakers_Page().getPlayersStatsFieldGoalsPercentageReverse()]
                field_goals_percentage_sorted_reverse = sorted(field_goals_percentage_reverse_float)
                log.info(
                    "Testing if Column 'Field Goals Percentage' in Player " + self.Lakers_Page().getPlayerName() + " Table is Ascending")
                assert field_goals_percentage_sorted_reverse == field_goals_percentage_reverse_float

                self.Lakers_Page().pressPlayersStatsThreePointPercentageHeader().click()

                three_point_percentage_float = [float(i) for i in
                                                self.Lakers_Page().getPlayersStatsThreePointPercentage()]
                three_point_percentage_sorted = sorted(three_point_percentage_float, reverse=True)
                log.info(
                    "Testing if Column 'Three Point Percentage' in Player " + self.Lakers_Page().getPlayerName() + " Table is Descending")
                assert three_point_percentage_sorted == three_point_percentage_float

                self.Lakers_Page().pressPlayersStatsThreePointPercentageHeader().click()

                three_point_percentage_reverse_float = [float(i) for i in
                                                        self.Lakers_Page().getPlayersStatsThreePointPercentageReverse()]
                three_point_percentage_sorted_reverse = sorted(three_point_percentage_reverse_float)
                log.info(
                    "Testing if Column 'Three Point Percentage' in Player " + self.Lakers_Page().getPlayerName() + " Table is Ascending")
                assert three_point_percentage_sorted_reverse == three_point_percentage_reverse_float

                self.Lakers_Page().pressPlayersStatsFreeThrowPercentageHeader().click()

                free_throw_percentage_float = [float(i) for i in
                                               self.Lakers_Page().getPlayersStatsFreethrowPercentage()]
                free_throw_percentage_sorted = sorted(free_throw_percentage_float, reverse=True)
                log.info(
                    "Testing if Column 'Free Throw Percentage' in Player " + self.Lakers_Page().getPlayerName() + " Table is Descending")
                assert free_throw_percentage_sorted == free_throw_percentage_float

                self.Lakers_Page().pressPlayersStatsFreeThrowPercentageHeader().click()

                free_throw_percentage_reverse_float = [float(i) for i in
                                                       self.Lakers_Page().getPlayersStatsFreethrowPercentageReverse()]
                free_throw_percentage_sorted_reverse = sorted(free_throw_percentage_reverse_float)
                log.info(
                    "Testing if Column 'Free Throw Percentage' in Player " + self.Lakers_Page().getPlayerName() + " Table is Ascending")
                assert free_throw_percentage_sorted_reverse == free_throw_percentage_reverse_float

                self.Lakers_Page().pressPlayersStatsReboundsHeader().click()

                rebounds_float = [float(i) for i in self.Lakers_Page().getPlayersStatsRebounds()]
                rebounds_sorted = sorted(rebounds_float, reverse=True)
                log.info(
                    "Testing if Column 'Rebounds' in Player " + self.Lakers_Page().getPlayerName() + " Table is Descending")
                assert rebounds_sorted == rebounds_float

                self.Lakers_Page().pressPlayersStatsReboundsHeader().click()

                rebounds_reverse_float = [float(i) for i in self.Lakers_Page().getPlayersStatsReboundsReverse()]
                rebounds_sorted_reverse = sorted(rebounds_reverse_float)
                log.info(
                    "Testing if Column 'Rebounds' in Player " + self.Lakers_Page().getPlayerName() + " Table is Ascending")
                assert rebounds_sorted_reverse == rebounds_reverse_float

                self.Lakers_Page().pressPlayersStatsAssistsHeader().click()

                assists_float = [float(i) for i in self.Lakers_Page().getPlayersStatsAssists()]
                assists_sorted = sorted(assists_float, reverse=True)
                log.info(
                    "Testing if Column 'Assists' in Player " + self.Lakers_Page().getPlayerName() + " Table is Descending")
                assert assists_sorted == assists_float

                self.Lakers_Page().pressPlayersStatsAssistsHeader().click()

                assists_reverse_float = [float(i) for i in self.Lakers_Page().getPlayersStatsAssistsReverse()]
                assists_sorted_reverse = sorted(assists_reverse_float)
                log.info(
                    "Testing if Column 'Assists' in Player " + self.Lakers_Page().getPlayerName() + " Table is Ascending")
                assert assists_sorted_reverse == assists_reverse_float

                self.Lakers_Page().pressPlayersStatsStealsHeader().click()

                steals_float = [float(i) for i in self.Lakers_Page().getPlayersStatsSteals()]
                steals_sorted = sorted(steals_float, reverse=True)
                log.info(
                    "Testing if Column 'Steals' in Player " + self.Lakers_Page().getPlayerName() + " Table is Descending")
                assert steals_sorted == steals_float

                self.Lakers_Page().pressPlayersStatsStealsHeader().click()

                steals_reverse_float = [float(i) for i in self.Lakers_Page().getPlayersStatsStealsReverse()]
                steals_sorted_reverse = sorted(steals_reverse_float)
                log.info(
                    "Testing if Column 'Steals' in Player " + self.Lakers_Page().getPlayerName() + " Table is Ascending")
                assert steals_sorted_reverse == steals_reverse_float

                self.Lakers_Page().pressPlayersStatsBlocksHeader().click()

                blocks_float = [float(i) for i in self.Lakers_Page().getPlayersStatsBlocks()]
                blocks_sorted = sorted(blocks_float, reverse=True)
                log.info(
                    "Testing if Column 'Blocks' in Player " + self.Lakers_Page().getPlayerName() + " Table is Descending")
                assert blocks_sorted == blocks_float

                self.Lakers_Page().pressPlayersStatsBlocksHeader().click()

                blocks_reverse_float = [float(i) for i in self.Lakers_Page().getPlayersStatsBlocksReverse()]
                blocks_sorted_reverse = sorted(blocks_reverse_float)
                log.info(
                    "Testing if Column 'Blocks' in Player " + self.Lakers_Page().getPlayerName() + " Table is Ascending")
                assert blocks_sorted_reverse == blocks_reverse_float

                self.Lakers_Page().pressPlayersStatsTurnoversHeader().click()

                turnovers_float = [float(i) for i in self.Lakers_Page().getPlayersStatsTurnovers()]
                turnovers_sorted = sorted(turnovers_float, reverse=True)
                log.info(
                    "Testing if Column 'Turnovers' in Player " + self.Lakers_Page().getPlayerName() + " Table is Descending")
                assert turnovers_sorted == turnovers_float

                self.Lakers_Page().pressPlayersStatsTurnoversHeader().click()

                turnovers_reverse_float = [float(i) for i in self.Lakers_Page().getPlayersStatsTurnoversReverse()]
                turnovers_sorted_reverse = sorted(turnovers_reverse_float)
                log.info(
                    "Testing if Column 'Turnovers' in Player " + self.Lakers_Page().getPlayerName() + " Table is Ascending")
                assert turnovers_sorted_reverse == turnovers_reverse_float

                self.Lakers_Page().pressPlayersStatsPointsHeader().click()

                points_float = [float(i) for i in self.Lakers_Page().getPlayersStatsPoints()]
                points_sorted = sorted(points_float, reverse=True)
                log.info(
                    "Testing if Column 'Points' in Player " + self.Lakers_Page().getPlayerName() + " Table is Descending")
                assert points_sorted == points_float

                self.Lakers_Page().pressPlayersStatsPointsHeader().click()

                points_reverse_float = [float(i) for i in self.Lakers_Page().getPlayersStatsPointsReverse()]
                points_sorted_reverse = sorted(points_reverse_float)
                log.info(
                    "Testing if Column 'Points' in Player " + self.Lakers_Page().getPlayerName() + " Table is Ascending")
                assert points_sorted_reverse == points_reverse_float

                self.Lakers_Page().pressPlayersStatsDoubleDoublesHeader().click()

                double_doubles_int = [int(i) for i in self.Lakers_Page().getPlayersStatsDoubleDoubles()]
                double_doubles_sorted = sorted(double_doubles_int, reverse=True)
                log.info(
                    "Testing if Column 'DoubleDoubles' in Player " + self.Lakers_Page().getPlayerName() + " Table is Descending")
                assert double_doubles_sorted == double_doubles_int

                self.Lakers_Page().pressPlayersStatsDoubleDoublesHeader().click()

                double_doubles_reverse_int = [int(i) for i in self.Lakers_Page().getPlayersStatsDoubleDoublesReverse()]
                double_doubles_sorted_reverse = sorted(double_doubles_reverse_int)
                log.info(
                    "Testing if Column 'DoubleDoubles' in Player " + self.Lakers_Page().getPlayerName() + " Table is Ascending")
                assert double_doubles_sorted_reverse == double_doubles_reverse_int

                self.Lakers_Page().pressPlayersStatsTripleDoublesHeader().click()

                triple_doubles_int = [int(i) for i in self.Lakers_Page().getPlayersStatsTripleDoubles()]
                triple_doubles_sorted = sorted(triple_doubles_int, reverse=True)
                log.info(
                    "Testing if Column 'TripleDoubles' in Player " + self.Lakers_Page().getPlayerName() + " Table is Descending")
                assert triple_doubles_sorted == triple_doubles_int

                self.Lakers_Page().pressPlayersStatsTripleDoublesHeader().click()

                triple_doubles_reverse_int = [int(i) for i in self.Lakers_Page().getPlayersStatsTripleDoublesReverse()]
                triple_doubles_sorted_reverse = sorted(triple_doubles_reverse_int)
                log.info(
                    "Testing if Column 'TripleDoubles' in Player " + self.Lakers_Page().getPlayerName() + " Table is Ascending")
                assert triple_doubles_sorted_reverse == triple_doubles_reverse_int

            else:
                # time.sleep(1)

                players_with_out_stats.append(self.Lakers_Page().getPlayerName())
                # time.sleep(1)

            self.Lakers_Page().closePlayerStatsCloseButton().click()
        log.info("List of players with updated stats: " + str(players_with_updated_stats))
        log.info("List of players without updated stats: " + str(players_with_out_stats))
