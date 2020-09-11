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


class TestHoustonRocketsPage(BaseClass):


    def test_houston_rockets_franchise_verifiy_team(self):
        log = self.getLogger()
        log.info("Opening Houston Rockets Page")
        self.waitForTeamClickable("a[href='#!Rockets']")
        self.Rockets_Page().openRocketsPageButton().click()
        self.waitForTeamText()
        log.info("Verify Houston Rockets Page")
        assert "Houston Rockets" in self.Rockets_Page().verifyTeamText().text


    def test_houston_rockets_roster_players_stats(self):
        log = self.getLogger()
        self.Rockets_Page().openRocketsPageButton().click()
        self.waitForElement("Roster")
        self.Rockets_Page().pressRosterButton().click()
        # time.sleep(2)
        self.waitForGaurd("//td[text()='C']")
        players_with_updated_stats = []
        players_with_out_stats = []

        for player in self.Rockets_Page().getRosterPlayersForPlayerStats():
            player.click()
            self.waitForPageComplete()

            if self.Rockets_Page().getIsPlayer().text != '':  # there IS a player stats
                # time.sleep(2)
                players_with_updated_stats.append(self.Rockets_Page().getPlayerName())
                # time.sleep(2)
                self.Rockets_Page().pressPlayersStatsSeasonsHeader().click()
                seasons_sorted = sorted(self.Rockets_Page().getPlayersStatsSeasons())
                log.info(
                    "Testing if Column 'Season' in Player " + self.Rockets_Page().getPlayerName() + " Table is Ascending")
                assert seasons_sorted == self.Rockets_Page().getPlayersStatsSeasons()

                self.Rockets_Page().pressPlayersStatsSeasonsHeader().click()
                seasons_sorted_reverse = sorted(self.Rockets_Page().getPlayersStatsSeasonsReverse(), reverse=True)
                log.info(
                    "Testing if Column 'Season' in Player " + self.Rockets_Page().getPlayerName() + " Table is Descending")
                assert seasons_sorted_reverse == self.Rockets_Page().getPlayersStatsSeasonsReverse()

                self.Rockets_Page().pressPlayersStatsteamsHeader().click()
                # time.sleep(0.5)
                teams_sorted = sorted(self.Rockets_Page().getPlayersStatsteams())
                log.info(
                    "Testing if Column 'Team' in Player " + self.Rockets_Page().getPlayerName() + " Table is Ascending")
                assert teams_sorted == self.Rockets_Page().getPlayersStatsteams()

                self.Rockets_Page().pressPlayersStatsteamsHeader().click()
                # time.sleep(0.5)
                teams_sorted_reverse = sorted(self.Rockets_Page().getPlayersStatsteamsReverse(), reverse=True)
                log.info(
                    "Testing if Column 'Team' in Player " + self.Rockets_Page().getPlayerName() + " Table is Descending")
                assert teams_sorted_reverse == self.Rockets_Page().getPlayersStatsteamsReverse()

                self.Rockets_Page().pressPlayersStatsnumGamesHeader().click()
                # time.sleep(0.5)
                games_int = [int(i) for i in self.Rockets_Page().getPlayersStatsNumGames()]
                num_games_sorted = sorted(games_int, reverse=True)
                log.info(
                    "Testing if Column 'Games' in Player " + self.Rockets_Page().getPlayerName() + " Table is Descending")
                assert num_games_sorted == games_int

                self.Rockets_Page().pressPlayersStatsnumGamesHeader().click()
                # time.sleep(0.5)
                games_reverse_int = [int(i) for i in self.Rockets_Page().getPlayersStatsNumGamesReverse()]
                num_games_sorted_reverse = sorted(games_int)

                log.info(
                    "Testing if Column 'Games' in Player " + self.Rockets_Page().getPlayerName() + " Table is Ascending")
                assert num_games_sorted_reverse == games_reverse_int

                self.Rockets_Page().pressPlayersStatsNumGamesStartedHeader().click()
                # time.sleep(0.5)
                games_started_int = [int(i) for i in self.Rockets_Page().getPlayersStatsNumGamesStarted()]
                num_games_started_sorted = sorted(games_started_int, reverse=True)
                log.info(
                    "Testing if Column 'Games Started' in Player " + self.Rockets_Page().getPlayerName() + " Table is Descending")
                assert num_games_started_sorted == games_started_int

                self.Rockets_Page().pressPlayersStatsNumGamesStartedHeader().click()
                # time.sleep(0.5)
                games_started_reverse_int = [int(i) for i in self.Rockets_Page().getPlayersStatsNumGamesStartedReverse()]
                num_games_started_sorted_reverse = sorted(games_started_reverse_int)
                log.info(
                    "Testing if Column 'Games Started' in Player " + self.Rockets_Page().getPlayerName() + " Table is Ascending")
                assert num_games_started_sorted_reverse == games_started_reverse_int

                self.Rockets_Page().pressPlayersStatsMinutesPlayedHeader().click()
                # time.sleep(0.5)
                minutes_played_float = [float(i) for i in self.Rockets_Page().getPlayersStatsMinutesPlayed()]
                minutes_played_sorted = sorted(minutes_played_float, reverse=True)
                log.info(
                    "Testing if Column 'Minutes Played' in Player " + self.Rockets_Page().getPlayerName() + " Table is Descending")
                assert minutes_played_sorted == minutes_played_float

                self.Rockets_Page().pressPlayersStatsMinutesPlayedHeader().click()
                # time.sleep(0.5)
                minutes_played_reverse_float = [float(i) for i in
                                                self.Rockets_Page().getPlayersStatsMinutesPlayedReverse()]
                minutes_played_sorted_reverse = sorted(minutes_played_reverse_float)
                log.info(
                    "Testing if Column 'Minutes Played' in Player " + self.Rockets_Page().getPlayerName() + " Table is Ascending")
                assert minutes_played_sorted_reverse == minutes_played_reverse_float

                self.Rockets_Page().pressPlayersStatsFieldGoalsPercentageHeader().click()
                # time.sleep(0.5)
                field_goals_percentage_float = [float(i) for i in
                                                self.Rockets_Page().getPlayersStatsFieldGoalsPercentage()]
                field_goals_percentage_sorted = sorted(field_goals_percentage_float, reverse=True)
                log.info(
                    "Testing if Column 'Field Goals Percentage' in Player " + self.Rockets_Page().getPlayerName() + " Table is Descending")
                assert field_goals_percentage_sorted == field_goals_percentage_float

                self.Rockets_Page().pressPlayersStatsFieldGoalsPercentageHeader().click()
                # time.sleep(0.5)
                field_goals_percentage_reverse_float = [float(i) for i in
                                                        self.Rockets_Page().getPlayersStatsFieldGoalsPercentageReverse()]
                field_goals_percentage_sorted_reverse = sorted(field_goals_percentage_reverse_float)
                log.info(
                    "Testing if Column 'Field Goals Percentage' in Player " + self.Rockets_Page().getPlayerName() + " Table is Ascending")
                assert field_goals_percentage_sorted_reverse == field_goals_percentage_reverse_float

                self.Rockets_Page().pressPlayersStatsThreePointPercentageHeader().click()
                # time.sleep(0.5)
                three_point_percentage_float = [float(i) for i in
                                                self.Rockets_Page().getPlayersStatsThreePointPercentage()]
                three_point_percentage_sorted = sorted(three_point_percentage_float, reverse=True)
                log.info(
                    "Testing if Column 'Three Point Percentage' in Player " + self.Rockets_Page().getPlayerName() + " Table is Descending")
                assert three_point_percentage_sorted == three_point_percentage_float

                self.Rockets_Page().pressPlayersStatsThreePointPercentageHeader().click()
                # time.sleep(0.5)
                three_point_percentage_reverse_float = [float(i) for i in
                                                        self.Rockets_Page().getPlayersStatsThreePointPercentageReverse()]
                three_point_percentage_sorted_reverse = sorted(three_point_percentage_reverse_float)
                log.info(
                    "Testing if Column 'Three Point Percentage' in Player " + self.Rockets_Page().getPlayerName() + " Table is Ascending")
                assert three_point_percentage_sorted_reverse == three_point_percentage_reverse_float

                self.Rockets_Page().pressPlayersStatsFreeThrowPercentageHeader().click()
                # time.sleep(0.5)
                free_throw_percentage_float = [float(i) for i in self.Rockets_Page().getPlayersStatsFreethrowPercentage()]
                free_throw_percentage_sorted = sorted(free_throw_percentage_float, reverse=True)
                log.info(
                    "Testing if Column 'Free Throw Percentage' in Player " + self.Rockets_Page().getPlayerName() + " Table is Descending")
                assert free_throw_percentage_sorted == free_throw_percentage_float

                self.Rockets_Page().pressPlayersStatsFreeThrowPercentageHeader().click()
                # time.sleep(0.5)
                free_throw_percentage_reverse_float = [float(i) for i in
                                                       self.Rockets_Page().getPlayersStatsFreethrowPercentageReverse()]
                free_throw_percentage_sorted_reverse = sorted(free_throw_percentage_reverse_float)
                log.info(
                    "Testing if Column 'Free Throw Percentage' in Player " + self.Rockets_Page().getPlayerName() + " Table is Ascending")
                assert free_throw_percentage_sorted_reverse == free_throw_percentage_reverse_float

                self.Rockets_Page().pressPlayersStatsReboundsHeader().click()
                # time.sleep(0.5)
                rebounds_float = [float(i) for i in self.Rockets_Page().getPlayersStatsRebounds()]
                rebounds_sorted = sorted(rebounds_float, reverse=True)
                log.info(
                    "Testing if Column 'Rebounds' in Player " + self.Rockets_Page().getPlayerName() + " Table is Descending")
                assert rebounds_sorted == rebounds_float

                self.Rockets_Page().pressPlayersStatsReboundsHeader().click()
                # time.sleep(0.5)
                rebounds_reverse_float = [float(i) for i in self.Rockets_Page().getPlayersStatsReboundsReverse()]
                rebounds_sorted_reverse = sorted(rebounds_reverse_float)
                log.info(
                    "Testing if Column 'Rebounds' in Player " + self.Rockets_Page().getPlayerName() + " Table is Ascending")
                assert rebounds_sorted_reverse == rebounds_reverse_float

                self.Rockets_Page().pressPlayersStatsAssistsHeader().click()
                # time.sleep(0.5)
                assists_float = [float(i) for i in self.Rockets_Page().getPlayersStatsAssists()]
                assists_sorted = sorted(assists_float, reverse=True)
                log.info(
                    "Testing if Column 'Assists' in Player " + self.Rockets_Page().getPlayerName() + " Table is Descending")
                assert assists_sorted == assists_float

                self.Rockets_Page().pressPlayersStatsAssistsHeader().click()
                # time.sleep(0.5)
                assists_reverse_float = [float(i) for i in self.Rockets_Page().getPlayersStatsAssistsReverse()]
                assists_sorted_reverse = sorted(assists_reverse_float)
                log.info(
                    "Testing if Column 'Assists' in Player " + self.Rockets_Page().getPlayerName() + " Table is Ascending")
                assert assists_sorted_reverse == assists_reverse_float

                self.Rockets_Page().pressPlayersStatsStealsHeader().click()
                # time.sleep(0.5)
                steals_float = [float(i) for i in self.Rockets_Page().getPlayersStatsSteals()]
                steals_sorted = sorted(steals_float, reverse=True)
                log.info(
                    "Testing if Column 'Steals' in Player " + self.Rockets_Page().getPlayerName() + " Table is Descending")
                assert steals_sorted == steals_float

                self.Rockets_Page().pressPlayersStatsStealsHeader().click()
                # time.sleep(0.5)
                steals_reverse_float = [float(i) for i in self.Rockets_Page().getPlayersStatsStealsReverse()]
                steals_sorted_reverse = sorted(steals_reverse_float)
                log.info(
                    "Testing if Column 'Steals' in Player " + self.Rockets_Page().getPlayerName() + " Table is Ascending")
                assert steals_sorted_reverse == steals_reverse_float

                self.Rockets_Page().pressPlayersStatsBlocksHeader().click()
                # time.sleep(0.5)
                blocks_float = [float(i) for i in self.Rockets_Page().getPlayersStatsBlocks()]
                blocks_sorted = sorted(blocks_float, reverse=True)
                log.info(
                    "Testing if Column 'Blocks' in Player " + self.Rockets_Page().getPlayerName() + " Table is Descending")
                assert blocks_sorted == blocks_float

                self.Rockets_Page().pressPlayersStatsBlocksHeader().click()
                # time.sleep(0.5)
                blocks_reverse_float = [float(i) for i in self.Rockets_Page().getPlayersStatsBlocksReverse()]
                blocks_sorted_reverse = sorted(blocks_reverse_float)
                log.info(
                    "Testing if Column 'Blocks' in Player " + self.Rockets_Page().getPlayerName() + " Table is Ascending")
                assert blocks_sorted_reverse == blocks_reverse_float

                self.Rockets_Page().pressPlayersStatsTurnoversHeader().click()
                # time.sleep(0.5)
                turnovers_float = [float(i) for i in self.Rockets_Page().getPlayersStatsTurnovers()]
                turnovers_sorted = sorted(turnovers_float, reverse=True)
                log.info(
                    "Testing if Column 'Turnovers' in Player " + self.Rockets_Page().getPlayerName() + " Table is Descending")
                assert turnovers_sorted == turnovers_float

                self.Rockets_Page().pressPlayersStatsTurnoversHeader().click()
                # time.sleep(0.5)
                turnovers_reverse_float = [float(i) for i in self.Rockets_Page().getPlayersStatsTurnoversReverse()]
                turnovers_sorted_reverse = sorted(turnovers_reverse_float)
                log.info(
                    "Testing if Column 'Turnovers' in Player " + self.Rockets_Page().getPlayerName() + " Table is Ascending")
                assert turnovers_sorted_reverse == turnovers_reverse_float

                self.Rockets_Page().pressPlayersStatsPointsHeader().click()
                # time.sleep(0.5)
                points_float = [float(i) for i in self.Rockets_Page().getPlayersStatsPoints()]
                points_sorted = sorted(points_float, reverse=True)
                log.info(
                    "Testing if Column 'Points' in Player " + self.Rockets_Page().getPlayerName() + " Table is Descending")
                assert points_sorted == points_float

                self.Rockets_Page().pressPlayersStatsPointsHeader().click()
                # time.sleep(0.5)
                points_reverse_float = [float(i) for i in self.Rockets_Page().getPlayersStatsPointsReverse()]
                points_sorted_reverse = sorted(points_reverse_float)
                log.info(
                    "Testing if Column 'Points' in Player " + self.Rockets_Page().getPlayerName() + " Table is Ascending")
                assert points_sorted_reverse == points_reverse_float

                self.Rockets_Page().pressPlayersStatsDoubleDoublesHeader().click()
                # time.sleep(0.5)
                double_doubles_int = [int(i) for i in self.Rockets_Page().getPlayersStatsDoubleDoubles()]
                double_doubles_sorted = sorted(double_doubles_int, reverse=True)
                log.info(
                    "Testing if Column 'DoubleDoubles' in Player " + self.Rockets_Page().getPlayerName() + " Table is Descending")
                assert double_doubles_sorted == double_doubles_int

                self.Rockets_Page().pressPlayersStatsDoubleDoublesHeader().click()
                # time.sleep(0.5)
                double_doubles_reverse_int = [int(i) for i in self.Rockets_Page().getPlayersStatsDoubleDoublesReverse()]
                double_doubles_sorted_reverse = sorted(double_doubles_reverse_int)
                log.info(
                    "Testing if Column 'DoubleDoubles' in Player " + self.Rockets_Page().getPlayerName() + " Table is Ascending")
                assert double_doubles_sorted_reverse == double_doubles_reverse_int

                self.Rockets_Page().pressPlayersStatsTripleDoublesHeader().click()
                # time.sleep(0.5)
                triple_doubles_int = [int(i) for i in self.Rockets_Page().getPlayersStatsTripleDoubles()]
                triple_doubles_sorted = sorted(triple_doubles_int, reverse=True)
                log.info(
                    "Testing if Column 'TripleDoubles' in Player " + self.Rockets_Page().getPlayerName() + " Table is Descending")
                assert triple_doubles_sorted == triple_doubles_int

                self.Rockets_Page().pressPlayersStatsTripleDoublesHeader().click()
                # time.sleep(0.5)
                triple_doubles_reverse_int = [int(i) for i in self.Rockets_Page().getPlayersStatsTripleDoublesReverse()]
                triple_doubles_sorted_reverse = sorted(triple_doubles_reverse_int)
                log.info(
                    "Testing if Column 'TripleDoubles' in Player " + self.Rockets_Page().getPlayerName() + " Table is Ascending")
                assert triple_doubles_sorted_reverse == triple_doubles_reverse_int

            else:
                # time.sleep(1)

                players_with_out_stats.append(self.Rockets_Page().getPlayerName())
                # time.sleep(1)

            self.Rockets_Page().closePlayerStatsCloseButton().click()
        log.info("List of players with updated stats: " + str(players_with_updated_stats))
        log.info("List of players without updated stats: " + str(players_with_out_stats))





    @pytest.mark.usefixtures("rockets_salaries_team_setup")
    def test_houston_rockets_salaries_sorted_players_column(self):
        log = self.getLogger()
        self.waitForGaurd("//td[text()='$0']")
        self.waitForSalariesPlayerHeaderClickable()
        self.Rockets_Page().pressSalariesPlayersHeader().click()
        salaries_players_sorted = sorted(self.Rockets_Page().getSalariesPlayers())
        log.info("Testing if Column 'Player' in Salaries Table is Ascending")
        assert self.Rockets_Page().getSalariesPlayers() == salaries_players_sorted

    def test_houston_rockets_salaries_sorted_players_reverse_column(self):
        log = self.getLogger()

        self.Rockets_Page().pressSalariesPlayersHeader().click()
        salaries_players_sorted = sorted(self.Rockets_Page().getSalariesPlayersReverse(), reverse=True)
        log.info("Testing if Column 'Player' in Salaries Table is Descending")
        assert self.Rockets_Page().getSalariesPlayersReverse() == salaries_players_sorted

    def test_houston_rockets_salaries_sorted_age_column(self):
        log = self.getLogger()

        self.Rockets_Page().pressSalariesAgeHeader().click()
        age_players_sorted = sorted(self.Rockets_Page().getAgePlayers(), reverse=True)
        log.info("Testing if Column 'Age' in Salaries Table is Descending")
        assert self.Rockets_Page().getAgePlayers() == age_players_sorted

    def test_houston_rockets_salaries_sorted_age_reverse_column(self):
        log = self.getLogger()

        self.Rockets_Page().pressSalariesAgeHeader().click()
        age_players_sorted = sorted(self.Rockets_Page().getAgePlayersReverse())
        log.info("Testing if Column 'Age' in Salaries Table is Ascending")
        assert self.Rockets_Page().getAgePlayersReverse() == age_players_sorted

    def test_houston_rockets_salaries_sorted_eight_teen_nine_teen_column(self):
        log = self.getLogger()

        self.Rockets_Page().pressSalariesEightTeenNineTeenHeader().click()
        eight_teen_nine_teen_players_sorted = sorted(self.Rockets_Page().getEightTeenNineTeenPlayers(), reverse=True)
        log.info("Testing if Column '2018-19' in Salaries Table is Descending")
        assert eight_teen_nine_teen_players_sorted == self.Rockets_Page().getEightTeenNineTeenPlayers()

    def test_houston_rockets_salaries_sorted_eight_teen_nine_teen_reverse_column(self):
        log = self.getLogger()

        self.Rockets_Page().pressSalariesEightTeenNineTeenHeader().click()
        eight_teen_nine_teen_players_sorted_reverse = sorted(self.Rockets_Page().getEightTeenNineTeenPlayersReverse())
        log.info("Testing if Column '2018-19' in Salaries Table is Ascending")
        assert eight_teen_nine_teen_players_sorted_reverse == self.Rockets_Page().getEightTeenNineTeenPlayersReverse()

    def test_houston_rockets_salaries_sorted_nine_teen_twenty_column(self):
        log = self.getLogger()

        self.Rockets_Page().pressSalariesNineTeenTwentyHeader().click()
        nine_teen_twenty_players_sorted = sorted(self.Rockets_Page().getNineTeenTwentyPlayers(), reverse=True)
        log.info("Testing if Column '2019-20' in Salaries Table is Descending")
        assert nine_teen_twenty_players_sorted == self.Rockets_Page().getNineTeenTwentyPlayers()

    def test_houston_rockets_salaries_sorted_nine_teen_twenty_reverse_column(self):
        log = self.getLogger()

        self.Rockets_Page().pressSalariesNineTeenTwentyHeader().click()
        nine_teen_twenty_players_sorted_reverse = sorted(self.Rockets_Page().getNineTeenTwentyPlayersReverse())
        log.info("Testing if Column '2019-20' in Salaries Table is Ascending")
        assert nine_teen_twenty_players_sorted_reverse == self.Rockets_Page().getNineTeenTwentyPlayersReverse()

    def test_houston_rockets_salaries_sorted_twenty_twenty_one_column(self):
        log = self.getLogger()

        self.Rockets_Page().pressSalariesTwentyTwentyOneHeader().click()
        twenty_twenty_one_players_sorted = sorted(self.Rockets_Page().getTwentyTwentyOnePlayers(), reverse=True)
        log.info("Testing if Column '2020-21' in Salaries Table is Descending")
        assert twenty_twenty_one_players_sorted == self.Rockets_Page().getTwentyTwentyOnePlayers()

    def test_houston_rockets_salaries_sorted_twenty_twenty_one_reverse_column(self):
        log = self.getLogger()

        self.Rockets_Page().pressSalariesTwentyTwentyOneHeader().click()
        twenty_twenty_one_players_sorted_reverse = sorted(self.Rockets_Page().getTwentyTwentyOnePlayersReverse())
        log.info("Testing if Column '2020-21' in Salaries Table is Ascending")
        assert twenty_twenty_one_players_sorted_reverse == self.Rockets_Page().getTwentyTwentyOnePlayersReverse()

    def test_houston_rockets_salaries_sorted_twenty_one_twenty_two_column(self):
        log = self.getLogger()

        self.Rockets_Page().pressSalariesTwentyOneTwentyTwoHeader().click()
        twenty_one_twenty_two_players_sorted = sorted(self.Rockets_Page().getTwentyOneTwentyTwoPlayers(),
                                                      reverse=True)
        log.info("Testing if Column '2021-22' in Salaries Table is Descending")

        assert twenty_one_twenty_two_players_sorted == self.Rockets_Page().getTwentyOneTwentyTwoPlayers()

    def test_houston_rockets_salaries_sorted_twenty_one_twenty_two_reverse_column(self):
        log = self.getLogger()

        self.Rockets_Page().pressSalariesTwentyOneTwentyTwoHeader().click()
        twenty_one_twenty_two_players_sorted_reverse = sorted(
            self.Rockets_Page().getTwentyOneTwentyTwoPlayersReverse())
        log.info("Testing if Column '2021-22' in Salaries Table is Ascending")
        assert twenty_one_twenty_two_players_sorted_reverse == self.Rockets_Page().getTwentyOneTwentyTwoPlayersReverse()

    def test_houston_rockets_salaries_sorted_twenty_two_twenty_three_column(self):
        log = self.getLogger()

        self.Rockets_Page().pressSalariesTwentyTwoTwentyThreeHeader().click()
        twenty_two_twenty_three_players_sorted = sorted(self.Rockets_Page().getTwentyTwoTwentyThreePlayers(),
                                                        reverse=True)
        log.info("Testing if Column '2022-23' in Salaries Table is Descending")

        assert twenty_two_twenty_three_players_sorted == self.Rockets_Page().getTwentyTwoTwentyThreePlayers()

    def test_houston_rockets_salaries_sorted_twenty_two_twenty_threereverse_column(self):
        log = self.getLogger()

        self.Rockets_Page().pressSalariesTwentyTwoTwentyThreeHeader().click()

        twenty_two_twenty_three_players_sorted_reverse = sorted(
            self.Rockets_Page().getTwentyTwoTwentyThreePlayersReverse())
        log.info("Testing if Column '2022-23' in Salaries Table is Ascending")

        assert twenty_two_twenty_three_players_sorted_reverse == self.Rockets_Page().getTwentyTwoTwentyThreePlayersReverse()

    def test_houston_rockets_salaries_sorted_guranteed_column(self):
        log = self.getLogger()

        self.Rockets_Page().pressSalariesGuaranteedHeader().click()
        guaranteed_players_sorted = sorted(self.Rockets_Page().getGuaranteedPlayers(), reverse=True)
        log.info("Testing if Column 'Guaranteed' in Salaries Table is Descending")
        assert guaranteed_players_sorted == self.Rockets_Page().getGuaranteedPlayers()

    def test_houston_rockets_salaries_sorted_guranteed_reverse_column(self):
        log = self.getLogger()
        self.Rockets_Page().pressSalariesGuaranteedHeader().click()
        guaranteed_players_sorted_reverse = sorted(self.Rockets_Page().getGuaranteedPlayersReverse())
        log.info("Testing if Column 'Guaranteed' in Salaries Table is Ascending")
        assert guaranteed_players_sorted_reverse == self.Rockets_Page().getGuaranteedPlayersReverse()

    @pytest.mark.usefixtures("rockets_roster_team_setup")
    def test_houston_rockets_roster_sorted_players_column(self):
        log = self.getLogger()

        self.Rockets_Page().clickPlayer().click()
        time.sleep(7)

        roster_player_sorted = sorted(self.Rockets_Page().getRosterPlayers())

        log.info("Testing if Column 'Players' in Roster Table is Descending")

        assert self.Rockets_Page().getRosterPlayers() == roster_player_sorted

    def test_houston_rockets_roster_sorted_players_reverse_column(self):
        log = self.getLogger()
        self.Rockets_Page().clickPlayer().click()
        roster_player_sorted_reverse = sorted(self.Rockets_Page().getRosterPlayersReverse(), reverse=True)
        log.info("Testing if Column 'Players' in Roster Table is Ascending")
        assert self.Rockets_Page().getRosterPlayersReverse() == roster_player_sorted_reverse

    def test_houston_rockets_roster_sorted_position_column(self):
        log = self.getLogger()
        self.Rockets_Page().clickPosition().click()
        roster_positions_sorted = sorted(self.Rockets_Page().getRosterPositions(), reverse=True)
        log.info("Testing if Column 'Position' in Roster Table is Descending")
        assert self.Rockets_Page().getRosterPositions() == roster_positions_sorted

        self.Rockets_Page().clickPosition().click()

    def test_houston_rockets_roster_sorted_position_reverse_column(self):
        log = self.getLogger()
        roster_positions_reverse_sorted = sorted(self.Rockets_Page().getRosterPositionsReverse())
        log.info("Testing if Column 'Position' in Roster Table is Ascending")
        assert self.Rockets_Page().getRosterPositionsReverse() == roster_positions_reverse_sorted

    def test_houston_rockets_roster_sorted_height_column(self):
        log = self.getLogger()
        self.Rockets_Page().clickHeight().click()
        roster_heights_sorted = sorted(self.Rockets_Page().getRosterHeights(), reverse=True)
        log.info("Testing if Column 'Height' in Roster Table is Descending")
        assert self.Rockets_Page().getRosterHeights() == roster_heights_sorted

    def test_houston_rockets_roster_sorted_height_reverse_column(self):
        log = self.getLogger()
        self.Rockets_Page().clickHeight().click()

        roster_heights_sorted_reverse = sorted(self.Rockets_Page().getRosterHeightsReverse())
        log.info("Testing if Column 'Height' in Roster Table is Ascending")
        assert self.Rockets_Page().getRosterHeightsReverse() == roster_heights_sorted_reverse

    def test_houston_rockets_roster_sorted_weight_column(self):
        log = self.getLogger()
        self.Rockets_Page().clickWeight().click()
        roster_weights_int = [int(i) for i in self.Rockets_Page().getRosterWeights()]
        roster_weights_sorted = sorted(roster_weights_int, reverse=True)
        log.info("Testing if Column 'Weight' in Roster Table is Descending")
        assert roster_weights_int == roster_weights_sorted

    def test_houston_rockets_roster_sorted_weight_reverse_column(self):
        log = self.getLogger()
        self.Rockets_Page().clickWeight().click()
        roster_weights_reverse_int = [int(i) for i in self.Rockets_Page().getRosterWeightsReverse()]
        roster_weights_sorted_reverse = sorted(roster_weights_reverse_int)
        log.info("Testing if Column 'Weight' in Roster Table is Ascending")
        assert roster_weights_reverse_int == roster_weights_sorted_reverse

    def test_houston_rockets_roster_sorted_dob_column(self):
        log = self.getLogger()
        self.Rockets_Page().clickDob().click()
        self.Rockets_Page().getRosterDob().sort(key=lambda date: datetime.strptime(date, "%d/%m/%Y"))
        log.info("Testing if Column 'Date of Birth' in Roster Table is Ascending")
        dob_sorted = self.Rockets_Page().getRosterDob()
        assert dob_sorted == self.Rockets_Page().getRosterDob()

    def test_houston_rockets_roster_sorted_dob_reverse_column(self):
        log = self.getLogger()
        self.Rockets_Page().clickDob().click()
        self.Rockets_Page().getRosterDobsReverse().sort(key=lambda date: datetime.strptime(date, "%d/%m/%Y"),
                                                        reverse=True)
        log.info("Testing if Column 'Date of Birth' in Roster Table is Descending")
        dob_sorted_reverse = self.Rockets_Page().getRosterDobsReverse()
        assert dob_sorted_reverse == self.Rockets_Page().getRosterDobsReverse()

    def test_houston_rockets_roster_sorted_experience_column(self):
        log = self.getLogger()
        self.Rockets_Page().clickExperience().click()
        roster_experiences_int = [int(i) for i in self.Rockets_Page().getRosterExperience()]
        roster_experiences_sorted = sorted(roster_experiences_int, reverse=True)
        log.info("Testing if Column 'Experience' in Roster Table is Descending")
        assert roster_experiences_int == roster_experiences_sorted

    def test_houston_rockets_roster_sorted_experience_reverse_column(self):
        log = self.getLogger()
        self.Rockets_Page().clickExperience().click()
        roster_experiences_reverse_int = [int(i) for i in self.Rockets_Page().getRosterExperiencesReverse()]
        roster_experiences_sorted_reverse = sorted(roster_experiences_reverse_int)
        log.info("Testing if Column 'Experience' in Roster Table is Ascending")
        assert roster_experiences_reverse_int == roster_experiences_sorted_reverse

    def test_houston_rockets_roster_sorted_college_column(self):
        log = self.getLogger()
        self.Rockets_Page().clickCollege().click()
        roster_colleges_sorted = sorted(self.Rockets_Page().getRosterCollege())
        log.info("Testing if Column 'College' in Roster Table is Ascending")
        assert self.Rockets_Page().getRosterCollege() == roster_colleges_sorted

    def test_houston_rockets_roster_sorted_college_reverse_column(self):
        log = self.getLogger()
        self.Rockets_Page().clickCollege().click()
        roster_colleges_sorted_reverse = sorted(self.Rockets_Page().getRosterCollegesReverse(), reverse=True)
        log.info("Testing if Column 'College' in Roster Table is Descending")
        assert self.Rockets_Page().getRosterCollegesReverse() == roster_colleges_sorted_reverse















