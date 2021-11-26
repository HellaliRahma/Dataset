from Environment import*
import csv

class generation_database:
    def __init__(self):
        self.env = Environment()
    def init(self):
        self.env = Environment()
    def generate_state(self):
        file_name = "test.csv"
        write_csv = csv.writer(open(file_name,'w'),lineterminator='\n')
        write_csv.writerow(["time","temperature","luminosity","season"])
        for i in range(6400):
            self.env.set_state()
            print(self.env.state)
            temps=self.env.state[0]
            temp=self.env.state[1]
            lum=self.env.state[2]
            season=self.env.state[3]
            write_csv.writerow([temps,temp,lum,season])

if __name__ == '__main__':
    xcs=generation_database()
    xcs.generate_state()