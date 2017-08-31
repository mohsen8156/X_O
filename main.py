#!/usr/bin/python3.5
class Playing:
    clicks = 9
    def __init__(self, random, app, who_winner):
        self.app = app
        self.random = random
        self.who_winner = who_winner
        self.first_player = random.randint(1,2)# فعلا از این قابلیت استفاده نشود
        self.check_button_list = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9']
    def onclick_event_B1(self):
        if self.clicks%2 == 1:
            self.app.B1['text'] = 'X'
            self.app.B1['bg'] = 'blue'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B1')
            self.who_winner.performance()
    def onclick_event_B2(self):
        if self.clicks%2 == 1:
            self.app.B2['text'] = 'X'
            self.app.B2['bg'] = 'blue'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B2')
            self.who_winner.performance()
    def onclick_event_B3(self):
        if self.clicks%2 == 1:
            self.app.B3['text'] = 'X'
            self.app.B3['bg'] = 'blue'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B3')
            self.who_winner.performance()
    def onclick_event_B4(self):
        if self.clicks%2 == 1:
            self.app.B4['text'] = 'X'
            self.app.B4['bg'] = 'blue'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B4')
            self.who_winner.performance()
    def onclick_event_B5(self):
        if self.clicks%2 == 1:
            self.app.B5['text'] = 'X'
            self.app.B5['bg'] = 'blue'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B5')
            self.who_winner.performance()
    def onclick_event_B6(self):
        if self.clicks%2 == 1:
            self.app.B6['text'] = 'X'
            self.app.B6['bg'] = 'blue'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B6')
            self.who_winner.performance()
    def onclick_event_B7(self):
        if self.clicks%2 == 1:
            self.app.B7['text'] = 'X'
            self.app.B7['bg'] = 'blue'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B7')
            self.who_winner.performance()
    def onclick_event_B8(self):
        if self.clicks%2 == 1:
            self.app.B8['text'] = 'X'
            self.app.B8['bg'] = 'blue'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B8')
            self.who_winner.performance()
    def onclick_event_B9(self):
        if self.clicks%2 == 1:
            self.app.B9['text'] = 'X'
            self.app.B9['bg'] = 'blue'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B9')
            self.who_winner.performance()
    def compyter_event(self):
        # ways to win computer
        if ((self.app.B1['text'] == self.app.B2['text'] == 'O') and (self.app.B3['text'] == '')) and (self.clicks%2 == 0):# row1.1
            self.app.B3['text'] = 'O'
            self.app.B3['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B3')
            self.who_winner.performance()
        elif ((self.app.B4['text'] == self.app.B5['text'] == 'O') and (self.app.B6['text'] == '')) and (self.clicks%2 == 0):# row2.1
            self.app.B6['text'] = 'O'
            self.app.B6['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B6')
            self.who_winner.performance()
        elif ((self.app.B7['text'] == self.app.B8['text'] == 'O') and (self.app.B9['text'] == '')) and (self.clicks%2 == 0):# row3.1
            self.app.B9['text'] = 'O'
            self.app.B9['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B9')
            self.who_winner.performance()
        elif ((self.app.B2['text'] == self.app.B3['text'] == 'O') and (self.app.B1['text'] == '')) and (self.clicks%2 == 0):# row1.2
            self.app.B1['text'] = 'O'
            self.app.B1['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B1')
            self.who_winner.performance()
        elif ((self.app.B5['text'] == self.app.B6['text'] == 'O') and (self.app.B4['text'] == '')) and (self.clicks%2 == 0):# row2.2
            self.app.B4['text'] = 'O'
            self.app.B4['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B4')
            self.who_winner.performance()
        elif ((self.app.B8['text'] == self.app.B9['text'] == 'O') and (self.app.B7['text'] == '')) and (self.clicks%2 == 0):# row3.2
            self.app.B7['text'] = 'O'
            self.app.B7['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B7')
            self.who_winner.performance()
        elif ((self.app.B1['text'] == self.app.B3['text'] == 'O') and (self.app.B2['text'] == '')) and (self.clicks%2 == 0):# row1.3
            self.app.B2['text'] = 'O'
            self.app.B2['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B2')
            self.who_winner.performance()
        elif ((self.app.B4['text'] == self.app.B6['text'] == 'O') and (self.app.B5['text'] == '')) and (self.clicks%2 == 0):# row2.3
            self.app.B5['text'] = 'O'
            self.app.B5['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B5')
            self.who_winner.performance()
        elif ((self.app.B7['text'] == self.app.B9['text'] == 'O') and (self.app.B8['text'] == '')) and (self.clicks%2 == 0):# row3.3
            self.app.B8['text'] = 'O'
            self.app.B8['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B8')
            self.who_winner.performance()
        elif ((self.app.B1['text'] == self.app.B4['text'] == 'O') and (self.app.B7['text'] == '')) and (self.clicks%2 == 0):# column1.1
            self.app.B7['text'] = 'O'
            self.app.B7['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B7')
            self.who_winner.performance()
        elif ((self.app.B2['text'] == self.app.B5['text'] == 'O') and (self.app.B8['text'] == '')) and (self.clicks%2 == 0):# column1.2
            self.app.B8['text'] = 'O'
            self.app.B8['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B8')
            self.who_winner.performance()
        elif ((self.app.B3['text'] == self.app.B6['text'] == 'O') and (self.app.B9['text'] == '')) and (self.clicks%2 == 0):# column1.3
            self.app.B9['text'] = 'O'
            self.app.B9['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B9')
            self.who_winner.performance()
        elif ((self.app.B4['text'] == self.app.B7['text'] == 'O') and (self.app.B1['text'] == '')) and (self.clicks%2 == 0):# column1.2
            self.app.B1['text'] = 'O'
            self.app.B1['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B1')
            self.who_winner.performance()
        elif ((self.app.B5['text'] == self.app.B8['text'] == 'O') and (self.app.B2['text'] == '')) and (self.clicks%2 == 0):# column2.2
            self.app.B2['text'] = 'O'
            self.app.B2['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B2')
            self.who_winner.performance()
        elif ((self.app.B6['text'] == self.app.B9['text'] == 'O') and (self.app.B3['text'] == '')) and (self.clicks%2 == 0):# column3.2
            self.app.B3['text'] = 'O'
            self.app.B3['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B3')
            self.who_winner.performance()
        elif ((self.app.B1['text'] == self.app.B7['text'] == 'O') and (self.app.B4['text'] == '')) and (self.clicks%2 == 0):# column1.3
            self.app.B4['text'] = 'O'
            self.app.B4['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B4')
            self.who_winner.performance()
        elif ((self.app.B2['text'] == self.app.B8['text'] == 'O') and (self.app.B5['text'] == '')) and (self.clicks%2 == 0):# column2.3
            self.app.B5['text'] = 'O'
            self.app.B5['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B5')
            self.who_winner.performance()
        elif ((self.app.B3['text'] == self.app.B9['text'] == 'O') and (self.app.B6['text'] == '')) and (self.clicks%2 == 0):# column3.3
            self.app.B6['text'] = 'O'
            self.app.B6['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B6')
            self.who_winner.performance()
        elif ((self.app.B1['text'] == self.app.B5['text'] == 'O') and (self.app.B9['text'] == '')) and (self.clicks%2 == 0):# diameter1.1
            self.app.B9['text'] = 'O'
            self.app.B9['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B9')
            self.who_winner.performance()
        elif ((self.app.B3['text'] == self.app.B5['text'] == 'O') and (self.app.B7['text'] == '')) and (self.clicks%2 == 0):# diameter2.1
            self.app.B7['text'] = 'O'
            self.app.B7['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B7')
            self.who_winner.performance()
        elif ((self.app.B5['text'] == self.app.B9['text'] == 'O') and (self.app.B1['text'] == '')) and (self.clicks%2 == 0):# diameter1.2
            self.app.B1['text'] = 'O'
            self.app.B1['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B1')
            self.who_winner.performance()
        elif ((self.app.B5['text'] == self.app.B7['text'] == 'O') and (self.app.B3['text'] == '')) and (self.clicks%2 == 0):# diameter2.2
            self.app.B3['text'] = 'O'
            self.app.B3['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B3')
            self.who_winner.performance()
        # ways to lose computer
        elif ((self.app.B1['text'] == self.app.B2['text'] == 'X') and (self.app.B3['text'] == '')) and (self.clicks%2==0):# row1.1
            self.app.B3['text'] = 'O'
            self.app.B3['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B3')
            self.who_winner.performance()
        elif ((self.app.B4['text'] == self.app.B5['text'] == 'X') and (self.app.B6['text'] == '')) and (self.clicks%2 == 0):# row2.1
            self.app.B6['text'] = 'O'
            self.app.B6['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B6')
            self.who_winner.performance()
        elif ((self.app.B7['text'] == self.app.B8['text'] == 'X') and (self.app.B9['text'] == '')) and (self.clicks%2 == 0):# row3.1
            self.app.B9['text'] = 'O'
            self.app.B9['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B9')
            self.who_winner.performance()
        elif ((self.app.B2['text'] == self.app.B3['text'] == 'X') and (self.app.B1['text'] == '')) and (self.clicks%2 == 0):# row1.2
            self.app.B1['text'] = 'O'
            self.app.B1['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B1')
            self.who_winner.performance()
        elif ((self.app.B5['text'] == self.app.B6['text'] == 'X') and (self.app.B4['text'] == '')) and (self.clicks%2 == 0):# row2.2
            self.app.B4['text'] = 'O'
            self.app.B4['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B4')
            self.who_winner.performance()
        elif ((self.app.B8['text'] == self.app.B9['text'] == 'X') and (self.app.B7['text'] == '')) and (self.clicks%2 == 0):# row3.2
            self.app.B7['text'] = 'O'
            self.app.B7['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B7')
            self.who_winner.performance()
        elif ((self.app.B1['text'] == self.app.B3['text'] == 'X') and (self.app.B2['text'] == '')) and (self.clicks%2 == 0):# row1.3
            self.app.B2['text'] = 'O'
            self.app.B2['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B2')
            self.who_winner.performance()
        elif ((self.app.B4['text'] == self.app.B6['text'] == 'X') and (self.app.B5['text'] == '')) and (self.clicks%2 == 0):# row2.3
            self.app.B5['text'] = 'O'
            self.app.B5['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B5')
            self.who_winner.performance()
        elif ((self.app.B7['text'] == self.app.B9['text'] == 'X') and (self.app.B8['text'] == '')) and (self.clicks%2 == 0):# row3.3
            self.app.B8['text'] = 'O'
            self.app.B8['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B8')
            self.who_winner.performance()
        elif ((self.app.B1['text'] == self.app.B4['text'] == 'X') and (self.app.B7['text'] == '')) and (self.clicks%2 == 0):# column1.1
            self.app.B7['text'] = 'O'
            self.app.B7['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B7')
            self.who_winner.performance()
        elif ((self.app.B2['text'] == self.app.B5['text'] == 'X') and (self.app.B8['text'] == '')) and (self.clicks%2 == 0):# column1.2
            self.app.B8['text'] = 'O'
            self.app.B8['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B8')
            self.who_winner.performance()
        elif ((self.app.B3['text'] == self.app.B6['text'] == 'X') and (self.app.B9['text'] == '')) and (self.clicks%2 == 0):# column1.3
            self.app.B9['text'] = 'O'
            self.app.B9['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B9')
            self.who_winner.performance()
        elif ((self.app.B4['text'] == self.app.B7['text'] == 'X') and (self.app.B1['text'] == '')) and (self.clicks%2 == 0):# column1.2
            self.app.B1['text'] = 'O'
            self.app.B1['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B1')
            self.who_winner.performance()
        elif ((self.app.B5['text'] == self.app.B8['text'] == 'X') and (self.app.B2['text'] == '')) and (self.clicks%2 == 0):# column2.2
            self.app.B2['text'] = 'O'
            self.app.B2['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B2')
            self.who_winner.performance()
        elif ((self.app.B6['text'] == self.app.B9['text'] == 'X') and (self.app.B3['text'] == '')) and (self.clicks%2 == 0):# column3.2
            self.app.B3['text'] = 'O'
            self.app.B3['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B3')
            self.who_winner.performance()
        elif ((self.app.B1['text'] == self.app.B7['text'] == 'X') and (self.app.B4['text'] == '')) and (self.clicks%2 == 0):# column1.3
            self.app.B4['text'] = 'O'
            self.app.B4['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B4')
            self.who_winner.performance()
        elif ((self.app.B2['text'] == self.app.B8['text'] == 'X') and (self.app.B5['text'] == '')) and (self.clicks%2 == 0):# column2.3
            self.app.B5['text'] = 'O'
            self.app.B5['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B5')
            self.who_winner.performance()
        elif ((self.app.B3['text'] == self.app.B9['text'] == 'X') and (self.app.B6['text'] == '')) and (self.clicks%2 == 0):# column3.3
            self.app.B6['text'] = 'O'
            self.app.B6['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B6')
            self.who_winner.performance()
        elif ((self.app.B1['text'] == self.app.B5['text'] == 'X') and (self.app.B9['text'] == '')) and (self.clicks%2 == 0):# diameter1.1
            self.app.B9['text'] = 'O'
            self.app.B9['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B9')
            self.who_winner.performance()
        elif ((self.app.B3['text'] == self.app.B5['text'] == 'X') and (self.app.B7['text'] == '')) and (self.clicks%2 == 0):# diameter2.1
            self.app.B7['text'] = 'O'
            self.app.B7['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B7')
            self.who_winner.performance()
        elif ((self.app.B5['text'] == self.app.B9['text'] == 'X') and (self.app.B1['text'] == '')) and (self.clicks%2 == 0):# diameter1.2
            self.app.B1['text'] = 'O'
            self.app.B1['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B1')
            self.who_winner.performance()
        elif ((self.app.B5['text'] == self.app.B7['text'] == 'X') and (self.app.B3['text'] == '')) and (self.clicks%2 == 0):# diameter2.2
            self.app.B3['text'] = 'O'
            self.app.B3['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B3')
            self.who_winner.performance()

        # خالی بودن وسط
        elif (self.app.B5['text'] == '') and (self.clicks%2 == 0):
            self.app.B5['text'] = 'O'
            self.app.B5['bg'] = 'red'
            self.clicks =self.clicks - 1
            self.check_button_list.remove('B5')
            self.who_winner.performance()
        # random if dosen't choose Button
        elif self.clicks%2 == 0:
            self.index = len(self.check_button_list)-1
            self.accident_button = self.check_button_list[self.random.randint(0, self.index)]
            if self.accident_button == 'B1':
                self.app.B1['text'] = 'O'
                self.app.B1['bg'] = 'red'
                self.clicks =self.clicks - 1
                self.check_button_list.remove('B1')
                self.who_winner.performance()
            elif self.accident_button == 'B2':
                self.app.B2['text'] = 'O'
                self.app.B2['bg'] = 'red'
                self.clicks =self.clicks - 1
                self.check_button_list.remove('B2')
                self.who_winner.performance()
            elif self.accident_button == 'B3':
                self.app.B3['text'] = 'O'
                self.app.B3['bg'] = 'red'
                self.clicks =self.clicks - 1
                self.check_button_list.remove('B3')
                self.who_winner.performance()
            elif self.accident_button == 'B4':
                self.app.B4['text'] = 'O'
                self.app.B4['bg'] = 'red'
                self.clicks =self.clicks - 1
                self.check_button_list.remove('B4')
                self.who_winner.performance()
            elif self.accident_button == 'B5':
                self.app.B5['text'] = 'O'
                self.app.B5['bg'] = 'red'
                self.clicks =self.clicks - 1
                self.check_button_list.remove('B5')
                self.who_winner.performance()
            elif self.accident_button == 'B6':
                self.app.B6['text'] = 'O'
                self.app.B6['bg'] = 'red'
                self.clicks =self.clicks - 1
                self.check_button_list.remove('B6')
                self.who_winner.performance()
            elif self.accident_button == 'B7':
                self.app.B7['text'] = 'O'
                self.app.B7['bg'] = 'red'
                self.clicks =self.clicks - 1
                self.check_button_list.remove('B7')
                self.who_winner.performance()
            elif self.accident_button == 'B8':
                self.app.B8['text'] = 'O'
                self.app.B8['bg'] = 'red'
                self.clicks =self.clicks - 1
                self.check_button_list.remove('B8')
                self.who_winner.performance()
            elif self.accident_button == 'B9':
                self.app.B9['text'] = 'O'
                self.app.B9['bg'] = 'red'
                self.clicks =self.clicks - 1
                self.check_button_list.remove('B9')
                self.who_winner.performance()
    def restart(self):
        self.clicks = 9
        self.app.B1['text'], self.app.B2['text'], self.app.B3['text'], self.app.B4['text'], self.app.B5['text'], self.app.B6['text'], self.app.B7['text'], self.app.B8['text'], self.app.B9['text'] = '', '', '', '', '', '', '', '', ''
        self.app.B1['bg'], self.app.B2['bg'], self.app.B3['bg'], self.app.B4['bg'], self.app.B5['bg'], self.app.B6['bg'], self.app.B7['bg'], self.app.B8['bg'], self.app.B9['bg'] = 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'
        self.check_button_list = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9']

class lose_or_win:
    def __init__(self, app, tk, surface):
        self.app = app
        self.tk = tk
        self.surface = surface
    def row1_winner(self):
        if self.app.B1['text'] == self.app.B2['text'] == self.app.B3['text'] == 'X':
            self.app.winner_message(self.tk)
    def row2_winner(self):
        if self.app.B4['text'] == self.app.B5['text'] == self.app.B6['text'] == 'X':
            self.app.winner_message(self.tk)
    def row3_winner(self):
        if self.app.B7['text'] == self.app.B8['text'] == self.app.B9['text'] == 'X':
            self.app.winner_message(self.tk)
    def column1_winner(self):
        if self.app.B1['text'] == self.app.B4['text'] == self.app.B7['text'] == 'X':
            self.app.winner_message(self.tk)
    def column2_winner(self):
        if self.app.B2['text'] == self.app.B5['text'] == self.app.B8['text'] == 'X' :
            self.app.winner_message(self.tk)
    def column3_winner(self):
        if self.app.B3['text'] == self.app.B6['text'] == self.app.B9['text'] == 'X':
            self.app.winner_message(self.tk)
    def diameter1_winner(self):
        if self.app.B1['text'] == self.app.B5['text'] == self.app.B9['text'] == 'X':
            self.app.winner_message(self.tk)
    def diameter2_winner(self):
        if self.app.B3['text'] == self.app.B5['text'] == self.app.B7['text'] == 'X':
            self.app.winner_message(self.tk)
    def row1_loser(self):
        if self.app.B1['text'] == self.app.B2['text'] == self.app.B3['text'] == 'O':
            self.app.loser_message(self.tk)
    def row2_loser(self):
        if self.app.B4['text'] == self.app.B5['text'] == self.app.B6['text'] == 'O':
            self.app.loser_message(self.tk)
    def row3_loser(self):
        if self.app.B7['text'] == self.app.B8['text'] == self.app.B9['text'] == 'O':
            self.app.loser_message(self.tk)
    def column1_loser(self):
        if self.app.B1['text'] == self.app.B4['text'] == self.app.B7['text'] == 'O':
            self.app.loser_message(self.tk)
    def column2_loser(self):
        if self.app.B2['text'] == self.app.B5['text'] == self.app.B8['text'] == 'O' :
            self.app.loser_message(self.tk)
    def column3_loser(self):
        if self.app.B3['text'] == self.app.B6['text'] == self.app.B9['text'] == 'O':
            self.app.loser_message(self.tk)
    def diameter1_loser(self):
        if self.app.B1['text'] == self.app.B5['text'] == self.app.B9['text'] == 'O':
            self.app.loser_message(self.tk)
    def diameter2_loser(self):
        if self.app.B3['text'] == self.app.B5['text'] == self.app.B7['text'] == 'O':
            self.app.loser_message(self.tk)
    def performance(self):
        lose_or_win.row1_winner(self)
        lose_or_win.row2_winner(self)
        lose_or_win.row3_winner(self)
        lose_or_win.column1_winner(self)
        lose_or_win.column2_winner(self)
        lose_or_win.column3_winner(self)
        lose_or_win.diameter1_winner(self)
        lose_or_win.diameter2_winner(self)
        lose_or_win.row1_loser(self)
        lose_or_win.row2_loser(self)
        lose_or_win.row3_loser(self)
        lose_or_win.column1_loser(self)
        lose_or_win.column2_loser(self)
        lose_or_win.column3_loser(self)
        lose_or_win.diameter1_loser(self)
        lose_or_win.diameter2_loser(self)

def gui_performance(app, tk, surface, playing):
    app.game_Buttons(tk, surface, playing)
    app.chalange_computer(tk, surface, playing)
    app.try_again(tk, surface, playing)
def main():
    import random, GUI #begin the game you or com
    import tkinter as tk
    surface = tk.Tk()
    program = GUI.app
    app = program.App(tk, surface)
    who_winner = lose_or_win(app, tk, surface)
    playing = Playing(random, app, who_winner)
    gui_performance(app, tk, surface, playing)
    surface.mainloop()
if __name__ == '__main__':main()
