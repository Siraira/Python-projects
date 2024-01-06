#Import class Userinterface
from UserInterface import UserInterface
#Import class Team
from TEAM import Team

#the main function
def main():
    #create an instance of class UserInterface
    user1 = UserInterface()
    #access the method using the dot notation
    user1.menu_print()
    # create an instance of class Team
    team1 = Team()
    option = input("please enter your option number >> ")
    print()
    while option != "0":
        #while user not existing the program
        if option == "1":
            #if user select the option 1 which is to add teams
            number_of_team = int(input("How many teams you want to add? "))
            team_list = []
            for i in range(number_of_team):
                team1 = Team()
                team1.add_my_team()
                print()
                case = team1.display_team_details()
                team_list.append(case)
                team1.saving_team_data(team_list)
                print("                    ID            ","Name ", "Type", " Fee"," paid", " Date    ", "Time")
                team1.reading_my_teams_database()

        elif option == "2":
            # if user select the option 2 which is to display teams
            team1.reading_my_teams_database()

        elif option == "3":
            # if user select the option 3 which is to update teams
            team1.reading_my_teams_database()
            given_id = input("Enter the id of the team you want to update: ")
            s_value = input("what field you want to update? name or type ")
            if s_value == "name":
                new_value = str(input("what is the new name? "))
                print()
                team1.update_my_team_name(given_id, new_value)
                print("your updated team  is", team1.reading_my_teams_database())
            if s_value == "type":
                new_value = str(input("what is the new type? "))
                print()
                team1.update_my_team_type(given_id, new_value)
                print("your updated team  is", team1.reading_my_teams_database())

        elif option == "4":
            # if user select the option 4 which is to delete teams
            team1.reading_my_teams_database()
            print()
            given_id = int(input("Enter the id of the team you want to delete: "))
            team1.delete_team(given_id)
            print("The selected team is now deleted... ")

        elif option == "5":
            # if user select the option 5 which is to cancel participation of a team
            team1.reading_my_teams_database()
            id_cancel = int(input("Print the id of the team you want to cancel its participation "))
            team1.cancel_participation_team(id_cancel)
            team1.read_cancel_file()

        elif option == "6":
            # if user select the option 6 which is to display the number of registered teams
            # and see the percentage of fee paying teams
            print("The number of registered teams in the Event is :", team1.registered_teams())
            print("The number of teams who paid their fees is: ", team1.teams_who_paid())
            print("The percentage of teams who paid their fees is: ",
                  round((team1.teams_who_paid() / team1.registered_teams()) * 100), "%")

        else:
            print("invalid option , please try again")
        print()
        user1.menu_print()
        option = input("please enter your option number >> ")
    print("Thank you for using Handball Event program... Goodbye :) ")
main()

