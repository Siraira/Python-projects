from datetime import datetime


class Team:
    # the init function
    def __init__(self):
        self.name = None
        self.type_of_team = None
        self.fee = None
        self.fee_status = None

    # this function set the attributes of class team
    def add_my_team(self):
        self.name = self.name_set()
        self.type_of_team = self.type_set()
        self.fee = 150
        self.fee_status = self.fee_status_set()

    # this function set the name and make sure that the user have entered only text data
    def name_set(self):
        while True:
            val = str(input("please enter your team's name:"))
            if val.isalpha():
                self.name = val
                return self.name
            else:
                print("Your team name have to be string without spaces.")
                continue

    # this function set the type of the team and make sure that the user only press b(for boys teams) or g(for girls
    # teams)
    def type_set(self):
        while True:
            val = str(input("please enter your team's type(press b for boys or g for girls):"))
            if val.strip().lower() == 'b':
                self.type_of_team = 'Boys'
                return self.type_of_team
            elif val.strip().lower() == 'g':
                self.type_of_team = 'Girls'
                return self.type_of_team
            else:
                print("Error, please type b or g")
                continue

    # this function check whether the team have paid the fee or not
    def fee_status_set(self):
        while True:
            val = str(input("Did you paid the fee?"))
            if val.strip().lower() == 'y':
                print("Thank you for paying")
                return True
            elif val.strip().lower() == 'n':
                print("The required fee is 150 $,Make sure to pay before the deadline :) ")
                return False
            else:
                print("Error, please type y or n")
                continue

    # this function put all the data in a list
    def display_team_details(self):
        team_data = [id(self.name), self.name, self.type_of_team, self.fee, self.fee_status, datetime.now()]
        return team_data

    # this function save the list created in display team details in a text file
    def saving_team_data(self, user_list_of_team):
        with open('team.txt', 'w') as f:
            for item in user_list_of_team:
                f.write(" ".join(map(str, item)))
                f.write("\n")

    # this function reads the team data from the text file
    def reading_my_teams_database(self):
        with open('team.txt', 'r') as f:
            for line in f:
                print("Available Teams are", line, end='')

    # this function updates the name of the team , it takes the id and the new value and search in the list of data
    # the id that matches and then update the name of the matched id
    def update_my_team_name(self, given_id, new_value):
        with open('team.txt', 'r') as fr:
            lines = fr.readlines()
            my_team_list = []
            for line in lines:
                my_team_list.append(line.split())
                for i in range(len(my_team_list)):
                    if my_team_list[i][0] == given_id:
                        my_team_list[i][1] = new_value
                with open('team.txt', 'w') as fw:
                    for item in my_team_list:
                        fw.write(" ".join(map(str, item)))
                        fw.write("\n")


    # this function updates the type of the team , it takes the id and the new value and search in the list of data
    # the id that matches and then update the type of the matched id
    def update_my_team_type(self, given_id, new_value):
        with open('team.txt', 'r') as fr:
            lines = fr.readlines()
            my_team_list = []
            for line in lines:
                my_team_list.append(line.split())
                for i in range(len(my_team_list)):
                    if my_team_list[i][0] == given_id:
                        my_team_list[i][2] = new_value
            with open('team.txt', 'w') as fw:
                for item in my_team_list:
                    fw.write(" ".join(map(str, item)))
                    fw.write("\n")


    # this function delete the team with the given id , it first loads the data from the team text file and takes the
    # id and search in the list of data for the id that matches and delete the matched team and writes the data back
    # to file
    def delete_team(self, given_id):
        with open('team.txt', 'r') as fr:
            lines = fr.readlines()
            my_team_list = []
            for line in lines:
                my_team_list.append(line.split())
            for i in range(len(my_team_list)):
                if int(my_team_list[i][0]) == given_id:
                    my_team_list.pop(i)
                with open('team.txt', 'w') as fw:
                    for item in my_team_list:
                        fw.write(" ".join(map(str, item)))
                        fw.write("\n")

    # this function return the Total number of teams in the program
    def registered_teams(self):
        with open('team.txt', 'r') as f:
            lines = f.readlines()
            total = len(lines)
            return total

    # this function return the Total number of teams who paid the fees in the program
    def teams_who_paid(self):
        with open('team.txt', 'r') as f:
            lines = f.readlines()
            my_team_list = []
            for line in lines:
                my_team_list.append(line.split())
                count = 0
                for i in range(len(my_team_list)):
                    if 'True' in my_team_list[i]:
                        count += 1
            return count
    # this function takes the id of the team that want to cancel his participation
    # and create new text file called cancel_team and write the id and date of cancellation into that file
    def cancel_participation_team(self, given_id):
        now = datetime.today().date()
        cancel_teams = ["Team with Id", given_id, "Canceled participation on", now]
        with open('cancel_team.txt', 'w') as fw:
            fw.write(" ".join(map(str, cancel_teams)))

    # this function reads the cancel text data file and displayed to the user when he or she selects option 5
    def read_cancel_file(self):
        with open('cancel_team.txt', 'r') as fr:
            lines = fr.readlines()
        print(lines)
